from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from generator import generator
from datetime import datetime
from model1 import create_nn
from sklearn.model_selection import train_test_split
import json
import os
import pandas as pd

f = open('config.json')
jsonfile = json.load(f)

mixed_path = jsonfile["train.py"]["mixed_path"]
clean_path = jsonfile["train.py"]["clean_path"]
dataset_path = jsonfile["train.py"]["dataset_csv"]

# Load dataset
dataset = pd.read_csv(dataset_path, header=0)
# print(dataset.head())
dataset['mix_filename'] = dataset['mix_filename'].astype('string')
dataset['clean_file'] = dataset['clean_file'].astype('string')
# dataset.info()


random_st = 0
train_df, other_df = train_test_split(
    dataset[['mix_filename', 'clean_file']], test_size=0.3, random_state=random_st)
train_df.reset_index(inplace=True, drop=True)

test_df, val_df = train_test_split(
    other_df[['mix_filename', 'clean_file']], test_size=0.5, random_state=random_st)
test_df.reset_index(inplace=True, drop=True)
val_df.reset_index(inplace=True, drop=True)

# Assign generator to the data split in order to input data to the NN
traingen = generator(train_df, mix_path=mixed_path, clean_path=clean_path)
valgen = generator(val_df, mix_path=mixed_path, clean_path=clean_path)

try:
    os.mkdir(os.path.join(os.getcwd(), "Model1"))
except OSError as error:
    print(error, end=", ")
    print("models will save in the folder: Model1")

now = datetime.now()
time_tr = now.strftime("%m_%d_%Y_%H:%M:%S")

fname1 = f"mod1-{time_tr}"
fname2 = "-e{epoch:03d}-l{loss:.4f}-vl{val_loss:.4f}"
fname = os.path.join("Model1", fname1)

checkpoints = ModelCheckpoint(fname+fname2, save_best_only=True, mode="min", verbose=1)
early_stop = EarlyStopping(monitor='loss', patience=6, verbose=1)


layers = jsonfile["train.py"]["layers"]

file_layers = open(fname+'.txt', 'w')
for layer in layers:
    file_layers.write(str(layer)+'\n')
file_layers.close()


model = create_nn(layers)

epochs = jsonfile["train.py"]["epochs"]

history = model.fit(traingen, validation_data=valgen, epochs=epochs,
                    verbose=1, callbacks=[early_stop, checkpoints])

# convert the history.history dict to a pandas DataFrame:
hist_df = pd.DataFrame(history.history)
hist_csv_file = fname+'history.csv'
with open(hist_csv_file, mode='w') as f:
    hist_df.to_csv(f)
