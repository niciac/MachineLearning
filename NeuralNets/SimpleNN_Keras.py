import tensorflow as tf
import keras
from keras.layers import InputLayer, Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plotting params
FONTSIZE = 18
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = FONTSIZE


def build_model(n_inputs, n_hidden, n_output, activation="elu", lrate=0.001):
    """
    Build a simple dense model

    n_inputs: number of inputs
    n_hidden: number of units in the hidden layer
    n_output: number of outputs
    activation: the activation function for hidden and output
    lrate: learning rate of the network

    """

    # define model
    model = Sequential()

    # the input layer
    model.add(InputLayer(input_shape=(n_inputs,)))

    # hidden layers
    model.add(Dense(n_hidden, use_bias=True, name="hidden", activation=activation))

    # output layers
    model.add(Dense(n_output, use_bias=True, name="output", activation=activation))

    # optimiser
    opt = keras.optimizers.Adam(learning_rate=lrate, epsilon=None)

    # compile the model
    model.compile(loss="mse", optimizer=opt)

    # display network
    print(model.summary())

    return model


# create training set
ins = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outs = np.array([[0], [1], [1], [0]])

model = build_model(ins.shape[1], 2, outs.shape[1], activation="sigmoid")

history = model.fit(
    x=ins,
    y=outs,
    epochs=2000,
)

plt.figure()
plt.plot(history.history["loss"])
plt.ylabel("MSE")
plt.xlabel("epochs")

model.predict(ins)
