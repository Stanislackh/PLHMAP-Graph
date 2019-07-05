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

formuleDeveloppeeString = "[Apollôn#[Dêlios+Kalumnas-Medeôn]]/[Apollôn#Zeus]"
formuleDeveloppeeList = ['[', 'Apollôn', '#', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', '[', 'Apollôn', '#',
                         'Zeus', ']']

formuleBrutList = ['Apollôn', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK si pas de -1

formuleBrutList3 = ['Apollôn', '#', '(', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', 'Zeus', ')']  # Ok

formuleBrutList4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "Hêra", ')', '#', "Epêkoos"]

formuleBrutList2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']

# noms = {
#     1: "Zeus",
#     2: "Hêlios",
#     3: "Megas",
#     4: "Sarapis",
#     5: "Apollôn",
#     6: "Puthios",
#     7: "Kedrieus",
#     8: "Kurios",
#     9: "Hêra",
#     10: "Epêkoos",
#     11: "Ammôn",
#     12: "Chnoubis",
#     13: "Satis",
#     14: "Hestia",
#     15: "Anoukis",
#     16: "Isis",
#     17: "Sôtêr",
#     18: "Astartê",
#     19: "Aphroditê",
#     20: "Euploia",
#     21: "Theos",
#     22: "Artemis",
#     23: "Athêna",
#     24: "Boulaios",
#     25: "Dêlios",
#     26: "Kalumnas-Medeôn",
#     27: "Hugieia",
#     28: "Telesphoros",
#     29: "Alexiponos",
#     30: "Dionusos",
#     31: "Phleos",
#     32: "Brontôn",
#     33: "Karpodotês",
#     34: "Eucharistos",
#     35: "Asklêpios"}
#
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


#
#
# def tableAdjacence(formule):  # Crée la table d'adjacence
#     listeNoms = []
#     for element in noms.values():  # récupère la liste de noms
#         if element in formule:
#             listeNoms.append(element)
#
#     couples = []  # fait les associations soit des tuples
#     dernierElemListe = len(listeNoms)  # Eviter les out of index
#
#     if dernierElemListe == 1:  # Si le nom est seul l'ajoute a la liste sinon fait les couples
#         couples.append(listeNoms[0])
#     else:
#         for i in range(dernierElemListe - 1):  # Pour chaque élément crée une paire avec les eléments suivants
#             j = 0  # Initialise pour le tant que
#             while j < dernierElemListe - 1:
#                 # Vérifie que les noms soit différents et fait des paires uniques
#                 if listeNoms[i] != listeNoms[j + 1] and ((listeNoms[j + 1], listeNoms[i]) not in couples):
#                     couples.append((listeNoms[i], listeNoms[j + 1]))
#                 j += 1
#
#     return couples
#
#
# def comparerFormule(formuleBrut, formuleDeveloppee, table):
#     # Pour donner les valeurs aux couples
#     valeurModif = 1
#     index = 0
#     dicoPaireValeur = {}
#     co = 0
#     cf = 0
#
#     def valeurMin(valeurModif):
#         if valeurModif == 0:
#             valeurModif = 1
#         return valeurModif
#
#     for indice in range(len(formuleBrutList)):  # Parcours l'expression
#
#         if formuleBrutList[indice] == '[':
#             co += 1
#         elif formuleBrutList[indice] == ']':
#             cf += 1
#
#         # Si l'element de l'expression est pas un carac spécial
#         if indice < len(formuleBrutList) - 1 and formuleBrutList[indice] not in signes.values():
#             if formuleBrutList[indice + 1] == '#' or '+':  # Si l'element suivant est #
#                 paire = []  # initialise la liste qui recevra le tuple
#                 cpt = indice + 1
#                 paire.append(formuleBrutList[indice], )  # Crée le tuple avec l'element et vide
#                 while cpt < len(formuleBrutList) - 1:  # tant que cpt est inférieur a la longueur de la liste - 1
#                     while formuleBrutList[cpt] in signes.values():  # Tant que l'element comparé est un carac spécial
#
#                         print("ininin")
#                         print(formuleBrutList[cpt])
#                         print()
#                         if co == cf or formuleBrutList[cpt - 1] == "]":
#                             cf += 1
#                             valeurModif -= 1
#                         cpt += 1
#                         paire[index] = (formuleBrutList[indice], formuleBrutList[cpt])  # Ajoute le 2eme element
#                     cpt += 1
#                     if formuleBrutList[cpt - 1] == "]" or cpt == len(formuleBrutList):
#                         dicoPaireValeur[paire[index]] = valeurModif  # ajoute au dictionnaire avec la valeur calculée
#                     else:
#                         dicoPaireValeur[paire[index]] = valeurModif  # Trouver un moyen pour supprimer le -1 ...
#                         if dicoPaireValeur[paire[index]] == 0:
#                             valeurModif = valeurMin(valeurModif)
#                             dicoPaireValeur[paire[index]] = valeurModif
#
#         else:
#             if formuleBrutList[indice] == "(":
#                 valeurModif += 1
#
#             elif formuleBrutList[indice] == "[":
#                 valeurModif += 1
#
#             elif formuleBrutList[indice] == ")":
#                 valeurModif -= 1
#
#             # elif formuleBrutList[indice] == "]":
#             #     valeurModif -= 1
#
#     print("dico Valeurs")
#     print(dicoPaireValeur)
#     print("")
#
#
# # print("Table d'Adjacence")
# res = tableAdjacence(formuleBrutString)
# # print(tableAdjacence(formuleBrutString))
# # print("")
#
# print("Valeurs apres comparaison des formules")
# print(comparerFormule(formuleBrutList, formuleDeveloppeeList, res))
# print("")


def newAlgo(formule):
    couple1 = ""  # Permier élement pour le tuple
    couple2 = ""  # Second élément pour le tuple

    dico_paire_force = {}  # Dictionnaire des couples possibles avec les forces des liens

    crochet_ouvert = 0  # compte le nombre de crochet ouveert
    parenthese_ouverte = 0  # Compte le nombre de parenthèses ouverte

    force_lien = 1  # Force du lien en les 2 élements du tuple

    index = 0  # Index de l'élément couple1 1 3 7 9

    while index < len(formule):

        indice = index  # Indice pour avancer dans l'expression

        if index == len(formule) - 1:  # Si l'index a la même valeur que la longuer de la formule stop
            break

        else:  # Regarde si il reste des elements non spéciaux sinon break
            stop = index
            if stop < len(formule) - 1:
                if formule[stop] in signes.values():
                    stop += 1
                if formule[indice] == len(formule) - 1:
                    break
                stop += 1

        while indice < len(formule) - 1:  # Tant que l'indice est inférieur a la longeur de

            if formule[indice] == "[" and couple1 == "":  # Si l'élément set un crochet ouvert reçoit 3

                crochet_ouvert += 1  # Ajoute 1 au nombre de crochets ouvert
                force_lien = 3  # Force de lien 3
                indice += 1

            elif formule[indice] == "(" and couple1 == "":  # Si l'élément est une parenthèse ouverte reçoit 2
                if crochet_ouvert == 0:  # Si pas de crochet ouvrant
                    parenthese_ouverte += 1  # Ajoute 1 au nombre de parenthèses ouverte
                    force_lien = 2  # Force de lien 2
                    indice += 1
                else:  # si pas de crochets ouvrants
                    parenthese_ouverte += 1  # Ajoute 1 au nombre de parenthèses ouverte
                    force_lien = 1  # Force de lien 1
                    indice += 1

            elif formule[indice] == ")":  # Si l'élément est une parenthèse fermante
                if parenthese_ouverte == 0:  # le nombre de parenthèses ouverte est 0 laisse a 0
                    parenthese_ouverte = 0
                else:
                    parenthese_ouverte -= 1  # Enlève une parenthèse

                if crochet_ouvert > 0:  # Regarde le nombre de crochet ouvert
                    force_lien -= 1  # Si il y des crochets ouverts enlève 1 a la force
                    indice += 1
                else:  # Sinon remet la force a 1
                    force_lien = 1
                    indice += 1

            elif formule[indice] == "]":
                if crochet_ouvert == 0:  # Si le nombre de crochet ouvert est 0 laisse a 0
                    crochet_ouvert = 0
                else:
                    crochet_ouvert -= 1  # Enlève un crochet

                if parenthese_ouverte > 0:
                    force_lien -= 1  # Si il y a des parenthèsse ouvertes enlève 1 a la force
                    indice += 1
                else:  # Sinon remet la force a 1
                    force_lien = 1
                    indice += 1
            else:  # Si symbole autre avance de 1
                indice += 1

            if formule[indice] not in signes.values():  # Si l'élément est pas un signe spécial
                if couple1 == "":  # L'ajoute a couple 1 si celui ci est vide sinon ajoute a couple 2
                    couple1 = formule[indice]
                    index = indice
                    indice += 1
                else:
                    couple2 = formule[indice]  # Si couple1 est pris ajoute au second
                    indice += 1

            if couple1 != "" and couple2 != "":  # Si les 2 variables sont non vides les ajoute au dictionnaire
                dico_paire_force[(couple1, couple2)] = force_lien
                couple2 = ""

        couple1 = ""  # Réinitialise pour le prochain élément

    print(dico_paire_force)


newAlgo(formuleBrutList2)
