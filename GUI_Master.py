import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Insect Detection And Insecticide Recommendation System.")

# ++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
image2 = Image.open('11.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 



label_l1 = tk.Label(root, text="Insect Detection And Insecticide Recommendation System",font=("Times New Roman", 35, 'bold'),
                    background="#5F9EA0", fg="white", width=52, height=1)
label_l1.place(x=0, y=10)


def insect():
    from subprocess import call
    call(["python","GUI_Master_old.py"])
    
def pest():
    from subprocess import call
    call(["python","predication.py"] )  
    



button1 = tk.Button(root, text="Insect Detection", command=insect, width=16,height=1,font=('times', 20, 'bold'), bg="#BC8F8F", fg="black")
button1.place(x=100, y=190)

button2 = tk.Button(root, text="Pesticide Suggestion",command=pest,width=16, height=1,font=('times', 20, 'bold'), bg="#152238", fg="white")
button2.place(x=100, y=300)


root.mainloop()
