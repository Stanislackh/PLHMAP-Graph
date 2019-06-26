# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

""" Fichier test pour le traitement des formules avec certaines contraintes

Définition des symbloles :
    /   Symbole de la juxtaposition
    #   Symbole d'un qualifiant
    +   Symbole de la coordination => et
    ()  Symbole de la distributivité
    []  Symbole de l'ensemble
    =   Symbole de l'équivalence

    une formule ressemble à ceci:   ([Kurios # Zeus] + Hêra ) # Epêkoos

    la décomposition est la suivante:

    Kurios Zeus est un ensemble dans lequel Kurios définit Zeus et Hêra est définit Epêkoos ainsi que Kurios Zeus
    Ensemble                                                  Coordianation         Distributivité

Travaillons sur un algorithme pour travailler la formule
"""

"""Liste des imports nécéssaires"""

import csv
import os
from collections import Counter

#  Liste des formules à étudier

f1 = "Zeus / Hêlios / Megas / Sarapis"
f2 = "[Apollôn # Puthios] + [Apollôn # Kedrieus]"

f3 = "Apollôn # (Puthios + Kedrieus)"

f4 = "([Kurios # Zeus] + Hêra) # Epêkoos"
f5 = "[Ammôn = Chnoubis] + [Hêra = Satis] + [Hestia = Anoukis]"
f14 = "Isis # Sôtêr # (Astartê / Aphroditê) # (Euploia + Epêkoos)"
f7 = "[Theos # Sôtêr] # (Artemis + Apollôn)"
f6 = "(Zeus + Hêra) # Sôtêr"
f8 = "[Zeus # Sôtêr] + (Athêna # Sôtêr)"
f9 = "[Zeus # Boulaios] + [Athêna # Boulaios] + Hestia"
f13 = "Apollôn # (Dêlios + Kalumnas-Medeôn)"
f15 = "(Asklêpios + Hugieia + Telesphoros) # Alexiponos"
f10 = "Artemis # Puthios"
f11 = "Dionusos # Phleos"
f16 = "Sôtêr"
f12 = "[Zeus # Brontôn] + [Zeus # Karpodotês] + [Zeus # Eucharistos]"

# Liste des attestations
global attestations
attestations = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16]
# """Liste des Dieux et Mots"""

"""Lecture du CSV et stockage dans une liste """
# def lectureCSV()

noms = {
    1: "Zeus",
    2: "Hêlios",
    3: "Megas",
    4: "Sarapis",
    5: "Apollôn",
    6: "Puthios",
    7: "Kedrieus",
    8: "Kurios",
    9: "Hêra",
    10: "Epêkoos",
    11: "Ammôn",
    12: "Chnoubis",
    13: "Satis",
    14: "Hestia",
    15: "Anoukis",
    16: "Isis",
    17: "Sôtêr",
    18: "Astartê",
    19: "Aphroditê",
    20: "Euploia",
    21: "Theos",
    22: "Artemis",
    23: "Athêna",
    24: "Boulaios",
    25: "Dêlios",
    26: "Kalumnas-Medeôn",
    27: "Hugieia",
    28: "Telesphoros",
    29: "Alexiponos",
    30: "Dionusos",
    31: "Phleos",
    32: "Brontôn",
    33: "Karpodotês",
    34: "Eucharistos",
    35: "Asklêpios"}

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
    :return Le nombre de fois qu'un nom appraît dans la formule

    """

    """Compte le poids pour les noeuds"""
    poids = {}  # Dictionnaire qui indique le nombre total d'apparition du mot
    cle = 0  # Clé pour le dictionnaire à incrémenter
    noeud = {}  # Dictionnaire qui indique le nombre de formules où un mot est mentionné (unique)
    nomsDansFormules = {}  # Dictionnaire pour voir les relations entre les mots
    clea = 0  # Clé pour les arcs

    # Lit pour chaque élément de la liste
    for element in liste:  # Applique pour chaque élément de la liste le traitement de la formule
        formule = element
        res = formule.split(" ")  # Permet de découper la formule en supprimant les espaces

        for i in res:
            for j in signes.values():  # Regarde dans le dictionnaire des signes si il apparait
                if i == j:
                    res.remove(j)  # Supprime les signes spéciaux des formules
        temp = []  # Liste temporaire

        # A mettre dans une autre fonction
        for i in res:  # Permet de parcourir les élément de la liste res
            temp.append(" ")  # Ajoute chaque element à la liste coupé a l'espace
            for j in i:
                if j not in signes.values():  # Ajoute les caractères non spéciaux
                    temp.append(j)

        del temp[0]  # Supprime l'espace ajouté au début de la liste

        """Calcule le nombre total d'apparition du mot"""
        chaine = ""  # Création de la chaine vide qui sera split par l'espace

        for i in temp:  # Parcours la liste temp pour la traduire en chaine de caractère
            chaine += i
        final = chaine.split(" ")  # Coupe la chaine de caractère à l'espace pour en refaire uen liste

        """Ajoute les listes de noms à un dictionnaire"""
        nomsDansFormules[clea] = final
        clea += 1
        compte = {}.fromkeys(set(final), 0)  # Définit le compteur pour chaque mot présent

        for valeur in final:  # Compte le nombre d'occurence de mots dans la liste
            compte[valeur] += 1
        poids[cle] = compte  # Ajoute le nombre de fois qu'apparait un nom dans chaque formule
        cle += 1  # Incrémente la clé du dictionnaire de stockage

    """Calcul pour les arcs"""
    arc = {}  # Initialise le dictionnaire avec sa clé
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
                apparait[nom] = nombre  # Ajoute le mot et sa valeur associée
            else:
                apparait[nom] += nombre  # Ajoute la valeur si le nom existe déjà

    """Calcule le nombre de fois qu'un nom apparait dans toutes les formules"""

    for element in poids.values():  # Parcous le dictionnaire de dictionnaire
        for i in element:  # Parcours chaque élémément du dictionnaire
            if i not in noeud.keys():  # Regarde si un élement est dans la liste sinon l'ajoute
                noeud[i] = 1  # Ajoute l'élément et l'initialise a 1
            else:
                noeud[i] += 1  # Incrémente la valeur si celui ci est présent

    """Ecrit dans un csv les résultats en appelant la fonction csvGraphes"""

    csvGraphes(noeud, apparait, weightEdges)  # les 3 dictionnaires associés en paramètres

    return noeud, poids, arc  # Revoie le dictionnaire avec les nombres d'apparition des noms par formules et le total


