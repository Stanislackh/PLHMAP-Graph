# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivité"""
from itertools import combinations

cas1 = "([a#b]+[[c#d]/[e#f]])#[g#h]"  # OK
# => [a#b]#[g#h]+[[c#d]/[e#f]]#[g#h]

cas2 = "Apollôn#(Puthios+Kedrieus)"  # OK

cas3 = "(Zeus+Hêra)#Sôtêr"  # OK

cas4 = "Apollôn # (Puthios + Kedrieus)"  # OK

cas5 = "[Theos#Sôtêr]#(Artemis+Apollôn)"  # OK

cas6 = "[[Zeus/Hêlios]/[Megas#Sarapis]]+[Sunnaoi#Theoi]"  # OK

cas7 = "([Isis#Sôtêr]/Astartê / [Aphroditê # Euploia]) # Epêkoos + [Erôs / Harpokratês / Apollôn]"  # OK

cas8 = "[dieux # saints] # de Byblos"  # OK

cas9 = "Ashtart # [dans le sanctuaire # [du dieu # de Hamon]]"  # OK

cas10 = "[Apollôn # Puthios] + [Apollôn # Kedrieus]"  # OK

cas11 = "[Ammôn=Chnoubis]+[Hêra=Satis]+[Hestia=Anoukis]+[Dionusos=Petempamentis]+[Hallos#Theos]"  # OK

cas12 = "([Kurios # Zeus] + Hêra) # Epêkoos"  # OK

cas13 = "à mes dames # ([[à la déesse # puissante] # Isis] / [la déesse # Ashtart]) + [aux dieux # qui]"
# Cas 13 Explose et j'arrive pas à lire ...

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

    # Récupère les formules sans espaces
    listeCasNettoye = supprimeEspace(listeCas)

    print("listeCasNettoye")
    print(listeCasNettoye)

    # Si une des fonctions retourne True ne passe pas à la suite
    if (checkNbParCroch(listeCasNettoye) is False) and (caracMalPlace(listeCasNettoye) is False):
        pileA = []

        for cas in listeCasNettoye:  # Regarde dans la liste des formules
            pileB = []
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

            # print("PileB")
            # print(pileB)

            res = allInOne(pileB)

            # Applique la distibutivité si il y en a à la liste de formule
            dicoResultat[dicoResultatCle] = distributiviteCrochet(res)
            dicoResultatCle += 1  # incrémente la clé du dictionnaire

            dicoReecrit = {}
            cle = 0

            for objet in dicoResultat.values():
                trigger = ""
                for i in objet:
                    for j in i:
                        trigger += j

                dicoReecrit[cle] = trigger
                cle += 1

        print("dicoréécrit Version lisible ")
        for i, j in dicoReecrit.items():
            print(i, j)
            print("")


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


def caracMalPlace(listeCasNettoye):  # Regarde dans la liste des erreurs de syntaxes si elle y figure

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


