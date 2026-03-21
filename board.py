from typing import Optional

from utils import BOARD_SIZE, COLOR


class Board:

    def __init__(self) -> None:
        self.size: int = BOARD_SIZE
        self.squares: list[Optional[Square]] = [
            Square(COLOR(((i // self.size) + (i % self.size)) % 2))
            for i in range(self.size * self.size)
        ]
        self.coordConv()

    def coordConv(self) -> None:
        letters = "ABCDEFGH"
        self.coords = ["" for _ in range(len(letters) ** 2)]

        for y in range(len(letters)):
            for x in range(len(letters)):
                self.coords[x + y] = letters[x] + str(8 - y)

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

    def __init__(self, color: COLOR) -> None:
        self.color = color
