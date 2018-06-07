from tkinter import *
from PIL import Image, ImageTk
import Classify_Img as ci
from Predictor import *

predictordd = ci
pp = Predictor()

print(pp.ImgPath)

root = Tk()
root.title('KittieGUI')

lFrame = Frame(root)
lFrame.pack(side='left', fill='both', expand=True)
rFrame = Frame(root)
rFrame.pack(side='right', fill='both', expand=True)

resultList = Listbox(lFrame, selectmode='single', width=30)
resultList.pack(fill='y', expand=True, anchor='w')

predictButton = Button(rFrame, text='Predict Images')
predictButton.pack(anchor='ne', padx=10, pady=10)

image = Image.open('data/Stuff/Kokyo.JPG')
image = image.resize((150, 150))
image = image.resize((300, 300))
photoImage = ImageTk.PhotoImage(image)
imgLabel = Label(rFrame, image=photoImage, height=300, width=300)
imgLabel.image = photoImage

predictions = predictordd.main()

for item in predictions:
    resultList.insert(END, item)

imgLabel.pack(anchor='se', padx=10, pady=10)

root.mainloop()