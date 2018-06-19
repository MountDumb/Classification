import pickle
import matplotlib.pyplot as plt

history = None
with open('Model/BinaryClasshistoryDict', 'rb') as file:
    history = pickle.load(file)

loss = history['loss']
val_loss = history['val_loss']

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='val_Loss')
plt.title('Training and Validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

