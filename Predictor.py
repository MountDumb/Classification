from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import helperfunctions as hf


class Predictor(object):

    def __init__(self):
        self.__img_width, self._img_height = 150, 150
        self.__img_path = 'data/input'

    #region Properties

    @property
    def img_width(self):
        return self.__img_width

    @img_width.setter
    def img_width(self, new_width):
        self.__img_width = new_width

    @property
    def img_path(self):
        return self.__img_path

    @img_path.setter
    def img_path(self, new_path):
        self.__img_path = new_path

    #endregion


if __name__ == '__main__':
    pass

