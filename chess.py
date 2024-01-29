class Board():

    def __init__(self):
        self.width = 8
        self.height = 8
        self.squares = [[0 for _ in range(self.width)]
                        for _ in range(self.height)]

    def coordConv(self):
        letters = "ABCDEFGH"
        # initialisierung eines zweidimensionalen 8x8 arrays gefüllt mit 0
        self.coords = [[0 for _ in range(8)] for _ in range(8)]
        i = 8

        for y in range(0, 8):
            for x, letter in enumerate(letters):
                self.coords[y][x] = letter+str(i)
            i = i-1
        return self.coords


class Square():

    blackASCII = " "
    whiteASCII = "█"

    def __init__(self, color):
        self.color = color


class Piece():

    def __init__(self, pieceColor):
        self.pieceColor = pieceColor


class King(Piece):
    whiteKing = "♔"
    blackKing = "♚"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteKing
        else:
            self.icon = self.blackKing


class Queen(Piece):
    whiteQueen = "♕"
    blackQueen = "♛"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteQueen
        else:
            self.icon = self.blackQueen


class Bishop(Piece):
    whiteBishop = "♗"
    blackBishop = "♝"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteBishop
        else:
            self.icon = self.blackBishop


class Knight(Piece):
    whiteKnight = "♘"
    blackKnight = "♞"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteKnight
        else:
            self.icon = self.blackKnight


class Rook(Piece):
    whiteRook = "♖"
    blackRook = "♜"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteRook
        else:
            self.icon = self.blackRook


class Pawn(Piece):
    whitePawn = "♙"
    blackPawn = "♟️"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whitePawn
        else:
            self.icon = self.blackPawn


class Gamestate():

    def __init__(self):
        # initialisierung der Anzahl an Figuren für die Startaufstellung
        self.gamestate = [[0 for _ in range(8)] for _ in range(8)]
        self.whiteKing = [King(0)]
        self.whiteQueen = [Queen(0)]
        self.whiteBishop = [Bishop(0) for _ in range(2)]
        self.whiteKnight = [Knight(0) for _ in range(2)]
        self.whiteRook = [Rook(0) for _ in range(2)]
        self.whitePawn = [Pawn(0) for _ in range(8)]
        self.blackKing = [King(1)]
        self.blackQueen = [Queen(1)]
        self.blackBishop = [Bishop(1) for _ in range(2)]
        self.blackKnight = [Knight(1) for _ in range(2)]
        self.blackRook = [Rook(1) for _ in range(2)]
        self.blackPawn = [Pawn(1) for _ in range(8)]

        # Positionierung der schwarzen Figuren in der Startaufstellung
        self.gamestate[0][0] = self.blackRook[0]
        self.gamestate[1][0] = self.blackKnight[0]
        self.gamestate[2][0] = self.blackBishop[0]
        self.gamestate[3][0] = self.blackQueen[0]
        self.gamestate[4][0] = self.blackKing[0]
        self.gamestate[5][0] = self.blackBishop[1]
        self.gamestate[6][0] = self.blackKnight[1]
        self.gamestate[7][0] = self.blackRook[1]
        for square in range(8):
            self.gamestate[square][1] = self.blackPawn[square]

        # Positionierung der weißen Figuren in der Startaufstellung
        for square in range(8):
            self.gamestate[square][6] = self.whitePawn[square]
        self.gamestate[0][7] = self.whiteRook[0]
        self.gamestate[1][7] = self.whiteKnight[0]
        self.gamestate[2][7] = self.whiteBishop[0]
        self.gamestate[3][7] = self.whiteQueen[0]
        self.gamestate[4][7] = self.whiteKing[0]
        self.gamestate[5][7] = self.whiteBishop[1]
        self.gamestate[6][7] = self.whiteKnight[1]
        self.gamestate[7][7] = self.whiteRook[1]

    def inputConv(self, chessNotation):
        stateCoords = 0, 0

        # konvertierung einer Koordinate
        for i, k in enumerate(Board().coordConv()):
            for j, l in enumerate(k):
                if l == chessNotation:
                    stateCoords = j, i
        return stateCoords

    def move(self, chessNotation):

        pieceCoords = chessNotation[:2]
        moveCoords = chessNotation[-2::]

        yConvPieceCoords, xConvPieceCoords = self.inputConv(pieceCoords)
        yConvMoveCoords, xConvMoveCoords = self.inputConv(moveCoords)

        if self.gamestate[yConvPieceCoords][xConvPieceCoords] == 0:
            print("Enter a square with a piece on it!")
        elif self.gamestate[yConvMoveCoords][xConvMoveCoords] != 0 or self.gamestate[yConvMoveCoords][xConvMoveCoords] == 0:
            self.gamestate[yConvMoveCoords][xConvMoveCoords] = self.gamestate[yConvPieceCoords][xConvPieceCoords]
            self.gamestate[yConvPieceCoords][xConvPieceCoords] = 0
            print("Move done!")
        else:
            print("Enter a valid square to move to!")


