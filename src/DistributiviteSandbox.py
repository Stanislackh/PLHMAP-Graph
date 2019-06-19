# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivité"""

cas1 = "([a#b] + [[c#d] / [e#f]])# [g#h]"
# => [a#b]# [g#h] + [[c#d] / [e#f]]# [g#h]

cas2 = "(b+c)#a"  # CAS OK
cas8 = "a#b"
cas3 = "a #(b + c)"
# => a#b + a#c

cas4 = "(a+b)         #c"
# => a#c + b#c

cas5 = "Apollôn # (Puthios + Kedrieus)"
cas6 = "Apollôn + (Puthios + Kedrieus)"
cas7 = "[a + b] (a+s) + a"

"""Liste de cas"""
listeCas = [cas3]

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
    ")(": True,
    ")[": True,
    ")=": True,

    "[+": True,
    "[/": True,
    "[#": True,
    "[)": True,
    "[]": True,
    "[=": True,

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
    # Récupère les formules sans espaces
    listeCasNettoye = supprimeEspace(listeCas)

    # Si une des fonctions retourne True ne passe pas à la suite
    if (checkNbParCroch(listeCasNettoye) is False) and (caracMalPlace(listeCasNettoye) is False):

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

        # print(pileB)
        distributivite(pileB)  # Applique la distibutivité si il y en a


"""Regarde si les nombres de crochets et parenthèses ouvrante fermante sont identiques"""


def checkNbParCroch(listeCasNettoye):
    # Liste des variables locales
    nbParO = 0
    nbParF = 0
    nbCrochO = 0
    nbCrochF = 0

    for formule in listeCasNettoye:  # Regarde chaque formules
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


def caracMalPlace(listeCasNettoye):  # Regare dans la liste des erreurs de syntaxes si elle y figure

    syntaxeErreur = False

    for cas in listeCasNettoye:  # Regarde dans la liste des formules
        if syntaxeErreur == False:
            temp = cas.split(",")
            for phrase in temp:  # Regarde la formule
                # Regarde pour chaque paire de caractère si il figure dans le dictionnaire des erreurs
                for indice in range(len(phrase) - 1):
                    if ((phrase[indice] + phrase[indice + 1]) in dicoErreurs.keys()) or \
                            ((phrase[indice] == ")") and (phrase[indice + 1] not in signes.values())) or \
                            ((phrase[indice] == "]") and (phrase[indice + 1] not in signes.values())) or \
                            ((phrase[indice] not in signes.values()) and (phrase[indice + 1] == "(")) or \
                            ((phrase[indice] not in signes.values()) and (phrase[indice + 1] == "[")):
                        print("Erreur de saisie, Vérifiez la syntaxe de " + phrase)
                        print(phrase[indice] + phrase[indice + 1])
                        syntaxeErreur = True
                        return syntaxeErreur

    return syntaxeErreur


"""Supprime les espaces de la chaine de caractère"""


def supprimeEspace(listeCas):
    listeCasNettoye = []
    chaineSansEspace = ""

    for expression in listeCas:  # Ragarde pour chauqe expression
        for carac in expression:  # Regarde chaque caractère de l'expression, garde tous ceux différents de l'espace
            if carac == " ":
                pass
            else:
                chaineSansEspace += carac
        listeCasNettoye.append(chaineSansEspace)  # Rajoute l'expression sans les espaces
        chaineSansEspace = ""  # Vide la variable tampon

    return listeCasNettoye


"""(b+c)#a"""""


def distributivite(listeFormule):
    # Pile pour la gestion des  parentheses
    pileA = []
    pileB = []

    # Pile pour la gestion des  #
    pileC = []
    pileD = []

    # Resultat de la distributivité
    res = []

    for formule in listeFormule:  # Récupération de l'expression dans la parenthèse
        for indice in range(len(formule)):
            compt = indice
            if formule[indice] == "(":
                while formule[compt] != ")":
                    pileA.append(formule[compt])
                    compt += 1
            elif formule[indice] == "#":
                if (formule[indice - 1] not in signes.values()) and (formule[indice + 1] not in signes.values()):
                    pileD.append(formule[indice - 1])
                    pileD.append(formule[indice])
                    pileD.append(formule[indice + 1])
                elif formule[indice - 1] not in signes.values():
                    pileC.append(formule[indice - 1])
                    pileC.append(formule[indice])
                elif formule[indice + 1] not in signes.values():
                    pileC.append(formule[indice])
                    pileC.append(formule[indice + 1])

        if len(pileA) != 0:  # Supprime la première parenthèse
            del pileA[0]

        pileB.append(pileA)
        pileA = []

        for i in pileB:
            print(i)
            for j in i:
                print(j)
                if j not in signes.values():
                    res.append(j)
                    for k in pileC:
                        res.append(k)
                elif j == "+":
                    res.append(j)
    print(res)

    """ reste a faire la distributivité dans l'autre sens"""
    # print(pileA)
    # print(pileB)
    # print(pileC)
    # print(pileD)


splitPropre(listeCas)
