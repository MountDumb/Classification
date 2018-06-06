from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import helperfunctions as hf

img_width, img_height = 150, 150
img_path = 'data/input'

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
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

model.load_weights('Model_Weights.h5')

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

datagen = ImageDataGenerator(rescale=1. / 255)

imagegenerator = hf.get_absfilenames(img_path)
outputs = []

for item in imagegenerator:
    img = load_img(item, target_size=(img_width, img_height))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    outputs.append(model.predict(x))

itt = len(outputs)
names = list(hf.get_filenames(img_path))
prednamepairs = []

for i in range(itt):
    prediction = outputs[i][0][0]
    if prediction > 0.5:
        prediction = 'dog'
    elif prediction < 0.5:
        prediction = 'cat'
    else:
        prediction = 'I don\'t know'

    predictionfilename = names[i]
    prednamepairs.append((prediction, predictionfilename))

for p in prednamepairs:
    print(p)







