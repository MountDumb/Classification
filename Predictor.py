from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import helperfunctions as hf


class Predictor(object):

    def __init__(self):
        self.img_width, self.img_height = 150, 150
        self.input_shape = (self.img_width, self.img_height, 3)
        self.model = None
        self.prediction_pairs = None
        self.abs_paths = []
        self.img_path = 'data/input'

    def define_model(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=self.input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))
        self.model = model

    def activate_model(self):
        self.model.load_weights('Model/Model_Weights.h5')

        self.model.compile(loss='binary_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])

    def predict(self):
        imagepaths = hf.get_absfilenames(self.img_path)
        outputs = []

        for item in imagepaths:
            self.abs_paths.append(item)
            img = load_img(item, target_size=(self.img_width, self.img_height))
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)
            outputs.append(self.model.predict(x))

        itt = len(outputs)
        names = list(hf.get_filenames(self.img_path))
        prednamepairs = []

        for i in range(itt):
            predictionfilename = names[i]

            prednamepairs.append('{} : {}'.format(predictionfilename, outputs[i][0][0]))

        self.prediction_pairs = prednamepairs


if __name__ == '__main__':
    pass

