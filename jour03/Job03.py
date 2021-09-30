import re

file = open("data.txt", "r")
line = file.read()
file.close()
line.lower()
x = line.split() #on sépare le texte en tableau de mot pour les tester un a un
cpt = 0

taille = int(input("Des mots de quelle taille voulez-vous chercher ?\n"))

for i in x:
    if i[-1:] == "." or i[-1:] == "," or i[-1:] == ";" or i[-1:] == ":" or i[-1:] == "!" or i[-1:] == "?": #on supprime les caractères spéciaux pour qu'ils ne
        i = i[:-1]                                                          #modifient pas la taille de nos mots
    if len(i) == taille:
        cpt += 1            #on incrémente le compteur dès qu'on est tombé sur un mot sans caractères spéciaux

print("Il y a", cpt, "mots de taille", taille, "dans data.txt")