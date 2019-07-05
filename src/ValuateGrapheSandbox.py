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

formuleDeveloppeeString = "[Apoll�n#[D�lios+Kalumnas-Mede�n]]/[Apoll�n#Zeus]"
formuleDeveloppeeList = ['[', 'Apoll�n', '#', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', '[', 'Apoll�n', '#',
                         'Zeus', ']']

formuleBrutList = ['Apoll�n', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK si pas de -1

formuleBrutList3 = ['Apoll�n', '#', '(', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', 'Zeus', ')']  # Ok

formuleBrutList4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "H�ra", ')', '#', "Ep�koos"]

formuleBrutList2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']

# noms = {
#     1: "Zeus",
#     2: "H�lios",
#     3: "Megas",
#     4: "Sarapis",
#     5: "Apoll�n",
#     6: "Puthios",
#     7: "Kedrieus",
#     8: "Kurios",
#     9: "H�ra",
#     10: "Ep�koos",
#     11: "Amm�n",
#     12: "Chnoubis",
#     13: "Satis",
#     14: "Hestia",
#     15: "Anoukis",
#     16: "Isis",
#     17: "S�t�r",
#     18: "Astart�",
#     19: "Aphrodit�",
#     20: "Euploia",
#     21: "Theos",
#     22: "Artemis",
#     23: "Ath�na",
#     24: "Boulaios",
#     25: "D�lios",
#     26: "Kalumnas-Mede�n",
#     27: "Hugieia",
#     28: "Telesphoros",
#     29: "Alexiponos",
#     30: "Dionusos",
#     31: "Phleos",
#     32: "Bront�n",
#     33: "Karpodot�s",
#     34: "Eucharistos",
#     35: "Askl�pios"}
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
# def tableAdjacence(formule):  # Cr�e la table d'adjacence
#     listeNoms = []
#     for element in noms.values():  # r�cup�re la liste de noms
#         if element in formule:
#             listeNoms.append(element)
#
#     couples = []  # fait les associations soit des tuples
#     dernierElemListe = len(listeNoms)  # Eviter les out of index
#
#     if dernierElemListe == 1:  # Si le nom est seul l'ajoute a la liste sinon fait les couples
#         couples.append(listeNoms[0])
#     else:
#         for i in range(dernierElemListe - 1):  # Pour chaque �l�ment cr�e une paire avec les el�ments suivants
#             j = 0  # Initialise pour le tant que
#             while j < dernierElemListe - 1:
#                 # V�rifie que les noms soit diff�rents et fait des paires uniques
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
#         # Si l'element de l'expression est pas un carac sp�cial
#         if indice < len(formuleBrutList) - 1 and formuleBrutList[indice] not in signes.values():
#             if formuleBrutList[indice + 1] == '#' or '+':  # Si l'element suivant est #
#                 paire = []  # initialise la liste qui recevra le tuple
#                 cpt = indice + 1
#                 paire.append(formuleBrutList[indice], )  # Cr�e le tuple avec l'element et vide
#                 while cpt < len(formuleBrutList) - 1:  # tant que cpt est inf�rieur a la longueur de la liste - 1
#                     while formuleBrutList[cpt] in signes.values():  # Tant que l'element compar� est un carac sp�cial
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
#                         dicoPaireValeur[paire[index]] = valeurModif  # ajoute au dictionnaire avec la valeur calcul�e
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
    couple1 = ""  # Permier �lement pour le tuple
    couple2 = ""  # Second �l�ment pour le tuple

    dico_paire_force = {}  # Dictionnaire des couples possibles avec les forces des liens

    crochet_ouvert = 0  # compte le nombre de crochet ouveert
    parenthese_ouverte = 0  # Compte le nombre de parenth�ses ouverte

    force_lien = 1  # Force du lien en les 2 �lements du tuple

    index = 0  # Index de l'�l�ment couple1 1 3 7 9

    while index < len(formule):

        indice = index  # Indice pour avancer dans l'expression

        if index == len(formule) - 1:  # Si l'index a la m�me valeur que la longuer de la formule stop
            break

        else:  # Regarde si il reste des elements non sp�ciaux sinon break
            stop = index
            if stop < len(formule) - 1:
                if formule[stop] in signes.values():
                    stop += 1
                if formule[indice] == len(formule) - 1:
                    break
                stop += 1

        while indice < len(formule) - 1:  # Tant que l'indice est inf�rieur a la longeur de

            if formule[indice] == "[" and couple1 == "":  # Si l'�l�ment set un crochet ouvert re�oit 3

                crochet_ouvert += 1  # Ajoute 1 au nombre de crochets ouvert
                force_lien = 3  # Force de lien 3
                indice += 1

            elif formule[indice] == "(" and couple1 == "":  # Si l'�l�ment est une parenth�se ouverte re�oit 2
                if crochet_ouvert == 0:  # Si pas de crochet ouvrant
                    parenthese_ouverte += 1  # Ajoute 1 au nombre de parenth�ses ouverte
                    force_lien = 2  # Force de lien 2
                    indice += 1
                else:  # si pas de crochets ouvrants
                    parenthese_ouverte += 1  # Ajoute 1 au nombre de parenth�ses ouverte
                    force_lien = 1  # Force de lien 1
                    indice += 1

            elif formule[indice] == ")":  # Si l'�l�ment est une parenth�se fermante
                if parenthese_ouverte == 0:  # le nombre de parenth�ses ouverte est 0 laisse a 0
                    parenthese_ouverte = 0
                else:
                    parenthese_ouverte -= 1  # Enl�ve une parenth�se

                if crochet_ouvert > 0:  # Regarde le nombre de crochet ouvert
                    force_lien -= 1  # Si il y des crochets ouverts enl�ve 1 a la force
                    indice += 1
                else:  # Sinon remet la force a 1
                    force_lien = 1
                    indice += 1

            elif formule[indice] == "]":
                if crochet_ouvert == 0:  # Si le nombre de crochet ouvert est 0 laisse a 0
                    crochet_ouvert = 0
                else:
                    crochet_ouvert -= 1  # Enl�ve un crochet

                if parenthese_ouverte > 0:
                    force_lien -= 1  # Si il y a des parenth�sse ouvertes enl�ve 1 a la force
                    indice += 1
                else:  # Sinon remet la force a 1
                    force_lien = 1
                    indice += 1
            else:  # Si symbole autre avance de 1
                indice += 1

            if formule[indice] not in signes.values():  # Si l'�l�ment est pas un signe sp�cial
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

        couple1 = ""  # R�initialise pour le prochain �l�ment

    print(dico_paire_force)


newAlgo(formuleBrutList2)
