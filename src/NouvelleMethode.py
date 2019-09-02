# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

import csv
import os
import VerificationFormules

from datetime import datetime

# Récupère l'heure et la date du jour
date = datetime.now()
datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')


# Algorithme de traitement des formules
def calculEG(listeFormules):
    global dico_paire_force
    listePrete = VerificationFormules.nettoyageFormules(listeFormules)  # Prépare les formules pour le traitement

    apparition = calcul_nombre_apparition(listeFormules)  # Calcule le nombre d'apparition dans les formules

    for formule in listePrete:
        couple1 = u""  # Permier élement pour le tuple
        couple2 = u""  # Second élément pour le tuple

        repeat = u""  # Le nom qui est répété
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

                if formule[element] not in VerificationFormules.signes.values():
                    # Si element est pas un caracrère spécial
                    if formule[element] not in elementCompte:  # L'ajoute a la liste
                        if couple1 == u"":  # Si couple1 est vide ajoute l'element
                            couple1 = formule[element]
                            elementCompte.append(formule[element])
                        else:  # Sinon l'ajoute a couple2
                            couple2 = formule[element]
                    else:  # Sinon passe au suivant
                        if couple1 == formule[element] and repeat == u"":
                            repeat = element
                            repetition = True  # Indique une répétition
                        if repetition is True:
                            pass
                        else:
                            force_lien = (crochet_ouvert * 3) + (parenthese_ouverte * 2)

                if couple1 != u"" and couple2 != u"":  # Si les 2 variables sont différente de vide
                    if (couple1, couple2) in dico_paire_force:  # Si le couple existe fait rien
                        pass
                    else:  # Sinon l'ajoute au dictionnaire avec la force de lien associé
                        if force_lien == 0:
                            force_lien = 1
                        dico_paire_force[(couple1, couple2)] = force_lien
                    couple2 = u""  # Réinitialise le couple 2
            couple1 = u""  # Réinitialise couple 1

        # Gestion de la répétition
        if repeat != u"":
            for i in reversed(range(repeat)):  # Parcours en sens inverse depuis l'élément répété
                if formule[i] == '[':  # Si l'element est un crochet ajoute 1 et lien * 3
                    crochet_ouvert += 1
                    force_lien = crochet_ouvert * 3

                if formule[i] == '(':  # Si l'element est une parenthèse ajoute 1 et lien * 2
                    parenthese_ouverte += 1
                    force_lien = parenthese_ouverte * 2

                if formule[i] not in VerificationFormules.signes.values():
                    # Si rencontre une élément non spécial coupe la boucle
                    break

            couple1 = formule[repeat]  # Couple1 recoit l'element répété

            for i in formule[repeat + 1:]:  # Parcours la boucle depuis l'élément répété
                if i not in VerificationFormules.signes.values():
                    # Si l'élément est pas un caratère spécial couple2 = i
                    couple2 = i
                if couple1 != u"" and couple2 != u"":  # Si les 2 variables sont différente de vide
                    # Si le couple existe replace la valeur si elle est plus grande
                    if (couple1, couple2) in dico_paire_force:
                        if force_lien > dico_paire_force[(couple1, couple2)]:
                            dico_paire_force[(couple1, couple2)] = force_lien

            fusion = fusion_dictionnaire(dico_paire_force, apparition)

            # Ecrit dans le CSV le resultat
            ecrireCSV(elementCompte, fusion)
            repeat = u""

        else:
            fusion = fusion_dictionnaire(dico_paire_force, apparition)
            # Ecrit dans le CSV le resultat
            ecrireCSV(elementCompte, fusion)


