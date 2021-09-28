def plus_proche(chain):
    longueur = len(chain)
    for i in range(1, longueur):
        k = chain[longueur - i]
        j = i+1
        while k < chain[longueur - j]:
            j = j + 1
        




x = plus_proche("abcde")
print(x)