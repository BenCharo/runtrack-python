import matplotlib.pyplot as plt
import re

file = open("data.txt", "r")
line = file.read()
file.close()
line.lower()
x = "abcdefghijklmnopqrstuvwxyz"
alph = sorted(x)

split = line.split()

dic = {}
for i in range(25):
    for j in split:
        if j[0] == alph[i]:
            if alph[i] in dic:
                dic[alph[i]] += 1
            else:
                dic[alph[i]] = 1

print(dic)
plt.bar(dic.keys(), dic.values(), 0.75, color='r')
plt.show()