# Fonction de calcul du nombre d'apparition d'un mot
def calcul_nombre_apparition(listeFormules):
    dico_apparait = {}  # Dictionnaire qui stocke les noms et le nombre d'apparition du mot

    for exp in listeFormules:  # Regarde chaque formule
        trigger = u""
        nombre_apparition = 1  # nombre d'apparition

        for carac in exp:
            if carac not in VerificationFormules.signes.values():  # Récupère tout hors caractère spécial
                trigger += carac
            else:
                if trigger != u"":  # Reconstitue le nom
                    if trigger in dico_apparait.keys():  # Ajoute 1 en plus a chaque apparition par formule
                        dico_apparait[trigger] = nombre_apparition + 1
                        trigger = u""
                    else:
                        dico_apparait[trigger] = nombre_apparition  # Ajoute le nom pour la première fois
                        trigger = u""

        if trigger != u"":  # Ajoute le dernier nom
            dico_apparait[trigger] = 1
            trigger = u""

    print('dico_noms')
    print(dico_apparait)
    print()

    return dico_apparait


# Fonction pour regrouper les dictionnaires
def fusion_dictionnaire(dico_paire_force, apparition):
    fusion_dico = {}

    for couple, force in dico_paire_force.items():
        for nom, nombre in apparition.items():  # Regarde pour chaque couple le nombre d'apparition du nom
            if couple[0] == nom:  # Stocke la valeur pour le premier element du couple
                temp = (couple[0], nombre)

            if couple[1] == nom:  # Stocke la valeur pour le second element du couple
                temp2 = (couple[1], nombre)

        # Quand les deux variables sont non nulles les assembles en un tuple dans un dictionnaire
        if temp != u"" and temp2 != u"":
            fusion_dico[couple] = (force, temp[1], temp2[1])

    return fusion_dico


# Fonction écriture du CSV
def ecrireCSV(elementCompte, fusion):  # Ecris le CSV avec la nouvelle méthode de calcul
    global nomfichierEdge

    # Récupère l'heure et la date du jour
    date = datetime.now()
    datestr = date.strftime('_%Y-%m-%d-%H-%M-%S')

    nomfichierEdge = 'CSVTraiteMAP/CalculMAP_Edges' + datestr

    id = 1  # Id pour les paires
    if os.path.exists('CSVTraiteMAP/CalculMAP_Edges' + datestr + '.csv'):  # Si le fichier existe ecrit a la suite
        with open('CSVTraiteMAP/CalculMAP_Edges' + datestr + '.csv', 'a', newline='', encoding='utf-8') as csvfile:

            nomfichierEdge = 'CSVTraiteMAP/CalculMAP_Edges' + datestr

            writer = csv.writer(csvfile, delimiter=',')
            # writer.writerow(("Source", "Target", "Id", "Force_lien"))
            for cle, valeur in fusion.items():
                writer.writerow((cle[0], cle[1], id, valeur[0], valeur[1], valeur[2]))
                id += 1

        with open('CSVTraiteMAP/CalculMAP_Nodes' + datestr + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(('', '', ''))

            num = 1
            for i in elementCompte:
                writer.writerow((num, i, i))
                num += 1
    else:  # Si le fichier n'existe pas le crée

        if not os.path.exists('CSVTraiteMAP'):  # Crée le dossier qui contiendra les fichiers traités
            os.makedirs('CSVTraiteMAP')
        with open('CSVTraiteMAP/CalculMAP_Edges' + datestr + '.csv', 'w', newline='', encoding='utf-8') as csvfile:

            nomfichierEdge = 'CSVTraiteMAP/CalculMAP_Edges' + datestr

            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(("Source", "Target", "Id", "Force_lien", "ForceSrc", "ForceTgt"))

            for cle, valeur in fusion.items():
                writer.writerow((cle[0], cle[1], id, valeur[0], valeur[1], valeur[2]))
                id += 1

        with open('CSVTraiteMAP/CalculMAP_Nodes' + datestr + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(('Nodes', 'nom', 'Label',))

            num = 1
            for i in elementCompte:
                writer.writerow((num, i, i))
                num += 1


if __name__ == "__main__":
    # Liste
    lise3 = ['[([Isis#Sôtêr]/Astartê/[Aphroditê#Euploia])#Epêkoos]+[Erôs/Harpokratês/Apollôn]']
    lise2 = ["([Kurios#Zeus]+Hêra)#Epêkoos", '[Apollôn#Zeus]+[Apollôn#Kedrieus]']
    lise = ['[Apollôn#Zeus]+[Apollôn#Kedrieus]']
    # calcul_nombre_apparition(lise2)
    calculEG(lise3)
