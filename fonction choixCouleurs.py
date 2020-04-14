import tkinter as tk

def choixCouleur() :
   couleur = coul.get()
   if couleur == "noir":
    affichageCouleur.configure(text="Vous pouvez ajouter des pièces de n'importe quelle couleur.")
   if couleur == "blanc":
    affichageCouleur.configure(text="Vous pouvez ajouter des pièces de n'importe quelle couleur.")
   if couleur == "rouge" :
    affichageCouleur.configure(text="Vous pouvez ajouter des pièces noires ou blanches.")
   if couleur == "jean":
    affichageCouleur.configure(text="Vous pouvez ajouter des pièces de n'importe quelle couleur sauf du jean.")
   if couleur == "marine":
    affichageCouleur.configure(text="Evitez d'ajouter des pièces noires.")
   if couleur == "vert":
    affichageCouleur.configure(text="Evitez d'ajouter des pièces rouges.")
   if couleur == "orange":
    affichageCouleur.configure(text="Evitez d'ajouter des pièces roses.")
   if couleur == "violet":
    affichageCouleur.configure(text="Evitez d'ajouter des pièces jaunes.")
   if couleur == "beige":
    affichageCouleur.configure(text="Vous pouvez ajouter des pièces noires ou blanches.")
   if couleur == "doré":
    affichageCouleur.configure(text="Ne pas ajouter de pièces argenteés.")


fenetre = tk.Tk()

coul = tk.StringVar()
tk.Label(text="Entrez une couleur : ").grid(row=0, column=0)
tk.Entry(textvariable = coul).grid(row=0,column=1)

tk.Button(text="Valider", command=choixCouleur).grid(row=0,column=2)

affichageCouleur = tk.Label()
affichageCouleur.grid(row=1, column=0, columnspan=3)

fenetre.mainloop()