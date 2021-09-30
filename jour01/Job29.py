def draw_triangle(height):
    dist = 0    # j'utilise la variable dist qui sera la distance entre l'axe qui coupe le triangle en 2 et son côté
    while dist < height:
        for i in range(2 * height):
            if i == height - 1 - dist:
                print("/", end='')
            elif i == height + dist:
                print("\\", end='')
            elif i == 2 * height - 1:
                print(" ")
            elif i == 2 * height - 1 and dist == height-1: #ici on est sur la derniere ligne donc
                print("_")                                  #au lieu de mettre des espace, on met des _
            elif dist == height-1:
                print("_", end='')
            else:
                print(" ", end='')
        dist = dist + 1


draw_triangle(3)


