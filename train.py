from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve

from sklearn.metrics import confusion_matrix, accuracy_score

root = tk.Tk()
root.title("train")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('Slide1.jpeg')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


label_l2 = tk.Label(root, text="___Pesticide Suggestion___",font=("times", 30, 'bold','italic'),
                    background="green", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv("Pesticide.csv" )

data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv("Pesticide.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
   #data['StationId'] = le.fit_transform(data['StationId'])
    
   
    
    data['Temperature'] = le.fit_transform(data['Temperature'])
    data['Humidity'] = le.fit_transform(data['Humidity'])
    data['Moisture'] = le.fit_transform(data['Moisture'])
    data['Soil_Type'] = le.fit_transform(data['Soil_Type'])
    data['Crop_Type'] = le.fit_transform(data['Crop_Type'])
    data['Nitrogen'] = le.fit_transform(data['Nitrogen'])
    data['Potassium'] = le.fit_transform(data['Potassium'])
    data['Phosphorous'] = le.fit_transform(data['Phosphorous'])
    data['insect'] = le.fit_transform(data['insect'])

    
    

    """Feature Selection => Manual"""
    x = data.drop(['Pesticides'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Pesticides']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="grey",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=300, y=120)


def Model_Training():
    data = pd.read_csv("Pesticide.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
   #data['StationId'] = le.fit_transform(data['StationId'])
    
   
    
    data['Temperature'] = le.fit_transform(data['Temperature'])
    data['Humidity'] = le.fit_transform(data['Humidity'])
    data['Moisture'] = le.fit_transform(data['Moisture'])
    data['Soil_Type'] = le.fit_transform(data['Soil_Type'])
    data['Crop_Type'] = le.fit_transform(data['Crop_Type'])
    data['Nitrogen'] = le.fit_transform(data['Nitrogen'])
    data['Potassium'] = le.fit_transform(data['Potassium'])
    data['Phosphorous'] = le.fit_transform(data['Phosphorous'])
    data['insect'] = le.fit_transform(data['insect'])
    
    

    """Feature Selection => Manual"""
    x = data.drop(['Pesticides'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Pesticides']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=10)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear',random_state=10)
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=300,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as Pesticide_SVM_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=300,y=420)
    from joblib import dump
    dump (svcclassifier,"Pesticide_SVM_MODEL.joblib")
    print("Model saved as Pesticide_SVM_MODEL.joblib")

# def DT():
#     data = pd.read_csv("Pesticide.csv")
#     data.head()

#     data = data.dropna()

#     """One Hot Encoding"""

#     le = LabelEncoder()
    
#    #data['StationId'] = le.fit_transform(data['StationId'])
    
   
    
#     data['Temperature'] = le.fit_transform(data['Temperature'])
#     data['Humidity'] = le.fit_transform(data['Humidity'])
#     data['Moisture'] = le.fit_transform(data['Moisture'])
#     data['Soil_Type'] = le.fit_transform(data['Soil_Type'])
#     data['Crop_Type'] = le.fit_transform(data['Crop_Type'])
#     data['Nitrogen'] = le.fit_transform(data['Nitrogen'])
#     data['Potassium'] = le.fit_transform(data['Potassium'])
#     data['Phosphorous'] = le.fit_transform(data['Phosphorous'])

    
    

#     """Feature Selection => Manual"""
#     x = data.drop(['Pesticides'], axis=1)
#     data = data.dropna()

#     print(type(x))
#     y = data['Pesticides']
#     print(type(y))
#     x.shape

#     from sklearn.model_selection import train_test_split
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=10)

#     from sklearn.svm import SVC
#     from sklearn.tree import DecisionTreeClassifier
#     clf = DecisionTreeClassifier()
#     clf.fit(x_train, y_train)

#     y_pred = clf.predict(x_test)
#     print(y_pred)

    
#     print("=" * 40)
#     print("==========")
#     print("Classification Report : ",(classification_report(y_test, y_pred)))
#     print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
#     accuracy = accuracy_score(y_test, y_pred)
#     print("Accuracy: %.2f%%" % (accuracy * 100.0))
#     ACC = (accuracy_score(y_test, y_pred) * 100)
#     repo = (classification_report(y_test, y_pred))
    
    
#     label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label4.place(x=300,y=200)
    
#     label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as Pesticide_DT_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label5.place(x=300,y=420)
#     from joblib import dump
#     dump (clf,"Pesticide_DT_MODEL.joblib")
#     print("Model saved as Pesticide_DT_MODEL.joblib")


# def NB():
#     data = pd.read_csv("Pesticide.csv")
#     data.head()

#     data = data.dropna()

#     """One Hot Encoding"""

#     le = LabelEncoder()
    
#    #data['StationId'] = le.fit_transform(data['StationId'])
    
   
    
#     data['Temperature'] = le.fit_transform(data['Temperature'])
#     data['Humidity'] = le.fit_transform(data['Humidity'])
#     data['Moisture'] = le.fit_transform(data['Moisture'])
#     data['Soil_Type'] = le.fit_transform(data['Soil_Type'])
#     data['Crop_Type'] = le.fit_transform(data['Crop_Type'])
#     data['Nitrogen'] = le.fit_transform(data['Nitrogen'])
#     data['Potassium'] = le.fit_transform(data['Potassium'])
#     data['Phosphorous'] = le.fit_transform(data['Phosphorous'])

    
    

#     """Feature Selection => Manual"""
#     x = data.drop(['Pesticides'], axis=1)
#     data = data.dropna()

#     print(type(x))
#     y = data['Pesticides']
#     print(type(y))
#     x.shape

#     from sklearn.model_selection import train_test_split
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=6)

#    # from sklearn.svm import SVC
#     from sklearn.naive_bayes import GaussianNB  
#     clf = GaussianNB() 
#     clf.fit(x_train, y_train)

#     y_pred = clf.predict(x_test)
#     print(y_pred)
#     cm = confusion_matrix(y_test,y_pred)
#     cm
#     accuracy = (cm[0][0]+cm[1][1])/(cm[0][1] + cm[1][0] +cm[0][0] +cm[1][1])
    
#     print("=" * 40)
#     print("==========")
#     print("Classification Report : ",(classification_report(y_test, y_pred)))
#     print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
#     accuracy = accuracy_score(y_test, y_pred)
#     print("Accuracy: %.2f%%" % (accuracy * 100.0))
#     ACC = (accuracy_score(y_test, y_pred) * 100)
#     repo = (classification_report(y_test, y_pred))
    
    
#     label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label4.place(x=205,y=200)
    
#     label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as Pesticide_NB_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label5.place(x=205,y=420)
#     from joblib import dump
#     dump (clf,"Pesticide_NB_MODEL.joblib")
#     print("Model saved as Pesticide_NB_MODEL.joblib")



def call_file():
   from subprocess import call
   call(['python','predication.py'])





def window():
    root.destroy()

button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=20, height=2)
button2.place(x=5, y=120)


button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="SVM Training", command=Model_Training, width=20, height=2)
button3.place(x=5, y=220)


# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="DT Training", command=DT, width=20, height=2)
# button3.place(x=5, y=320)


# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="NB Training", command=NB, width=20, height=2)
# button3.place(x=5, y=420)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Pesticide Suggestion", command=call_file, width=20, height=2)
button4.place(x=5, y=320)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=420)

root.mainloop()
'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''