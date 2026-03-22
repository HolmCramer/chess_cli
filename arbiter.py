from gamestate import Gamestate


class Arbiter:
    def __init__(self) -> None:
        super()

    def check(self, state: Gamestate, move: tuple) -> bool:
        piece_coord, move_coord = move
        if len(state.gamestate) >= piece_coord:
            print("test")
            return True
        return False
