from enum import Enum

BOARD_SIZE = 8


def inputConv(chessNotation, board) -> tuple:
    stateCoordsX = 0
    stateCoordsY = 0

    # konvertierung einer Koordinate
    for y, k in enumerate(board.coords):
        for x, l in enumerate(k):
            if l == chessNotation:
                stateCoordsX = x
                stateCoordsY = y

    return stateCoordsX, stateCoordsY


class COLOR(Enum):
    WHITE = 0
    BLACK = 1
