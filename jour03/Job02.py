import re

file = open("data.txt", "r")
line = file.read()
file.close()
x = re.split("\s", line)
cpt = 0



for i in x:
    if i.isalnum() is True:
        cpt += 1

print(x)
#print("Il y a", cpt, "mots sans caractères spéciaux dans data.txt")