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
f4 = "([Kurios # Zeus] + Hêra ) # Epêkoos"
f5 = "[Ammôn = Chnoubis] + [Hêra = Satis] + [Hestia = Anoukis]"
f6 = "(Zeus + Hêra) # Sôtêr"

# Liste des Dieux et Mots

dico = {
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

# résultat pour F1
"""Si split aux / Je garde que les noms"""
# res = f1.split("/")
# print(res)

"""Si split a l'espace je garde tout """
res2 = f1.split(" ")
print(res2)

"""Affichage de res après boucle"""
res = f1.split(" ")
for i in res:
    print(i)


