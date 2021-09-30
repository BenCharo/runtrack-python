import matplotlib.pyplot as plt
import re

file = open("data.txt", "r")
line = file.read()
file.close()
line.lower()
x = "abcdefghijklmnopqrstuvwxyz"
alph = sorted(x)

dic = {}
for i in range(25):
    cpt = line.count(alph[i])
    dic[alph[i]] = cpt/(len(line))


print(dic)
plt.bar(dic.keys(), dic.values(), 0.75, color='g')
plt.show()