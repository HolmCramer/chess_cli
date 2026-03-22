from gamestate import Gamestate
from pieces import Piece


class Arbiter:
    def __init__(self) -> None:
        super()

    def check(self, state: Gamestate, move: tuple) -> bool:
        piece_coord, move_coord = move
        if len(state.gamestate) < piece_coord:
            return False
        if not isinstance(state.gamestate[piece_coord], Piece):
            print("fail")
            return False
        return True

    def white_to_move(self, state: Gamestate) -> bool:
        if state.move_number % 2 == 1:
            return True
        else:
            return False
