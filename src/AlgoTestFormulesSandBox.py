# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

""" Fichier test pour le traitement des formules avec certaines contraintes

D�finition des symbloles :
    /   Symbole de la juxtaposition
    #   Symbole d'un qualifiant
    +   Symbole de la coordination => et
    ()  Symbole de la distributivit�
    []  Symbole de l'ensemble
    =   Symbole de l'�quivalence

    une formule ressemble � ceci:   ([Kurios # Zeus] + H�ra ) # Ep�koos

    la d�composition est la suivante:

    Kurios Zeus est un ensemble dans lequel Kurios d�finit Zeus et H�ra est d�finit Ep�koos ainsi que Kurios Zeus
    Ensemble                                                  Coordianation         Distributivit�

Travaillons sur un algorithme pour travailler la formule
"""

"""Liste des imports n�c�ssaires"""

import csv
import os
from datetime import datetime
from collections import Counter

#  Liste des formules � �tudier

f1 = "Zeus / H�lios / Megas / Sarapis"
f2 = "[Apoll�n # Puthios] + [Apoll�n # Kedrieus]"

f3 = "Apoll�n # (Puthios + Kedrieus)"

f4 = "([Kurios # Zeus] + H�ra) # Ep�koos"
f5 = "[Amm�n = Chnoubis] + [H�ra = Satis] + [Hestia = Anoukis]"
f14 = "Isis # S�t�r # (Astart� / Aphrodit�) # (Euploia + Ep�koos)"
f7 = "[Theos # S�t�r] # (Artemis + Apoll�n)"
f6 = "(Zeus + H�ra) # S�t�r"
f8 = "[Zeus # S�t�r] + (Ath�na # S�t�r)"
f9 = "[Zeus # Boulaios] + [Ath�na # Boulaios] + Hestia"
f13 = "Apoll�n # (D�lios + Kalumnas-Mede�n)"
f15 = "(Askl�pios + Hugieia + Telesphoros) # Alexiponos"
f10 = "Artemis # Puthios"
f11 = ""
f16 = "{38}#[{45}#({46}#{47})]"
f12 = "[Zeus#Bront�n]+[Zeus#Karpodot�s]+[Zeus#Eucharistos]"

# Liste des attestations
global attestations
attestations = [f12]

""" Liste des signes pour les formules """

signes = {
    1: "+",
    2: "/",
    3: "#",
    4: "(",
    5: ")",
    6: "[",
    7: "]",
    8: "=",
    9: " ",
    10: "{",
    11: "}"
}

date = datetime.now()  # R�cup�re l'heure et la date du jour
datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')


# Pr�pare les formules pour le traitement
def nettoyageFormules(listeformules):
    listeInter = []

    trigger = ""  # Pour reformer le nom

    for indice in range(len(listeformules)):  # Regarde pour la longueur de la liste de formule
        listeSplit = []  # Stockage de la formule splitt�e

        for j in listeformules[indice]:  # Pour chaque �l�ment de la formule
            listeSplit.append(j)  # L'ajoute a la liste
        listeInter.append(listeSplit)  # La listes est ajout�e a la liste

    listeSuperPropre = []  # Liste de fin

    for i in listeInter:  # Pour la liste interm�diaire

        listePropre = []  # Initialise la liste tampons
        for j in i:  # Pour chaque �l�ment dans la liste
            if j in signes.values():  # Si j est un caract�re sp�cial
                if trigger != "":  # Si trigger est pas vide ajoute trigger � la liste
                    listePropre.append(trigger)
                    trigger = ""  # R�initialise Trigger
                listePropre.append(j)  # Ajoute � la liste
            else:
                trigger += j  # trigger re�oit la caract�ne non sp�cial
        listePropre.append(trigger)
        trigger = ""  # R�initialise trigger
        listeSuperPropre.append(listePropre)  # Ajoute � la liste de fin

    return listeSuperPropre  # Renvoie la liste de fin


def creationDicoDynamique(nomsDansFormules):  # Fonction qui permet de cr�er le dictionnaire des noms dynamiquement
    global dicoNoms
    global cleDico

    dicoNoms = {}  # Dictionaire des noms
    cleDico = 0  # Cl� pour le dictionnaire

    for i in nomsDansFormules.values():  # Pour chaque nom dans tri�e dans les formules
        for element in i:  # Pour chaque �l�ment dans la liste
            if element in dicoNoms.values():  # Si l l'�l�ment est dans da liste pass Sinon l'ajoute
                pass
            else:
                dicoNoms[cleDico] = element
                cleDico += 1

    return dicoNoms  # Renvoie le dictionnaire


