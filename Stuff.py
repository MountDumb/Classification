import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

digit = train_images[0]

plt.imshow(digit)

print(train_images.shape)
