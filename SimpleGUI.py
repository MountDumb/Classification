from tkinter import *
from PIL import Image, ImageTk
from Predictor import Predictor as pr

def on_result_select(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = predictions.abs_paths[index]
    set_image(value)
    print('You selected item %d: "%s"' % (index, value))

def set_image(img_path):
    img = Image.open(img_path)
    img = img.resize((150, 150))
    img = img.resize((300, 300))
    new_img = ImageTk.PhotoImage(img)
    imgLabel.configure(image=new_img)
    imgLabel.image = new_img


root = Tk()
root.title('KittieGUI')

lFrame = Frame(root)
lFrame.pack(side='left', fill='both', expand=True)
rFrame = Frame(root)
rFrame.pack(side='right', fill='both', expand=True)

resultList = Listbox(lFrame, selectmode='single', width=50)
resultList.bind('<<ListboxSelect>>', on_result_select)
resultList.pack(fill='y', expand=True, anchor='w')

image = Image.open('data/Stuff/Kokyo.JPG')
image = image.resize((150, 150))
image = image.resize((300, 300))
photoImage = ImageTk.PhotoImage(image)
imgLabel = Label(rFrame, image=photoImage, height=300, width=300)
imgLabel.image = photoImage

predictions = pr()
predictions.define_model()
predictions.activate_model()
predictions.predict()

for item in predictions.prediction_pairs:
    resultList.insert(END, item)

imgLabel.pack(anchor='se', padx=10, pady=10)

root.mainloop()