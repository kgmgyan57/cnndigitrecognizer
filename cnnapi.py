import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os

model = tf.keras.models.load_model("cnn_dc")

model.summary()
