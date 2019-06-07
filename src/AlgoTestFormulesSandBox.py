# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

""" Fichier test pour le traitement des formules avec certaines contraintes

Définition des symbloles :
    /   Symbole de la juxtaposition
    #   Symbole d'un qualifiant
    +   Symbole de la coordination => et
    ()  Symbole de la distributivité
    []  Symbole de l'ensemble
    =   Symbole de l'équivalence

    une formule ressemble à ceci:   ([Kurios # Zeus] + Hêra ) # Epêkoos

    la décomposition est la suivante:

    Kurios Zeus est un ensemble dans lequel Kurios définit Zeus et Hêra est définit Epêkoos ainsi que Kurios Zeus
    Ensemble                                                  Coordianation         Distributivité

Travaillons sur un algorithme pour travailler la formule
"""

#  Liste des formules à étudier

f1 = "Zeus / Hêlios / Megas / Sarapis"
f2 = "[Apollôn # Puthios] + [Apollôn # Kedrieus]"
f3 = "Apollôn # (Puthios + Kedrieus)"
f4 = "([Kurios # Zeus] + Hêra) # Epêkoos"
f5 = "[Ammôn = Chnoubis] + [Hêra = Satis] + [Hestia = Anoukis]"
f6 = "(Zeus + Hêra) # Sôtêr"
f7 = "[Theos # Sôtêr] # (Artemis + Apollôn)"
f8 = "[Zeus # Sôtêr] + (Athêna # Sôtêr)"
f9 = "[Zeus # Boulaios] + [Athêna # Boulaios] + Hestia"
f10 = "Artemis # Puthios"
f11 = "Dionusos # Phleos"
f12 = "[Zeus # Brontôn] + [Zeus # Karpodotês] + [Zeus # Eucharistos]"
f13 = "Apollôn # (Dêlios + Kalumnas-Medeôn)"
f14 = "Isis # Sôtêr # (Astartê / Aphroditê) # (Euploia + Epêkoos)"
f15 = "(Asklêpios + Hugieia + Telephoros) # Alexiponos"
f16 = "Sôtêr"

# Liste des attestations
attestations = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16]

"""Liste des Dieux et Mots"""

noms = {
    1: "Zeus",
    2: "Hêlios",
    3: "Megas",
    4: "Sarapis",
    5: "Appolôn",
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
    21: "Theoi",
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
    34: "Eucharistos"}

""" Liste des signes pour les formules """

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

""" Foctionne avec variable"""


def coocurenceArc(formule):  # Permet de calculer la Coocurence des formules
    """
    :param formule
    :return Le nombre de fois qu'un nom appraît dans la formule et les liens avec les autres noms

    """
    noeud = {}  # Permet de stocker la taille des noeuds
    cle = 0  # Clé pour le dictionnaire à incrémenter
    noeud2 = {}  # Dictionnaire avec les nombre de noms mentionnés dans les formules

    res = formule.split(" ")  # Permet de découper la formule en supprimant les espaces
    for i in res:
        for j in signes.values():  # Regarde dans le dictionnaire des signes si il apparait
            if i == j:
                res.remove(j)  # Supprime les signes spéciaux des formules

    temp = []  # Liste temporaire

    for i in res:  # Permet de parcourir les élément de la liste res
        temp.append(" ")  # Ajoute chaque element à la liste coupé a l'espace
        for j in i:
            if j not in signes.values():  # Ajoute les caractères non spéciaux
                temp.append(j)

    del temp[0]  # Supprime l'espace ajouté au début de la liste

    """Calcule la taille des noeuds"""
    chaine = ""  # Création de la chaine vide qui sera split par l'espace

    for i in temp:  # Parcours la liste temp pour la traduire en chaine de caractère
        chaine += i
    final = chaine.split(" ")  # Coupe la chaine de caractère à l'espace pour en refaire uen liste
    compte = {}.fromkeys(set(final), 0)  # Définit le compteur pour chaque mot présent

    for valeur in final:  # Compte le nombre d'occurence de mots dans la liste
        compte[valeur] += 1
    noeud[cle] = compte  # Ajoute le nombre de fois qu'apparait un nom dans chaque formule
    cle += 1  # Incrémente la clé du dictionnaire de stockage

    print(noeud)
    """Calcule le nombre de fois qu'un nom apparait dans toutes les formules"""
    #  A mettre dans une autre fonction

    # for element in noeud.values():  # Parcous le dictionnaire de dictionnaire
    #     for i in element:  # Parcours chaque élémément du dictionnaire
    #         if i not in noeud2.keys():  # Regarde si un élement est dans la liste sinon l'ajoute
    #             noeud2[i] = 1  # Ajoute l'élément et l'initialise a 1
    #         else:
    #             noeud2[i] += 1  # Incrémente la valeur si celui ci est présent
    #
    # return noeud2  # Revoie le dictionnaire avec les nobres d'apparition des noms


