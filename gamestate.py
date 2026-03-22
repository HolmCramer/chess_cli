from typing import Optional

from pieces import *
from utils import BOARD_SIZE, COLOR


class Gamestate:

    def __init__(self) -> None:
        self.move_number = 0
        self.gamestate: list[Optional[Piece]] = [None for _ in range(BOARD_SIZE**2)]
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

        self.gamestate[0] = self.blackRook[0]
        self.gamestate[1] = self.blackKnight[0]
        self.gamestate[2] = self.blackBishop[0]
        self.gamestate[3] = self.blackQueen[0]
        self.gamestate[4] = self.blackKing[0]
        self.gamestate[5] = self.blackBishop[1]
        self.gamestate[6] = self.blackKnight[1]
        self.gamestate[7] = self.blackRook[1]
        for square in range(8):
            self.gamestate[8 + square] = self.blackPawn[square]

        for square in range(8):
            self.gamestate[48 + square] = self.whitePawn[square]
        self.gamestate[56] = self.whiteRook[0]
        self.gamestate[57] = self.whiteKnight[0]
        self.gamestate[58] = self.whiteBishop[0]
        self.gamestate[59] = self.whiteQueen[0]
        self.gamestate[60] = self.whiteKing[0]
        self.gamestate[61] = self.whiteBishop[1]
        self.gamestate[62] = self.whiteKnight[1]
        self.gamestate[63] = self.whiteRook[1]

    def move(self, move: tuple) -> None:
        piece_coord, move_coord = move

        if self.gamestate[piece_coord] is None:
            print("Enter a square with a piece on it!")
        elif (
            self.gamestate[move_coord] is not None or self.gamestate[move_coord] is None
        ):
            self.gamestate[move_coord] = self.gamestate[piece_coord]
            self.gamestate[piece_coord] = None
            self.increment_move_number()
            print("Move done!")
        else:
            print("Enter a valid square to move to!")

    def increment_move_number(self) -> None:
        self.move_number += 1
