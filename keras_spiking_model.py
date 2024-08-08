import keras_spiking
import tensorflow as tf

# Define the model
model = tf.keras.Sequential()

# Add convolutional layers
model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu', input_shape=(80, 80, 1)))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Flatten())

# Add dense layer with spiking activation
model.add(tf.keras.layers.Dense(units=64))
model.add(keras_spiking.SpikingActivation('relu', spiking_aware_training=False))

# Output layer for rotation and translation properties
# Assuming the output is a vector with rotation angle and translation (x, y)
model.add(tf.keras.layers.Dense(units=3))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Summary of the model
model.summary()