class Player():

    def __init__(self):
        pass


class GUI():
    board = Board()
    gamestate = Gamestate().gamestate

    def __init__(self):
        # Border Top
        print(" " + 6*Board().width*"_", end="")
        print()
        # y Zeilennummer
        for y in range(Board().height):
            for lines in range(3):
                # oberste Feldreihe
                if lines == 0:
                    print("|", end="")  # linker Rand
                    for x in range(Board().width):
                        color = (x+y) % 2
                        self.board.squares[x][y] = Square(color)
                        # Wenn die Feldfarbe Weiß ist dann whiteasycii benutzen
                        if self.board.squares[x][y].color == 0:
                            print(6*Square.whiteASCII, end="")
                        else:
                            print(6*Square.blackASCII, end="")
                    print("|", end="")  # rechter Rand
                    print()
                # mittlere Feldreihe
                if lines == 1:
                    print("|", end="")
                    for x in range(self.board.width):
                        color = (x+y) % 2
                        self.board.squares[x][y] = Square(color)
                        if self.board.squares[x][y].color == 0:
                            print(2*Square.whiteASCII, end="")
                            if self.gamestate[x][y] != 0:
                                print(self.gamestate[x][y].icon + " ", end="")
                            else:
                                print(2*Square.whiteASCII, end="")
                            print(2*Square.whiteASCII, end="")
                        else:
                            print(2*Square.blackASCII, end="")
                            if self.gamestate[x][y] != 0:
                                print(self.gamestate[x][y].icon + " ", end="")
                            else:
                                print(2*Square.blackASCII, end="")
                            print(2*Square.blackASCII, end="")
                    print("|", end="")
                    print()
                # untere Feldreihe
                if lines == 2:
                    print("|", end="")
                    for x in range(self.board.width):
                        color = (x+y) % 2
                        self.board.squares[x][y] = Square(color)
                        if self.board.squares[x][y].color == 0:
                            print(self.board.coordConv()[y][x], end="")
                            print(4*Square.whiteASCII, end="")
                        else:
                            print(self.board.coordConv()[y][x], end="")
                            print(4*Square.blackASCII, end="")
                    print("|", end="")
                    print()
        print(" " + 6*self.board.width*"¯", end="")
        print()

    def updateGUI(self, newGamestate):
        self.gamestate = newGamestate
        self.__init__()


class Main():

    def __init__(self):
        self.board = Board()
        self.gamestate = Gamestate()
        self.gui = GUI()

    def play(self):
        while True:
            moveIn = input("Enter a valid move for example 'D2 to D3'\n"
                           + "Enter your move here:")
            break
        return moveIn


main = Main()
# main.gamestate.move("D2 B5")
# test = main.gamestate.inputConv("B2")
# print(test)
# main.gamestate.move("D2 to D3")
# main.gamestate.move("D3D4")
main.gamestate.move("B1 to C3")
# print(main.gamestate.inputConv("D2"))
# print(main.gamestate.inputConv("D3"))
# print(main.gamestate.gamestate[3][6])
# print(main.gamestate.gamestate[3][5])
main.gui.updateGUI(main.gamestate.gamestate)
# print(type(main.gamestate.gamestate))
# main.play()
