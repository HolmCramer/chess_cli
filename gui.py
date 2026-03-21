from board import Board, Square
from gamestate import Gamestate
from utils import COLOR


class GUI:

    def __init__(self) -> None:
        self.board = Board()

    def drawBoard(self, gamestate: Gamestate) -> None:
        self.clear_terminal()
        self.draw_top_boarder()
        self.draw_mid(gamestate)
        self.draw_bottom_boarder()

    def print_top(self, y: int) -> None:
        print("|", end="")
        for x in range(self.board.width):
            square = self.board.squares[x][y]
            if square is not None and square.color == COLOR.WHITE:
                print(6 * Square.whiteASCII, end="")
            else:
                print(6 * Square.blackASCII, end="")
        print("|", end="")
        print()

    def print_mid(self, y: int, gamestate: Gamestate) -> None:
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

    def print_bottom(self, y: int) -> None:
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

    def draw_top_boarder(self) -> None:
        print(" " + 6 * self.board.width * "_", end="")
        print()

    def draw_bottom_boarder(self) -> None:
        print(" " + 6 * self.board.width * "¯", end="")
        print()

    def draw_mid(self, gamestate: Gamestate) -> None:
        for y in range(self.board.height):
            for lines in range(3):
                if lines == 0:
                    self.print_top(y)
                if lines == 1:
                    self.print_mid(y, gamestate)
                if lines == 2:
                    self.print_bottom(y)

    def clear_terminal(self) -> None:
        print("\033[H\033[J", end="")

    def enterMove(self) -> str:
        moveInput = ""
        print("Enter a Valid Move like in the Format 'D2 to D4'!")
        moveInput = input("Enter a Move: ").upper()
        return moveInput
