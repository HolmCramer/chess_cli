class Piece():

    def __init__(self, pieceColor):
        self.pieceColor = pieceColor


class King(Piece):
    whiteKing = "♔"
    blackKing = "♚"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteKing
        else:
            self.icon = self.blackKing


class Queen(Piece):
    whiteQueen = "♕"
    blackQueen = "♛"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteQueen
        else:
            self.icon = self.blackQueen


class Bishop(Piece):
    whiteBishop = "♗"
    blackBishop = "♝"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteBishop
        else:
            self.icon = self.blackBishop


class Knight(Piece):
    whiteKnight = "♘"
    blackKnight = "♞"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteKnight
        else:
            self.icon = self.blackKnight


class Rook(Piece):
    whiteRook = "♖"
    blackRook = "♜"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whiteRook
        else:
            self.icon = self.blackRook


class Pawn(Piece):
    whitePawn = "♙"
    blackPawn = "♟️"

    def __init__(self, pieceColor):
        super().__init__(pieceColor)
        if self.pieceColor == 0:
            self.icon = self.whitePawn
        else:
            self.icon = self.blackPawn