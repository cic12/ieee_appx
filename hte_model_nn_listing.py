import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def build_model(n_neurons):
    model = keras.Sequential([
                            layers.Dense(n_neurons, activation='relu', input_shape=[len(train_dataset.keys())]),
                            layers.Dense(n_neurons, activation='relu'),
                            layers.Dense(1)])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae','mse'])
    return model


# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 save_freq='epoch')

# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

EPOCHS = 1000 # Max number of epochs

history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split = 0.2, verbose=1,
    callbacks=[tfdocs.modeling.EpochDots(),cp_callback,early_stop])