def dame(x, y, nbDames):
    if nbDames == 0:
        return
    else:
        if x > n:
             x = x - n
        board[x][y] = "X"
        dame(x + 2, y + 1, nbDames - 1)



n = int(input("Taille du côté :\n"))

board = [["O"] * n for i in range(n)]

if n % 3 == 0 and n % 2 == 0:
     dame(1, 0, n)
elif n % 2 != 0:
    dame(0, 0, n)
else:
    print("Impossible")

print(board)