def distributiviteCrochet(listeFormule):
    dist = False  # Garde pour lancer la séquence

    # print("ListeFormule")
    # print(listeFormule)

    for i in listeFormule:  # Regarde si un # est dans l'expression pour la distributivité
        for j in i:
            if j == "#":
                dist = True

    if dist is True:  # Si la garde est levée

        print("Liste Formule")
        print(listeFormule)

        # Pile pour la gestion des  parentheses
        pileA = []
        pileB = []
        # Pile pour la gestion des  #
        pileC = []
        pileD = []
        pileE = []

        # Resultat de la distributivité
        res = []

        garde = False  # Garde pour lancer la séquence

        for formule in listeFormule:  # Récupération de l'expression dans la parenthèse

            print("fomuleaasdasd")
            print(formule)

            for i in formule:  # Regarde si il y a des parenthèses avant de lancer la séuence suivante
                if i == "(":
                    garde = True  # Lève la garde
                    break

            if garde is True:  # Si la garde est levée lance la sequence
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
                        pileE.append(formule[index])  # Récupère l'expression

                print("PileE")
                print(pileE)

                if len(pileA) != 0:  # Supprime la première parenthèse
                    del pileA[0]

                print("pileA resresrse")
                print(pileA)

                print("pileB resresrse")
                print(pileB)

                print("pileC resresrse")
                print(pileC)

                print("pileD resresrse")
                print(pileD)

                pileB.append(pileA)  # Rajoute les élements a la pileB
                pileA = []  # Réinitialise la pile A

                for i in formule:
                    for k in range(len(pileB)):  # Regarde l'expression stocké qui était dans la parenthèse
                        for index in range(len(formule) - 1):
                            # Si la formule contient )# distribue de cette façon
                            if formule[index] + formule[index + 1] == ")#":
                                for j in pileB[k]:
                                    if j not in signes.values():  # Regarde si le caractère est spécial si non l'ajoute
                                        res.append("[")  # Ajoute les crochets pour marqeur l'ensemble
                                        res.append(j)
                                        for k in pileC:  # Rajoute les elements stockés
                                            res.append(k)
                                        res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                                    elif j == "+" or j == "=" or j == "/" or "+":  # Ajoute l'opérateur
                                        res.append(j)

                            # Si la formule contient #( distribue de cette façon
                            elif formule[index] + formule[index + 1] == "#(":
                                for j in pileB[k]:
                                    if j not in signes.values():  # Regarde si le caractère est spécial si non l'ajoute
                                        res.append("[")  # Ajoute les crochets pour marquer l'ensemble
                                        for k in pileC:  # Rajoute les elements stockés
                                            res.append(k)
                                        res.append(j)
                                        res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                                    elif j == "+" or j == "=" or j == "/" or "+":  # Ajoute l'opérateur
                                        res.append(j)

                            else:
                                for l in pileD:  # Ajoute la formule sans parenthèses
                                    res.append(l)

                        # Réinitialise les variables
                        pileB = []
                        pileC = []
                        pileD = []

                    for i in pileE:  # Regarde dans la liste les élement qui manquent et les rajoute
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
    # Resultat de la distributivité
    res = []

    dicoResultat = {}
    dicoResultatCle = 0

    for formule in listeFormule:  # Récupération de l'expression dans la parenthèse
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

        if len(pileA) != 0:  # Supprime la première parenthèse
            del pileA[0]

        pileB.append(pileA)  # Rajoute les élements a la pileB
        pileA = []  # Réinitialise la pila A

        for i in formule:
            for k in range(len(pileB)):  # Regarde l'expression stocké qui était dans la parenthèse
                dicoResultat[dicoResultatCle] = res  # Ajoute au dictionnaire
                dicoResultatCle += 1  # Incrémente la clé

                for index in range(len(formule) - 1):
                    # Si la formule contient )# distribue de cette façon
                    if formule[index] + formule[index + 1] == ")#":
                        for j in pileB[k]:
                            if j not in signes.values():  # Regarde si le caractère est spécial si non l'ajoute
                                res.append("[")  # Ajoute les crochets pour marqeur l'ensemble
                                res.append(j)
                                for k in pileC:  # Rajoute les elements stockés
                                    res.append(k)
                                res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                            elif j == "+" or j == "=":  # Ajoute l'opérateur
                                res.append(j)

                    # Si la formule contient #( distribue de cette façon
                    elif formule[index] + formule[index + 1] == "#(":
                        for j in pileB[k]:
                            if j not in signes.values():  # Regarde si le caractère est spécial si non l'ajoute
                                res.append("[")  # Ajoute les crochets pour marquer l'ensemble
                                for k in pileC:  # Rajoute les elements stockés
                                    res.append(k)
                                res.append(j)
                                res.append("]")  # Ajoute les crochets pour marquer l'ensemble
                            elif j == "+" or j == "=":  # Ajoute l'opérateur
                                res.append(j)

                else:
                    for l in pileD:  # Ajoute la formule sans parenthèses
                        res.append(l)
                # Réinitialise les variables
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

    for i in listedeListe:  # Vérifie si l'expression à des crochets
        for j in i:
            if j == "[":
                suite = True
                break

    if suite is True:  # Si l'expression a des crochets
        for i in listedeListe:  # Récupère l'expression dans la liste
            for j in i:
                enListe.append(j)

        elemSep = []  # Variables intermédiaires
        nette = []
        final = []

        element = ""
        cpt = 0
        garde = False

        print("listedeListe")
        print(listedeListe)

        for indice in range(len(enListe)):  # Pour la longueur de l'expression
            if element != "":  # si element est différente de ""
                elemSep.append(element)  # Ajoute a la liste des elements entre crochets en 1 element
                element = ""  # Réinitialise element

            if enListe[indice] == "[" and enListe[indice + 1] != "[":  # Si pas 2 crochets succéssifs
                if garde is False and enListe[0] == "[":
                    element += enListe[cpt]
                    garde = True
                while enListe[cpt] != "]":  # Tant que l'element de la liste est différent de ]
                    element += enListe[cpt + 1]
                    cpt += 1

            cpt = indice  # donne la valeur de l'indice a cpt pour pouvoir continuer a l'indice arrêté

        # print("SepElem")
        # print(elemSep)

        indice = 0
        pos = 0

        co = 0
        cf = 0
        blap = True

        while indice < len(enListe):  # Tant que indice est inférieur a la longueur de la liste de l'expression

            if enListe[indice] == "[":
                co += 1

            if enListe[indice] == "[" and enListe[indice + 1] != "[":  # Si pas 2 crochets consécutifs
                re = indice
                while enListe[re] != "]":  # Tant que l'indice est différent de ] avance l'indice
                    re += 1
                nette.append(elemSep[pos])  # Ajoute l'élément de la liste a la liste intermédiaire

                pos += 1  # Avance la position
                indice = re

            else:
                if enListe[indice] == "]" and enListe[indice - 1] == "]":
                    nette.append(enListe[indice])  # Sinon ajoute à la liste
                    indice += 1
                    cf -= 1

                elif enListe[indice] == "]" and enListe[indice - 1] != "]":  # Si 2 crochets consécutifs avance l'indice
                    cf += 1
                    if co == cf and blap is True:
                        nette.append(enListe[indice])
                        blap = False
                        indice += 1
                    else:
                        indice += 1
                else:
                    nette.append(enListe[indice])  # Sinon ajoute à la liste
                    indice += 1

        print("nette")
        print(nette)

        for i in range(len(nette)):  # pour la longeur de la liste
            if nette[i] == "[" and nette[i + 1] != "[":  # Si pas 2 crochets consécutifs
                re = i
                trigger = ""
                while nette[re - 1] != "]":  # Tant que l'element est différent de ] avance l'indice

                    # print("trigger")
                    # print(trigger)

                    trigger += nette[re]
                    re += 1
                final.append(trigger)  # Ajoute la la liste

        # print("final")
        # print(final)

        indice = 0
        pos = 0

        while indice < len(nette):  # Tant que l'indice est inférieur a la longueur de la liste
            if nette[indice] == "[" and nette[indice + 1] != "[":  # Si pas 2 crochets consécutifs
                re = indice
                while nette[re - 1] != "]":  # Tant que l'element est différent de ] avance l'indice
                    re += 1
                finale.append(final[pos])  # Ajoute l'élément à la liste
                pos += 1
                indice = re

            else:
                if nette[indice] == "]":
                    indice += 1
                else:
                    finale.append(nette[indice])  # Ajoute l'element à la liste
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
