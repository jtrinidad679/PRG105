from tkinter import *
from PIL import Image, ImageTk
import cv2

wow_image = 'worldofwarcraft.jpg'
image = cv2.imread('worldofwarcraft.jpg')

b, g, r = cv2.split(image)
img = cv2.merge((r, g, b))

root = Tk()

im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

Label(root, image=imgtk).pack()

root.mainloop()



# canvas = tkinter.Canvas(window, width=2000, height=2000)
# canvas.pack()
#
# photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
#
# window.mainloop()
