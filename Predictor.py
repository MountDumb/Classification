from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import helperfunctions as hf


class Predictor(object):

    def __init__(self):
        self._img_width, self._img_height = 150, 150
        self._img_path = 'data/input'

    def set_img_path(self, new_path):
        self._img_path = new_path

    def get_img_path(self):
        return self._img_path

    ImgPath = property(get_img_path, set_img_path)


if __name__ == '__main__':
    pass

