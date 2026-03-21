from typing import Optional

from utils import BOARD_SIZE, COLOR


class Board:

    def __init__(self) -> None:
        self.size: int = BOARD_SIZE
        self.squares: list[Optional[Square]] = self.create_squares()

    def create_squares(self) -> list[Optional[Square]]:
        squares = []
        for row in range(self.size):
            for column in range(self.size):
                squares.append(Square(COLOR((row + column) % 2), row, column))
        return squares

    def inputConv(self, chessNotation: str) -> tuple:
        stateCoordsX = 0
        stateCoordsY = 0

        for y, k in enumerate(self.coords):
            for x, l in enumerate(k):
                if l == chessNotation:
                    stateCoordsX = x
                    stateCoordsY = y

        return stateCoordsX, stateCoordsY


class Square:

    blackASCII = " "
    whiteASCII = "█"

    def __init__(self, color: COLOR, row: int, column: int) -> None:
        self.color = color
        self.coord = self.create_coord(row, column)

    def create_coord(self, row: int, column: int) -> str:
        letters = "ABCDEFGH"
        return f"{letters[column]}{8 - row}"
