def draw_rectangle(width, height):
    for i in range(height):
        print("|", end='') #end='' est ici pour empecher le retour a la ligne
        for j in range(width):
            if i == 0 or i == height - 1:
                print("-", end='')
            else:
                print(" ", end='')
        print("|")

draw_rectangle(10,3)