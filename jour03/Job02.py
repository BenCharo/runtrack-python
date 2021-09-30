import re

file = open("data.txt", "r")
line = file.read()
file.close()
x = line.split() #on sépare le texte en tableau de mot pour les tester un a un
cpt = 0



for i in x:
    if i[-1:] == "." or i[-1:] == "," or i[-1:] == ";" or i[-1:] == ":" or i[-1:] == "!" or i[-1:] == "?": #on vérifie que les caracteres speciaux des mots ne sont
        i = i[:-1]                                                       #pas dûs à la ponctuation, et on les supprime dans ce cas la
    if i.isalnum() is True:
        cpt += 1            #on incrémente le compteur dès qu'on est tombé sur un mot sans caractères spéciaux

print("Il y a", cpt, "mots sans caractères spéciaux dans data.txt")