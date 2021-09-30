import matplotlib.pyplot as plt
import re

file = open("data.txt", "r")
line = file.read()
file.close()
x = "abcdefghijklmnopqrstuvwxyz"
alph = sorted(x)
y = x.upper()
alph_upp = sorted(y)
split = line.split()

dic = {}
for i in range(25):
    for j in split:
        if j[0] == alph[i] or j[0] == alph_upp[i]:
            if alph_upp[i] in dic:
                dic[alph_upp[i]] += 1
            else:
                dic[alph_upp[i]] = 1

print(dic)
plt.bar(dic.keys(), dic.values(), 0.75, color='r')
plt.show()