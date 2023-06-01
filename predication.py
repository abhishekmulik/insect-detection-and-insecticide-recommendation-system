from tkinter import *
import tkinter as ttk

def Train():
    """GUI"""
    import tkinter as tk
    import tkinter as ttk

    import numpy as np
    import pandas as pd
    from PIL import Image, ImageTk

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    #root.geometry("800x850+0+0")
    root.title("Pesticide Suggestion")
    root.configure(background="purple")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    image2 = Image.open('Slide1.jpeg')

    image2 = image2.resize((w, h), Image.ANTIALIAS)
    
    background_image = ImageTk.PhotoImage(image2)
    
    
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

    
    #StationId = tk.StringVar()
    
    Temperature = tk.IntVar()
    Humidity = tk.IntVar()
    Moisture = tk.IntVar()
    Soil_Type = tk.IntVar()
    Crop_Type = tk.IntVar()
    Nitrogen = tk.IntVar()
    Potassium = tk.IntVar()
    Phosphorous = tk.IntVar()
    insect = tk.IntVar()
    
    
    #===============================================================================================



    def Detect():
        
        
        e1= Temperature.get()
        print(e1)
        e2=Humidity.get()
        print(e2)
        e3= Moisture.get()
        print(e3)
        e4=Soil_Type.get()
        print(e4)
        e5=Crop_Type.get()
        print(e5)
        e6=Nitrogen.get()
        print(e6)
        e7=Potassium.get() 
        print(e7)
        e8=Phosphorous.get() 
        print(e8)
        e9=insect.get()
        print(e9)
       
        #########################################################################################
        
        from joblib import dump , load
        a1=load('./Pesticide_SVM_MODEL.joblib')
        v= a1.predict([[e1,e2,e3, e4, e5, e6, e7, e8,e9]])
       
        if v[0]==0:
            print("0")
            l1 = tk.Label(frame_alpr,text="Pesticide suggest: UREA",background="Red",foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            l1.place(x=300,y=50)
            
            
        elif v[0]==1:
            print("1")
            lab1 = tk.Label(frame_alpr, text="Pesticide suggest: DAP", background="Red", foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            lab1.place(x=300,y=50)
        
            
        elif v[0]==2:
            print("2")
            lab1 = tk.Label(frame_alpr, text="Pesticide suggest: 14-35-14", background="Red", foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            lab1.place(x=300,y=50)
        
        elif v[0]==3:
            print("3")
            lab1 = tk.Label(frame_alpr, text="Pesticide suggest: 28-28", background="Red", foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            lab1.place(x=300,y=50)
            
        elif v[0]==4:
            print("4")
            lab1 = tk.Label(frame_alpr, text="Pesticide suggest: 17-17-17", background="Red", foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            lab1.place(x=300,y=50)
            
        elif v[0]==5:
            print("5")
            lab1 = tk.Label(frame_alpr, text="Pesticide suggest: 20-20", background="Red", foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            lab1.place(x=300,y=50)
            
        elif v[0]==6:
            print("6")
            lab1 = tk.Label(frame_alpr, text="Pesticide suggest: 10/26/26", background="Red", foreground="white",font=('times', 20, ' bold '),width=20, height=2)
            lab1.place(x=300,y=50)
            
        
    
    
    
    frame_alpr = tk.LabelFrame(root, text=" --Pesticide Detection-- ", width=1000, height=800, bd=5, font=('Algerian', 14, ' bold '),bg="white")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=300, y=20)



    
    l4=tk.Label(frame_alpr,text="Temperature",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l4.place(x=150,y=130)
    DOI=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Temperature)
    DOI.place(x=350,y=130)
    
    
   
    l4=tk.Label(frame_alpr,text="Humidity",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l4.place(x=150,y=180)
    CitedByCount=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Humidity)
    CitedByCount.place(x=350,y=180)

    l5=tk.Label(frame_alpr,text="Moisture",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l5.place(x=150,y=230)
    Year=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Moisture)
    Year.place(x=350,y=230)

    l6=tk.Label(frame_alpr,text="Soil_Type",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l6.place(x=500,y=180)
    tk.Radiobutton(frame_alpr, text="Sandy", padx=5, width=5, bg="snow", font=("bold", 15), variable=Soil_Type, value=1).place(x=700,
                                                                                                                    y=180)
    tk.Radiobutton(frame_alpr, text="Loamy", padx=20, width=4, bg="snow", font=("bold", 15), variable=Soil_Type, value=2).place(
        x=800, y=180)
    tk.Radiobutton(frame_alpr, text="Black", padx=5, width=5, bg="snow", font=("bold", 15), variable=Soil_Type, value=3).place(x=700,
                                                                                                                    y=230)
    tk.Radiobutton(frame_alpr, text="Red", padx=20, width=4, bg="snow", font=("bold", 15), variable=Soil_Type, value=4).place(
        x=800, y=230)
    
    tk.Radiobutton(frame_alpr, text="Clayey", padx=20, width=4, bg="snow", font=("bold", 15), variable=Soil_Type, value=5).place(
        x=700, y=280)

    l7=tk.Label(frame_alpr,text="Crop_Type",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l7.place(x=500,y=330)
    tk.Radiobutton(frame_alpr, text="Maize", padx=5, width=5, bg="snow", font=("bold", 15), variable=Crop_Type, value=1).place(x=700,
                                                                                                                    y=330)
    tk.Radiobutton(frame_alpr, text="Sugarcane", padx=20, width=4, bg="snow", font=("bold", 15), variable=Crop_Type, value=2).place(
        x=800, y=330)
    tk.Radiobutton(frame_alpr, text="Cotton", padx=5, width=5, bg="snow", font=("bold", 15), variable=Crop_Type, value=3).place(x=700,
                                                                                                                    y=380)
    tk.Radiobutton(frame_alpr, text="Tobacco", padx=20, width=4, bg="snow", font=("bold", 15), variable=Crop_Type, value=4).place(
        x=800, y=380)
    tk.Radiobutton(frame_alpr, text="Paddy", padx=5, width=5, bg="snow", font=("bold", 15), variable=Crop_Type, value=5).place(x=700,
                                                                                                                    y=430)
    tk.Radiobutton(frame_alpr, text="Barley", padx=20, width=4, bg="snow", font=("bold", 15), variable=Crop_Type, value=6).place(
        x=800, y=430)
    
    tk.Radiobutton(frame_alpr, text="Wheat", padx=5, width=5, bg="snow", font=("bold", 15), variable=Crop_Type, value=7).place(x=700,
                                                                                                                    y=480)
    tk.Radiobutton(frame_alpr, text="Millets", padx=20, width=4, bg="snow", font=("bold", 15), variable=Crop_Type, value=8).place(
        x=800, y=480)
    tk.Radiobutton(frame_alpr, text="Oil seeds", padx=5, width=7, bg="snow", font=("bold", 15), variable=Crop_Type, value=9).place(x=700,
                                                                                                                    y=530)
    tk.Radiobutton(frame_alpr, text="Pulses", padx=20, width=4, bg="snow", font=("bold", 15), variable=Crop_Type, value=10).place(
        x=800, y=530)
    tk.Radiobutton(frame_alpr, text="Ground Nuts", padx=5, width=9, bg="snow", font=("bold", 15), variable=Crop_Type, value=11).place(x=700,
                                                                                                                    y=580)
    
    l8=tk.Label(frame_alpr,text="Nitrogen",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l8.place(x=150,y=280)
    charges=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Nitrogen)
    charges.place(x=350,y=280)
    
    l9=tk.Label(frame_alpr,text="Potassium",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l9.place(x=150,y=330)
    charges=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Potassium)
    charges.place(x=350,y=330)

    l10=tk.Label(frame_alpr,text="Phosphorous",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l10.place(x=150,y=380)
    charges=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Phosphorous)
    charges.place(x=350,y=380)
    
    l7=tk.Label(frame_alpr,text="Insect",background="black",fg="white",font=('times', 20, ' bold '),width=10)
    l7.place(x=150,y=430)
    tk.Radiobutton(frame_alpr, text="aphides", padx=5, width=5, bg="snow", font=("bold", 15), variable=insect, value=1).place(x=350,
                                                                                                                    y=430)
    tk.Radiobutton(frame_alpr, text="armyworm", padx=20, width=4, bg="snow", font=("bold", 15), variable=insect, value=2).place(
        x=230, y=480)
    tk.Radiobutton(frame_alpr, text="beetle", padx=5, width=5, bg="snow", font=("bold", 15), variable=insect, value=3).place(x=350,
                                                                                                                    y=480)
    tk.Radiobutton(frame_alpr, text="bollworm", padx=20, width=4, bg="snow", font=("bold", 15), variable=insect, value=4).place(
        x=230, y=530)
    tk.Radiobutton(frame_alpr, text="grasshopper", padx=5, width=9, bg="snow", font=("bold", 15), variable=insect, value=5).place(x=350,
                                                                                                                    y=530)
    tk.Radiobutton(frame_alpr, text="mites", padx=20, width=4, bg="snow", font=("bold", 15), variable=insect, value=6).place(
        x=230, y=580)
    
    tk.Radiobutton(frame_alpr, text="mosquito", padx=5, width=7, bg="snow", font=("bold", 15), variable=insect, value=7).place(x=350,
                                                                                                                    y=580)
    tk.Radiobutton(frame_alpr, text="sawfly", padx=20, width=4, bg="snow", font=("bold", 15), variable=insect, value=8).place(
        x=230, y=630)
    tk.Radiobutton(frame_alpr, text="stem_borer", padx=5, width=10, bg="snow", font=("bold", 15), variable=insect, value=9).place(x=350,
                                                                                                                    y=630)
   

    button1 = tk.Button(frame_alpr,text="Submit",command=Detect,font=('times', 20, ' bold '),background='brown',width=10)
    button1.place(x=700,y=650)


    root.mainloop()

Train()