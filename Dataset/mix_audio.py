from scipy.io import wavfile
import numpy as np
import glob
import librosa
import os
import pandas as pd
import random
import json


def mix(noise, clean, snr):
    # Normalize clean audio to -25 dB FS(avoiding that the mixing clips)
    rmsclean = (clean**2).mean()**0.5
    minscale = 14
    if(rmsclean > (10 ** (-25 / 20) / minscale)):
        # if the RMS is greater than the threshold there is no "silence"
        scalarclean = 10 ** (-25 / 20) / rmsclean
        clean = clean * scalarclean
        rmsclean = (clean**2).mean()**0.5

        # Normalize clean audio to - 25 dB FS(avoiding that the mixing clips)
        rmsnoise = (noise**2).mean()**0.5
        scalarnoise = 10 ** (-25 / 20) / rmsnoise
        noise = noise * scalarnoise
        rmsnoise = (noise**2).mean()**0.5

        noisescalar = rmsclean / (10**(snr/20)) / rmsnoise
        noisenewlevel = noise * noisescalar
        noisyspeech = clean + noisenewlevel

    else:
        # RMS of clean is lower than threshold (5s silence) then skip the file
        return None, None, None, None

    return noisyspeech, clean, scalarclean, noisescalar


f = open('config.json')
jsonfile = json.load(f)


clean = jsonfile["mix_audio.py"]["clean_path"]
clean_csv = jsonfile["mix_audio.py"]["clean_csv"]
clean_data = pd.read_csv(clean_csv, header=0)
clean_files = glob.glob(clean+"/*.wav")  # list all clean audio files
random.Random(1).shuffle(clean_files)  # shuffle clean audio files
clean_data['reader'] = clean_data['reader'].astype('string')
clean_data['file_name'] = clean_data['file'].astype('string')
clean_data['tipo'] = clean_data['voice_type'].astype('string')

noise = jsonfile["mix_audio.py"]["noise_path"]
noise_csv = jsonfile["mix_audio.py"]["noise_csv"]
noise_data = pd.read_csv(noise_csv, header=0)
noise_files = glob.glob(noise+"/*.wav")  # list all noise audio files
random.Random(1).shuffle(noise_files)  # shuffle noise audio files
noise_data['filename'] = noise_data['filename'].astype('string')
noise_data['category'] = noise_data['category'].astype('string')

result = jsonfile["mix_audio.py"]["mix_output_path"]
result_csv = jsonfile["mix_audio.py"]["mix_csv_out_path"]
result_c = jsonfile["mix_audio.py"]["norm_clean_out_path"]


mixed_data = []

levels = np.arange(start=0, stop=50.5, step=0.5)

np.random.seed(0)  # seed to reproduce results

FS = 22050

i = 0

while i < len(clean_files):
    cl = clean_files[i]
    # snr = levels[i % len(levels)]
    snr = np.around(np.random.rand()+np.random.randint(50), 2)
    ns = noise_files[i % len(noise_files)]
    # print(cl[len(clean)+1:], "\tsnr:", snr, "\t", ns[len(noise)+1:])

    clean_signal, Fs = librosa.load(cl, sr=22050)
    noise_signal, Fs = librosa.load(ns, sr=22050)

    mixed_signal, clean_new, clean_sc, noise_sc = mix(noise_signal, clean_signal, snr)
    # noisyspeech, clean, scalarclean, noisescalar = mix()

    if mixed_signal is not None:  # If the signals mixed then save
        cl_name = cl[len(clean)+1:]  # select only name of the file w/o path
        ns_name = ns[len(noise)+1:]  # select only name of the file w/o path

        val = clean_data.loc[clean_data['file'] == cl_name]['reader']
        reader = val.iloc[0]  # obtain reader fron clean audio data
        val = clean_data.loc[clean_data['file'] == cl_name]['voice_type']
        v_type = val.iloc[0]  # obtain voice type (F/M) from clean audio data
        val = noise_data.loc[noise_data['filename'] == ns_name]['category']
        n_type = val.iloc[0]  # obtain category of noise from noise data

        mix_filename = str(i)+"_"+v_type+"_"+reader+"_"+ns_name[:-4]+"_"+str(snr)+"dB.wav"

        # append data to list to make the csv containing mixed audio data
        mixed_data.append([mix_filename, reader, ns_name, v_type, n_type,
                          snr, 'n'+cl_name, clean_sc, noise_sc])
        ##
        # mixed_data = [mix_filename, reader, noise, voice_t, noise_t, snr, clean_factor, cleanfile]
        ##

        save_mix = os.path.join(result, mix_filename)
        wavfile.write(save_mix, Fs, mixed_signal)

        save_clean = os.path.join(result_c, 'n'+cl_name)
        wavfile.write(save_clean, Fs, clean_new)

    # update progress in the terminal when running
    print("audio file # ", i+1, "of "+str(len(clean_files)), end='\r')

    i += 1
    # end loop

dfout = pd.DataFrame(mixed_data, columns=[
    'mix_filename', 'reader', 'noise_file', 'voice_type', 'noise_type', 'snr', 'clean_file', 'clean_factor', 'noise_factor'])
dfout.info()
print(dfout.head())
dfout.to_csv(result_csv, index=False)
