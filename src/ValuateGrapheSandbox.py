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
import csv

formuleBrutList1 = ['Apoll�n', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK
formuleBrutList2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']  # OK

formuleBrutList3 = ['Apoll�n', '#', '(', '[', 'D�lios', '+', 'Kalumnas-Mede�n', ']', '/', 'Zeus', ')']  # OK
formuleBrutList4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "H�ra", ')', '#', "Ep�koos"]  # OK

formuleBrutList5 = ['[', '[', 'Zeus', '/', 'Heios', ']', '/', '[', 'Megas', '#', 'Sarapis', ']', ']', '+', '[',
                    'Sunnaoi', '#', 'Theoi', ']']  # OK

formuleBrutList6 = ['[', 'Apollon', '#', 'Puthios', ']', '+', '[', 'Apollon', '#', 'Kedrieus', ']']

formuleBrutListBoss = ['[', '(', '[', 'Isis', '#', 'S�t�r', ']', '/', 'Astart�', '/', '[', 'Aphrodit�', '#', 'Euploia',
                       ']', ')', '#', 'Ep�koos', ']', '+', '[', 'Er�s', '/', 'Harpokrat�s', '/', 'Apoll�n', ']']  # OK
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


""" Peut etre une solution

Parcourir la s�quence autant de fois qu'il y a d'�lement,
des que �l�ment non sp�cial garder l'indice dans une liste 'index' et le faire une comparaison plus tard
si l'indice de boucle est dans la liste ignore et passe a la suivante puis fait le traitement 
avec le second element non sp�cial ect ... 
Normalement �a devrait le faire puis faire en sorte d'int�rgrer le nouveau syst�me de comptage cumulatif"""


def superAlgo(formule):
    couple1 = ""  # Permier �lement pour le tuple
    couple2 = ""  # Second �l�ment pour le tuple

    dico_paire_force = {}  # Dictionnaire des couples possibles avec les forces des liens

    elementCompte = []  # Permet de stocker un element non sp�cial  d�j� trait�

    for index in range(len(formule)):  # Parcours la liste autant de fois qu'il y a d'�l�ments

        crochet_ouvert = 0  # compte le nombre de crochet ouveert
        parenthese_ouverte = 0  # Compte le nombre de parenth�ses ouverte

        force_lien = 1  # Force du lien en les 2 �lements du tuple

        for element in range(len(formule)):  # Regarde pour chaque �l�ment

            if formule[element] == '[' and couple1 == "":  # Si l'element est un crochet ouvert
                crochet_ouvert += 1  # Ajoute 1 aux crochets ouvert
                if crochet_ouvert >= 1:  # Si le nobre de crochets ouvert est > 1 ajoute 3 sinon mets la force a 3
                    force_lien = crochet_ouvert * 3  # Donne au lien le nombre de crochet * 3
            elif formule[element] == '[':  # Si l'element est un crochet et que couple1 ets non vide rajoute 1
                crochet_ouvert += 1

            if formule[element] == ']':  # Si l'element est un crochet fermant
                crochet_ouvert -= 1  # Enl�ve 1 aux crochets ouvert
                if crochet_ouvert >= 1 and parenthese_ouverte == 0:  # Si le nombre de crochet ouvert est > 1 enl�ve 3
                    force_lien -= 3
                    if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                        force_lien = 1
                elif crochet_ouvert >= 1 and parenthese_ouverte >= 1:  # Si le nombre est >= enl�ve 1
                    force_lien -= 1
                    if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                        force_lien = 1
                elif crochet_ouvert == 0 and parenthese_ouverte >= 1:  # Si pas de crochet enleve 1 de force
                    force_lien -= 1
                    if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                        force_lien = 1
                else:
                    force_lien = 1

            if formule[element] == '(' and couple1 == "":  # Si l'�lement est une parenth�se ouvrante
                parenthese_ouverte += 1  # Ajoute 1 aux parenth�ses ouvrantes
                if parenthese_ouverte >= 1:  # Si parenth�ses ouvrant est > 1  force = 2 * nb parenth�ses
                    force_lien = parenthese_ouverte * 2
                else:  # Sinon met la force � 2
                    force_lien = 2
            elif formule[element] == '(':  # Si parenth�se ouvrante et couple1 non vide ajoute 1
                parenthese_ouverte += 1

            if formule[element] == ')':  # Si l'element est une parenth�se fermante enl�ve 1 aux parenth�ses ouvrantes
                parenthese_ouverte -= 1  # Enl�ve 1 aux parenth�ses ouvrantes
                if crochet_ouvert >= 1 and parenthese_ouverte >= 1:
                    force_lien -= 1
                    if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                        force_lien = 1

                elif crochet_ouvert >= 1 and parenthese_ouverte == 0:
                    force_lien = crochet_ouvert * 3
                elif parenthese_ouverte >= 1:  # Si le nombre de parenth�ses ouvrante est > 1
                    force_lien -= 2
                    if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                        force_lien = 1
                else:
                    force_lien = 1

            if formule[element] not in signes.values():  # Si element est pas un caracr�re sp�cial
                if formule[element] not in elementCompte:  # L'ajoute a la liste
                    if couple1 == "":  # Si couple1 est vide ajoute l'element
                        couple1 = formule[element]
                        elementCompte.append(formule[element])
                    else:  # Sinon l'ajoute a couple2
                        couple2 = formule[element]
                else:  # Sinon passe au suivant
                    pass

            if couple1 != "" and couple2 != "":  # Si les 2 variables sont diff�rente de vide
                if (couple1, couple2) in dico_paire_force:  # Si le couple existe fait rien
                    pass
                else:  # Sinon l'ajoute au dictionnaire avec la force de lien associ�
                    dico_paire_force[(couple1, couple2)] = force_lien
                couple2 = ""  # R�initialise le couple 2
        couple1 = ""  # R�initialise couple 1

    print("Dico Yay")
    for i, j in dico_paire_force.items():
        print(i, ": ", j)
    print()

    # Ecrit dans le CSV le resultat
    ecrireCSV(dico_paire_force)


def ecrireCSV(dicoPaireForce):
    with open('GrapheValue.csv', 'w', newline='', encoding='windows-1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(("Source", "Target", "Id", "Weight"))

        id = 1  # Cl� pour l'id
        for cle, valeur in dicoPaireForce.items():
            writer.writerow((cle[0], cle[1], id, valeur))
            id += 1


if __name__ == "__main__":
    superAlgo(formuleBrutList6)
