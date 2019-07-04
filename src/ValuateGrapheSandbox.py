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
formuleBrutList3 = ['Apoll�n', '#', '(', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', 'Zeus', ')']  # Ok

formuleDeveloppeeString = "[Apoll�n#[D�lios+Kalumnas-Mede�n]]/[Apoll�n#Zeus]"
formuleDeveloppeeList = ['[', 'Apoll�n', '#', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', '[', 'Apoll�n', '#',
                         'Zeus', ']']

formuleBrutList = ['Apoll�n', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK si pas de -1

formuleBrutList4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "H�ra", ')', '#', "Ep�koos"]

formuleBrutList2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']

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
    valeurModif = 1
    index = 0
    dicoPaireValeur = {}
    co = 0
    cf = 0

    def valeurMin(valeurModif):
        if valeurModif == 0:
            valeurModif = 1
        return valeurModif

    for indice in range(len(formuleBrutList)):  # Parcours l'expression

        if formuleBrutList[indice] == '[':
            co += 1
        elif formuleBrutList[indice] == ']':
            cf += 1

        # Si l'element de l'expression est pas un carac sp�cial
        if indice < len(formuleBrutList) - 1 and formuleBrutList[indice] not in signes.values():
            if formuleBrutList[indice + 1] == '#' or '+':  # Si l'element suivant est #
                paire = []  # initialise la liste qui recevra le tuple
                cpt = indice + 1
                paire.append(formuleBrutList[indice], )  # Cr�e le tuple avec l'element et vide
                while cpt < len(formuleBrutList) - 1:  # tant que cpt est inf�rieur a la longueur de la liste - 1
                    while formuleBrutList[cpt] in signes.values():  # Tant que l'element compar� est un carac sp�cial

                        print("ininin")
                        print(formuleBrutList[cpt])
                        print()
                        if co == cf or formuleBrutList[cpt - 1] == "]":
                            cf += 1
                            valeurModif -= 1
                        cpt += 1
                        paire[index] = (formuleBrutList[indice], formuleBrutList[cpt])  # Ajoute le 2eme element
                    cpt += 1
                    if formuleBrutList[cpt - 1] == "]" or cpt == len(formuleBrutList):
                        dicoPaireValeur[paire[index]] = valeurModif  # ajoute au dictionnaire avec la valeur calcul�e
                    else:
                        dicoPaireValeur[paire[index]] = valeurModif  # Trouver un moyen pour supprimer le -1 ...
                        if dicoPaireValeur[paire[index]] == 0:
                            valeurModif = valeurMin(valeurModif)
                            dicoPaireValeur[paire[index]] = valeurModif

        else:
            if formuleBrutList[indice] == "(":
                valeurModif += 1

            elif formuleBrutList[indice] == "[":
                valeurModif += 1

            elif formuleBrutList[indice] == ")":
                valeurModif -= 1

            # elif formuleBrutList[indice] == "]":
            #     valeurModif -= 1

    print("dico Valeurs")
    print(dicoPaireValeur)
    print("")


# print("Table d'Adjacence")
res = tableAdjacence(formuleBrutString)
# print(tableAdjacence(formuleBrutString))
# print("")

print("Valeurs apres comparaison des formules")
print(comparerFormule(formuleBrutList, formuleDeveloppeeList, res))
print("")
