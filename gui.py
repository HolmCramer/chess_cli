from board import Board, Square
from gamestate import Gamestate
from utils import COLOR


class GUI:

    def __init__(self) -> None:
        self.board = Board()

    def drawBoard(self, gamestate: Gamestate) -> None:
        self.clear_terminal()
        self.draw_top_boarder()
        n = 0

        for _ in range(self.board.size):
            self.draw_rank(n, gamestate)
            n += 8

        self.draw_bottom_boarder()

    def draw_rank(self, n: int, gamestate: Gamestate) -> None:
        self.print_top(n)
        self.print_mid(n, gamestate)
        self.print_bottom(n)

    def print_top(self, n: int) -> None:
        print("|", end="")
        for i in range(self.board.size):
            square = self.board.squares[n + i]
            if square is not None and square.color == COLOR.WHITE:
                print(6 * Square.whiteASCII, end="")
            else:
                print(6 * Square.blackASCII, end="")
        print("|", end="")
        print()

    def print_mid(self, n: int, gamestate: Gamestate) -> None:
        print("|", end="")
        for x in range(self.board.size):
            square = self.board.squares[x + n]
            piece = (
                gamestate.gamestate[x + n]
                if gamestate.gamestate[x + n] is not None
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

    def print_bottom(self, n: int) -> None:
        print("|", end="")
        for x in range(self.board.size):
            square = self.board.squares[x + n]
            if square is not None and square.color == COLOR.WHITE:
                print(square.coord, end="")
                print(4 * Square.whiteASCII, end="")
            elif square is not None:
                print(square.coord, end="")
                print(4 * Square.blackASCII, end="")
        print("|", end="")
        print()

    def draw_top_boarder(self) -> None:
        print(" " + 6 * self.board.size * "_", end="")
        print()

    def draw_bottom_boarder(self) -> None:
        print(" " + 6 * self.board.size * "¯", end="")
        print()

    def clear_terminal(self) -> None:
        print("\033[H\033[J", end="")

    def enterMove(self) -> str:
        moveInput = ""
        print("Enter a Valid Move like in the Format 'D2 to D4'!")
        moveInput = input("Enter a Move: ").upper()
        return moveInput
