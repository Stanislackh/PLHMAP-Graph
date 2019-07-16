# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh

"""Projet graphe valué

objectifs:
 - Faire une table d'adjacence
 - Comparer avec la formule développée
 - Mettre les valeurs en fonction des crochets
"""

import csv
import os
from datetime import datetime

f1 = ['Apollôn', '#', '(', "Puthios", '+', "Kedrieus", ')']  # OK
f2 = ['[', 'Theos', '#', 'Soter', ']', '#', '(', 'Artemis', '+', 'Apollon', ')']  # OK

f3 = ['Apollôn', '#', '(', '[', 'Dêlios', '+', 'Kalumnas-Medeôn', ']', '/', 'Zeus', ')']  # OK
f4 = ['(', '[', "Kurios", '#', 'Zeus', ']', '+', "Hêra", ')', '#', "Epêkoos"]  # OK

f5 = ['[', '[', 'Zeus', '/', 'Heios', ']', '/', '[', 'Megas', '#', 'Sarapis', ']', ']', '+', '[',
      'Sunnaoi', '#', 'Theoi', ']']  # OK

f6 = ['[', 'Apollon', '#', 'Puthios', ']', '+', '[', 'Apollon', '#', 'Kedrieus', ']']

f7 = ['[', '(', '[', 'Isis', '#', 'Sôtêr', ']', '/', 'Astartê', '/', '[', 'Aphroditê', '#', 'Euploia',
      ']', ')', '#', 'Epêkoos', ']', '+', '[', 'Erôs', '/', 'Harpokratês', '/', 'Apollôn', ']']  # OK
ff1 = "([Kurios#Zeus]+Hêra)#Epêkoos"
ff2 = "[Theos#Soter]#(Artemis+Apollon)"
ff3 = "[([Isis# Sôtêr]/Astartê/[Aphroditê#Euploia])#Epêkoos] + [Erôs/Harpokratês/Apollôn]"
ff4 = "[Apollôn#Puthios]+[Apollôn#Kedrieus]"
ff5 = "38#[45#(46#47)]"
listeFormules2 = [f1, f2, f3, f4, f5, f7]
listeFormules = [ff5]

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

date = datetime.now()  # Récupère l'heure et la date du jour
datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')


def nettoyageFormules(listeformules):
    listeInter = []

    trigger = ""  # Pour reformer le nom

    for indice in range(len(listeformules)):  # Regarde pour la longueur de la liste de formule
        listeSplit = []  # Stockage de la formule splittée

        for j in listeformules[indice]:  # Pour chaque élément de la formule
            listeSplit.append(j)  # L'ajoute a la liste
        listeInter.append(listeSplit)  # La listes est ajoutée a la liste

    listeSuperPropre = []  # Liste de fin

    for i in listeInter:  # Pour la liste intermédiaire

        listePropre = []  # Initialise la liste tampons
        for j in i:  # Pour chaque élément dans la liste
            if j in signes.values():  # Si j est un caractère spécial
                if trigger != "":  # Si trigger est pas vide ajoute trigger à la liste
                    listePropre.append(trigger)
                    trigger = ""  # Réinitialise Trigger
                listePropre.append(j)  # Ajoute à la liste
            else:
                trigger += j  # trigger reçoit la caractène non spécial
        listePropre.append(trigger)
        trigger = ""  # Réinitialise trigger
        listeSuperPropre.append(listePropre)  # Ajoute à la liste de fin

    return listeSuperPropre  # Renvoie la liste de fin


def creationDicoDynamique(nomsDansFormules):  # Fonction qui permet de créer le dictionnaire des noms dynamiquement
    global dicoNoms
    global cleDico

    dicoNoms = {}  # Dictionaire des noms
    cleDico = 0  # Clé pour le dictionnaire

    for i in nomsDansFormules.values():  # Pour chaque nom dans triée dans les formules
        for element in i:  # Pour chaque élément dans la liste
            if element in dicoNoms.values():  # Si l l'élément est dans da liste passe Sinon l'ajoute
                pass
            else:
                dicoNoms[cleDico] = element
                cleDico += 1

    return dicoNoms  # Renvoie le dictionnaire


