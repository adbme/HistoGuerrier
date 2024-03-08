import tensorflow as tf
from tensorflow.keras import layers, models


print("c bon")
print(tf.__version__)

data = tf.keras.datasets.mnist.load_data()

print(data)