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
formuleBrutList3 = ['Apollôn', '#', '(', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', 'Zeus', ')']  # Ok

formuleDeveloppeeString = "[Apollôn#[Dêlios+Kalumnas-Medeôn]]/[Apollôn#Zeus]"
formuleDeveloppeeList = ['[', 'Apollôn', '#', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', '[', 'Apollôn', '#',
                         'Zeus', ']']

formuleBrutList = ['Apollôn', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK si pas de -1

formuleBrutList4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "Hêra", ')', '#', "Epêkoos"]

formuleBrutList2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']

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

        # Si l'element de l'expression est pas un carac spécial
        if indice < len(formuleBrutList) - 1 and formuleBrutList[indice] not in signes.values():
            if formuleBrutList[indice + 1] == '#' or '+':  # Si l'element suivant est #
                paire = []  # initialise la liste qui recevra le tuple
                cpt = indice + 1
                paire.append(formuleBrutList[indice], )  # Crée le tuple avec l'element et vide
                while cpt < len(formuleBrutList) - 1:  # tant que cpt est inférieur a la longueur de la liste - 1
                    while formuleBrutList[cpt] in signes.values():  # Tant que l'element comparé est un carac spécial

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
                        dicoPaireValeur[paire[index]] = valeurModif  # ajoute au dictionnaire avec la valeur calculée
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
