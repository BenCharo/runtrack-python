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




board = Board(5, 5)
board.play(2, "J")
board.play(3, "R")
board.play(1, "J")
board.play(2, "R")
board.play(1, "J")
board.play(1, "R")
board.play(0, "J")
board.play(0, "R")
board.play(2, "J")
board.play(0, "R")
board.play(4, "J")
board.play(0, "R")

board.afficherBoard()
