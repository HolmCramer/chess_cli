from arbiter import Arbiter
from gamestate import Gamestate
from gui import GUI


class Game:

    def __init__(self) -> None:
        self.gamestate = Gamestate()
        self.gui = GUI()
        self.arbiter = Arbiter()

    def play(self) -> None:
        while True:
            self.gui.drawBoard(self.gamestate)
            input = self.gui.enterMove()
            if input == "QUIT" or input == "Q":
                break
            else:
                move = self.gui.to_move(input)
                if self.arbiter.is_valid_move(self.gamestate, move):
                    self.gamestate.move(move)
