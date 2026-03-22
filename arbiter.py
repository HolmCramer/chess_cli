from gamestate import Gamestate
from pieces import Piece


class Arbiter:
    def __init__(self) -> None:
        super()

    def is_valid_move(self, state: Gamestate, move: tuple) -> bool:
        piece_coord, move_coord = move
        if not self.is_valid_piece_coord(state, piece_coord):
            return False
        if not self.is_valid_move_coord(state, move_coord):
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
        elif isinstance(state.gamestate[move_coord], Piece):
            return False
        else:
            return True

    def is_white_to_move(self, state: Gamestate) -> bool:
        if state.move_number % 2 == 1:
            return True
        else:
            return False
