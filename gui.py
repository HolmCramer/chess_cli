
class Board:

    def __init__(self):
        self.width = 8
        self.height = 8
        self.squares = [[0 for _ in range(self.width)]
                        for _ in range(self.height)]
        self.coordConv()

    def coordConv(self):
        letters = "ABCDEFGH"
        # initialisierung eines zweidimensionalen 8x8 arrays gefüllt mit 0
        self.coords = [[0 for _ in range(8)] for _ in range(8)]
        i = 8

        for y in range(0, 8):
            for x, letter in enumerate(letters):
                self.coords[y][x] = letter+str(i)
            i = i-1
        return


class Square():

    blackASCII = " "
    whiteASCII = "█"

    def __init__(self, color):
        self.color = color

class GUI():
    
    def __init__(self):
        pass

    def drawBoard(self, board, gamestate):
                # Border Top
        print(" " + 6*board.width*"_", end="")
        print()
        # y Zeilennummer
        for y in range(board.height):
            for lines in range(3):
                # oberste Feldreihe
                if lines == 0:
                    print("|", end="")  # linker Rand
                    for x in range(board.width):
                        color = (x+y) % 2
                        board.squares[x][y] = Square(color)
                        # Wenn die Feldfarbe Weiß ist dann whiteasycii benutzen
                        if board.squares[x][y].color == 0:
                            print(6*Square.whiteASCII, end="")
                        else:
                            print(6*Square.blackASCII, end="")
                    print("|", end="")  # rechter Rand
                    print()
                # mittlere Feldreihe
                if lines == 1:
                    print("|", end="")
                    for x in range(board.width):
                        color = (x+y) % 2
                        board.squares[x][y] = Square(color)
                        if board.squares[x][y].color == 0:
                            print(2*Square.whiteASCII, end="")
                            if gamestate[x][y] != 0:
                                print(gamestate[x][y].icon + " ", end="")
                            else:
                                print(2*Square.whiteASCII, end="")
                            print(2*Square.whiteASCII, end="")
                        else:
                            print(2*Square.blackASCII, end="")
                            if gamestate[x][y] != 0:
                                print(gamestate[x][y].icon + " ", end="")
                            else:
                                print(2*Square.blackASCII, end="")
                            print(2*Square.blackASCII, end="")
                    print("|", end="")
                    print()
                # untere Feldreihe
                if lines == 2:
                    print("|", end="")
                    for x in range(board.width):
                        color = (x+y) % 2
                        board.squares[x][y] = Square(color)
                        if board.squares[x][y].color == 0:
                            print(board.coords[y][x], end="")
                            print(4*Square.whiteASCII, end="")
                        else:
                            print(board.coords[y][x], end="")
                            print(4*Square.blackASCII, end="")
                    print("|", end="")
                    print()
        print(" " + 6*board.width*"¯", end="")
        print()

    def enterMove(self):
        moveInput = ""
        print("Enter a Valid Move like in the Format 'D2 to D4'!")
        moveInput = input("Enter a Move: ").upper()
        return moveInput


    # def updateGUI(self, newGamestate):
    #     gamestate = newGamestate
    #     self.__init__()