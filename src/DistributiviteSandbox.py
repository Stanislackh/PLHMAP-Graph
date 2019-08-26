# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivit�"""
from itertools import combinations

cas1 = "([a#b]+[[c#d]/[e#f]])#[g#h]"  # OK
# => [a#b]#[g#h]+[[c#d]/[e#f]]#[g#h]

cas2 = "Apoll�n#(Puthios+Kedrieus)"  # OK

cas3 = "(Zeus+H�ra)#S�t�r"  # OK

cas4 = "Apoll�n # (Puthios + Kedrieus)"  # OK

cas5 = "[Theos#S�t�r]#(Artemis+Apoll�n)"  # OK

cas6 = "[[Zeus/H�lios]/[Megas#Sarapis]]+[Sunnaoi#Theoi]"  # OK

cas7 = "([Isis#S�t�r]/Astart� / [Aphrodit� # Euploia]) # Ep�koos + [Er�s / Harpokrat�s / Apoll�n]"  # OK

cas8 = "[dieux # saints] # de Byblos"  # OK

cas9 = "Ashtart # [dans le sanctuaire # [du dieu # de Hamon]]"  # OK

cas10 = "[Apoll�n # Puthios] + [Apoll�n # Kedrieus]"  # OK

cas11 = "[Amm�n=Chnoubis]+[H�ra=Satis]+[Hestia=Anoukis]+[Dionusos=Petempamentis]+[Hallos#Theos]"  # OK

cas12 = "([Kurios # Zeus] + H�ra) # Ep�koos"  # OK

cas13 = "� mes dames # ([[� la d�esse # puissante] # Isis] / [la d�esse # Ashtart]) + [aux dieux # qui]"
# Cas 13 Explose et j'arrive pas � lire ...

listeCas2 = [cas10]  # Fonctionne pas

listeCas = [cas1, cas2, cas3, cas4, cas5, cas6, cas7, cas8, cas9, cas10, cas11, cas12, cas13]  # Fonctionne

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
    dicoResultat = {}
    dicoResultatCle = 0

    # R�cup�re les formules sans espaces
    listeCasNettoye = supprimeEspace(listeCas)

    print("listeCasNettoye")
    print(listeCasNettoye)

    # Si une des fonctions retourne True ne passe pas � la suite
    if (checkNbParCroch(listeCasNettoye) is False) and (caracMalPlace(listeCasNettoye) is False):
        pileA = []

        for cas in listeCasNettoye:  # Regarde dans la liste des formules
            pileB = []
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

            # print("PileB")
            # print(pileB)

            res = allInOne(pileB)

            # Applique la distibutivit� si il y en a � la liste de formule
            dicoResultat[dicoResultatCle] = distributiviteCrochet(res)
            dicoResultatCle += 1  # incr�mente la cl� du dictionnaire

            dicoReecrit = {}
            cle = 0

            for objet in dicoResultat.values():
                trigger = ""
                for i in objet:
                    for j in i:
                        trigger += j

                dicoReecrit[cle] = trigger
                cle += 1

        print("dicor��crit Version lisible ")
        for i, j in dicoReecrit.items():
            print(i, j)
            print("")


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


