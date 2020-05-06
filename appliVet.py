# Créé par NICOLAS, le 18/05/2016 en Python 3.2

import tkinter as tk
# pour utiliser un objet tkinter on fera précéder le nom par tk.

from random import randint
from tkinter import ttk

from PIL import Image, ImageTk

meteo = ['froid','pluvieux','couvert','beau','chaud']
evenements = ['travail','sortie','sport','maison','ceremonie']

fenetre = tk.Tk()
fenetre.title("Que mettre aujourd'hui")

# on crée un canvas pour pouvoir insérer la photo de la personne
image1 = tk.Canvas(fenetre, width=100,height=100, bg="black")
image1.grid(row=1, column=1)
image2 = tk.Canvas(fenetre, width=100,height=100, bg="black")
image2.grid(row=2, column=1)
# grace à PIL on insère la photo dans le canvas
# image redimensionnée grace à paint avec un longueur ou lageur maximale de 100px
pilImage1 = Image.open("haut1.png")
imag1 = ImageTk.PhotoImage(pilImage1)
imagesprite1 = image1.create_image(50,50,image=imag1) # les deux 50 correspondent au centre de la photo

pilImage2 = Image.open("bas1.png")
imag2 = ImageTk.PhotoImage(pilImage2)
imagesprite2 = image2.create_image(50,50,image=imag2)

#select1 = StringVar()
ListeCombo1 = ttk.Combobox(fenetre, values=meteo)
ListeCombo1.grid(row=1, column=2)

ListeCombo2 = ttk.Combobox(fenetre, values=evenements)
ListeCombo2.grid(row=2, column=2)

quitter = tk.Button(text='Quitter', command = fenetre.destroy)
quitter.grid(row=5, column=3,columnspan=2)

fenetre.mainloop()

