# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

import csv
import os

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
import tkinter.filedialog


# import AlgoTestFormuleSandBox

# Centre la fenetre
def geoliste(g):
    r = [i for i in range(0, len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]), int(g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])]


def centrefenetre(fen):
    fen.update_idletasks()
    l, h, x, y = geoliste(fen.geometry())
    fen.geometry("%dx%d%+d%+d" % (l, h, (fen.winfo_screenwidth() - l) // 2, (fen.winfo_screenheight() - h) // 2))


# Ferme la fenêtre en question
def fenDestroy(fenetre):
    fenetre.destroy()


# Fonction d'ouverture boite de dialogue pour l'import des CSV
def ouvrirCSV():
    global fichiers
    global listeNomFichiers
    fichiers = tkinter.filedialog.askopenfilenames(title="Ouvrir un fichier CSV", filetypes=[('CSV files', '.csv')])

    fi = 0
    listeNomFichiers = []
    for i in range(len(fichiers)):
        r = os.path.split(fichiers[fi])
        listeNomFichiers.append(r[1])
        fi += 1

    fenDestroy(fenAccueil)
    fenetrePrincipale()  # ouvre le fenêtre de résultat


# Fonction qui permet d'ouvrir la fenêtre d'aide
def fenetreAide():
    # Création de la fenêtre
    fenAide = Tk()
    fenAide.geometry("500x500")
    centrefenetre(fenAide)
    fenAide.title("Aide")

    # Titre en haut de la fenêtre
    titre = Label(fenAide, text="Comment utiliser l'application")
    titre.grid(column=1, row=0)

    # Première ligne de texte explicatif
    h1 = Label(fenAide, text="Je l'éditerai plus tard")
    h1.grid(column=0, row=1)


# Fonction qui fait appel à la barre des menus
def barreMenu(fenetre):
    # Barre de menu
    menubar = Menu(fenetre)
    fenetre.config(menu=menubar)

    # Onglet d'import des CSV
    menuCSV = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Importer CSV", menu=menuCSV)
    menuCSV.add_command(label="Importer CSV", command=ouvrirCSV)

    # Onglet d'ouverture de la page d'aide
    menuAide = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Aide", menu=menuAide)
    menuAide.add_command(label="Aide", command=fenetreAide)


# Ajoute les onglets à la fenêtre
def ongletsCSV(fenetre, listeNomFichiers):
    tabControl = ttk.Notebook(fenetre)
    # tabControl.grid(row=1, column=0, columnspan=50, rowspan=50, sticky='NSEW')
    tabControl.pack()

    nomOnglet = []  # Liste des noms d'onglets

    # Crée les onglets en fonction du nombre de ficheirs importés
    for j in range(len(listeNomFichiers)):
        nomOnglet.append("onglet_" + str(j))  # Crée un nom en boucle
        nomOnglet[j] = listeNomFichiers[j]  # l'onglet ercoit le nom du fichier
        nomOnglet[j] = ttk.Frame(tabControl)  # Permet de créer l'espace pour afficher l'onglet

        remplirOnglet(nomOnglet[j], listeNomFichiers[j])  # Fonction qui permet de remplir l'onglet

        tabControl.add(nomOnglet[j], text=listeNomFichiers[j])  # Ajoute l'onglet et le montre


# Fonction qui permet d'afficher les boutons de selection
def afficheBouton(fenetre):
    # Check all checkboxes
    boutonCheckAll = Button(fenetre, text="Check All", command="", width=15, height=5)
    boutonCheckAll.pack(side=LEFT, padx=5, pady=1)

    # Uncheck all checkboxes
    boutonUnchekAll = Button(fenetre, text="Uncheck All", command="", width=15, height=5)
    boutonUnchekAll.pack(side=LEFT, padx=5, pady=1)

    # Calcul avec le graphe valué
    boutonGrapheValue = Button(fenetre, text="Graphe value", command=fenetreGrpahe, width=15, height=5)
    boutonGrapheValue.pack(side=RIGHT, padx=5, pady=1)

    # Calcul avec la Coocurence
    boutonCooccurrence = Button(fenetre, text="Coocurrence", command=fenetreGrpahe, width=15, height=5)
    boutonCooccurrence.pack(side=RIGHT, padx=5, pady=1)

#Fonction qui remplis les onglets
def remplirOnglet(nomOnglet, nomFichier):
    with open(nomFichier, 'r', newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")

        ligne = 5  # Placement des lignes
        checkbox = []  # Noms des labels
        titre = 0
        for i in reader:
            if titre == 0:
                titre += 1
            else:
                checkbox.append("Label_" + str(i[0]))

                # lecture des lignes du csv
                checkbox[0] = IntVar()
                checkbox[0] = Checkbutton(nomOnglet, text=(str(i[1])))
                # labels[0].grid(column=3, row=ligne)
                checkbox[0].pack(anchor=W)

                ligne += 1  # Ajoute 1 pour passer à la ligne suivante

            # Fonction pour afficher la barre déroulante


# def barreDeroulante(fenetre):
#     scrollbar = Scrollbar(fenetre)
#     scrollbar.pack(side=LEFT, fill=Y)
#
#     scrollbar.config(command=resultat.yview)
#

# Création des checkboxes
def checkBoxes():
    # Création des checkboxes
    var1 = IntVar()
    Checkbutton(fenPrincipale, text="male", variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(fenPrincipale, text="female", variable=var2).grid(row=1, sticky=W)


# Permet d'afficher la ColorDialog
def choixCouleur():
    couleur = colorchooser.askcolor(title="Choisissez la couleur")
    print(couleur)


# Création de la fenêtre d'accueil
def fenetreAccueil():
    global fenAccueil

    # Création de la fenêtre
    fenAccueil = Tk()
    fenAccueil.geometry("500x500")
    centrefenetre(fenAccueil)
    fenAccueil.title("PLH / MAP")

    # Barre de status
    statusbar = Label(fenAccueil, text="Bienvenue, Je suis la barre de status", relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X)

    barreMenu(fenAccueil)  # Appel de la fonction qui affiche la barre de menu

    # Message d'accueuil
    titre = Label(fenAccueil, text="PLH / MAP")
    titre.pack()

    # Image de Présentation
    Can1 = Canvas(fenAccueil, width=500, height=500)
    photo = PhotoImage(file='images/map.gif')
    item = Can1.create_image(250, 250, image=photo)
    Can1.pack()

    fenAccueil.mainloop()


def fenetrePrincipale():
    global fenPrincipale

    fenPrincipale = Tk()
    fenPrincipale.geometry("500x500")
    centrefenetre(fenPrincipale)
    fenPrincipale.title("PLH / MAP")

    # # Barre de status
    # statusbar = Label(fenPrincipale, text="Bienvenue, Je suis la barre de status", relief=SUNKEN, anchor=W)
    # statusbar.grid(side=BOTTOM, fill=X)

    barreMenu(fenPrincipale)  # Appel de la fonction qui affiche la barre de menu

    ongletsCSV(fenPrincipale, listeNomFichiers)  # Appel dela fonction pour mettre des onglets par fichier

    afficheBouton(fenPrincipale)  # Affiche les boutons pour le type d'algo a utiliser et le check des checkboxes

    fenPrincipale.mainloop()


# Ouvrre le fenêtre pour la coocurence

def fenetreGrpahe():
    fenCoo = Toplevel()
    fenCoo.geometry("500x500")
    centrefenetre(fenCoo)
    fenCoo.title("Aide")

    # Barre de menu
    menubar = Menu(fenCoo)
    fenCoo.config(menu=menubar)

    # Onglet d'import des CSV
    menuOptions = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=menuOptions)
    menuOptions.add_command(label="Couleur Noeud", command=choixCouleur)
    menuOptions.add_command(label="Couleur Arc", command=choixCouleur)
    menuOptions.add_separator()
    menuOptions.add_command(label="Taille Noeud", command="")
    menuOptions.add_command(label="Taille Arc", command="")
    menuOptions.add_separator()
    menuOptions.add_command(label="Exporter Graphe", command="")

    fenCoo.mainloop()


if __name__ == "__main__":
    fenetreAccueil()
