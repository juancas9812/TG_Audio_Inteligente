import pandas as pd
from sklearn.model_selection import train_test_split
import os
import json


fpaths = open('config.json')
jsonfile = json.load(fpaths)

mixed_path = jsonfile["dataset_list.py"]["mixed_path"]
clean_path = jsonfile["dataset_list.py"]["clean_path"]
dataset_path = jsonfile["dataset_list.py"]["dataset_csv"]
output_path = jsonfile["dataset_list.py"]["output_path"]


# Load dataset
dataset = pd.read_csv(dataset_path, header=0)
dataset['mix_filename'] = dataset['mix_filename'].astype('string')
dataset['clean_file'] = dataset['clean_file'].astype('string')

random_st = 0
train_df, other_df = train_test_split(
    dataset[['mix_filename', 'clean_file']], test_size=0.3, random_state=random_st)
train_df.reset_index(inplace=True, drop=True)

test_df, val_df = train_test_split(
    other_df[['mix_filename', 'clean_file']], test_size=0.5, random_state=random_st)
test_df.reset_index(inplace=True, drop=True)
val_df.reset_index(inplace=True, drop=True)

train_df['mix_filename'] = mixed_path+os.sep+train_df['mix_filename']
train_df['clean_file'] = clean_path+os.sep+train_df['clean_file']
test_df['mix_filename'] = mixed_path+os.sep+test_df['mix_filename']
test_df['clean_file'] = clean_path+os.sep+test_df['clean_file']
val_df['mix_filename'] = mixed_path+os.sep+val_df['mix_filename']
val_df['clean_file'] = clean_path+os.sep+val_df['clean_file']


name_train = os.path.join(output_path, "train_list_dataset.txt")
name_test1 = os.path.join(output_path, "test_list_dataset.txt")
name_test2 = os.path.join(output_path, "test_dataset_onlynoisy.txt")
name_validation = os.path.join(output_path, "validation_list_dataset.txt")


train_df.to_csv(name_train, index=False, header=False, sep=' ')
test_df['mix_filename'].to_csv(name_test1, index=False, header=False)
val_df.to_csv(name_validation, index=False, header=False, sep=' ')