def distributiviteCrochet(listeFormule):
    dist = False  # Garde pour lancer la s�quence

    # print("ListeFormule")
    # print(listeFormule)

    for i in listeFormule:  # Regarde si un # est dans l'expression pour la distributivit�
        for j in i:
            if j == "#":
                dist = True

    if dist is True:  # Si la garde est lev�e

        print("Liste Formule")
        print(listeFormule)

        # Pile pour la gestion des  parentheses
        pileA = []
        pileB = []
        # Pile pour la gestion des  #
        pileC = []
        pileD = []
        pileE = []

        # Resultat de la distributivit�
        res = []

        garde = False  # Garde pour lancer la s�quence

        for formule in listeFormule:  # R�cup�ration de l'expression dans la parenth�se

            print("fomuleaasdasd")
            print(formule)

            for i in formule:  # Regarde si il y a des parenth�ses avant de lancer la s�uence suivante
                if i == "(":
                    garde = True  # L�ve la garde
                    break

            if garde is True:  # Si la garde est lev�e lance la sequence
                for index in range(len(formule)):
                    compt = index
                    if formule[index] == "(":
                        while formule[compt] != ")":
                            pileA.append(formule[compt])
                            compt += 1

                        print("pileA njnjnjnjn")
                        print(pileA)

                    elif formule[index] == ("#" or "=" or "/" or "+"):  # Ajoute a # b
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
                    else:
                        pileE.append(formule[index])  # R�cup�re l'expression

                print("PileE")
                print(pileE)

                if len(pileA) != 0:  # Supprime la premi�re parenth�se
                    del pileA[0]

                print("pileA resresrse")
                print(pileA)

                print("pileB resresrse")
                print(pileB)

                print("pileC resresrse")
                print(pileC)

                print("pileD resresrse")
                print(pileD)

                pileB.append(pileA)  # Rajoute les �lements a la pileB
                pileA = []  # R�initialise la pile A

                for i in formule:
                    for k in range(len(pileB)):  # Regarde l'expression stock� qui �tait dans la parenth�se
                        for index in range(len(formule) - 1):
                            # Si la formule contient )# distribue de cette fa�on
                            if formule[index] + formule[index + 1] == ")#":
                                for j in pileB[k]:
                                    if j not in signes.values():  # Regarde si le caract�re est sp�cial si non l'ajoute
                                        res.append("[")  # Ajoute les crochets pour marqeur l'ensemble
                                        res.append(j)
                                        for k in pileC:  # Rajoute les elements stock�s
                                            res.append(k)
                                        res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                                    elif j == "+" or j == "=" or j == "/" or "+":  # Ajoute l'op�rateur
                                        res.append(j)

                            # Si la formule contient #( distribue de cette fa�on
                            elif formule[index] + formule[index + 1] == "#(":
                                for j in pileB[k]:
                                    if j not in signes.values():  # Regarde si le caract�re est sp�cial si non l'ajoute
                                        res.append("[")  # Ajoute les crochets pour marquer l'ensemble
                                        for k in pileC:  # Rajoute les elements stock�s
                                            res.append(k)
                                        res.append(j)
                                        res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                                    elif j == "+" or j == "=" or j == "/" or "+":  # Ajoute l'op�rateur
                                        res.append(j)

                            else:
                                for l in pileD:  # Ajoute la formule sans parenth�ses
                                    res.append(l)

                        # R�initialise les variables
                        pileB = []
                        pileC = []
                        pileD = []

                    for i in pileE:  # Regarde dans la liste les �lement qui manquent et les rajoute
                        if i not in res and i != ")":
                            res.append(i)

                    return res
            else:
                return listeFormule
    else:
        return listeFormule


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
            for k in range(len(pileB)):  # Regarde l'expression stock� qui �tait dans la parenth�se
                dicoResultat[dicoResultatCle] = res  # Ajoute au dictionnaire
                dicoResultatCle += 1  # Incr�mente la cl�

                for index in range(len(formule) - 1):
                    # Si la formule contient )# distribue de cette fa�on
                    if formule[index] + formule[index + 1] == ")#":
                        for j in pileB[k]:
                            if j not in signes.values():  # Regarde si le caract�re est sp�cial si non l'ajoute
                                res.append("[")  # Ajoute les crochets pour marqeur l'ensemble
                                res.append(j)
                                for k in pileC:  # Rajoute les elements stock�s
                                    res.append(k)
                                res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                            elif j == "+" or j == "=":  # Ajoute l'op�rateur
                                res.append(j)

                    # Si la formule contient #( distribue de cette fa�on
                    elif formule[index] + formule[index + 1] == "#(":
                        for j in pileB[k]:
                            if j not in signes.values():  # Regarde si le caract�re est sp�cial si non l'ajoute
                                res.append("[")  # Ajoute les crochets pour marquer l'ensemble
                                for k in pileC:  # Rajoute les elements stock�s
                                    res.append(k)
                                res.append(j)
                                res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                            elif j == "+" or j == "=":  # Ajoute l'op�rateur
                                res.append(j)

                else:
                    for l in pileD:  # Ajoute la formule sans parenth�ses
                        res.append(l)
                # R�initialise les variables
                pileB = []
                pileC = []
                pileD = []
                res = []

    print("dico resultat")
    print(dicoResultat)
    return dicoResultat