""" Peut etre une solution

Parcourir la séquence autant de fois qu'il y a d'élement,
des que élément non spécial garder l'indice dans une liste 'index' et le faire une comparaison plus tard
si l'indice de boucle est dans la liste ignore et passe a la suivante puis fait le traitement 
avec le second element non spécial ect ... 
Normalement ça devrait le faire puis faire en sorte d'intérgrer le nouveau système de comptage cumulatif"""


def superAlgo(listeFormules):
    listePrete = nettoyageFormules(listeFormules)  # Prépare les formules pour le traitement
    # creationDicoDynamique(listeFormules)  # Crée un dictionnaire avec les noms

    for formule in listePrete:
        couple1 = ""  # Permier élement pour le tuple
        couple2 = ""  # Second élément pour le tuple

        repeat = ""  # Le nom qui est répété
        repetition = False

        crochet_ouvert = 0  # compte le nombre de crochet ouveert
        parenthese_ouverte = 0  # Compte le nombre de parenthèses ouverte

        dico_paire_force = {}  # Dictionnaire des couples possibles avec les forces des liens
        elementCompte = []  # Permet de stocker un element non spécial  déjà traité

        for index in range(len(formule)):  # Parcours la liste autant de fois qu'il y a d'éléments

            force_lien = 1  # Force du lien en les 2 élements du tuple

            for element in range(len(formule)):  # Regarde pour chaque élément

                if formule[element] == '[' and couple1 == "":  # Si l'element est un crochet ouvert
                    crochet_ouvert += 1  # Ajoute 1 aux crochets ouvert
                    if crochet_ouvert >= 1:  # Si le nobre de crochets ouvert est > 1 ajoute 3 sinon mets la force a 3
                        # Donne au lien le nombre de crochet * 3
                        force_lien = crochet_ouvert * 3 + parenthese_ouverte * 2
                elif formule[element] == '[':  # Si l'element est un crochet et que couple1 ets non vide rajoute 1
                    crochet_ouvert += 1

                if formule[element] == ']':  # Si l'element est un crochet fermant
                    crochet_ouvert -= 1  # Enlève 1 aux crochets ouvert
                    if crochet_ouvert >= 1 and parenthese_ouverte == 0:  # Si le nombre de crochet est > 1 crochet *3
                        force_lien = crochet_ouvert * 3
                        if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                            force_lien = 1
                    # Si le nombre de crochet et parenthèse est >= 1 crochet *3 + parenthèses * 2
                    elif crochet_ouvert >= 1 and parenthese_ouverte >= 1:
                        force_lien = crochet_ouvert * 3 + parenthese_ouverte * 2
                        if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                            force_lien = 1
                    elif crochet_ouvert == 0 and parenthese_ouverte >= 1:  # Si pas de crochet parenthèses * 2
                        force_lien = parenthese_ouverte * 2
                        if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                            force_lien = 1
                    else:
                        force_lien = 1

                if formule[element] == '(' and couple1 == "":  # Si l'élement est une parenthèse ouvrante
                    parenthese_ouverte += 1  # Ajoute 1 aux parenthèses ouvrantes
                    if parenthese_ouverte >= 1:  # Si parenthèses ouvrant est > 1  force = 2 * nb parenthèses
                        force_lien = parenthese_ouverte * 2 + crochet_ouvert * 3
                    else:  # Sinon met la force à 2
                        force_lien = 2
                elif formule[element] == '(':  # Si parenthèse ouvrante et couple1 non vide ajoute 1
                    parenthese_ouverte += 1

                if formule[element] == ')':  # Si l'element est une parenthèse fermante enlève 1 aux parenthèses
                    parenthese_ouverte -= 1  # Enlève 1 aux parenthèses ouvrantes
                    if crochet_ouvert >= 1 and parenthese_ouverte >= 1:
                        force_lien -= 1
                        if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                            force_lien = 1

                    elif crochet_ouvert >= 1 and parenthese_ouverte == 0:
                        force_lien = crochet_ouvert * 3
                    elif parenthese_ouverte >= 1:  # Si le nombre de parenthèses ouvrante est > 1
                        force_lien -= 2
                        if force_lien <= 0:  # Si la force du lien atteint 0 ou moins le remet a 1
                            force_lien = 1
                    else:
                        force_lien = 1

                if formule[element] not in signes.values():  # Si element est pas un caracrère spécial
                    if formule[element] not in elementCompte:  # L'ajoute a la liste
                        if couple1 == "":  # Si couple1 est vide ajoute l'element
                            couple1 = formule[element]
                            elementCompte.append(formule[element])
                        else:  # Sinon l'ajoute a couple2
                            couple2 = formule[element]
                    else:  # Sinon passe au suivant
                        if couple1 == formule[element] and repeat == "":
                            repeat = element
                            repetition = True  # Indique une répétition
                        if repetition is True:
                            pass
                        else:
                            force_lien = (crochet_ouvert * 3) + (parenthese_ouverte * 2)

                if couple1 != "" and couple2 != "":  # Si les 2 variables sont différente de vide
                    if (couple1, couple2) in dico_paire_force:  # Si le couple existe fait rien
                        pass
                    else:  # Sinon l'ajoute au dictionnaire avec la force de lien associé
                        dico_paire_force[(couple1, couple2)] = force_lien
                    couple2 = ""  # Réinitialise le couple 2
            couple1 = ""  # Réinitialise couple 1

        # Gestion de la répétition
        if repeat != "":
            for i in reversed(range(repeat)):  # Parcours en sens inverse depuis l'élément répété
                if formule[i] == '[':  # Si l'element est un crochet ajoute 1 et lien * 3
                    crochet_ouvert += 1
                    force_lien = crochet_ouvert * 3

                if formule[i] == '(':  # Si l'element est une parenthèse ajoute 1 et lien * 2
                    parenthese_ouverte += 1
                    force_lien = parenthese_ouverte * 2

                if formule[i] not in signes.values():  # Si rencontre une élément non spécial coupe la boucle
                    break

            couple1 = formule[repeat]  # Couple1 recoit l'element répété

            for i in formule[repeat + 1:]:  # Parcours la boucle depuis l'élément répété
                if i not in signes.values():  # Si l'élément est pas un caratère spécial couple2 = i
                    couple2 = i
                if couple1 != "" and couple2 != "":  # Si les 2 variables sont différente de vide
                    # Si le couple existe replace la valeur si elle est plus grande
                    if (couple1, couple2) in dico_paire_force:
                        if force_lien > dico_paire_force[(couple1, couple2)]:
                            dico_paire_force[(couple1, couple2)] = force_lien

            print("dico force")
            print(dico_paire_force)
            # Ecrit dans le CSV le resultat
            # ecrireCSV(dico_paire_force, elementCompte)
            repeat = ""

        else:
            print("dico force 2")
            print(dico_paire_force)
            # Ecrit dans le CSV le resultat
            # ecrireCSV(dico_paire_force, elementCompte)


