def factorielle(k):
    if k > 0:
        fact = k * factorielle(k-1)
        print(fact)
    else:
        fact = 1
    return fact

factorielle(6)