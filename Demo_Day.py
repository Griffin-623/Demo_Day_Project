from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
root.title("Demo Day")
root.geometry("600x600")
def changeimage(*args):
    path = heroes[variable.get()]
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image = img)
    panel.img = img
def writeimage(*args):
    info = heroes_information[variable.get()]
def show():
    label.config( text =clicked.get())
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
options = [
"Home Page",
"Rosa Parks",
"MLK",
"Hariet Tubman",
"Sojourner Truth",
"Malcolm X"
]
heroes = {'Home Page': 'assets/HomePage.jpeg','Rosa Parks':'assets/Rosaparks.jpeg', 'MLK':'assets/MLK.jpeg', 'Hariet Tubman':'assets/Harriet.jpeg', 'Sojourner Truth':'assets/Sojourner_Truth.png', 'Malcolm X':'assets/Malcolm_X.jpeg'}
heroes_information= {'Home Page':'you are on the home page','Rosa Parks':'rosa parks information', 'MLK':'mlk info', 'Hariet Tubman':'Harriet Tubman info', 'Sojourner Truth':'Sojourner info', 'Malcolm X': 'Malcom X info'}
variable = StringVar(root)
variable.set(options[0])
w = OptionMenu(root, variable, *options)
path = heroes[variable.get()]
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(frame2, image = img)
panel.pack()
w.pack()
frame1.pack()
frame2.pack()
variable.trace_add('write', changeimage)
variable.trace_add('write', writeimage)
root.mainloop()