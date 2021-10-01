def puissance2(k):
    if k > 0:
        puis = 2 * puissance2(k - 1)
    else:
        puis = 1
    return puis

x = int(input("Choisissez la puissance de 2 que vous voulez calculer\n"))
print("2^", x, " = ", puissance2(x))