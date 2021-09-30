import re

file = open("domains.xml", "r")
line = file.read() #transforme file en str
x = re.findall("<column name=\"domain\">", line)  #on cherche le nombre d'utilisation de la balise domaine utilisée a chaque nom de domaine
print(len(x))