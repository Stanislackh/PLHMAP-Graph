# -- coding: utf-8 --
# Created by Slackh
# Github : https://github.com/Stanislackh

# Liste des signes spéciaux
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

# Dictionnaire de toutes les erreurs possibles avec les symboles
dicoErreurs = {
    "+#": True,
    "+/": True,
    "+)": True,
    "+]": True,
    "+=": True,
    "++": True,

    "/+": True,
    "/#": True,
    "/)": True,
    "/]": True,
    "/=": True,
    "//": True,

    "#+": True,
    "#/": True,
    "#)": True,
    "#]": True,
    "#=": True,
    "##": True,

    "(+": True,
    "(/": True,
    "(#": True,
    "()": True,
    "(]": True,
    "(=": True,

    ")/": True,
    ")(": True,
    ")[": True,
    ")=": True,

    "[+": True,
    "[/": True,
    "[#": True,
    "[)": True,
    "[]": True,
    "[=": True,

    "](": True,
    "]=": True,
    "][": True,

    "=+": True,
    "=/": True,
    "=#": True,
    "=(": True,
    "=)": True,
    "=[": True,
    "=]": True,
    "==": True,
}


def checkNbParCroch(listeCasNettoye):  # Regarde le si le nombre de crochets est ok
    global kek
    # Liste des variables locales
    nbParO = 0
    nbParF = 0
    nbCrochO = 0
    nbCrochF = 0

    for formule in listeCasNettoye:  # Regarde chaque formules
        kek = formule
        print(kek)
        for carac in formule:
            if carac == "(":  # Ajoute 1 si égal a (
                nbParO += 1
            elif carac == ')':  # Ajoute 1 si égal a )
                nbParF += 1
            elif carac == '[':  # Ajoute 1 si égal a [
                nbCrochO += 1
            elif carac == "]":  # Ajoute 1 si égal a ]
                nbCrochF += 1

        erreur = False
        if (nbCrochF != nbCrochO) or (nbParF != nbParO):
            # print("Erreur de syntaxe, Vérifiez le nombre de crochets et de parenthèses")
            erreur = True
            break

    return erreur


def caracMalPlace(listeCasNettoye):  # Regarde dans la liste des erreurs de syntaxes si elle y figure
    global phrase
    syntaxeErreur = False

    for cas in listeCasNettoye:  # Regarde dans la liste des formules
        if syntaxeErreur == False:
            temp = cas.split(",")
            for phrase in temp:  # Regarde la formule
                # Regarde pour chaque paire de caractère si il figure dans le dictionnaire des erreurs
                for indice in range(len(phrase) - 1):
                    if ((phrase[indice] + phrase[indice + 1]) in dicoErreurs.keys()) or \
                            ((phrase[indice] == ")") and (phrase[indice + 1] not in signes.values())) or \
                            ((phrase[indice] == "]") and (phrase[indice + 1] not in signes.values())) or \
                            ((phrase[indice] not in signes.values()) and (phrase[indice + 1] == "(")) or \
                            ((phrase[indice] not in signes.values()) and (phrase[indice + 1] == "[")):
                        print("Erreur de saisie, Vérifiez la syntaxe de " + phrase)
                        print(phrase[indice] + phrase[indice + 1])
                        syntaxeErreur = True

                        return syntaxeErreur, phrase

    return syntaxeErreur


# Prépare les formules pour le traitement
def nettoyageFormules(listeformules):
    if (checkNbParCroch(listeformules) is False) and (caracMalPlace(listeformules) is False):
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
        print(listeSuperPropre)
        return listeSuperPropre  # Renvoie la liste de fin
    else:
        print("erreur")
