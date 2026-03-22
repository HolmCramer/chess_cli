from enum import Enum

BOARD_SIZE = 8
NOTATION_CHARS = "abcdefgh"
FEN_KIND = "rnbqkpPRNBQK"
FEN_NUMBERS = "12345678"
DEFAULT_POS = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


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


def index_to_notation(index: int) -> str:
    notation: str = ""
    notation = NOTATION_CHARS[index % 8]
    notation += str(8 - (index // 8))

    return notation


def notation_to_index(notation: str) -> int:
    index: int = 0
    notation.lower()

    index = NOTATION_CHARS.index(notation[0])
    index += (8 - int(notation[1])) * 8
    return index
