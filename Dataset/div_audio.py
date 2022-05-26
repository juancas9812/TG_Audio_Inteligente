import glob
import librosa
from scipy.io.wavfile import write
import numpy as np
import pandas as pd
import json


fpaths = open('config.json')
jsonfile = json.load(fpaths)

path = jsonfile["div_audio.py"]["uncut_librivox_audio"]
dest = jsonfile["div_audio.py"]["audio_dest"]

libri_path = jsonfile["div_audio.py"]["librivox_csv"]
lib_path_save = jsonfile["div_audio.py"]["cut_audio_csv"]

df = pd.read_csv(libri_path, header=0, encoding='unicode_escape')
df['reader'] = df['reader'].astype('string')
df['file_name'] = df['file_name'].astype('string')
df['tipo'] = df['tipo'].astype('string')
new_data = []

df.info()

# segments gives a list of numbers to divide audio up to 10 mins(max_t) in 5s chuncks
max_time = 600.0  # 600s or 10m
max_t = 22050*max_time

segments = np.arange(start=22050*5, stop=max_t, step=22050*5)

readers = {}
ls = glob.glob(path + '/*')

for pth in ls:
    files = glob.glob(pth+'/*.wav')
    for f in files:
        f_name = f[len(pth)+1:]
        i = 0
        data, Fs = librosa.load(f, sr=None)
        L = data.size/Fs
        print(f_name)
        val_read = df.loc[df['file_name'] == f_name]['reader']
        print(val_read)
        reader = val_read.iloc[0]
        val_tipo = df.loc[df['file_name'] == f_name]['tipo']
        tipo = val_tipo.iloc[0]
        if reader not in readers:
            readers[reader] = 0.0
        rd = readers.get(reader)
        if rd < max_time:
            div = np.array_split(data, np.arange(start=Fs*5, stop=data.size, step=Fs*5))
            for d in div:
                if d.size == Fs*5 and i < 120:
                    dst = f[len(pth)+1:-4]
                    file_name_data = dst+'_'+str(i)+'.wav'
                    file_name_div = dest+'/'+file_name_data
                    write(file_name_div, Fs, d)
                    i = i+1
                    readers[reader] += d.size/Fs
                    new_data.append([reader, file_name_data, tipo])

print(readers)
dfout = pd.DataFrame(new_data, columns=['reader', 'file', 'voice_type'])
dfout.info()
print(dfout.head())
dfout.to_csv(lib_path_save, index=False)
