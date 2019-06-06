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

f1 = "Zeus / Hêlios / Megas / Sarapis / Zeus / Zeus"
f2 = "[Apollôn # Puthios] + [Apollôn # Kedrieus]"
f3 = "Apollôn # (Puthios + Kedrieus)"
f4 = "([Kurios # Zeus] + Hêra ) # Epêkoos"
f5 = "[Ammôn = Chnoubis] + [Hêra = Satis] + [Hestia = Anoukis]"
f6 = "(Zeus + Hêra) # Sôtêr"

"""Liste des Dieux et Mots"""

noms = {
    1: "Zeus",
    2: "Hêlios",
    3: "Megas",
    4: "Sarapis",
    5: "Apollôn",
    6: "Puthios",
    7: "Kedrieus",
    8: "Hêra",
    9: "Epêkoos",
    10: "Ammôn",
    11: "Chnoubis",
    13: "Satis",
    14: "Anoukis",
    15: "Sôtêr",
    16: "Kurios",
    17: "Hestia"
}
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
# résultat pour F1
"""Si split aux / Je garde que les noms"""
# res = f1.split("/")


"""Affichage de res après boucle"""
# res = f1.split(" ")
# for i in res:
#     print(i)

"""Affichage avec le dictionnaire"""
# for key, valeur in dico.items():
#     print(valeur)

"""Combinaison V1 OK"""


def coocurence(formule):  # Permet de calculer la Coocurence des formules
    """
    :param formule
    :return Le nombre de fois qu'un nom appraît dans la formule

    """

    res = formule.split(" ")  # Permet de découper la formule en supprimant les espaces
    for i in res:
        for j in signes.values():  # Regarde dans le dictionnaire des signes si il apparait
            if i == j:
                res.remove(j)  # Supprime les signes spéciaux des formules

    temp = []  # Liste temporaire

    for i in res:  # Permet de parcourir les élément de la liste res
        temp.append(" ")  # Ajoute chaque
        for j in i:
            if j not in signes.values():  # Ajoute les caractères non spéciaux
                temp.append(j)

    del temp[0]  # Supprime l'espace ajouté au début de la liste
    chaine = ""  # Création de la chaine vide qui sera split par l'espace

    for i in temp:  # Parcours la liste temp pour la traduire en chaine de caractère
        chaine += i
    final = chaine.split(" ")  # Coupe la chaine de caractère à l'espace pour en refaire uen liste
    compte = {}.fromkeys(set(final), 0)  # Définit le compteur pour chaque mot présent

    for valeur in final:  # Compte le nombre d'occurence de mots dans la liste
        compte[valeur] += 1
    return compte  # Renvoie la liste


if __name__ == "__main__":
    print(coocurence(f1))
