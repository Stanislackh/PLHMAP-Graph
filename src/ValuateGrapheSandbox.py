# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

"""Projet graphe valué

objectifs:
 - Faire une table d'adjacence
 - Comparer avec la formule développée
 - Mettre les valeurs en fonction des crochets

"""
import DistributiviteSandbox

formuleBrutString = "Apollôn#([Dêlios+Kalumnas-Medeôn]/Zeus)"
formuleBrutList = ['Apollôn', '#', '(', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', 'Zeus', ')']

formuleDeveloppeeString = "[Apollôn#[Dêlios+Kalumnas-Medeôn]]/[Apollôn#Zeus]"
formuleDeveloppeeList = ['[', 'Apollôn', '#', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', '[', 'Apollôn', '#',
                         'Zeus', ']']

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


def tableAdjacence(formule):  # Crée la table d'adjacence
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
