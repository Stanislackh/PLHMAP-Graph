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
from datetime import datetime
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
f11 = ""
f16 = "{38}#[{45}#({46}#{47})]"
f12 = "[Zeus#Brontôn]+[Zeus#Karpodotês]+[Zeus#Eucharistos]"

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

date = datetime.now()  # Récupère l'heure et la date du jour
datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')


# Prépare les formules pour le traitement
def nettoyageFormules(listeformules):
    listeInter = []

    trigger = ""  # Pour reformer le nom

    for indice in range(len(listeformules)):  # Regarde pour la longueur de la liste de formule
        listeSplit = []  # Stockage de la formule splittée

        for j in listeformules[indice]:  # Pour chaque élément de la formule
            listeSplit.append(j)  # L'ajoute a la liste
        listeInter.append(listeSplit)  # La listes est ajoutée a la liste

    listeSuperPropre = []  # Liste de fin

    for i in listeInter:  # Pour la liste intermédiaire

        listePropre = []  # Initialise la liste tampons
        for j in i:  # Pour chaque élément dans la liste
            if j in signes.values():  # Si j est un caractère spécial
                if trigger != "":  # Si trigger est pas vide ajoute trigger à la liste
                    listePropre.append(trigger)
                    trigger = ""  # Réinitialise Trigger
                listePropre.append(j)  # Ajoute à la liste
            else:
                trigger += j  # trigger reçoit la caractène non spécial
        listePropre.append(trigger)
        trigger = ""  # Réinitialise trigger
        listeSuperPropre.append(listePropre)  # Ajoute à la liste de fin

    return listeSuperPropre  # Renvoie la liste de fin


def creationDicoDynamique(nomsDansFormules):  # Fonction qui permet de créer le dictionnaire des noms dynamiquement
    global dicoNoms
    global cleDico

    dicoNoms = {}  # Dictionaire des noms
    cleDico = 0  # Clé pour le dictionnaire

    for i in nomsDansFormules.values():  # Pour chaque nom dans triée dans les formules
        for element in i:  # Pour chaque élément dans la liste
            if element in dicoNoms.values():  # Si l l'élément est dans da liste pass Sinon l'ajoute
                pass
            else:
                dicoNoms[cleDico] = element
                cleDico += 1

    return dicoNoms  # Renvoie le dictionnaire


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

        trigger = ""  # Pour récupérer les noms
        final = []  # Liste qui récupère les noms

        # Nettoyeage de la formule
        for i in formule:
            if i not in signes.values():  # Si non spécial ajoute a trigger
                trigger += i
            else:
                if trigger != "":  # si Trigger différent de vide ajoute a la liste et la réinitialise
                    final.append(trigger)
                    trigger = ""

        """Ajoute les listes de noms à un dictionnaire"""
        nomsDansFormules[clea] = final
        clea += 1
        compte = {}.fromkeys(set(final), 0)  # Définit le compteur pour chaque mot présent

        creationDicoDynamique(nomsDansFormules)  # Crée le dictionnaire avec une clé par nom différent

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

    apparait = {}  # nombre total d'apparition

    for elem, val in poids.items():  # Regarde dans le Dictionnaire
        for nom, nombre in val.items():  # Ragarde dans le dictionnaire du dictionnaire
            if nom not in apparait:
                apparait[nom] = nombre  # Ajoute le mot et sa valeur associée
            else:
                apparait[nom] += nombre  # Ajoute la valeur si le nom existe déjà

    """Calcul le nombre de fois qu'un nom apparait dans toutes les formules"""

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
    for element in dicoNoms.values():  # récupère la liste de noms
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
            for cle, valeur in dicoNoms.items():
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
    if os.path.exists(
            "Nodes" + datestr + ".csv"):  # Si le fichier existe il est supprimé pour en créer un nouveau
        os.remove("Nodes" + datestr + ".csv")
        nodes(noeud, apparait)  # Appelle la fonction qui écrit le CSV pour les Noeuds
    else:
        nodes(noeud, apparait)  # Appelle la fonction qui écrit le CSV pour les Noeuds

    """Test écriture du CSV pour les Arcs"""
    if os.path.exists(
            "Edges" + datestr + ".csv"):  # Si le fichier existe il est supprimé pour en créer un nouveau
        os.remove("Edges" + datestr + ".csv")
        edges(arc)  # Appelle la fonction qui écrit le CSV pour les Arcs
    else:
        edges(arc)  # Appelle la fonction qui écrit le CSV pour les Arcs


""" Ecriture des noeuds dans un csv"""


def nodes(noeud, apparait):  # faire une option de nommage du fichier
    with open("Nodes" + datestr + ".csv", 'w', newline='', encoding='windows-1252') as csvfile:
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
            for cle, element in dicoNoms.items():
                if element == i:
                    idNoms.append(cle)

        for nombre in noeud.values():  # Récupération dans une liste
            tempApparait.append(nombre)  # Weight1

        for id in range(len(apparait.values())):  # Ecriture des ligens du csv
            writer.writerow((id + 1, idNoms[id], tempCle[id], tempApparait[id], tempElem[id]))


""" Ecritures des arc dans un csv"""


def edges(arc):  # faire une option de nommage du fichier
    with open("Edges" + datestr + ".csv", 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Source", "Target", "Type", "Id", "libelle", "Weight"))  # Ecriture en-tête du fichier

        id = 0  # Clé pour l'id
        for cle, element in arc.items():
            writer.writerow((cle[0], cle[1], "Undirected", id, "", element))
            id += 1


if __name__ == "__main__":
    coocurenceListe(attestations)  # OK Done !
    # print("")
    # print(creationDicoDynamique(attestations))
