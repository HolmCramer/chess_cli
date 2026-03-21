from board import Board, Square
from gamestate import Gamestate
from utils import COLOR


class GUI:

    def __init__(self) -> None:
        self.board = Board()

    def drawBoard(self, gamestate: Gamestate) -> None:
        print("\033[H\033[J", end="")
        print(" " + 6 * self.board.width * "_", end="")
        print()
        for y in range(self.board.height):
            for lines in range(3):
                if lines == 0:
                    print("|", end="")
                    for x in range(self.board.width):
                        square = self.board.squares[x][y]
                        if square is not None and square.color == COLOR.WHITE:
                            print(6 * Square.whiteASCII, end="")
                        else:
                            print(6 * Square.blackASCII, end="")
                    print("|", end="")
                    print()
                if lines == 1:
                    print("|", end="")
                    for x in range(self.board.width):
                        square = self.board.squares[x][y]
                        piece = (
                            gamestate.gamestate[x][y]
                            if gamestate.gamestate[x][y] is not None
                            else None
                        )

                        bg = (
                            Square.whiteASCII
                            if square and square.color == COLOR.WHITE
                            else Square.blackASCII
                        )

                        print(2 * bg, end="")

                        if piece:
                            print(piece.icon + " ", end="")
                        else:
                            print(2 * bg, end="")

                        print(2 * bg, end="")
                    print("|", end="")
                    print()
                if lines == 2:
                    print("|", end="")
                    for x in range(self.board.width):
                        square = self.board.squares[x][y]
                        if square is not None and square.color == COLOR.WHITE:
                            print(self.board.coords[y][x], end="")
                            print(4 * Square.whiteASCII, end="")
                        else:
                            print(self.board.coords[y][x], end="")
                            print(4 * Square.blackASCII, end="")
                    print("|", end="")
                    print()
        print(" " + 6 * self.board.width * "¯", end="")
        print()

    def enterMove(self) -> str:
        moveInput = ""
        print("Enter a Valid Move like in the Format 'D2 to D4'!")
        moveInput = input("Enter a Move: ").upper()
        return moveInput
