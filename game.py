from gamestate import Gamestate
from gui import GUI


class Game:

    def __init__(self) -> None:
        self.gamestate = Gamestate()
        self.gui = GUI()

    def play(self) -> None:
        while True:
            self.gui.drawBoard(self.gamestate)
            input = self.gui.enterMove()
            if input == "QUIT" or input == "Q":
                break
            else:
                move = self.to_move(input)
                self.gamestate.move(move)

    def to_move(self, input: str) -> tuple:
        piece_coords = input[:2]
        move_coords = input[-2::]

        conv_piece_coords = self.inputConv(piece_coords)
        conv_move_coords = self.inputConv(move_coords)
        return conv_piece_coords, conv_move_coords

    def inputConv(self, chess_notation: str) -> int:
        index = 0

        for i, square in enumerate(self.gui.board.squares):
            if square is not None and square.coord == chess_notation:
                index = i

        return index
