from gamestate import Gamestate
from pieces import Piece
from utils import COLOR, KIND


class Arbiter:
    def __init__(self) -> None:
        super()

    def is_valid_move(self, state: Gamestate, move: tuple) -> bool:
        piece_coord, move_coord = move
        piece = state.position[piece_coord]
        if piece is None or not self.is_valid_piece_coord(state, piece_coord):
            return False
        if COLOR(not state.is_white_move) != state.position[piece_coord].color:
            return False
        if not self.is_valid_move_coord(state, move_coord):
            return False
        if not self.is_valid_piece_move(state, move):
            return False
        return True

    def is_valid_piece_coord(self, state: Gamestate, piece_coord: int) -> bool:
        if len(state.position) < piece_coord:
            return False
        elif not isinstance(state.position[piece_coord], Piece):
            return False
        else:
            return True

    def is_valid_color(self) -> bool:

        return True

    def is_valid_move_coord(self, state: Gamestate, move_coord: int) -> bool:
        if len(state.position) < move_coord:
            return False
        else:
            return True

    def is_valid_piece_move(self, state: Gamestate, move: tuple) -> bool:
        kind = state.position[move[0]].kind
        if kind == KIND.KING and self.is_valid_king_move(state, move):
            return True
        if kind == KIND.QUEEN and self.is_valid_queen_move(state, move):
            return True
        if kind == KIND.BISHOP and self.is_valid_bishop_move(state, move):
            return True
        if kind == KIND.KNIGHT and self.is_valid_knight_move(state, move):
            return True
        if kind == KIND.ROOK and self.is_valid_rook_move(state, move):
            return True
        if kind == KIND.PAWN and self.is_valid_pawn_move(state, move):
            return True
        else:
            return False

    def is_valid_king_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.position
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
        if (
            dest in valid_moves
            and state[dest] is not None
            and state[dest].color == state[pos].color
        ):
            return False
        if dest in valid_moves:
            return True
        else:
            return False

    def is_valid_queen_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.position
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

    def is_valid_bishop_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.position
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

    def is_valid_knight_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.position
        pos, dest = move
        valid_moves = [pos - 10, pos - 6]
        if dest in valid_moves:
            return True
        else:
            return False

    def is_valid_rook_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.position
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

    def is_valid_pawn_move(self, gamestate: Gamestate, move: tuple) -> bool:
        state = gamestate.position
        pos, dest = move
        color = state[pos].color
        valid_moves = []

        if color == COLOR.WHITE and pos - 8 == dest and state[dest] is None:
            valid_moves.append(pos - 8)
        elif pos + 8 == dest and state[dest] is None:
            valid_moves.append(pos + 8)

        if (
            color == COLOR.WHITE
            and pos // 8 == 6
            and state[pos - 16] is None
            and state[pos - 8] is None
        ):
            valid_moves.append(pos - 16)
        elif pos // 8 == 1 and state[pos + 8] is None and state[pos + 16] is None:
            valid_moves.append(pos + 16)

        if (
            color == COLOR.WHITE
            and isinstance(state[dest], Piece)
            and state[dest].color is COLOR.BLACK
            and (dest == pos - 9 or dest == pos - 7)
        ):
            valid_moves.append(dest)
        elif (
            isinstance(state[dest], Piece)
            and state[dest].color is COLOR.WHITE
            and (dest == pos + 9 or dest == pos + 7)
        ):
            valid_moves.append(dest)

        if (
            color == COLOR.WHITE
            and pos // 8 == 3
            and gamestate.en_passent
            and state[pos - 1] is not None
            and state[pos - 1].color == COLOR.BLACK
        ):
            valid_moves.append(pos - 9)
            state[pos - 1] = None
        elif (
            color == COLOR.WHITE
            and pos // 8 == 3
            and gamestate.en_passent
            and state[pos + 1] is not None
            and state[pos + 1].color == COLOR.BLACK
        ):
            valid_moves.append(pos - 7)
            state[pos + 1] = None

        if (
            color == COLOR.BLACK
            and pos // 8 == 4
            and gamestate.en_passent
            and state[pos - 1] is not None
            and state[pos - 1].color == COLOR.WHITE
        ):
            valid_moves.append(pos + 7)
            state[pos - 1] = None
        elif (
            color == COLOR.BLACK
            and pos // 8 == 4
            and gamestate.en_passent
            and state[pos + 1] is not None
            and state[pos + 1].color == COLOR.WHITE
        ):
            valid_moves.append(pos + 9)
            state[pos + 1] = None

        if dest in valid_moves:
            return True
        else:
            print(valid_moves)
            return False
