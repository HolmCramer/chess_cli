from enum import Enum

BOARD_SIZE = 8


class COLOR(Enum):
    WHITE = 0
    BLACK = 1


class KIND(Enum):
    KING = 0
    QUEEN = 1
    BISHOP = 2
    KNIGHT = 3
    ROOK = 4
    PAWN = 5
