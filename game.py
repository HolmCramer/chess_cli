from chess import *
from gui import GUI, Board

class Game():

    def __init__(self):
        self.board = Board()
        self.gamestate = Gamestate()
        self.gui = GUI()

    def play(self):
        while True:
            self.gui.drawBoard(self.board, self.gamestate.gamestate)
            input = self.gui.enterMove()
            if input == "quit":
                break
            else:
                self.gamestate.move(input, self.board)
