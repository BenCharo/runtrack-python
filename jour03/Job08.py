import re
import matplotlib.pyplot as plt

file = open("data.txt", "r")
line = file.read()
split = re.split(" ", line)
file.close()

dic = {}
for i in split:
    if i[-1:] == "." or i[-1:] == "," or i[-1:] == ";" or i[-1:] == ":" or i[-1:] == "!" or i[-1:] == "?":  # on supprime les caractères spéciaux pour qu'ils ne
        i = i[:-1]
    if len(i) in dic:
        dic[len(i)] += 1
    else:
        dic[len(i)] = 1

print(dic)
plt.bar(dic.keys(), dic.values(), 0.75, color='r')
plt.show()