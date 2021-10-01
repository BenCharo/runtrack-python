def factorielle(k):
    if k > 0:
        fact = k * factorielle(k-1)
    else:
        fact = 1
    return fact


x = int(input("Choisissez le nombre dont vous voulez calculer la factorielle\n"))
print(x, "! =", factorielle(x))