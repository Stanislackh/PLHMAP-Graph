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

formuleBrutList1 = ['Apollôn', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK
formuleBrutList2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']  # OK

formuleBrutList3 = ['Apollôn', '#', '(', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', 'Zeus', ')']
formuleBrutList4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "Hêra", ')', '#', "Epêkoos"]

formuleBrutListBoss = ['[', '(', '[', 'Isis', '#', 'Sôtêr', ']', '/', 'Astartê', '/', '[', 'Aphroditê', '#', 'Euploia',
                       ']', ')', '#', 'Epêkoos', ']', '+', '[', 'Erôs', '/', 'Harpokratês', '/', 'Apollôn', ']']
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

        if index == len(formule) - 1:  # Si l'index a la même valeur que la longueur que la formule stop
            break

        else:  # Regarde si il reste des elements non spéciaux sinon break
            stop = index
            if stop < len(formule) - 1:
                if formule[stop] in signes.values():
                    stop += 1
                if stop + 1 == len(formule) - 1:
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
            elif formule[indice] == '(':
                parenthese_ouverte += 1  # Ajoute 1 au nombre de parenthèses ouverte
                force_lien = 1  # Force de lien 1
                indice += 1

            elif formule[indice] == ")":  # Si l'élément est une parenthèse fermante

                if parenthese_ouverte < 0:  # le nombre de parenthèses ouverte est 0 laisse a 0
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

                if crochet_ouvert == 0 and parenthese_ouverte > 0:  # Pas de crochets mais une parenthèse force 2
                    force_lien = 2
                # if crochet_ouvert == 0 and parenthese_ouverte == 0:  # Si le nombre de crochet ouvert est 0 laisse a 0
                #     force_lien = 1
                elif crochet_ouvert < 0:  # Si le nombre est inférieur a 0 le remet a 0
                    crochet_ouvert = 0

                else:
                    crochet_ouvert -= 1  # Enlève un crochet

                if parenthese_ouverte > 0 and crochet_ouvert != 0:
                    force_lien -= 1  # Si il y a des parenthèsse ouvertes enlève 1 a la force
                    indice += 1
                else:  # Sinon remet la force a 1
                    indice += 1

            # Ajoute a couple 1 si vide et pas signe spécial
            elif couple1 == "" and formule[indice] not in signes.values():
                couple1 = formule[indice]
                index = indice + 1
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

            # Faire une condition
            # if parenthese_ouverte > 0 and crochet_ouvert == 0:
            #     force_lien = 2

            if couple1 != "" and couple2 != "":  # Si les 2 variables sont non vides les ajoute au dictionnaire
                if (couple1, couple2) in dico_paire_force:
                    pass
                else:
                    dico_paire_force[(couple1, couple2)] = force_lien
                couple2 = ""
        couple1 = ""  # Réinitialise pour le prochain élément

    print("dico")
    print(dico_paire_force)
    print()

    return dico_paire_force


# newAlgo(formuleBrutListBoss)

""" Peut etre une solution

Parcourir la séquence autant de fois qu'il y a d'élement,
des que élément non spécial garder l'indice dans une liste 'index' et le faire une comparaison plus tard
si l'indice de boucle est dans la liste ignore et passe a la suivante puis fait le traitement 
avec le second element non spécial ect ... 
Normalement ça devrait le faire puis faire en sorte d'intérgrer le nouveau système de comptage cumulatif"""


def superAlgo(formule):
    couple1 = ""  # Permier élement pour le tuple
    couple2 = ""  # Second élément pour le tuple

    dico_paire_force = {}  # Dictionnaire des couples possibles avec les forces des liens

    # crochet_ouvert = 0  # compte le nombre de crochet ouveert
    # parenthese_ouverte = 0  # Compte le nombre de parenthèses ouverte

    elementCompte = []  # Permet de stocker un element non spécial  déjà traité

    force_lien = 1  # Force du lien en les 2 élements du tuple

    for index in range(len(formule)):  # Parcours la liste autant de fois qu'il y a d'éléments

        crochet_ouvert = 0  # compte le nombre de crochet ouveert
        parenthese_ouverte = 0  # Compte le nombre de parenthèses ouverte

        force_lien = 1  # Force du lien en les 2 élements du tuple

        for element in range(len(formule)):  # Regarde pour chaque élément

            if formule[element] == '[' and couple1 == "":  # Si l'element est un crochet ouvert
                crochet_ouvert += 1  # Ajoute 1 aux crochets ouvert
                if crochet_ouvert >= 1:  # Si le nobre de crochets ouvert est > 1 ajoute 3 sinon mets la force a 3
                    force_lien = crochet_ouvert * 3  # Donne au lien le nombre de crochet * 3
            elif formule[element] == '[':
                crochet_ouvert += 1

            if formule[element] == ']':  # Si l'element est un crochet fermant
                crochet_ouvert -= 1  # Enlève 1 aux crochets ouvert
                if crochet_ouvert >= 1 and parenthese_ouverte == 0:  # Si le nombre de crochet ouvert est > 1 enlève 3
                    force_lien -= 3
                elif crochet_ouvert >= 1 and parenthese_ouverte >= 1:  # Si le nombre est >= enlève 1
                    force_lien -= 1
                elif crochet_ouvert == 0 and parenthese_ouverte >= 1:
                    force_lien -= 1
                else:
                    force_lien = 1

            if formule[element] == '(':  # Si l'élement est une parenthèse ouvrante
                parenthese_ouverte += 1  # Ajoute 1 aux parenthèses ouvrantes
                if parenthese_ouverte >= 1:  # Si parenthèses ouvrant est > 1 ajoute 2
                    force_lien = parenthese_ouverte * 2
                else:  # Sinon met la force à 2
                    force_lien = 2

            if formule[element] == ')':  # Si l'element est une parenthèse fermante enlève 1 aux parenthèses ouvrantes
                parenthese_ouverte -= 1  # Enlève 1 aux parenthèses ouvrantes
                if crochet_ouvert >= 1 and parenthese_ouverte >= 1:
                    force_lien -= 1
                elif crochet_ouvert >= 1 and parenthese_ouverte == 0:
                    force_lien = crochet_ouvert * 3
                elif parenthese_ouverte >= 1:  # Si le nombre de parenthèses ouvrante est > 1
                    force_lien -= 2
                else:
                    force_lien = 1

            if formule[element] not in signes.values():  # Si element est pas un caracrère spécial
                if formule[element] not in elementCompte:  # L'ajoute a la liste
                    if couple1 == "":  # Si couple1 est vide ajoute l'element
                        couple1 = formule[element]
                        elementCompte.append(formule[element])
                    else:
                        couple2 = formule[element]
                else:  # Sinon passe au suivant
                    pass

            if couple1 != "" and couple2 != "":  # Si les 2 variables sont différente de vide
                if (couple1, couple2) in dico_paire_force:  # Si le couple existe fait rien
                    pass
                else:  # Sinon l'ajoute au dictionnaire avec la force de lien associé
                    dico_paire_force[(couple1, couple2)] = force_lien
                couple2 = ""  # Réinitialise le couple 2
        couple1 = ""  # Réinitialise couple 1

    print("Dico Yay")
    print(dico_paire_force)
    print()


superAlgo(formuleBrutListBoss)
