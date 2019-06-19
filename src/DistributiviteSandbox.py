# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivité"""

cas1 = "([a#b] + [[c#d] / [e#f]])# [g#h]"
# => [a#b]# [g#h] + [[c#d] / [e#f]]# [g#h]

cas2 = "a#(b+c)"  # CAS OK
cas3 = "a #(b + c)"
# => a#b + a#c

cas4 = "(a+b)         #c"
# => a#c + b#c

cas5 = "Apollôn # (Puthios + Kedrieus)"
cas6 = "Apollôn + (Puthios + Kedrieus)"
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
    # Si une des fonctions retourne True ne passe pas à la suite
    if (checkNbParCroch(listeCas) is False) and (caracMalPlace(listeCas) is False):

        pileA = []
        pileB = []

        for cas in listeCas:  # Regarde dans la liste des formules
            temp = ""  # Variable temporaire pour stocker les caractères non spéciaux
            for element in cas:
                if element not in signes.values():  # Si pas dans le dico des signes l'ajoute a temp
                    temp += element
                else:
                    if temp == "":  # Si temp est vide fait rien
                        pass
                    else:  # Sinon l'ajoute à la pile
                        pileA.append(temp)
                    if element != " ":  # Ajoute l'élément si celui-ci est différent de l'espace
                        pileA.append(element)
                    temp = ""
            if temp != "":  # Ajoute le dernier élément si celui-ci est différent de vide
                pileA.append(temp)
            pileB.append(pileA)
            pileA = []

        print(pileA)
        print(pileB)

    # else:
    #     print("ce symbole est inconnu erreur de saisie !")


"""Regarde si les nombres de crochets et parenthèses ouvrante fermante sont identiques"""


def checkNbParCroch(listeCas):
    # Liste des variables locales
    nbParO = 0
    nbParF = 0
    nbCrochO = 0
    nbCrochF = 0

    for formule in listeCas:  # Regarde chaque formules
        for carac in formule:
            if carac == "(":  # Ajoute 1 si égal a (
                nbParO += 1
            elif carac == ')':  # Ajoute 1 si égal a )
                nbParF += 1
            elif carac == '[':  # Ajoute 1 si égal a [
                nbCrochO += 1
            elif carac == "]":  # Ajoute 1 si égal a ]
                nbCrochF += 1

    # Check le si le nombre de crochets et parenthèses sont égaux ouverture et fermeture
    erreur = False
    if (nbCrochF != nbCrochO) or (nbParF != nbParO):
        print("Erreur de syntaxe, Vérifiez le nombre de crochets et de parenthèses")
        erreur = True

    return erreur


"""Regarde si des caractères spéciaux sont mal placés"""


def caracMalPlace(listeCas):  # Regare dans la liste des erreurs de syntaxes si elle y figure

    syntaxeErreur = False

    for cas in listeCas:  # Regarde dans la liste des formules
        if syntaxeErreur == False:
            temp = cas.split(",")
            for phrase in temp:  # Regarde la formule
                # Regarde pour chaque paire de caractère si il figure dans le dictionnaire des erreurs
                for indice in range(len(phrase) - 1):
                    if ((phrase[indice] + phrase[indice + 1]) in dicoErreurs.keys()) or \
                            ((phrase[indice] == ")") and (phrase[indice + 1] not in signes)) or \
                            ((phrase[indice] == "]") and (phrase[indice + 1] not in signes)) or \
                            ((phrase[indice] not in signes) and (phrase[indice + 1] == "(")) or \
                            ((phrase[indice] not in signes) and (phrase[indice + 1] == "(")):

                        print("Erreur de saisie, Vérifiez la syntaxe")
                        syntaxeErreur = True
                        return syntaxeErreur

    return syntaxeErreur
    # print(temp)
    # print(temp[0])


splitPropre(listeCas)
# caracMalPlace(listeCas)
