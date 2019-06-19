# -- coding: windows-1252 --
# Created by Slackh
# Github : https://github.com/Stanislackh


"""faire de la distributivité"""

cas1 = "([a#b] + [[c#d] / [e#f]])# [g#h]"
# => [a#b]# [g#h] + [[c#d] / [e#f]]# [g#h]

cas2 = "a#(b+c)"  # CAS OK
cas3 = "a #(b + c)"
# => a#b + a#c

cas4 = "(a+b)#c"
# => a#c + b#c

"""tritement cas2"""

""" Liste des signes pour les formules """

signes = {
    1: "+", 2: "/", 3: "#", 4: "(", 5: ")", 6: "[", 7: "]", 8: "=", 9: " "
}

chaine = []

for carach in cas1:
    chaine.append(carach)

print(chaine)
pileA = []
pileB = []
pilePrenthese = []
nbParO = 0
nbParF = 0
nbCrochO = 0
nbCrochF = 0

for element in chaine:
    if element not in signes.values():
        pileA.append(element)
        if len(pileB) == 0:
            pass
    elif element == "/":
        pileA.append(element)

    elif element == "(":
        nbCrochO += 1
        for i in pileA:
            pileB.append(i)
    elif element == ")":
        nbCrochF += 1
        print("pileB")
        print(pileB)


    elif element == "#":
        pileA.append(element)

    elif element == "[":
        nbCrochO += 1
    elif element == "]":
        nbCrochF += 1

    elif element == "+":
        pileA.append(element)
        for i in pileB:
            pileA.append(i)

    elif element == "=":
        pileA.append(element)
    elif element == " ":
        pass
    else:
        print("ce symbole est inconnu erreur de saisie !")

if (nbCrochF != nbCrochO) or (nbParF != nbParO):
    print("Erreur de syntaxe")
print("Pile A Finale")
print(pileA)
res = ""
for i in pileA:
    res += str(i)
print(res)