"""Calcule les taille des arcs"""

"""Cooccurence avec liste en entrée"""


def coocurenceListe(liste):  # Permet de calculer la Coocurence des formules
    """
    :param Liste de formules
    :return Le nombre de fois qu'un nom appraît dans la formule

    """

    """Compte le poids pour les noeuds"""
    poids = {}  # Dictionnaire qui indique le nombre total d'apparition du mot
    cle = 0  # Clé pour le dictionnaire à incrémenter
    noeud = {}  # Dictionnaire qui indique le nombre de formules où un mot est mentionné (unique)
    arc = {}  # Dictionnaire pour voir les relations entre les mots
    clea = 0  # Clé pour les arcs
    # Lit pour chaque élément de la liste
    for element in liste:  # Applique pour chaque élément de la liste le traitement de la formule
        formule = element

        res = formule.split(" ")  # Permet de découper la formule en supprimant les espaces
        for i in res:
            for j in signes.values():  # Regarde dans le dictionnaire des signes si il apparait
                if i == j:
                    res.remove(j)  # Supprime les signes spéciaux des formules
        temp = []  # Liste temporaire

        # A mettre dans une autre fonction
        for i in res:  # Permet de parcourir les élément de la liste res
            temp.append(" ")  # Ajoute chaque element à la liste coupé a l'espace
            for j in i:
                if j not in signes.values():  # Ajoute les caractères non spéciaux
                    temp.append(j)

        del temp[0]  # Supprime l'espace ajouté au début de la liste

        """Calcule le nombre total d'apparition du mot"""
        chaine = ""  # Création de la chaine vide qui sera split par l'espace
        for i in temp:  # Parcours la liste temp pour la traduire en chaine de caractère
            chaine += i
        final = chaine.split(" ")  # Coupe la chaine de caractère à l'espace pour en refaire uen liste

        """Ajoute les listes de noms à un dictionnaire"""
        arc[clea] = final
        clea += 1

        compte = {}.fromkeys(set(final), 0)  # Définit le compteur pour chaque mot présent

        for valeur in final:  # Compte le nombre d'occurence de mots dans la liste
            compte[valeur] += 1
        poids[cle] = compte  # Ajoute le nombre de fois qu'apparait un nom dans chaque formule
        cle += 1  # Incrémente la clé du dictionnaire de stockage
    print("arc")
    print(arc)
    # nombre total d'apparition
    apparait = {}
    for elem, val in poids.items():  # Regarde dans le Dictionnaire
        for nom, nombre in val.items():  # Ragarde dans le dictionnaire du dictionnaire
            if nom not in apparait:
                apparait[nom] = nombre  # Ajoute le mot et sa valeur associée
            else:
                apparait[nom] += nombre  # Ajoute la valeur si le nom existe déjà
    print("apparait")
    print(apparait)
    """Calcule le nombre de fois qu'un nom apparait dans toutes les formules"""

    for element in poids.values():  # Parcous le dictionnaire de dictionnaire
        for i in element:  # Parcours chaque élémément du dictionnaire
            if i not in noeud.keys():  # Regarde si un élement est dans la liste sinon l'ajoute
                noeud[i] = 1  # Ajoute l'élément et l'initialise a 1
            else:
                noeud[i] += 1  # Incrémente la valeur si celui ci est présent
    print("noeud")
    print(noeud)
    # return noeud, poids  # Revoie le dictionnaire avec les nombres d'apparition des noms par formules et le total

    """Calcul pour les arcs"""


if __name__ == "__main__":
    # print(coocurenceArc(f12))
    coocurenceListe(attestations)
    print("")
