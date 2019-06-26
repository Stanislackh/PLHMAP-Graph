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
f11 = "Dionusos # Phleos"
f16 = "S�t�r"
f12 = "[Zeus # Bront�n] + [Zeus # Karpodot�s] + [Zeus # Eucharistos]"

# Liste des attestations
global attestations
attestations = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16]
# """Liste des Dieux et Mots"""

"""Lecture du CSV et stockage dans une liste """
# def lectureCSV()

noms = {
    1: "Zeus",
    2: "H�lios",
    3: "Megas",
    4: "Sarapis",
    5: "Apoll�n",
    6: "Puthios",
    7: "Kedrieus",
    8: "Kurios",
    9: "H�ra",
    10: "Ep�koos",
    11: "Amm�n",
    12: "Chnoubis",
    13: "Satis",
    14: "Hestia",
    15: "Anoukis",
    16: "Isis",
    17: "S�t�r",
    18: "Astart�",
    19: "Aphrodit�",
    20: "Euploia",
    21: "Theos",
    22: "Artemis",
    23: "Ath�na",
    24: "Boulaios",
    25: "D�lios",
    26: "Kalumnas-Mede�n",
    27: "Hugieia",
    28: "Telesphoros",
    29: "Alexiponos",
    30: "Dionusos",
    31: "Phleos",
    32: "Bront�n",
    33: "Karpodot�s",
    34: "Eucharistos",
    35: "Askl�pios"}

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
    9: " "
}


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
        res = formule.split(" ")  # Permet de d�couper la formule en supprimant les espaces

        for i in res:
            for j in signes.values():  # Regarde dans le dictionnaire des signes si il apparait
                if i == j:
                    res.remove(j)  # Supprime les signes sp�ciaux des formules
        temp = []  # Liste temporaire

        # A mettre dans une autre fonction
        for i in res:  # Permet de parcourir les �l�ment de la liste res
            temp.append(" ")  # Ajoute chaque element � la liste coup� a l'espace
            for j in i:
                if j not in signes.values():  # Ajoute les caract�res non sp�ciaux
                    temp.append(j)

        del temp[0]  # Supprime l'espace ajout� au d�but de la liste

        """Calcule le nombre total d'apparition du mot"""
        chaine = ""  # Cr�ation de la chaine vide qui sera split par l'espace

        for i in temp:  # Parcours la liste temp pour la traduire en chaine de caract�re
            chaine += i
        final = chaine.split(" ")  # Coupe la chaine de caract�re � l'espace pour en refaire uen liste

        """Ajoute les listes de noms � un dictionnaire"""
        nomsDansFormules[clea] = final
        clea += 1
        compte = {}.fromkeys(set(final), 0)  # D�finit le compteur pour chaque mot pr�sent

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
    # nombre total d'apparition
    apparait = {}

    for elem, val in poids.items():  # Regarde dans le Dictionnaire
        for nom, nombre in val.items():  # Ragarde dans le dictionnaire du dictionnaire
            if nom not in apparait:
                apparait[nom] = nombre  # Ajoute le mot et sa valeur associ�e
            else:
                apparait[nom] += nombre  # Ajoute la valeur si le nom existe d�j�

    """Calcule le nombre de fois qu'un nom apparait dans toutes les formules"""

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
    for element in noms.values():  # r�cup�re la liste de noms
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
            for cle, valeur in noms.items():
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
    if os.path.exists("Nodes.csv"):  # Si le fichier existe il est supprim� pour en cr�er un nouveau
        os.remove("Nodes.csv")
        nodes(noeud, apparait)
    else:
        nodes(noeud, apparait)

    """Test �criture du CSV pour les Arcs"""
    if os.path.exists("Edges.csv"):  # Si le fichier existe il est supprim� pour en cr�er un nouveau
        os.remove("Edges.csv")
        edges(arc)
    else:
        edges(arc)


""" Ecriture des noeuds dans un csv"""


def nodes(noeud, apparait):  # faire une option de nommage du fichier
    with open('Nodes.csv', 'w', newline='', encoding='windows-1252') as csvfile:
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
            for cle, element in noms.items():
                if element == i:
                    idNoms.append(cle)

        for nombre in noeud.values():  # R�cup�ration dans une liste
            tempApparait.append(nombre)  # Weight1

        for id in range(len(apparait.values())):  # Ecriture des ligens du csv
            writer.writerow((id + 1, idNoms[id], tempCle[id], tempApparait[id], tempElem[id]))


""" Ecritures des arc dans un csv"""


def edges(arc):  # faire une option de nommage du fichier
    with open('Edges.csv', 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Source", "Target", "Type", "Id", "libelle", "Weight"))  # Ecriture en-t�te du fichier

        id = 0  # Cl� pour l'id
        for cle, element in arc.items():
            writer.writerow((cle[0], cle[1], "Undirected", id, "", element))
            id += 1


# def writeCSVFormule(listeAttestations):  # Ecrit le CSV des formules de tests
#     with open('Formules.csv', 'w', newline='', encoding='windows-1252') as csvfile:
#         writer = csv.writer(csvfile, delimiter=';')
#         writer.writerow(("Id", "Formule"))  # Ecriture en-t�te du fichier
#
#         id = 0  # Cl� pour l'id
#         for formule in listeAttestations:
#             writer.writerow((id, formule))
#             id += 1


"""Fonction qui affiche le graphe"""

# def drawGraph(noeud, apparait, arc):
#     G = nx.Graph()
#
#     tempLabel = []
#     tempPoids = []
#
#     listeNodes = []
#     listeEdges = []
#
#     for cle, element in apparait.items():  # R�cup�ration dans les listes
#         tempLabel.append(cle)  # Label
#         tempPoids.append(element)  # Poids


"""Traite les symboles"""


def traiteSymbole(formule):
    for carac in formule:  # Regarde par quoi est s�par� les noms

        # Faire la m�me avec l'appel du dictionnaire
        if carac == "/":
            print("Jusxtapos�")
        elif carac == "(":
            print("d�but de distributivit�")
        elif carac == ")":
            print("Fin de distributivit�")
        elif carac == "#":
            print("qualifie")
        elif carac == "[":
            print("D�but ensemble")
        elif carac == "]":
            print("Fin ensemble")
        elif carac == "+":
            print("coordination")
        elif carac == "=":
            print("equivalence")
        else:
            print(carac)


def traiteFormule(formule):
    """Faire la distributivit�"""


if __name__ == "__main__":
    # print(coocurenceArc(f12))
    writeCSVFormule(attestations)
    # coocurenceListe(attestations)  # OK Done !
    # print("")
    # traiteFormule(f1)
