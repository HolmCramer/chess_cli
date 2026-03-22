from gamestate import Gamestate
from pieces import Piece
from utils import KIND


class Arbiter:
    def __init__(self) -> None:
        super()

    def is_valid_move(self, state: Gamestate, move: tuple) -> bool:
        piece_coord, move_coord = move
        if not self.is_valid_piece_coord(state, piece_coord):
            return False
        if not self.is_valid_move_coord(state, move_coord):
            return False
        if not self.is_valid_piece_move(state, move):
            return False
        return True

    def is_valid_piece_coord(self, state: Gamestate, piece_coord: int) -> bool:
        if len(state.gamestate) < piece_coord:
            return False
        elif not isinstance(state.gamestate[piece_coord], Piece):
            return False
        else:
            return True

    def is_valid_move_coord(self, state: Gamestate, move_coord: int) -> bool:
        if len(state.gamestate) < move_coord:
            return False
        else:
            return True

    def is_white_to_move(self, state: Gamestate) -> bool:
        if state.move_number % 2 == 1:
            return True
        else:
            return False

    def is_valid_piece_move(self, state: Gamestate, move: tuple) -> bool:
        kind = state.gamestate[move[0]].kind
        if kind == KIND.KING and self.is_valid_king_move(state, move):
            return True
        if kind == KIND.QUEEN and self.is_valid_king_move(state, move):
            return True
        else:
            return False

    def is_valid_king_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.gamestate
        pos, dest = move
        valid_moves = [
            pos + 1,
            pos - 1,
            pos + 7,
            pos - 7,
            pos + 8,
            pos - 8,
            pos + 9,
            pos - 9,
        ]
        if dest in valid_moves:
            return True
        else:
            return False
