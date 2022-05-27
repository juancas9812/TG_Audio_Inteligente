from scipy.io import wavfile
from generator import generator
from sklearn.model_selection import train_test_split
from tensorflow import keras
import pandas as pd
import os
import json


def saver(path, type, model):
    try:
        os.mkdir(path)
    except OSError:
        pass
    print(type+" signals used in model "+model+" will save in ", path)


f = open('config.json')
jsonfile = json.load(f)

mixed_path = jsonfile["enhance.py"]["mixed_path"]
clean_path = jsonfile["enhance.py"]["clean_path"]
dataset_path = jsonfile["enhance.py"]["dataset_csv"]
model1_pth = jsonfile["enhance.py"]["perceptron_path"]
output1_path = jsonfile["enhance.py"]["perceptron_enhancement_path"]
results_csv_name = os.path.join(output1_path, "model1_enhanced_output.csv")

if not os.path.exists(output1_path):
    os.mkdir(output1_path)
m1_out_enhanced_pth = os.path.join(output1_path, "enhanced")
saver(m1_out_enhanced_pth, "enhanced", "1")


# Read cdataset for model 1
#############################
dataset = pd.read_csv(dataset_path, header=0)
random_st = 0
_, other_df = train_test_split(
    dataset[['mix_filename', 'clean_file']], test_size=0.3, random_state=random_st)
test_df, _ = train_test_split(
    other_df[['mix_filename', 'clean_file']], test_size=0.5, random_state=random_st)
test_df.reset_index(inplace=True, drop=True)

audio_ls = []

model1 = keras.models.load_model(model1_pth)  # load model
total = range(len(test_df.index))
for pos in total:
    # Pass audios to model:
    test_sig1 = generator(test_df[pos:pos+1][:], mix_path=mixed_path,
                          clean_path=None, training=False)
    result_sig1 = model1.predict(test_sig1, verbose=0)  # predict audio

    mix_name = test_df.iloc[pos]["mix_filename"]
    clean_name = test_df.iloc[pos]["clean_file"]
    rename_mix_pos = mix_name.rfind("_")
    res_name = "m1_"+mix_name[:rename_mix_pos]+"_nhcd.wav"
    res_out = os.path.join(m1_out_enhanced_pth, res_name)
    wavfile.write(res_out, rate=22050, data=result_sig1)

    audio_ls.append([mix_name, clean_name, res_name])

    print("audio ", pos+1, " of ", 10, end='\r')


dfout = pd.DataFrame(audio_ls, columns=["mix_file", "clean_file", "result_file"])
dfout.to_csv(results_csv_name, index=False)
