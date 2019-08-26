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

import DistributiviteSandbox
import AncienneMethode
import NouvelleMethode
import pyvis_network_graph
import VerificationFormules


# Boutton reset
def resetProg():
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

    # Fonction d'ouverture boite de dialogue pour l'import des CSV
    def ouvrirCSV():
        global fichiers
        global listeNomFichiers
        global fileName

        fichiers = tkinter.filedialog.askopenfilenames(title="Ouvrir un fichier CSV", filetypes=[('CSV files', '.csv')])

        fi = 0
        listeNomFichiers = []
        fileName = []
        for i in range(len(fichiers)):
            r1, r2 = os.path.split(fichiers[fi])  # Coupe le path et le fichier

            nom, extension = os.path.splitext(r2)  # Garle le nom sans l'extension du fichier
            fileName.append(nom)

            listeNomFichiers.append(r2)  # Récupère le nom du fichier

            fi += 1

        fenDestroy(fenAccueil)  # Détruit la fenêtre d'accueil

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

    # Ajoute les onglets à la fenêtre
    def ongletsCSV(fenetre, listeNomFichiers):
        tabControl = ttk.Notebook(fenetre)
        tabControl.pack()

        nomOnglet = []  # Liste des noms d'onglets

        # Crée les onglets en fonction du nombre de ficheirs importés
        for j in range(len(listeNomFichiers)):
            nomOnglet.append("onglet_" + str(j))  # Crée un nom en boucle
            nomOnglet[j] = fileName[j]  # l'onglet recoit le nom du fichier
            nomOnglet[j] = ttk.Frame(tabControl, width=500,
                                     height=300)  # Permet de créer l'espace pour afficher l'onglet

            # Création du canvas qui permet d'avoir la barre déroulante et afficher les lignes du CSV avec checkboxes
            canvas = Canvas(nomOnglet[j], width=400, height=300)
            scroll = Scrollbar(nomOnglet[j], command=canvas.yview)

            canvas.config(yscrollcommand=scroll.set, scrollregion=(0, 0, 100, 5000))
            canvas.pack(side=LEFT, fill=BOTH, expand=True)
            scroll.pack(side=LEFT, fill=Y)

            frame = Frame(canvas, width=150, height=3000)

            remplirOnglet(frame, listeNomFichiers[j])  # Fonction qui permet de remplir l'onglet

            canvas.create_window(100, 1000, window=frame)

            # barreDeroulante(nomOnglet[j])  # Ajoute une barre déroulante dans l'onglet

            nomOnglet[j].pack_propagate(False)  # Evite l'aggrandissmenet dynamique
            tabControl.add(nomOnglet[j], text=fileName[j])  # Ajoute l'onglet et le montre et le nomme

    # Fonction qui permet d'afficher les boutons de selection et la fonction Check Uncheck
    def afficheBouton(fenetre):
        # Coche toutes les checkboxes
        def cocheTout(boxs=listeCheckboxes):
            for i in range(len(boxs)):
                boxs[i].select()
                listeV[i].set(1)

        # Décoche toutes les checkboxes
        def decocheTout(boxs=listeCheckboxes):
            for i in range(len(boxs)):
                boxs[i].deselect()
                listeV[i].set(0)

        # Check all checkboxes
        boutonCheckAll = Button(fenetre, text="Check All", command=cocheTout, width=10, height=5)
        boutonCheckAll.pack(side=LEFT, padx=5, pady=1)

        # Uncheck all checkboxes
        boutonUnchekAll = Button(fenetre, text="Uncheck All", command=decocheTout, width=10, height=5)
        boutonUnchekAll.pack(side=LEFT, padx=5, pady=1)

        # Calcul avec le graphe valué
        boutonGrapheValue = Button(fenetre, text="Graphe value",
                                   command=lambda: [NouvelleMethode.calculEG(recupererCheckboxCheck()),
                                                    pyvis_network_graph.create_graph(NouvelleMethode.nomfichierEdge)],
                                   width=10, height=5)
        boutonGrapheValue.pack(side=RIGHT, padx=5, pady=1)

        # Calcul avec la Coocurence
        boutonCooccurrence = Button(fenetre, text="Coocurrence",
                                    command=lambda: [AncienneMethode.coocurrence(recupererCheckboxCheck()),
                                                     pyvis_network_graph.create_graph(AncienneMethode.nameFileEdge)],
                                    width=10, height=5)
        boutonCooccurrence.pack(side=RIGHT, padx=5, pady=1)

        ButtonReset = Button(fenetre, text="RESET", command=resetProg, width=10, height=5)
        ButtonReset.pack()

        # Fonction qui remplit les onglets

    # Fonction pour récupére la liste des checkboxes cochées
    def recupererCheckboxCheck():
        listeCheck = []

        for i in range(len(listeV)):

            if listeV[i].get() == 1:
                listeCheck.append(listeLabels[i])
        messagebox.showinfo("Formules sélectionnées", str(listeCheck))  # Affiche la liste des formules selectionnées

        if VerificationFormules.checkNbParCroch(listeCheck) is True:
            messagebox.showinfo("Erreur de Crochets ou Parenthèses",
                                "Erreur de syntaxe, Vérifiez le nombre de crochets et de parenthèses dans la formule : "
                                + VerificationFormules.kek)
        elif VerificationFormules.caracMalPlace(listeCheck) is True:
            messagebox.showinfo("Erreur de Synthaxe", "Erreur de saisie, Vérifiez la syntaxe de la formule : "
                                + VerificationFormules.phrase)
        else:
            return listeCheck

    # Fonction pour remplir les onglets
    def remplirOnglet(canvas, nomFichier):
        global listeCheckboxes
        global listeV
        global listeLabels

        with open(nomFichier, 'r', newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            ligne = 1  # Placement des lignes
            cases = []  # Noms des labels
            v = []  # Valeur des variables
            labels = []

            listeCheckboxes = []  # Les boxes
            listeV = []  # les valeurs
            listeLabels = []  # Les formules

            titre = 0

            for i in reader:
                # print(i)
                if titre == 0:
                    titre += 1
                else:
                    listeLabels.append(str(i[1]))
                    cases.append("Label_" + str(i[0]))
                    v.append("Label_" + str(i[0]))
                    # lecture des lignes du csv
                    v[0] = IntVar()
                    cases[0] = Checkbutton(canvas, variable=v[0], text=(str(i[1])))
                    cases[0].pack(anchor=W)

                    listeCheckboxes.append(cases[0])  # Ajoute les checkboxes
                    listeV.append(v[0])
                    ligne += 1  # Ajoute 1 pour passer à la ligne suivante

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
        statusbar = Label(fenAccueil, text="PLH/MAP", relief=SUNKEN, anchor=W)
        statusbar.pack(side=BOTTOM, fill=X)

        barreMenu(fenAccueil)  # Appel de la fonction qui affiche la barre de menu

        # Message d'accueuil
        titre = Label(fenAccueil, text="PLH / MAP")
        titre.pack()

        boutonOpenCSV = Button(fenAccueil, text="Ouvrir CSV", command=ouvrirCSV, width=15, height=5)
        boutonOpenCSV.pack()

        # Image de Présentation
        Can1 = Canvas(fenAccueil, width=500, height=500)
        photo = PhotoImage(file='images/map.gif')
        item = Can1.create_image(250, 200, image=photo)
        Can1.pack()

        fenAccueil.mainloop()

    # Création de la fenêtre principale
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

        ongletsCSV(fenPrincipale, listeNomFichiers)  # Appel de la fonction pour mettre des onglets par fichier

        afficheBouton(fenPrincipale)  # Affiche les boutons pour le type d'algo à utiliser et le check des checkboxes

        fenPrincipale.mainloop()

    # Ouvre le fenêtre pour la coocurence ou le graphe valué
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

    fenetreAccueil()


if __name__ == "__main__":
    resetProg()
