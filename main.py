import cv2
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from subprocess import call
from tkinter import *
from tkinter import messagebox
import tkinter.font as font


def close_window():  # pour fermer la fenetere quand on clique suir le button Quitter
    import sys
    sys.exit()

def copyrights():
	
	messagebox.showinfo('COPYRIGHTS', 'Created by Adnane Drief ')

def retake():
    
    Title = ttk.Label(root, text = "|| Let's Go ||  ", background="#8080ff", font=('times',20)).place(x = 240,y = 8) 
    btn1 = ttk.Button(root, text="Select your file", command=c_open_file_old , image = openIcon ,compound = LEFT).place(x = 235,y = 60)
    location = ttk.Label(root, text = "PATH : ", background="#8080ff", font=('times',15)).place(x = 20,y = 120) 
    

def c_open_file_old():
    rep = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='shell:MyComputerFolder',
    	initialfile='file',
    	filetypes=[
    		("All files", "*"),
    		("JPEG", "*.jpg"),
    		("PNG", ".png")])
    #print("Répore ou se trouve le fichier est : ",rep) // juste pour afficher le répertoire en console
    #afficher un libel qui met le chemin ou se trouve l'image 
    
    list = root.grid_slaves() 
    # détruire  le button qui contient le path a chaque fois quand veut réutulisé
    for l in list:
        l.destroy()

    for i in range(1,8):
        Label(root, background="#8080ff").grid(row=i)
    
    # changer le font du button de PATH
    s = ttk.Style()
    s.configure('my.TButton', font=('Times', 12))

    chemin = ttk.Button(root, text="  "+rep[0],style='my.TButton').grid(row=8)
    retake() #cette fonction c'est juste pour affiche de nouveau le contenu de départ sur les lables vides 

    try:
      
	   # os.startfile(rep[0])
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

        # Read the input image
        img = cv2.imread(rep[0])  # rep[0] est non pas rep tout seul car rep est un tableau d'argument
        scale_percent = 50 #  le pourcentage à prendre de l'image original càd on veut redimensionner l'image original de 25%

        width = int(img.shape[1] * scale_percent / 100) #longeur
        height = int(img.shape[0] * scale_percent / 100) #hauteur
        dim = (width, height)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Convert into grayscale
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(resized, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the output
        cv2.imshow('Detected faces', resized)
        cv2.waitKey()
        
    except IndexError:
        print("No file selected")
    
    
#----------------------------------------------------------
#            GUI
#----------------------------------------------------
root = tk.Tk()
root.geometry("600x250")
root.title("Face Recognition")
root.resizable(width=False,height=False)
root.configure(bg='#8080ff') # changer la couleur de background
style = ttk.Style(root)
style.theme_use("clam")
#----------------------------------------------------------
#             Position de  GUI
#----------------------------------------------------
# Récupérer les valeurs de la longeur et la largeur de la fenetre 
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight() 
#Récupérer la valeur de largeur/longeur de l'ecran et de l'onglet actuel 
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2-50)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/3+50)
 
# Positionner l'onglet dans le centre de l'ecran 
root.geometry("+{}+{}".format(positionRight, positionDown))
#==================================================================================================
icon1 = PhotoImage(file = r"image/exit.png") 
photoExit = icon1.subsample(8,8)
icon2 = PhotoImage(file = r"icons/open.png") 
openIcon = icon2.subsample(17,17)

#==================================================================================================
#==================================================================================================

   

Title = ttk.Label(root, text = "|| Let's Go ||  ", background="#8080ff", font=('times',20)).place(x = 240,y = 8) 
btn1 = ttk.Button(root, text="Select your file", command=c_open_file_old , image = openIcon ,compound = LEFT).place(x = 235,y = 60)

exitButton = ttk.Button (root, text = "Exit ", command = close_window,compound = LEFT,image = photoExit)
exitButton.place(x = 450, y = 195)

location = ttk.Label(root, text = "PATH : ", background="#8080ff", font=('times',15)).place(x = 20,y = 120) 

CopyrightButton=ttk.Button(root, text = "COPYRIGHTS",command=copyrights)
CopyrightButton.place(x = 20, y = 203)

root.mainloop()