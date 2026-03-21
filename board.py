from typing import Optional

from utils import BOARD_SIZE, COLOR


class Board:

    def __init__(self) -> None:
        self.width: int = BOARD_SIZE
        self.height: int = BOARD_SIZE
        self.squares: list[list[Optional[Square]]] = [
            [Square(COLOR((x + y) % 2)) for x in range(self.width)]
            for y in range(self.height)
        ]
        self.coordConv()

    def coordConv(self) -> None:
        letters = "ABCDEFGH"
        self.coords = [["" for _ in range(8)] for _ in range(8)]
        i = 8

        for y in range(0, 8):
            for x, letter in enumerate(letters):
                self.coords[y][x] = letter + str(i)
            i = i - 1


class Square:

    blackASCII = " "
    whiteASCII = "█"

    def __init__(self, color: COLOR) -> None:
        self.color = color
