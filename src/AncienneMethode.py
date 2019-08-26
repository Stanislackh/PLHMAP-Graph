# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

import csv
import os
from datetime import datetime
from collections import Counter

# Liste des signes sp�ciaux
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

# R�cup�re l'heure et la date du jour
date = datetime.now()
datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')


# Fonction qui permet de cr�er le dictionnaire des noms dynamiquement
def creationDicoDynamique(nomsDansFormules):
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


# Permet de calculer la Coocurence dans les formules
def coocurrence(liste):
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


# Couple les noms pour faire les arcs
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


# Transforme les couples de noms dans le dictionnaire des arcs par rapport au dictionnaire des noms
def nomsNombres(dicoArc):
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


# Compte le nombre d'occurence des paires de noms
def comptePoidsArc(couplesId):  # Compte le nombre de fois o� le couple appara�t

    poidsArc = Counter(couplesId)
    return poidsArc


# Fonction d'�criture dans le CSV
def csvGraphes(noeud, apparait, arc):
    if os.path.exists(
            "Coocurrence_Nodes" + datestr + ".csv"):  # Si le fichier existe il est supprim� pour en cr�er un nouveau
        os.remove("Coocurrence_Nodes" + datestr + ".csv")
        nodes(noeud, apparait)  # Appelle la fonction qui �crit le CSV pour les Noeuds
    else:
        nodes(noeud, apparait)  # Appelle la fonction qui �crit le CSV pour les Noeuds

    """Test �criture du CSV pour les Arcs"""
    if os.path.exists(
            "Coocurrence_Edges" + datestr + ".csv"):  # Si le fichier existe il est supprim� pour en cr�er un nouveau
        os.remove("Coocurrence_Edges" + datestr + ".csv")
        edges(arc)  # Appelle la fonction qui �crit le CSV pour les Arcs
    else:
        edges(arc)  # Appelle la fonction qui �crit le CSV pour les Arcs


# Fonction d'�criture des noeuds dans le CSV
def nodes(noeud, apparait):  # faire une option de nommage du fichier
    with open("Coocurrence_Nodes" + datestr + ".csv", 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(("Nodes", "Id", "Label", "Force_lien", "Weight2"))  # Ecriture en-t�te du fichier

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


# Fonction d'�criture des arcs dans le CSV
def edges(arc):  # faire une option de nommage du fichier
    global nameFileEdge
    with open("Coocurrence_Edges" + datestr + ".csv", 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(("Source", "Target", "Force_lien", "Type", "Id", "libelle"))  # Ecriture en-t�te du fichier

        id = 0  # Cl� pour l'id
        for cle, element in arc.items():
            writer.writerow((cle[0], cle[1], "Undirected", id, "", element))
            id += 1

        nameFileEdge = 'Coocurrence_Edges' + datestr
