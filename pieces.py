from utils import COLOR, KIND


class Piece:

    def __init__(self, piece_color: COLOR, kind: KIND) -> None:
        self.piece_color = piece_color
        self.kind = kind
        self.icon = ""


class King(Piece):
    whiteKing = "♔"
    blackKing = "♚"
    kind = KIND.KING

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.whiteKing
        else:
            self.icon = self.blackKing


class Queen(Piece):
    whiteQueen = "♕"
    blackQueen = "♛"
    kind = KIND.QUEEN

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.whiteQueen
        else:
            self.icon = self.blackQueen


class Bishop(Piece):
    whiteBishop = "♗"
    blackBishop = "♝"
    kind = KIND.BISHOP

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.whiteBishop
        else:
            self.icon = self.blackBishop


class Knight(Piece):
    whiteKnight = "♘"
    blackKnight = "♞"
    kind = KIND.KNIGHT

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.whiteKnight
        else:
            self.icon = self.blackKnight


class Rook(Piece):
    whiteRook = "♖"
    blackRook = "♜"
    kind = KIND.ROOK

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.whiteRook
        else:
            self.icon = self.blackRook


class Pawn(Piece):
    whitePawn = "♙"
    blackPawn = "♟"
    kind = KIND.PAWN

    def __init__(self, piece_color):
        super().__init__(piece_color, self.kind)
        if self.piece_color == COLOR.WHITE:
            self.icon = self.whitePawn
        else:
            self.icon = self.blackPawn
