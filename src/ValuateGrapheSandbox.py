# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

"""Projet graphe valu�

objectifs:
 - Faire une table d'adjacence
 - Comparer avec la formule d�velopp�e
 - Mettre les valeurs en fonction des crochets

"""
import DistributiviteSandbox

formuleBrutString = "Apoll�n#([D�lios+Kalumnas-Mede�n]/Zeus)"
formuleBrutList = ['Apoll�n', '#', '(', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', 'Zeus', ')']

formuleDeveloppeeString = "[Apoll�n#[D�lios+Kalumnas-Mede�n]]/[Apoll�n#Zeus]"
formuleDeveloppeeList = ['[', 'Apoll�n', '#', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', '[', 'Apoll�n', '#',
                         'Zeus', ']']

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


def tableAdjacence(formule):  # Cr�e la table d'adjacence
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


def comparerFormule(formuleBrut, formuleDeveloppee, table):
    # Pour donner les valeurs aux couples
    valeurBase = 1
    valeurModif = 1
    paire = []
    index = 0
    dicoPaireValeur = {}

    print(len(formuleBrutList))

    for indice in range(len(formuleBrutList)):
        if formuleBrutList[indice] not in signes.values():
            if formuleBrutList[indice + 1] == '#':
                paire = []
                cpt = indice + 1
                paire.append(formuleBrutList[indice], )
                while cpt < len(formuleBrutList) - 1:
                    while formuleBrutList[cpt] in signes.values():
                        cpt += 1
                        paire[index] = (formuleBrutList[indice], formuleBrutList[cpt])
                    cpt += 1
                    dicoPaireValeur[paire[index]] = valeurBase



            elif formuleBrutList[indice + 1] == '+':
                paire = []

                cpt = indice + 1
                paire.append(formuleBrutList[indice], )
                while cpt < len(formuleBrutList) - 1:
                    while formuleBrutList[cpt] in signes.values():
                        cpt += 1
                        paire[index] = (formuleBrutList[indice], formuleBrutList[cpt])
                    cpt += 1
                    dicoPaireValeur[paire[index]] = valeurBase


            elif formuleBrutList[indice + 1] == ']':
                paire = []
                cpt = indice + 1
                paire.append(formuleBrutList[indice], )
                while cpt < len(formuleBrutList) - 1:
                    while formuleBrutList[cpt] in signes.values():
                        cpt += 1
                        paire[index] = (formuleBrutList[indice], formuleBrutList[cpt])
                    cpt += 1
                    dicoPaireValeur[paire[index]] = valeurBase
        else:
            if formuleBrutList[indice] != '[':
                valeurBase += 1

    print("paire")
    print(paire)
    print("")
    print("dico Valeurs")
    print(dicoPaireValeur)
    print("")


print("Table d'Adjacence")
res = tableAdjacence(formuleBrutString)
print(tableAdjacence(formuleBrutString))
print("")

print("Valeurs apres comparaison des formules")
print(comparerFormule(formuleBrutList, formuleDeveloppeeList, res))
print("")
