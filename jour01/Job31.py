def arrondissement(note):
    if note < 40:
        return note
    else:
        next_multiple = note // 5
        next_multiple = (next_multiple + 1)*5
        if note + 3 > next_multiple:
            return next_multiple
        else:
            return note

x = int(input("Insérez une note\n"))
print("La note finale est : ", arrondissement(x))