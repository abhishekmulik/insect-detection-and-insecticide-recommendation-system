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
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

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


# logo_label=tk.Label()
# logo_label.place(x=0,y=100)

# x = 1

# # function to change to next image
# def move():
# 	global x
# 	if x == 4:
# 		x = 1
# 	if x == 1:
# 		logo_label.config(image=img)
# 	elif x == 2:
# 		logo_label.config(image=img2)
# 	elif x == 3:
# 		logo_label.config(image=img3)
# 	x = x+1
# 	root.after(2000, move)

# calling the function
#move()



#
label_l1 = tk.Label(root, text="Insect Detection",font=("Times New Roman", 35, 'bold'),
                    background="#5F9EA0", fg="white", width=52, height=1)
label_l1.place(x=0, y=10)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

# def reg():
#     from subprocess import call
#     call(["python","socialdistance.py"])

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