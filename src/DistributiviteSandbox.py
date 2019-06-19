# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivit�"""

cas1 = "([a#b] + [[c#d] / [e#f]])# [g#h]"
# => [a#b]# [g#h] + [[c#d] / [e#f]]# [g#h]

cas2 = "a#(b+c)"  # CAS OK
cas3 = "a #(b + c)"
# => a#b + a#c

cas4 = "(a+b)         #c"
# => a#c + b#c

cas5 = "Apoll�n # (Puthios + Kedrieus)"
cas6 = "Apoll�n + (Puthios + Kedrieus)"
cas7 = "a+b(a+s)c"
"""Liste de cas"""
listeCas = [cas7]

""" Liste des signes pour les formules """

signes = {
    1: "+", 2: "/", 3: "#", 4: "(", 5: ")", 6: "[", 7: "]", 8: "=", 9: " "
}

dicoErreurs = {
    "+#": True,
    "+/": True,
    "+)": True,
    "+]": True,
    "+=": True,
    "++": True,

    "/+": True,
    "/#": True,
    "/)": True,
    "/]": True,
    "/=": True,
    "//": True,

    "#+": True,
    "#/": True,
    "#)": True,
    "#]": True,
    "#=": True,
    "##": True,

    "(+": True,
    "(/": True,
    "(#": True,
    "()": True,
    "(]": True,
    "(=": True,

    ")+": True,
    ")/": True,
    ")#": True,
    ")(": True,
    ")[": True,
    ")=": True,

    "[+": True,
    "[/": True,
    "[#": True,
    "[)": True,
    "[]": True,
    "[=": True,

    "]+": True,
    "]/": True,
    "]#": True,
    "](": True,
    "]=": True,
    "][": True,

    "=+": True,
    "=/": True,
    "=#": True,
    "=(": True,
    "=)": True,
    "=[": True,
    "=]": True,
    "==": True,
}

def splitPropre(listeCas):
    # Si une des fonctions retourne True ne passe pas � la suite
    if (checkNbParCroch(listeCas) is False) and (caracMalPlace(listeCas) is False):

        pileA = []
        pileB = []

        for cas in listeCas:  # Regarde dans la liste des formules
            temp = ""  # Variable temporaire pour stocker les caract�res non sp�ciaux
            for element in cas:
                if element not in signes.values():  # Si pas dans le dico des signes l'ajoute a temp
                    temp += element
                else:
                    if temp == "":  # Si temp est vide fait rien
                        pass
                    else:  # Sinon l'ajoute � la pile
                        pileA.append(temp)
                    if element != " ":  # Ajoute l'�l�ment si celui-ci est diff�rent de l'espace
                        pileA.append(element)
                    temp = ""
            if temp != "":  # Ajoute le dernier �l�ment si celui-ci est diff�rent de vide
                pileA.append(temp)
            pileB.append(pileA)
            pileA = []

        print(pileA)
        print(pileB)

    # else:
    #     print("ce symbole est inconnu erreur de saisie !")


"""Regarde si les nombres de crochets et parenth�ses ouvrante fermante sont identiques"""


def checkNbParCroch(listeCas):
    # Liste des variables locales
    nbParO = 0
    nbParF = 0
    nbCrochO = 0
    nbCrochF = 0

    for formule in listeCas:  # Regarde chaque formules
        for carac in formule:
            if carac == "(":  # Ajoute 1 si �gal a (
                nbParO += 1
            elif carac == ')':  # Ajoute 1 si �gal a )
                nbParF += 1
            elif carac == '[':  # Ajoute 1 si �gal a [
                nbCrochO += 1
            elif carac == "]":  # Ajoute 1 si �gal a ]
                nbCrochF += 1

    # Check le si le nombre de crochets et parenth�ses sont �gaux ouverture et fermeture
    erreur = False
    if (nbCrochF != nbCrochO) or (nbParF != nbParO):
        print("Erreur de syntaxe, V�rifiez le nombre de crochets et de parenth�ses")
        erreur = True

    return erreur


"""Regarde si des caract�res sp�ciaux sont mal plac�s"""


def caracMalPlace(listeCas):  # Regare dans la liste des erreurs de syntaxes si elle y figure

    syntaxeErreur = False

    for cas in listeCas:  # Regarde dans la liste des formules
        if syntaxeErreur == False:
            temp = cas.split(",")
            for phrase in temp:  # Regarde la formule
                # Regarde pour chaque paire de caract�re si il figure dans le dictionnaire des erreurs
                for indice in range(len(phrase) - 1):
                    if ((phrase[indice] + phrase[indice + 1]) in dicoErreurs.keys()) or \
                            ((phrase[indice] == ")") and (phrase[indice + 1] not in signes)) or \
                            ((phrase[indice] == "]") and (phrase[indice + 1] not in signes)) or \
                            ((phrase[indice] not in signes) and (phrase[indice + 1] == "(")) or \
                            ((phrase[indice] not in signes) and (phrase[indice + 1] == "(")):

                        print("Erreur de saisie, V�rifiez la syntaxe")
                        syntaxeErreur = True
                        return syntaxeErreur

    return syntaxeErreur
    # print(temp)
    # print(temp[0])


splitPropre(listeCas)
# caracMalPlace(listeCas)
