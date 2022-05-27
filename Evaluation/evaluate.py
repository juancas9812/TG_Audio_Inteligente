from evaluation_metrics import SNR
from evaluation_metrics import SDR
from evaluation_metrics import STOI
from evaluation_metrics import PESQ
from scipy.io import wavfile
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import numpy as np
import librosa
import json


# Read configuration
######################
f = open('config.json')
jsonfile = json.load(f)

mixed_path = jsonfile["evaluate.py"]["mixed_path"]
clean_path = jsonfile["evaluate.py"]["clean_path"]
dataset_csv_path = jsonfile["evaluate.py"]["dataset_csv"]
perceptron_folder = jsonfile["evaluate.py"]["perceptron_enhancement_path"]
crn_folder = jsonfile["evaluate.py"]["crn_enhancement_path"]
results_csv_pth = jsonfile["evaluate.py"]["results_csv_path"]


if not os.path.exists(results_csv_pth):
    os.mkdir(results_csv_pth)

# Read datasets
#############################
dataset = pd.read_csv(dataset_csv_path, header=0)
random_st = 0
_, other_df = train_test_split(
    dataset[['mix_filename', 'clean_file']], test_size=0.3, random_state=random_st)
test_df, _ = train_test_split(
    other_df[['mix_filename', 'clean_file']], test_size=0.5, random_state=random_st)
test_df.reset_index(inplace=True, drop=True)

perceptron_csv = os.path.join(perceptron_folder, "model1_enhanced_output.csv")
perceptron_audio = os.path.join(perceptron_folder, "enhanced")
df_per = pd.read_csv(perceptron_csv, header=0)
df_per['mix_file'] = df_per['mix_file'].astype('string')
df_per['clean_file'] = df_per['clean_file'].astype('string')
df_per['result_file'] = df_per['result_file'].astype('string')


res = []

total = len(test_df.index)
total = 4
for pos in range(total):

    # read mix signal
    mix_name = test_df.iloc[pos]["mix_filename"]
    mix = os.path.join(mixed_path, mix_name)
    mix_sig, _ = librosa.load(mix, sr=22050)

    # read clean signal
    clean_name = test_df.iloc[pos]["clean_file"]
    clean_in = os.path.join(clean_path, clean_name)
    clean_sig, _ = librosa.load(clean_in, sr=22050)
    clean_16k, _ = librosa.load(clean_in, sr=16000)
    wavfile.write("temp_clean.wav", rate=22050, data=clean_sig[1102:-1102])
    clean_m1_16k, _ = librosa.load("temp_clean.wav", sr=16000)
    os.remove("temp_clean.wav")

    # read signal from model 1
    result1_df = df_per.loc[df_per['mix_file'] == mix_name]
    result1_name = result1_df.iloc[0]["result_file"]
    result1 = os.path.join(perceptron_audio, result1_name)
    result1_sig, _ = librosa.load(result1, sr=22050)
    result1_16k, _ = librosa.load(result1, sr=16000)

    # read signal from model 2
    result2_name = mix_name
    result2_sig, _ = librosa.load(os.path.join(crn_folder, 'enhanced', result2_name), sr=16000)

    # Measure SNR,SDR,STOI and PESQ from original signals and enhanced signals
    snr_o = SNR(mix_sig, clean_sig)
    snr_org = snr_o.numpy()
    sdr_org = SDR(clean_sig, mix_sig)
    stoi_org = STOI(clean_sig, mix_sig, sr=22050)
    pesq_org = PESQ(clean_16k, mix_sig, sr=16000)

    # model1 outputs a signal cut 50ms at start and 50ms at end
    snr_1 = SNR(result1_sig, clean_sig[1102:-1102])
    snr_m1 = snr_1.numpy()
    sdr_m1 = SDR(clean_sig[1102:-1102], result1_sig)
    stoi_m1 = STOI(clean_sig[1102:-1102], result1_sig, sr=22050)
    pesq_m1 = STOI(clean_m1_16k, result1_16k, sr=16000)

    snr_2 = SNR(result2_sig, clean_16k)
    snr_m2 = snr_2.numpy()
    sdr_m2 = SDR(clean_16k, result2_sig)
    stoi_m2 = STOI(clean_16k, result2_sig, sr=16000)
    pesq_m2 = STOI(clean_16k, result2_sig, sr=16000)

    res.append([mix_name, clean_name, result1_name, result2_name,
                snr_org, sdr_org, pesq_org, stoi_org,
                snr_m1, sdr_m1, pesq_m1, stoi_m1,
                snr_m2, sdr_m2, pesq_m2, stoi_m2])

    print("file ", pos+1, " of ", total, end='\r')

#######
# [mixed,clean, model1_enh, model2_enh,
#         snr_org, sdr_org, pesq_org, stoi_org,
#             snr_m1, sdr_m1, pesq_m1, stoi_m1,
#                 snr_m2, sdr_m2, pesq_m2, stoi_m2]
#######
dfout = pd.DataFrame(res, columns=["mixed_file", "clean_file", "model1_file", "model2_file", "snr_org", "sdr_org",
                     "pesq_org", "stoi_org", "snr_m1", "sdr_m1", "pesq_m1", "stoi_m1", "snr_m2", "sdr_m2", "pesq_m2", "stoi_m2"])

dfout.to_csv(os.path.join(results_csv_pth, "measurements.csv"), index=False)
