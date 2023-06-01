# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:23:43 2021

@author: sheet
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

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
root.title("Insect Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
image2 = Image.open('11.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

# img=ImageTk.PhotoImage(Image.open("s1.jpg"))

# img2=ImageTk.PhotoImage(Image.open("s2.jpg"))

# img3=ImageTk.PhotoImage(Image.open("s3.jpg"))


label_l1 = tk.Label(root, text="Insect Detection",font=("Times New Roman", 35, 'bold'),
                    background="#5F9EA0", fg="white", width=52, height=1)
label_l1.place(x=0, y=10)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


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
