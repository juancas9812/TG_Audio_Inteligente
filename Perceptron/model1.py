import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import TensorBoard, EarlyStopping
from tensorflow.keras.optimizers import Adam


def create_nn(layers):

    model = tf.keras.models.Sequential()
    model.add(InputLayer((2205,)))
    
    print(layers)
    
    for layer in layers:
    	model.add(Dense(layer, activation=tf.nn.relu))
    	
    #model.add(Dense(100, input_shape=(2205,), activation=tf.nn.relu))
    #model.add(Dense(100, activation=tf.nn.relu))
    #model.add(Dense(80, activation=tf.nn.relu))
    #model.add(Dense(50, activation=tf.nn.relu))
    
    model.add(Dense(1))
    
    model.summary()
    
    model.compile(loss='mean_squared_error', optimizer='adam')

    return model


def create_nn_2():

    model = tf.keras.models.Sequential()

    model.add(Dense(50, input_shape=(2205,), activation=tf.nn.relu))

    model.add(Dense(50, activation=tf.nn.relu))

    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam')

    return model