def coocurenceListe(liste):  # Permet de calculer la Coocurence des formules
    """
    :param Liste de formules
    :return Le nombre de fois qu'un nom appra�t dans la formule

    """

    """Compte le poids pour les noeuds"""

    poids = {}  # Dictionnaire qui indique le nombre total d'apparition du mot
    cle = 0  # Cl� pour le dictionnaire � incr�menter
    noeud = {}  # Dictionnaire qui indique le nombre de formules o� un mot est mentionn� (unique)
    nomsDansFormules = {}  # Dictionnaire pour voir les relations entre les mots
    clea = 0  # Cl� pour les arcs

    # Lit pour chaque �l�ment de la liste
    for element in liste:  # Applique pour chaque �l�ment de la liste le traitement de la formule
        formule = element

        trigger = ""  # Pour r�cup�rer les noms
        final = []  # Liste qui r�cup�re les noms

        # Nettoyeage de la formule
        for i in formule:
            if i not in signes.values():  # Si non sp�cial ajoute a trigger
                trigger += i
            else:
                if trigger != "":  # si Trigger diff�rent de vide ajoute a la liste et la r�initialise
                    final.append(trigger)
                    trigger = ""

        """Ajoute les listes de noms � un dictionnaire"""
        nomsDansFormules[clea] = final
        clea += 1
        compte = {}.fromkeys(set(final), 0)  # D�finit le compteur pour chaque mot pr�sent

        creationDicoDynamique(nomsDansFormules)  # Cr�e le dictionnaire avec une cl� par nom diff�rent

        for valeur in final:  # Compte le nombre d'occurence de mots dans la liste
            compte[valeur] += 1
        poids[cle] = compte  # Ajoute le nombre de fois qu'apparait un nom dans chaque formule
        cle += 1  # Incr�mente la cl� du dictionnaire de stockage

    """Calcul pour les arcs"""
    arc = {}  # Initialise le dictionnaire avec sa cl�
    key = 0

    for element in nomsDansFormules.values():  # regarde dans le dictionnaires des noms dans les formules
        arc[key] = couplesArcs(element)  # Pour chaque formule ajoute les couples uniques au dictionnaire
        key += 1

    weightEdges = nomsNombres(arc)  # Appel de la fonction qui transforme les couples en Sources Targets

    """ Calcul pour savoir le nombre d'apparition du nom"""

    apparait = {}  # nombre total d'apparition

    for elem, val in poids.items():  # Regarde dans le Dictionnaire
        for nom, nombre in val.items():  # Ragarde dans le dictionnaire du dictionnaire
            if nom not in apparait:
                apparait[nom] = nombre  # Ajoute le mot et sa valeur associ�e
            else:
                apparait[nom] += nombre  # Ajoute la valeur si le nom existe d�j�

    """Calcul le nombre de fois qu'un nom apparait dans toutes les formules"""

    for element in poids.values():  # Parcous le dictionnaire de dictionnaire
        for i in element:  # Parcours chaque �l�m�ment du dictionnaire
            if i not in noeud.keys():  # Regarde si un �lement est dans la liste sinon l'ajoute
                noeud[i] = 1  # Ajoute l'�l�ment et l'initialise a 1
            else:
                noeud[i] += 1  # Incr�mente la valeur si celui ci est pr�sent

    """Ecrit dans un csv les r�sultats en appelant la fonction csvGraphes"""

    csvGraphes(noeud, apparait, weightEdges)  # les 3 dictionnaires associ�s en param�tres

    return noeud, poids, arc  # Revoie le dictionnaire avec les nombres d'apparition des noms par formules et le total


"""Fonction qui couples les noms pour les arcs"""


