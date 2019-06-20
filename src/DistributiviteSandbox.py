# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivit�"""

cas1 = "([a#b] + [[c#d] / [e#f]])# [g#h]"
# => [a#b]# [g#h] + [[c#d] / [e#f]]# [g#h]

cas5 = "Apoll�n # (Puthios + Kedrieus)"
cas6 = "(Zeus = H�ra) # S�t�r"

cas2 = "(Askl�pios + Hugieia + Telesphoros) # Alexiponos"
cas3 = "Alexiponos # (Askl�pios + Hugieia + Telesphoros)"

cas4 = "Dionusos # Phleos"

cas7 = "Apoll�n # (D�lios + Kalumnas-Mede�n)"
"""Liste de cas"""

listeCas = [cas6,cas4,cas7]

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
    # R�cup�re les formules sans espaces
    listeCasNettoye = supprimeEspace(listeCas)

    # Si une des fonctions retourne True ne passe pas � la suite
    if (checkNbParCroch(listeCasNettoye) is False) and (caracMalPlace(listeCasNettoye) is False):

        pileA = []
        pileB = []

        for cas in listeCasNettoye:  # Regarde dans la liste des formules
            print(cas)
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

            # print(pileB)
            distributiviteParentheses(pileB)  # Applique la distibutivit� si il y en a a la liste de formule


"""Regarde si les nombres de crochets et parenth�ses ouvrante fermante sont identiques"""


def checkNbParCroch(listeCasNettoye):
    # Liste des variables locales
    nbParO = 0
    nbParF = 0
    nbCrochO = 0
    nbCrochF = 0

    for formule in listeCasNettoye:  # Regarde chaque formules
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


def caracMalPlace(listeCasNettoye):  # Regarde dans la liste des erreurs de syntaxes si elle y figure

    syntaxeErreur = False

    for cas in listeCasNettoye:  # Regarde dans la liste des formules
        if syntaxeErreur == False:
            temp = cas.split(",")
            for phrase in temp:  # Regarde la formule
                # Regarde pour chaque paire de caract�re si il figure dans le dictionnaire des erreurs
                for indice in range(len(phrase) - 1):
                    if ((phrase[indice] + phrase[indice + 1]) in dicoErreurs.keys()) or \
                            ((phrase[indice] == ")") and (phrase[indice + 1] not in signes.values())) or \
                            ((phrase[indice] == "]") and (phrase[indice + 1] not in signes.values())) or \
                            ((phrase[indice] not in signes.values()) and (phrase[indice + 1] == "(")) or \
                            ((phrase[indice] not in signes.values()) and (phrase[indice + 1] == "[")):
                        print("Erreur de saisie, V�rifiez la syntaxe de " + phrase)
                        print(phrase[indice] + phrase[indice + 1])
                        syntaxeErreur = True
                        return syntaxeErreur

    return syntaxeErreur


"""Supprime les espaces de la chaine de caract�re"""


def supprimeEspace(listeCas):
    listeCasNettoye = []
    chaineSansEspace = ""

    for expression in listeCas:  # Ragarde pour chauqe expression
        for carac in expression:  # Regarde chaque caract�re de l'expression, garde tous ceux diff�rents de l'espace
            if carac == " ":
                pass
            else:
                chaineSansEspace += carac
        listeCasNettoye.append(chaineSansEspace)  # Rajoute l'expression sans les espaces
        chaineSansEspace = ""  # Vide la variable tampon

    return listeCasNettoye


"""(b+c)#a"""""


def distributiviteParentheses(listeFormule):
    # Pile pour la gestion des  parentheses
    pileA = []
    pileB = []

    # Pile pour la gestion des  #
    pileC = []
    pileD = []
    pileE = []
    # Resultat de la distributivit�
    res = []

    dicoResultat = {}
    dicoResultatCle = 0

    for formule in listeFormule:  # R�cup�ration de l'expression dans la parenth�se
        for index in range(len(formule)):
            compt = index
            if formule[index] == "(":
                while formule[compt] != ")":
                    pileA.append(formule[compt])
                    compt += 1

            elif formule[index] == ("#" or "="):  # Ajoute a # b
                if (formule[index - 1] not in signes.values()) and (formule[index + 1] not in signes.values()):
                    pileD.append(formule[index - 1])
                    pileD.append(formule[index])
                    pileD.append(formule[index + 1])
                elif formule[index - 1] not in signes.values():  # Ajoute a #
                    pileC.append(formule[index - 1])
                    pileC.append(formule[index])
                elif formule[index + 1] not in signes.values():  # Ajoute # b
                    pileC.append(formule[index])
                    pileC.append(formule[index + 1])

        if len(pileA) != 0:  # Supprime la premi�re parenth�se
            del pileA[0]

        pileB.append(pileA)  # Rajoute les �lements a la pileB
        pileA = []  # R�initialise la pila A

        for i in formule:
            if i == "(" or ")":
                for k in range(len(pileB)):  # Regarde l'expression stock� qui �tait dans la parenth�se
                    dicoResultat[dicoResultatCle] = res  # Ajoute au dictionnaire
                    dicoResultatCle += 1  # Incr�mente la cl�

                    for index in range(len(formule) - 1):
                        # Si la formule contient )# distribue de cette fa�on
                        if formule[index] + formule[index + 1] == ")#":
                            for j in pileB[k]:
                                if j not in signes.values():  # Regarde si le caract�re est sp�cial si non l'ajoute
                                    res.append(j)
                                    for k in pileC:  # Rajoute les elements stock�s
                                        res.append(k)
                                elif j == "+" or j == "=":  # Ajoute l'op�rateur
                                    res.append(j)

                        # Si la formule contient #( distribue de cette fa�on
                        elif formule[index] + formule[index + 1] == "#(":
                            for j in pileB[k]:
                                if j not in signes.values():  # Regarde si le caract�re est sp�cial si non l'ajoute
                                    for k in pileC:  # Rajoute les elements stock�s
                                        res.append(k)
                                    res.append(j)
                                elif j == "+" or j == "=":  # Ajoute l'op�rateur
                                    res.append(j)

                    else:
                        for i in pileD:  # Ajoute la formule sans parenth�ses
                            res.append(i)
                    # R�initialise les variables
                    pileB = []
                    pileC = []
                    pileD = []
                    res = []

    print(dicoResultat)
    return dicoResultat


splitPropre(listeCas)
