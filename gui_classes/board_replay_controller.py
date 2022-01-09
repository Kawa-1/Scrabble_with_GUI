from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

from auxiliary.gui_base_methods import set_image_to_label, set_image_to_button, hide_labels, string_to_board
from auxiliary.window_movement import DummyWindow
from gui_py_source.replay_board_window import Ui_replay_board_window
from gui_py_source.replay_manager_window import Ui_replay_manager_window
from management_database import ManagementGeneralLeaderboard


class BoardReplayController(DummyWindow):
    def __init__(self, menu, game_id: int):
        self.game_id = game_id
        self.menu_handle = menu
        # TODO: acquire all moves per game_id
        # get list of moves [1], not status [0]
        self.all_saved_moves = ManagementGeneralLeaderboard.acquire_board(game_id)[1]
        # self.all_saved_moves.sort(key=lambda x: x[2])
        """
            update replay_board with 1st move:
            copy all_saved_moves[0][3] (str) -> board -> into replay_board
        """
        self._current_move_id = 0

        # all saved moves does not account for turns when no tiles were placed
        self.total_moves = len(self.all_saved_moves)

        ### MANAGER INIT
        DummyWindow.__init__(self)
        self.ui = Ui_replay_manager_window()
        self.ui.setupUi(self)

        ### SET LABELS
        # self.ui.game_id_label.setText('game_id: {}'.format(str(self.game_id)))
        self.ui.game_id_label.hide()
        self.ui.label.setText('move: {} of {}'.format(1, self.total_moves))
        self.ui.current_player_label.setText('current player: {}'.format(self.all_saved_moves[0][1]))
        self.ui.next_player_label.setText(self.all_saved_moves[self._current_move_id + 1][1])

        hide_labels([self.ui.status_label])

        set_image_to_label(self.ui.player_icon_label, 'gamer.png')
        set_image_to_button(self.ui.prev_move_button, 'returnleft.png')
        set_image_to_button(self.ui.next_move_button, 'returnright.png')

        ### SET BUTTON EVENT HANDLERS
        self.ui.exit_button.clicked.connect(lambda: self.return_to_menu())
        self.ui.next_move_button.clicked.connect(lambda: self.show_next_move())
        self.ui.prev_move_button.clicked.connect(lambda: self.show_prev_move())

        ### BOARD INIT
        self.board_window = DummyWindow()
        self.ui2 = Ui_replay_board_window()
        self.ui2.setupUi(self.board_window)

        ### LOAD 1ST MOVE
        # albo w sumie chuj, nie laduje 1st move

        ### DEFAULT STYLING TO REVERT CHANGES APPLIED BY MOVES OVERRIDING ORIGINAL BOARD
        ### throws name error self not defined
        self.default_board_tile_stylesheets = self.collect_def_board_stylesheets()
        self.default_board_tile_txt = self.collect_def_board_txt()

        self.update_board()

        ### SHOW BOARD AND MANAGER
        self.show()
        self.board_window.show()

    def collect_def_board_stylesheets(self) -> list:
        return [[eval('self.ui2.board_label_{}_{}'.format(i, j), {'self': self}).styleSheet() for i in range(15)] for j in range(15)]

    def collect_def_board_txt(self) -> list:
        return [[eval('self.ui2.board_label_{}_{}'.format(i, j), {'self': self}).text() for i in range(15)] for j in range(15)]

    def show_next_move(self) -> None:
        print('next move clicked')
        hide_labels([self.ui.status_label])
        if self._current_move_id + 1 >= self.total_moves:
            print('cant go +')
            self.ui.status_label.setText('cannot go further')
            self.ui.status_label.setStyleSheet('color: red;')
            self.ui.status_label.setVisible(1)
        else:
            self._current_move_id += 1
            self.update_move_info()
            self.update_board()

    def show_prev_move(self) -> None:
        print('prev move')
        hide_labels([self.ui.status_label])
        if self._current_move_id - 1 < 0:
            print('cant go -')
            self.ui.status_label.setText('cannot rewind further')
            self.ui.status_label.setStyleSheet('color: red;')
            self.ui.status_label.setVisible(1)
        else:
            self._current_move_id -= 1
            self.update_move_info()
            self.update_board()

    def update_move_info(self) -> None:
        self.ui.current_player_label.setText(
            'current player: {}'.format(self.all_saved_moves[self._current_move_id][1])
        )
        # self.ui.label.setText('move: {} of {}'.format(self._current_move_id + 1, self.total_moves))
        self.ui.label.setText('move: {} of {}'.format(self._current_move_id + 1, self.total_moves))
        if self._current_move_id + 1 < self.total_moves:
            self.ui.next_player_label.setText(
                'next player: {}'.format(self.all_saved_moves[self._current_move_id+1][1])
            )
        else:
            self.ui.next_player_label.setText('last move')

    def update_board(self) -> None:
        print('update board')
        _new_board = string_to_board(self.all_saved_moves[self._current_move_id][3])
        for row in range(15):
            for column in range(15):
                _tile = eval('self.ui2.board_label_{}_{}'.format(row, column))
                _tile.setText('')
                # set default board stylesheet
                _tile.setStyleSheet(self.default_board_tile_stylesheets[row][column])
                _tile.setText(self.default_board_tile_txt[row][column])
                if _new_board[row][column] != "-":
                    _tile.setText(_new_board[row][column])
                    _tile.setStyleSheet(str(_tile.styleSheet()) + ';border: 2px solid red; color: black;')

    def signal_closing(self) -> None:
        self.menu_handle._is_replay_open = False

    # UPON RETURN TO MENU CLOSE BOARD AND MANAGER
    def return_to_menu(self):
        self.menu_handle.show()
        self.menu_handle._is_replay_open = False
        self.close()
        self.board_window.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ent = BoardReplayController(QMainWindow(), 2)
    sys.exit(app.exec())
