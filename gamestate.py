from typing import Optional

from board import Board
from pieces import *
from utils import BOARD_SIZE, COLOR


class Gamestate:

    def __init__(self) -> None:
        self.gamestate: list[list[Optional[Piece]]] = [
            [None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
        ]
        self.whiteKing: list[King] = [King(COLOR.WHITE)]
        self.whiteQueen: list[Queen] = [Queen(COLOR.WHITE)]
        self.whiteBishop: list[Bishop] = [Bishop(COLOR.WHITE) for _ in range(2)]
        self.whiteKnight: list[Knight] = [Knight(COLOR.WHITE) for _ in range(2)]
        self.whiteRook: list[Rook] = [Rook(COLOR.WHITE) for _ in range(2)]
        self.whitePawn: list[Pawn] = [Pawn(COLOR.WHITE) for _ in range(8)]
        self.blackKing: list[King] = [King(COLOR.BLACK)]
        self.blackQueen: list[Queen] = [Queen(COLOR.BLACK)]
        self.blackBishop: list[Bishop] = [Bishop(COLOR.BLACK) for _ in range(2)]
        self.blackKnight: list[Knight] = [Knight(COLOR.BLACK) for _ in range(2)]
        self.blackRook: list[Rook] = [Rook(COLOR.BLACK) for _ in range(2)]
        self.blackPawn: list[Pawn] = [Pawn(COLOR.BLACK) for _ in range(8)]

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

    def move(self, chessNotation: str, board: Board) -> None:

        pieceCoords = chessNotation[:2]
        moveCoords = chessNotation[-2::]

        yConvPieceCoords, xConvPieceCoords = board.inputConv(pieceCoords)
        yConvMoveCoords, xConvMoveCoords = board.inputConv(moveCoords)

        if self.gamestate[yConvPieceCoords][xConvPieceCoords] == 0:
            print("Enter a square with a piece on it!")
        elif (
            self.gamestate[yConvMoveCoords][xConvMoveCoords] != 0
            or self.gamestate[yConvMoveCoords][xConvMoveCoords] == 0
        ):
            self.gamestate[yConvMoveCoords][xConvMoveCoords] = self.gamestate[
                yConvPieceCoords
            ][xConvPieceCoords]
            self.gamestate[yConvPieceCoords][xConvPieceCoords] = None
            print("Move done!")
        else:
            print("Enter a valid square to move to!")
