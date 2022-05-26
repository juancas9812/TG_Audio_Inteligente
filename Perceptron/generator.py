import os
import tensorflow as tf
import numpy as np
from scipy.io import wavfile


# https://medium.com/analytics-vidhya/write-your-own-custom-data-generator-for-tensorflow-keras-1252b64e41c3

class generator(tf.keras.utils.Sequence):
    def __init__(self, df, mix_path, clean_path, win_size=2205, shuffle=True, training=True):

        self.df = df.copy()
        self.win_size = win_size
        self.clean_folder = clean_path
        self.mix_folder = mix_path
        self.n = len(self.df)
        self.shuffle = shuffle
        self.training = training

    def make_windows(self, mixed):
        start = 0
        end = mixed.size-self.win_size
        sub_windows = (
            start +
            np.expand_dims(np.arange(self.win_size), 0) +
            np.expand_dims(np.arange(end + 1), 0).T
        )
        return(mixed[sub_windows])

    def make_outputs(self, clean):
        return clean[1102:-1102]  # returns the center of the window at each step

    def make_data(self, batch):
        mix_file_path = os.path.join(self.mix_folder, batch['mix_filename'])
        _, mixed = wavfile.read(mix_file_path)  # loads mixed audio file
        # X_batch = self.make_windows(mixed)  # create the batch input for training(windowed signal)
        if self.training:
            X_batch = self.make_windows(mixed[33075:77175])
            # create the batch output for traing(center of windows or the 'label' for the input)
            clean_file_path = os.path.join(self.clean_folder, batch['clean_file'])
            _, clean = wavfile.read(clean_file_path)  # loads clean file
            #y_batch = self.make_outputs(clean)
            y_batch = self.make_outputs(clean[33075:77175])
            return X_batch, y_batch
        else:
            X_batch = self.make_windows(mixed)
            return X_batch

    def __getitem__(self, index):
        batch = self.df.iloc[index]
        # print(batch)
        if self.training:
            X, y = self.make_data(batch)
            return X, y
        else:
            X = self.make_data(batch)
            return X

    def __len__(self):
        return self.n

    def on_epoch_end(self):
        if self.shuffle:
            self.df = self.df.sample(frac=1).reset_index(drop=True)
