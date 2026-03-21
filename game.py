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
            if input == "quit":
                break
            else:
                self.gamestate.move(input, self.gui.board)