def couplesArcs(formule):
    listeNoms = []
    for element in dicoNoms.values():  # r�cup�re la liste de noms
        if element in formule:
            listeNoms.append(element)

    couples = []  # fait les associations soit des tuples
    dernierElemListe = len(listeNoms)  # Eviter les out of index

    if dernierElemListe == 1:  # Si le nom est seul l'ajoute a la liste sinon fait les couples
        couples.append(listeNoms[0])
    else:
        for i in range(dernierElemListe - 1):  # Pour chaque �l�ment cr�e une paire avec les el�ments suivants
            j = 0  # Initialise pour le tant que
            while j < dernierElemListe - 1:
                # V�rifie que les noms soit diff�rents et fait des paires uniques
                if listeNoms[i] != listeNoms[j + 1] and ((listeNoms[j + 1], listeNoms[i]) not in couples):
                    couples.append((listeNoms[i], listeNoms[j + 1]))
                j += 1
    return couples


"""Transorme les couples de noms de l'arc par rappout au dictionnaire des noms"""


def nomsNombres(dicoArc):  # Penser a faire le compte pour le nombre de paires identiques

    source = []
    target = []

    for element in dicoArc.values():  # Regarde pour chaque couple de nom l'id qui correspond a chaque nom
        for paire in element:
            for cle, valeur in dicoNoms.items():
                if valeur == paire[0]:
                    source.append(cle)
                if valeur == paire[1]:
                    target.append(cle)

    sourceTarget = []  # Liste initiale pour les couples d'Id

    for i in range(len(source)):  # Ajoute a la liste le nouveau couples d'Id
        sourceTarget.append((source[i], target[i]))

    def getKey(item):  # Fonction interne pour faire le tri par le premier �lement du tuple
        return item[0]

    sourceTargetSorted = sorted(sourceTarget, key=getKey)  # Trie la liste par le premier �l�ment
    weightEdge = comptePoidsArc(sourceTargetSorted)  # Appelle la fonction qui compte le nombre d'it�ration identiques

    return weightEdge


"""Compter le nombre d'occurences des paires"""


def comptePoidsArc(couplesId):  # Compte le nombre de fois o� le couple appara�t

    poidsArc = Counter(couplesId)
    return poidsArc


"""Ecrit les CSV pour les arcs et les Noeuds"""


def csvGraphes(noeud, apparait, arc):
    if os.path.exists(
            "Nodes" + datestr + ".csv"):  # Si le fichier existe il est supprim� pour en cr�er un nouveau
        os.remove("Nodes" + datestr + ".csv")
        nodes(noeud, apparait)  # Appelle la fonction qui �crit le CSV pour les Noeuds
    else:
        nodes(noeud, apparait)  # Appelle la fonction qui �crit le CSV pour les Noeuds

    """Test �criture du CSV pour les Arcs"""
    if os.path.exists(
            "Edges" + datestr + ".csv"):  # Si le fichier existe il est supprim� pour en cr�er un nouveau
        os.remove("Edges" + datestr + ".csv")
        edges(arc)  # Appelle la fonction qui �crit le CSV pour les Arcs
    else:
        edges(arc)  # Appelle la fonction qui �crit le CSV pour les Arcs


""" Ecriture des noeuds dans un csv"""


def nodes(noeud, apparait):  # faire une option de nommage du fichier
    with open("Nodes" + datestr + ".csv", 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Nodes", "Id", "Label", "Weight", "Weight2"))  # Ecriture en-t�te du fichier

        tempElem = []  # listes temporaires
        tempCle = []
        tempApparait = []
        idNoms = []

        for cle, element in apparait.items():  # R�cup�ration dans les listes
            tempCle.append(cle)  # Label
            tempElem.append(element)  # Weight2

        for i in tempCle:  # Associe au nom la cl� du dictionnaire
            for cle, element in dicoNoms.items():
                if element == i:
                    idNoms.append(cle)

        for nombre in noeud.values():  # R�cup�ration dans une liste
            tempApparait.append(nombre)  # Weight1

        for id in range(len(apparait.values())):  # Ecriture des ligens du csv
            writer.writerow((id + 1, idNoms[id], tempCle[id], tempApparait[id], tempElem[id]))


""" Ecritures des arc dans un csv"""


def edges(arc):  # faire une option de nommage du fichier
    with open("Edges" + datestr + ".csv", 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Source", "Target", "Type", "Id", "libelle", "Weight"))  # Ecriture en-t�te du fichier

        id = 0  # Cl� pour l'id
        for cle, element in arc.items():
            writer.writerow((cle[0], cle[1], "Undirected", id, "", element))
            id += 1


if __name__ == "__main__":
    coocurenceListe(attestations)  # OK Done !
    # print("")
    # print(creationDicoDynamique(attestations))
