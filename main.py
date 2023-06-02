import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Insect Detection And Insecticide Recommendation System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('ee.jpg')
image2 = image2.resize((1500, 800), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Insect Detection And Insecticide Recommendation System",font=("Times New Roman", 30, 'bold'),
                    background="#BC8F8F", fg="white", width=60, height=1)
label_l1.place(x=0, y=10)

<<<<<<< HEAD
=======
#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


>>>>>>> f548a5cc80a1c2ca711f8b2dd3d35de49ef07cb9
def log():
    from subprocess import call
    call(["python","login.py"])

def reg():
    from subprocess import call
    call(["python",r"registration.py"])

  
def window():
  root.destroy()

button1 = tk.Button(root, text="Login", command=log, width=20, height=1,font=('times', 20, ' bold '), bg="#DC143C", fg="white")
button1.place(x=90, y=150)

button2 = tk.Button(root, text="Register", command=reg, width=20, height=1,font=('times', 20, ' bold '), bg="#DC143C", fg="white")
button2.place(x=90, y=250)


button4 = tk.Button(root, text="Exit",command=window,width=20, height=1,font=('times', 20, ' bold '), bg="#2F4F4F", fg="white")
button4.place(x=90, y=350)

root.mainloop()
