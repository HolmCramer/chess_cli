from utils import COLOR, KIND


class Piece:

    def __init__(self, piece_color: COLOR, kind: KIND) -> None:
        self.piece_color = piece_color
        self.kind = kind
        self.icon = ""


class King(Piece):
    black_king = "♔"
    white_king = "♚"
    kind = KIND.KING

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.white_king
        else:
            self.icon = self.black_king


class Queen(Piece):
    black_queen = "♕"
    white_queen = "♛"
    kind = KIND.QUEEN

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.white_queen
        else:
            self.icon = self.black_queen


class Bishop(Piece):
    black_bishop = "♗"
    white_bishop = "♝"
    kind = KIND.BISHOP

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.white_bishop
        else:
            self.icon = self.black_bishop


class Knight(Piece):
    black_knight = "♘"
    white_knight = "♞"
    kind = KIND.KNIGHT

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.white_knight
        else:
            self.icon = self.black_knight


class Rook(Piece):
    black_rook = "♖"
    white_rook = "♜"
    kind = KIND.ROOK

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.white_rook
        else:
            self.icon = self.black_rook


class Pawn(Piece):
    black_pawn = "♙"
    white_pawn = "♟"
    kind = KIND.PAWN

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.white_pawn
        else:
            self.icon = self.black_pawn
