from pieces import *
from utils import inputConv

class Gamestate():

    def __init__(self):
        # initialisierung der Anzahl an Figuren für die Startaufstellung
        self.gamestate = [[0 for _ in range(8)] for _ in range(8)]
        self.whiteKing = [King(0)]
        self.whiteQueen = [Queen(0)]
        self.whiteBishop = [Bishop(0) for _ in range(2)]
        self.whiteKnight = [Knight(0) for _ in range(2)]
        self.whiteRook = [Rook(0) for _ in range(2)]
        self.whitePawn = [Pawn(0) for _ in range(8)]
        self.blackKing = [King(1)]
        self.blackQueen = [Queen(1)]
        self.blackBishop = [Bishop(1) for _ in range(2)]
        self.blackKnight = [Knight(1) for _ in range(2)]
        self.blackRook = [Rook(1) for _ in range(2)]
        self.blackPawn = [Pawn(1) for _ in range(8)]

        # Positionierung der schwarzen Figuren in der Startaufstellung
        self.gamestate[0][0] = self.blackRook[0]
        self.gamestate[1][0] = self.blackKnight[0]
        self.gamestate[2][0] = self.blackBishop[0]
        self.gamestate[3][0] = self.blackQueen[0]
        self.gamestate[4][0] = self.blackKing[0]
        self.gamestate[5][0] = self.blackBishop[1]
        self.gamestate[6][0] = self.blackKnight[1]
        self.gamestate[7][0] = self.blackRook[1]
        for square in range(8):
            self.gamestate[square][1] = self.blackPawn[square]

        # Positionierung der weißen Figuren in der Startaufstellung
        for square in range(8):
            self.gamestate[square][6] = self.whitePawn[square]
        self.gamestate[0][7] = self.whiteRook[0]
        self.gamestate[1][7] = self.whiteKnight[0]
        self.gamestate[2][7] = self.whiteBishop[0]
        self.gamestate[3][7] = self.whiteQueen[0]
        self.gamestate[4][7] = self.whiteKing[0]
        self.gamestate[5][7] = self.whiteBishop[1]
        self.gamestate[6][7] = self.whiteKnight[1]
        self.gamestate[7][7] = self.whiteRook[1]


    def move(self, chessNotation, board):

        pieceCoords = chessNotation[:2]
        moveCoords = chessNotation[-2::]

        yConvPieceCoords, xConvPieceCoords = inputConv(pieceCoords, board)
        yConvMoveCoords, xConvMoveCoords = inputConv(moveCoords, board)

        if self.gamestate[yConvPieceCoords][xConvPieceCoords] == 0:
            print("Enter a square with a piece on it!")
        elif self.gamestate[yConvMoveCoords][xConvMoveCoords] != 0 or self.gamestate[yConvMoveCoords][xConvMoveCoords] == 0:
            self.gamestate[yConvMoveCoords][xConvMoveCoords] = self.gamestate[yConvPieceCoords][xConvPieceCoords]
            self.gamestate[yConvPieceCoords][xConvPieceCoords] = 0
            print("Move done!")
        else:
            print("Enter a valid square to move to!")


class Player():

    def __init__(self):
        pass
