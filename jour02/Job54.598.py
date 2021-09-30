import random

class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.grille = [["O"] * j for i in range(j)]

    def afficherBoard(self):
        for x in range(self.i):
            for y in range(self.j):
                print(" |", self.grille[x][y], end='')
            print(" |\n")

    def isEmpty(self, x, y):
        if self.grille[x][y] == "O":
            return True
        else:
            return False

    def play(self, column, couleur):
        if column < 0 or column > self.j - 1:
            print("Hors du board")
        else:
            line = self.j - 1
            while self.isEmpty(line, column) is False and line >= 0:
                line -= 1

            if line < 0:
                print("La colonne est pleine")
            else:
                self.grille[line][column] = couleur

class AI_One:

    def __init__(self, couleur):
        self.couleur = couleur

    def think(self, board):
        for i in range(board.i - 1, 0):
            for j in range(board.j - 1):
                if board.grille[i][j] != "O" and (board.grille[i][j] == board.grille[i][j + 1] and board.grille[i][j] == board.grille[i][j + 2] or ((board.grille[i][j] == board.grille[i][j + 1]) and board.isEmpty(i, j-1) is True and board.isEmpty(i, j + 3) is True)):
                    if board.isEmpty(i, j + 3) is True:
                        board.play(j+3, self.couleur)
                        return
                    elif board.isEmpty(i, j - 1) is True:
                        board.play(j-1, self.couleur)
                        return
                elif board.grille[i][j] != "O" and (board.grille[i][j] == board.grille[i + 1][j] and board.grille[i][j] == board.grille[i + 2][j] and board.isEmpty(i + 3, j)):
                    board.play(j, self.couleur)
                    return
                elif board.grille[i][j] != "O" and (board.grille[i][j] == board.grille[i-1][j+1] and board.grille[i][j] == board.grille[i-2][j+2] and board.isEmpty(i-3, j+3) or (board.grille[i][j] == board.grille[i-1][j+1] and (board.isEmpty(i - 2, j + 2) is True and board.isEmpty(i - 1, j + 2) is False) and (board.isEmpty(i + 1, j + 1) is True and board.isEmpty(i, j + 1) is False))):
                    if board.isEmpty(i - 2, j + 2) is True:
                        board.play(j + 2, self.couleur)
                        return
                    elif board.isEmpty(i + 1, j + 1) is True:
                        board.play(j + 1, self.couleur)
                        return
                elif board.grille[i][j] != "O" and (board.grille[i][j] == board.grille[i - 1][j - 1] and board.grille[i][j] == board.grille[i - 2][j - 2] and (board.isEmpty(i - 3, j - 3) or (
                        board.grille[i][j] == board.grille[i - 1][j - 1] and (
                        board.isEmpty(i - 2, j - 2) is True and board.isEmpty(i - 1, j - 2) is False) and (
                                board.isEmpty(i + 1, j - 1) is True and board.isEmpty(i, j - 1) is False)))):
                    if board.isEmpty(i - 2, j - 2) is True:
                        board.play(j + 2, self.couleur)
                        return
                    elif board.isEmpty(i + 1, j - 1) is True:
                        board.play(j + 1, self.couleur)
                        return
        board.play(random.randrange(0, board.j + 1), self.couleur)



board = Board(5, 5)
IA = AI_One("R")
board.play(1, "J")
IA.think(board)
board.play(2, "J")
IA.think(board)
board.play(3, "J")
IA.think(board)
board.play(3, "J")
IA.think(board)
board.afficherBoard()