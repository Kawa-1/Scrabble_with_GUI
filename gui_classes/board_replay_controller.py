from PyQt6 import QtCore, QtGui, QtWidgets

from gui_py_source.board_window import Ui_board_window


class BoardReplayController(QtWidgets.QMainWindow):
    def __init__(self, all_saved_moves: list):
        self.all_saved_moves = all_saved_moves
        self.all_saved_moves.sort(key=lambda x: x[2])

        # all saved moves does not account for turns when no tiles were placed
        self.total_moves_per_game = len(self.all_saved_moves)

        # init gui of scrabble board
        QtWidgets.QMainWindow.__init__(self)
        # call constructor of board_window class
        self.ui = Ui_board_window()
        self.ui.setupUi(self)

        self.show()

