# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

import csv
import os
from datetime import datetime
from collections import Counter

"""nomsNombres : à modifier la cle a la place de la valeur pour gephi dans la boucle ligne 158 et 160"""

# Liste des signes spéciaux
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

# Récupère l'heure et la date du jour
date = datetime.now()
datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')


# Fonction qui permet de créer le dictionnaire des noms dynamiquement
def creationDicoDynamique(nomsDansFormules):
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


# Permet de calculer la Coocurence dans les formules
def coocurrence(liste):
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
        if trigger != "":
            final.append(trigger)
            trigger = ""

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
    print("arc")
    print(arc)
    """Ecrit dans un csv les résultats en appelant la fonction csvGraphes"""
    csvGraphes(noeud, apparait, weightEdges)  # les 3 dictionnaires associés en paramètres

    return noeud, poids, arc  # Revoie le dictionnaire avec les nombres d'apparition des noms par formules et le total


# Couple les noms pour faire les arcs
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


# Transforme les couples de noms dans le dictionnaire des arcs par rapport au dictionnaire des noms
def nomsNombres(dicoArc):
    source = []
    target = []

    for element in dicoArc.values():  # Regarde pour chaque couple de nom l'id qui correspond a chaque nom
        for paire in element:
            for cle, valeur in dicoNoms.items():
                if valeur == paire[0]:
                    source.append(valeur)
                if valeur == paire[1]:
                    target.append(valeur)

    sourceTarget = []  # Liste initiale pour les couples d'Id

    for i in range(len(source)):  # Ajoute a la liste le nouveau couples d'Id
        sourceTarget.append((source[i], target[i]))

    print('source')
    print(sourceTarget)

    def getKey(item):  # Fonction interne pour faire le tri par le premier élement du tuple
        return item[0]

    sourceTargetSorted = sorted(sourceTarget, key=getKey)  # Trie la liste par le premier élément
    weightEdge = comptePoidsArc(sourceTargetSorted)  # Appelle la fonction qui compte le nombre d'itération identiques

    return weightEdge


# Compte le nombre d'occurence des paires de noms
def comptePoidsArc(couplesId):  # Compte le nombre de fois où le couple apparaît

    poidsArc = Counter(couplesId)
    return poidsArc


# Fonction d'écriture dans le CSV
def csvGraphes(noeud, apparait, weightEdges):
    if os.path.exists("CSVTraiteMAPCooccurrence"):
        nodes(noeud, apparait)  # Appelle la fonction qui écrit le CSV pour les Noeuds
    else:
        os.mkdir("CSVTraiteMAPCooccurrence")  # Crée le dossier qui contient les fichiers traités
        nodes(noeud, apparait)  # Appelle la fonction qui écrit le CSV pour les Noeuds

    """Test écriture du CSV pour les Arcs"""
    if os.path.exists("CSVTraiteMAPCooccurrence"):
        edges(weightEdges)  # Appelle la fonction qui écrit le CSV pour les Arcs
    else:
        os.mkdir("CSVTraiteMAPCooccurrence")  # Crée le dossier qui contient les fichiers traités
        edges(weightEdges)  # Appelle la fonction qui écrit le CSV pour les Arcs


# Fonction d'écriture des noeuds dans le CSV
def nodes(noeud, apparait):  # faire une option de nommage du fichier
    with open("CSVTraiteMAPCooccurrence/Coocurrence_Nodes" + datestr + ".csv", 'a', newline='',
              encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(("Nodes", "Id", "Label", "Force_lien", "Weight2"))  # Ecriture en-tête du fichier

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


# Fonction d'écriture des arcs dans le CSV
def edges(weightEdges):  # faire une option de nommage du fichier
    global nameFileEdge
    with open("CSVTraiteMAPCooccurrence/Coocurrence_Edges" + datestr + ".csv", 'a', newline='',
              encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(("Source", "Target", "Force_lien", "Type", "Id", "libelle"))  # Ecriture en-tête du fichier

        id = 0  # Clé pour l'id
        for cle, element in weightEdges.items():
            writer.writerow((cle[0], cle[1], "Undirected", id, "", element))
            id += 1

        nameFileEdge = 'CSVTraiteMAPCooccurrence/Coocurrence_Edges' + datestr


if __name__ == "__main__":
    lise = ["([Kurios#Zeus]+Hêra)#Epêkoos"]
    coocurrence(lise)
