from typing import Optional

from pieces import *
from utils import BOARD_SIZE, COLOR, FEN_KIND, FEN_NUMBERS, notation_to_index


class Gamestate:

    def __init__(self, fen: str) -> None:
        self.fen: str = fen
        self.position: list[Optional[Piece]] = self.gen_position()
        self.is_white_move: bool = self.gen_is_white_move()
        self.castle_rights: str = self.gen_castle_rights()
        self.en_passent: Optional[int] = self.gen_en_passent()
        self.half_move_clock: int = self.gen_half_move_clock()
        self.full_move_number: int = self.gen_full_move_number()

    @classmethod
    def default(cls) -> Gamestate:
        return cls("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    @classmethod
    def with_fen(cls, fen: str) -> Gamestate:
        return cls(fen)

    def gen_full_move_number(self) -> int:
        return int(self.fen.split(" ")[5])

    def gen_half_move_clock(self) -> int:
        return int(self.fen.split(" ")[4])

    def gen_is_white_move(self) -> bool:
        if self.fen.split(" ")[1] == "w":
            return True
        else:
            return False

    def gen_position(self) -> list[Optional[Piece]]:
        position: list[Optional[Piece]] = [None for _ in range(BOARD_SIZE**2)]
        fen = self.fen.split(" ")
        print(fen)
        index = 0

        for char in fen[0]:
            if char in FEN_NUMBERS:
                index += int(char)
                continue
            if char in FEN_KIND:
                position[index] = self.fen_gen_piece(char)
                index += 1

        return position

    def gen_castle_rights(self) -> str:
        fen = self.fen.split(" ")[2]
        return fen

    def gen_en_passent(self) -> Optional[int]:
        en_passent = self.fen.split(" ")[3]
        if en_passent == "-":
            return None
        else:
            return notation_to_index(en_passent)

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

        if self.position[piece_coord] is None:
            print("enter a square with a piece on it!")
        elif self.position[move_coord] is not None or self.position[move_coord] is None:
            self.update_state()
            self.position[move_coord] = self.position[piece_coord]
            self.position[piece_coord] = None
            print("Move done!")
        else:
            print("Enter a valid square to move to!")

    def update_state(self) -> None:
        # need more updates
        self.increment_half_move_clock()
        self.increment_full_move_number()
        self.update_is_white_move()
        return

    def increment_full_move_number(self) -> None:
        if not self.is_white_move:
            self.full_move_number += 1
        else:
            return

    def increment_half_move_clock(self) -> None:
        # no pawn move or capture in the last 50 moves
        self.half_move_clock += 1
        return

    def update_is_white_move(self) -> None:
        if self.is_white_move:
            self.is_white_move = False
        else:
            self.is_white_move = True

    def init_fen_state(self) -> None:
        pass
