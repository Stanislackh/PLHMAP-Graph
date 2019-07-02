# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivit�"""

cas1 = "([a#b]+[[c#d]/[e#f]])#[g#h]"  # OK
# => [a#b]#[g#h]+[[c#d]/[e#f]]#[g#h]

cas5 = "Apoll�n#(Puthios+Kedrieus)"  # OK

cas6 = "(Zeus+H�ra)#S�t�r"  # OK

cas2 = "Apoll�n # (Puthios + Kedrieus)"  # OK

cas3 = "[Theos#S�t�r]#(Artemis+Apoll�n)"  # OK

cas4 = "[[Zeus/H�lios]/[Megas#Sarapis]]+[Sunnaoi#Theoi]"  # OK

cas7 = "(([Isis#S�t�r]/Astart� / [Aphrodit� # Euploia]) # Ep�koos) + [Er�s / Harpokrat�s / Apoll�n]"  # Blap les /

cas8 = "[dieux # saints] # de Byblos"  # Double entr�e

cas9 = "Ashtart # [dans le sanctuaire # [du dieu # de Hamon]]"  # Poser la question de la distribution

cas10 = "[Apoll�n # Puthios] + [Apoll�n # Kedrieus]"  # OK

cas11 = "[Amm�n=Chnoubis]+[H�ra=Satis]+[Hestia=Anoukis]+[Dionusos=Petempamentis]+[Hallos#Theos]"  # OK

cas12 = "([Kurios # Zeus] + H�ra) # Ep�koos"  # OK

cas13 = [["(", "[a#b]", "+", "[[c#d]/[e#f]]", ")", "#", "[g#h]"]]

listeCas = [cas7, cas8, cas9]  # Fonctionne pas

listeCas2 = [cas1, cas5, cas2, cas6, cas3, cas4, cas10, cas11, cas12]  # Fonctionne

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
            dicoResultat[dicoResultatCle] = distributiviteCrochet(
                res)  # Applique la distibutivit� si il y en a a la liste de formule
            dicoResultatCle += 1

            print("Dicoresultat yay")
            print(dicoResultat)


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
    dist = False
    sansDiese = []

    print("ListeFormule")
    print(listeFormule)

    for i in listeFormule:  # Regarde si un # est dans l'expression pour la distributivit�

        print("Je suis i")
        print(i)

        for j in i:
            if j == "#":
                dist = True

    if dist is True:
        listeFormulesCrochets = listeFormule

        print("Liste Formule Crochets")
        print(listeFormulesCrochets)

        # Pile pour la gestion des  parentheses
        pileA = []
        pileB = []
        # Pile pour la gestion des  #
        pileC = []
        pileD = []
        # Resultat de la distributivit�
        res = []

        for formule in listeFormulesCrochets:  # R�cup�ration de l'expression dans la parenth�se

            print("fomuleaasdasd")
            print(formule)

            for index in range(len(formule)):

                # print("l'index dezd ")
                # print(formule[index])

                compt = index
                if formule[index] == "(":
                    while formule[compt - 1] != ")":
                        pileA.append(formule[compt])
                        compt += 1

                    # print("rrzerzerzer")
                    # print(formule[index])

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
                        # print("dicoResultatCle 2")
                        # print(dicoResultatCle)
                    #
                    # dicoResultat[dicoResultatCle] = res  # Ajoute au dictionnaire
                    # dicoResultatCle += 1  # Incr�mente la cl�

                    # print("dicoResultatCle 3")
                    # print(dicoResultatCle)

                    # R�initialise les variables
                    pileB = []
                    pileC = []
                    pileD = []
                    # res = []

                # print("Dico Result if ")
                # print(dicoResultat)

                return res
    else:
        print("coucou")
        return listeFormule
        # dicoResultat[dicoResultatCle] = listeFormule  # Ajoute l'expression au dictionnaire
        #
        # print("dico else adazdad")
        # print(dicoResultat[dicoResultatCle])
        #
        # dicoResultatCle += 1  # Incr�mente la cl�
        #
        # print("dicoResultatCle")
        # print(dicoResultatCle)
        #
        # print("Dico Result else")
        # print(dicoResultat)
        # return res
    # return dicoResultat


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


#
# def separationCrochets(listeFormule):
#     listeIntermediareCrochets = []
#     listePropreCrochets = []
#     indice = []
#
#     for formule in listeFormule:  # Lit la formule
#         for index in range(len(formule)):
#             compt = index
#             if formule[index] == "[":  # Si la la valeur � l'index indiqu� est [ rentre dans la boucle
#                 trigger = ""  # Initaialise la variable de stockage
#                 while formule[compt] != "]":  # Tant que l'on rencontre pas ] stocke dans la variable
#                     trigger += formule[compt]  # R�cup�re la valeur
#                     indice.append(compt)  # R�cup�re l'indice
#                     compt += 1
#                 trigger += formule[compt]  # Ajoute le dernier �lemnent a la sortie de boucle
#                 # print(trigger)
#                 indice.append(compt)  # Ajoute le dernier indice a la sortie de boucle
#
#                 listeIntermediareCrochets.append(trigger)
#             trigger = ""  # R�initialise la variable de stockage
#             listeIntermediareCrochets.append(formule[index])
#
#             print("liste Interm�diaire Crochet")
#             print(listeIntermediareCrochets)
#
#     for i in indice:
#         del listeIntermediareCrochets[indice[0] + 1]  # enl�ve les caract�res qui ont �t� concat�n�es
#     listePropreCrochets.append(listeIntermediareCrochets)
#
#     print("Liste propre")
#     print(listePropreCrochets)
#     return listePropreCrochets


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

        indice = 0
        pos = 0

        print("ElemSep")
        print(elemSep)

        while indice < len(enListe):  # Tant que indice est inf�rieur a la longueur de la liste de l'expression
            if enListe[indice] == "[" and enListe[indice + 1] != "[":  # Si pas 2 crochets cons�cutifs
                re = indice
                while enListe[re] != "]":  # Tant que l'indice - 1 est diff�rent de ] avance l'indice
                    re += 1
                nette.append(elemSep[pos])  # Ajoute l'�l�ment de la liste a la liste interm�diaire

                # print("liste nette pos")
                # print(nette)

                pos += 1  # Avance la position
                indice = re
            else:

                # print("enListe[indice]")
                # print(enListe[indice])

                if enListe[indice] == "]" and enListe[indice - 1] != "]":  # Si 2 crochets cons�cutifs avance l'indice
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
                    trigger += nette[re]
                    re += 1
                final.append(trigger)  # Ajoute la la liste

        print("final")
        print(final)

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

        print("finale")
        print(finale)

        lastList.append(finale)

        return lastList

    else:

        print("listedeliste")
        print(listedeListe)

        return listedeListe


# separationCrochets(listeCas)
splitPropre(listeCas)
# allInOne(cas1)
