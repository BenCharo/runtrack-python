import re

file = open("domains.xml", "r")
line = file.read() #transforme file en str
file.close()
listDomaine = []

for x in range(len(line)):
    i = 7
    adresse = ''
    if line[x] == "d" and line[x + 1] == "o" and line[x + 2] == "m" and line[x + 3] == "a" and line[x + 4] == "i" and \
            line[x + 5] == "n" and line[x + 7] == ">": #on cherche lorsqu'il y a le fin de la balise <column "domaine">
        while line[x + i] != "<": #on parcourt l'adresse mail jusqu'a arriver a la fin et au debut de la balise </column>
            i += 1
        i -= 1
        while line[x + i] != ".":       #on retourne en arrière au dernier point qui sera le début du nom de domaine et on
            adresse += line[x + i]      #ajoute chaque lettre dans notre variable adresse (notre nom de domaine sera inversé)
            i -= 1
        adresse += line[x + i]
        listDomaine.append(adresse[::-1])   #on met notre nom de domaine a l'endroit

while len(listDomaine) != 0:    #dès qu'on a récupéré un nom de domaine, on le compte puis on le supprime de notre liste de nom de domaine
    print("Il y a ", listDomaine.count(listDomaine[0]), listDomaine[0])     #on repete ca jusqu'a ce que notre liste de domaine soit vide
    listDomaine = list(filter((listDomaine[0]).__ne__, listDomaine))