def allInOne(listedeListe):
    suite = False  # Permet de faire le traitement des crochets
    enListe = []  # Liste vide
    finale = []  # Liste finale
    lastList = []  # Vraie liste finale

    for i in listedeListe:  # V�rifie si l'expression � des crochets
        for j in i:
            if j == "[":
                suite = True
                break

    if suite is True:  # Si l'expression a des crochets
        for i in listedeListe:  # R�cup�re l'expression dans la liste
            for j in i:
                enListe.append(j)

        elemSep = []  # Variables interm�diaires
        nette = []
        final = []

        element = ""
        cpt = 0
        garde = False

        print("listedeListe")
        print(listedeListe)

        for indice in range(len(enListe)):  # Pour la longueur de l'expression
            if element != "":  # si element est diff�rente de ""
                elemSep.append(element)  # Ajoute a la liste des elements entre crochets en 1 element
                element = ""  # R�initialise element

            if enListe[indice] == "[" and enListe[indice + 1] != "[":  # Si pas 2 crochets succ�ssifs
                if garde is False and enListe[0] == "[":
                    element += enListe[cpt]
                    garde = True
                while enListe[cpt] != "]":  # Tant que l'element de la liste est diff�rent de ]
                    element += enListe[cpt + 1]
                    cpt += 1

            cpt = indice  # donne la valeur de l'indice a cpt pour pouvoir continuer a l'indice arr�t�

        # print("SepElem")
        # print(elemSep)

        indice = 0
        pos = 0

        co = 0
        cf = 0
        blap = True

        while indice < len(enListe):  # Tant que indice est inf�rieur a la longueur de la liste de l'expression

            if enListe[indice] == "[":
                co += 1

            if enListe[indice] == "[" and enListe[indice + 1] != "[":  # Si pas 2 crochets cons�cutifs
                re = indice
                while enListe[re] != "]":  # Tant que l'indice est diff�rent de ] avance l'indice
                    re += 1
                nette.append(elemSep[pos])  # Ajoute l'�l�ment de la liste a la liste interm�diaire

                pos += 1  # Avance la position
                indice = re

            else:
                if enListe[indice] == "]" and enListe[indice - 1] == "]":
                    nette.append(enListe[indice])  # Sinon ajoute � la liste
                    indice += 1
                    cf -= 1

                elif enListe[indice] == "]" and enListe[indice - 1] != "]":  # Si 2 crochets cons�cutifs avance l'indice
                    cf += 1
                    if co == cf and blap is True:
                        nette.append(enListe[indice])
                        blap = False
                        indice += 1
                    else:
                        indice += 1
                else:
                    nette.append(enListe[indice])  # Sinon ajoute � la liste
                    indice += 1

        print("nette")
        print(nette)

        for i in range(len(nette)):  # pour la longeur de la liste
            if nette[i] == "[" and nette[i + 1] != "[":  # Si pas 2 crochets cons�cutifs
                re = i
                trigger = ""
                while nette[re - 1] != "]":  # Tant que l'element est diff�rent de ] avance l'indice

                    # print("trigger")
                    # print(trigger)

                    trigger += nette[re]
                    re += 1
                final.append(trigger)  # Ajoute la la liste

        # print("final")
        # print(final)

        indice = 0
        pos = 0

        while indice < len(nette):  # Tant que l'indice est inf�rieur a la longueur de la liste
            if nette[indice] == "[" and nette[indice + 1] != "[":  # Si pas 2 crochets cons�cutifs
                re = indice
                while nette[re - 1] != "]":  # Tant que l'element est diff�rent de ] avance l'indice
                    re += 1
                finale.append(final[pos])  # Ajoute l'�l�ment � la liste
                pos += 1
                indice = re

            else:
                if nette[indice] == "]":
                    indice += 1
                else:
                    finale.append(nette[indice])  # Ajoute l'element � la liste
                    indice += 1

        # print("finale")
        # print(finale)

        lastList.append(finale)

        return lastList

    else:

        # print("listedeliste")
        # print(listedeListe)

        return listedeListe


if __name__ == "__main__":
    splitPropre(listeCas2)
    # allInOne(cas1)