"""Fonction qui couples les noms pour les arcs"""


def couplesArcs(formule):
    listeNoms = []
    for element in noms.values():  # récupère la liste de noms
        if element in formule:
            listeNoms.append(element)

    couples = []  # fait les associations soit des tuples
    dernierElemListe = len(listeNoms)  # Eviter les out of index

    if dernierElemListe == 1:  # Si le nom est seul l'ajoute a la liste sinon fait les couples
        couples.append(listeNoms[0])
    else:
        for i in range(dernierElemListe - 1):  # Pour chaque élément crée une paire avec les eléments suivants
            j = 0  # Initialise pour le tant que
            while j < dernierElemListe - 1:
                # Vérifie que les noms soit différents et fait des paires uniques
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

    def getKey(item):  # Fonction interne pour faire le tri par le premier élement du tuple
        return item[0]

    sourceTargetSorted = sorted(sourceTarget, key=getKey)  # Trie la liste par le premier élément
    weightEdge = comptePoidsArc(sourceTargetSorted)  # Appelle la fonction qui compte le nombre d'itération identiques

    return weightEdge


"""Compter le nombre d'occurences des paires"""


def comptePoidsArc(couplesId):  # Compte le nombre de fois où le couple apparaît

    poidsArc = Counter(couplesId)
    return poidsArc


"""Ecrit les CSV pour les arcs et les Noeuds"""


def csvGraphes(noeud, apparait, arc):
    if os.path.exists("Nodes.csv"):  # Si le fichier existe il est supprimé pour en créer un nouveau
        os.remove("Nodes.csv")
        nodes(noeud, apparait)
    else:
        nodes(noeud, apparait)

    """Test écriture du CSV pour les Arcs"""
    if os.path.exists("Edges.csv"):  # Si le fichier existe il est supprimé pour en créer un nouveau
        os.remove("Edges.csv")
        edges(arc)
    else:
        edges(arc)


""" Ecriture des noeuds dans un csv"""


def nodes(noeud, apparait):  # faire une option de nommage du fichier
    with open('Nodes.csv', 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Nodes", "Id", "Label", "Weight", "Weight2"))  # Ecriture en-tête du fichier

        tempElem = []  # listes temporaires
        tempCle = []
        tempApparait = []
        idNoms = []

        for cle, element in apparait.items():  # Récupération dans les listes
            tempCle.append(cle)  # Label
            tempElem.append(element)  # Weight2

        for i in tempCle:  # Associe au nom la clé du dictionnaire
            for cle, element in noms.items():
                if element == i:
                    idNoms.append(cle)

        for nombre in noeud.values():  # Récupération dans une liste
            tempApparait.append(nombre)  # Weight1

        for id in range(len(apparait.values())):  # Ecriture des ligens du csv
            writer.writerow((id + 1, idNoms[id], tempCle[id], tempApparait[id], tempElem[id]))


""" Ecritures des arc dans un csv"""


def edges(arc):  # faire une option de nommage du fichier
    with open('Edges.csv', 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Source", "Target", "Type", "Id", "libelle", "Weight"))  # Ecriture en-tête du fichier

        id = 0  # Clé pour l'id
        for cle, element in arc.items():
            writer.writerow((cle[0], cle[1], "Undirected", id, "", element))
            id += 1


# def writeCSVFormule(listeAttestations):  # Ecrit le CSV des formules de tests
#     with open('Formules.csv', 'w', newline='', encoding='windows-1252') as csvfile:
#         writer = csv.writer(csvfile, delimiter=';')
#         writer.writerow(("Id", "Formule"))  # Ecriture en-tête du fichier
#
#         id = 0  # Clé pour l'id
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
#     for cle, element in apparait.items():  # Récupération dans les listes
#         tempLabel.append(cle)  # Label
#         tempPoids.append(element)  # Poids


"""Traite les symboles"""


def traiteSymbole(formule):
    for carac in formule:  # Regarde par quoi est séparé les noms

        # Faire la même avec l'appel du dictionnaire
        if carac == "/":
            print("Jusxtaposé")
        elif carac == "(":
            print("début de distributivité")
        elif carac == ")":
            print("Fin de distributivité")
        elif carac == "#":
            print("qualifie")
        elif carac == "[":
            print("Début ensemble")
        elif carac == "]":
            print("Fin ensemble")
        elif carac == "+":
            print("coordination")
        elif carac == "=":
            print("equivalence")
        else:
            print(carac)


def traiteFormule(formule):
    """Faire la distributivité"""


if __name__ == "__main__":
    # print(coocurenceArc(f12))
    writeCSVFormule(attestations)
    # coocurenceListe(attestations)  # OK Done !
    # print("")
    # traiteFormule(f1)
