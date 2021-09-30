import matplotlib.pyplot as plt

file = open("data.txt", "r")
line = file.read()
file.close()
x = "abcdefghijklmnopqrstuvwxyz"
alph = sorted(x)
y = x.upper()
alph_upp = sorted(y)

dic = {}
for i in range(25):
    cpt = line.count(alph[i]) + line.count(alph_upp[i])
    dic[alph_upp[i]] = cpt

print(dic)
plt.bar(dic.keys(), dic.values(), 0.75, color='g')
plt.show()