def ecrireCSV(dicoPaireForce, elementCompte):  # Ecris le CSV avec la nouvelle méthode de calcul
    id = 1  # Id pour les paires
    if os.path.exists('GrapheValueEdges' + datestr + '.csv'):  # Si le fichier existe ecrit a la suite
        with open('GrapheValueEdges' + datestr + '.csv', 'a', newline='', encoding='windows-1252') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(("", "", "", ""))
            for cle, valeur in dicoPaireForce.items():
                writer.writerow((cle[0], cle[1], id, valeur))
                id += 1

        with open('GrapheValueNodes' + datestr + '.csv', 'a', newline='', encoding='windows-1252') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(('', '', ''))

            num = 1
            for i in elementCompte:
                writer.writerow((num, i, i))
                num += 1
    else:  # Si le fichier n'existe pas le crée

        # Correspond aux arcs dans Gephi
        with open('GrapheValueEdges' + datestr + '.csv', 'w', newline='', encoding='windows-1252') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(("Source", "Target", "Id", "Force_lien"))

            for cle, valeur in dicoPaireForce.items():
                writer.writerow((cle[0], cle[1], id, valeur))
                id += 1

        with open('GrapheValueNodes' + datestr + '.csv', 'w', newline='', encoding='windows-1252') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(('Nodes', 'nom', 'Label',))

            num = 1
            for i in elementCompte:
                writer.writerow((num, i, i))
                num += 1


if __name__ == "__main__":
    superAlgo(listeFormules)
