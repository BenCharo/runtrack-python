def plus_proche(text):
    text_ascii = []
    long = len(text) - 1
    for i in text:
        text_ascii.append(ord(i)) #changement en code ascii
    print(text_ascii)
    cpt = 1
    j = long
    while text_ascii[j] < text_ascii[j - cpt]:
        cpt += 1
        if cpt > j:
            cpt = 1
            j -= 1

    text_ascii[j], text_ascii[j-cpt] = text_ascii[j-cpt], text_ascii[j]
    print(text_ascii)

    for k in range(j-cpt + 1, long):
        if text_ascii[k] > text_ascii[k+1]:
            text_ascii[k], text_ascii[k+1] = text_ascii[k+1], text_ascii[k]
    print(text_ascii)

    next_word = []
    for l in text_ascii:
        next_word.append(chr(l)) #changement en texte

    return next_word


x = plus_proche("cdba")
print(x)