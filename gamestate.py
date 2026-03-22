from typing import Optional

from pieces import *
from utils import BOARD_SIZE, COLOR, FEN_KIND, FEN_NUMBERS


class Gamestate:

    def __init__(self, fen: str) -> None:
        self.move_number = 0
        self.en_passent = False
        self.fen = fen
        self.gamestate = self.gen_state()

    @classmethod
    def default(cls) -> Gamestate:
        return cls("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    @classmethod
    def with_fen(cls, fen: str) -> Gamestate:
        return cls(fen)

    def gen_state(self) -> list:
        state: list[Optional[Piece]] = [None for _ in range(BOARD_SIZE**2)]
        index = 0
        for char in self.fen:
            if char in FEN_NUMBERS:
                index += int(char)
                continue
            if char in FEN_KIND:
                print("in kind")
                print(index)
                state[index] = self.fen_gen_piece(char)
                index += 1
            if char == " " or index > 63:
                break
        return state

    def fen_gen_piece(self, char: str) -> Optional[Piece]:
        if char.islower():
            color = COLOR.BLACK
            if char == "r":
                return Rook(color)
            if char == "n":
                return Knight(color)
            if char == "b":
                return Bishop(color)
            if char == "q":
                return Queen(color)
            if char == "k":
                return King(color)
            if char == "p":
                return Pawn(color)
        else:
            color = COLOR.WHITE
            if char == "R":
                return Rook(color)
            if char == "N":
                return Knight(color)
            if char == "B":
                return Bishop(color)
            if char == "Q":
                return Queen(color)
            if char == "K":
                return King(color)
            if char == "P":
                return Pawn(color)
        return None

    def move(self, move: tuple) -> None:
        piece_coord, move_coord = move

        if self.gamestate[piece_coord] is None:
            print("enter a square with a piece on it!")
        elif (
            self.gamestate[move_coord] is not None or self.gamestate[move_coord] is None
        ):
            self.switch_en_passent(self.gamestate[piece_coord].kind)
            self.increment_move_number()
            self.gamestate[move_coord] = self.gamestate[piece_coord]
            self.gamestate[piece_coord] = None
            print("Move done!")
        else:
            print("Enter a valid square to move to!")

    def increment_move_number(self) -> None:
        self.move_number += 1

    def switch_en_passent(self, kind: KIND) -> None:
        if kind is KIND.PAWN:
            self.en_passent = True
        else:
            self.en_passent = False

    def init_fen_state(self) -> None:
        pass
