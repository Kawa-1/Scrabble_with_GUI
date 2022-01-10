from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from auxiliary.gui_base_methods import disable_mac_focus, set_image_to_label, set_image_to_button, return_to_menu, \
    hide_labels
from auxiliary.window_movement import DummyWindow
from gui_classes.board_replay_controller import BoardReplayController
from gui_py_source.replay_select_window import Ui_replay_select_window
from management_database import ManagementGeneralLeaderboard


class ReplaySelectController(DummyWindow):
    def __init__(self, menu):
        DummyWindow.__init__(self)
        self.menu_handle = menu
        """
            TODO: if paging is implemented, param number can be omitted
            now: len(saved_games) == 4
        """
        # omit [0] param == status
        self.saved_games = ManagementGeneralLeaderboard.acquire_games_list(number=4)[1]
        # self.saved_games = ManagementGeneralLeaderboard.acquire_games_list()[1]


        self.ui = Ui_replay_select_window()
        self.ui.setupUi(self)

        ### SET IMAGES
        set_image_to_label(self.ui.replay_icon_label, 'gamer.png')
        set_image_to_button(self.ui.forwards_button, 'returnright.png')
        set_image_to_button(self.ui.backwards_button, 'returnleft.png')
        set_image_to_button(self.ui.return_to_menu_button, 'returnleft.png')

        ### HIDE BUTTONS
        hide_labels(self.findChildren(QPushButton, QRegularExpression('game*')))

        ### SET BUTTON EVENT HANDLERS
        self.ui.return_to_menu_button.clicked.connect(lambda: self.return_to_menu())
        self.ui.forwards_button.clicked.connect(lambda: self.page_forwards())
        self.ui.backwards_button.clicked.connect(lambda: self.page_forwards())
        ### THIS WAY EXIT CLICKED DOESNT BUST THE WHOLE APP
        self.ui.exit_button.clicked.connect(lambda: return_to_menu(self, self.menu_handle))

        ### SET OPEN REPLAY METHODS TO BUTTONS
        """
            TODO: extend to all saved games -> add paging: 4 buttons(game_id) per page
            REQUIRED: custom QWidgets: QStackedWidget
        """
        for i in range(len(self.saved_games)):
            print(self.saved_games)
            print(self.saved_games[i][0])
            _game_index = self.saved_games[i][0]
            _players = self.saved_games[i][1]
            _text_2_btn = "{}{}{}".format(_game_index, ': ', _players)
            eval("self.ui.game{}_button".format(i+1)).setText(_text_2_btn)
            eval("self.ui.game{}_button".format(i+1)).clicked.connect(lambda state, x=_game_index: self.open_chosen_replay(x))
            eval("self.ui.game{}_button".format(i+1)).setVisible(1)

        ### ASSUME FOR NOW THAT ONLY FOUR GAMES CAN BE REPLAYED
        hide_labels([self.ui.backwards_button, self.ui.forwards_button])

        self.show()

    def page_backwards(self) -> None:
        pass

    def page_forwards(self) -> None:
        pass

    def open_chosen_replay(self, game: int) -> None:
        print('replay: {} opened'.format(game))

        # TODO: uncomment the below when finished
        BoardReplayController(menu=self.menu_handle, game_id=game)
        # TODO: signal to menu that replay had finished
        self.menu_handle._is_replay_open = False
        self.close()

    def signal_closing(self) -> None:
        self.menu_handle._is_replay_open = False

    def add_game_replay_handlers(self) -> None:
        _pages = 1
        for _game in range(self.saved_games):
            if _game % 4:
                _game_index = self.saved_games[_game][0]
                _players = self.saved_games[_game][1]
                _text_2_btn = "{}{}{}".format(_game_index, ': ', _players)
                eval("self.ui.game{}_button".format(_game + 1)).setText(_text_2_btn)
                eval("self.ui.game{}_button".format(_game + 1)).clicked.connect(
                    lambda state, x=_game_index: self.open_chosen_replay(x)
                )
                eval("self.ui.game{}_button".format(_game + 1)).setVisible(1)

    def add_pages(self) -> None:
        pass

    def return_to_menu(self):
        self.menu_handle.show()
        self.menu_handle._is_replay_open = False
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ent = ReplaySelectController(QMainWindow())
    sys.exit(app.exec())