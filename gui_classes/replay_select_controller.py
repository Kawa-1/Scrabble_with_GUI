from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel

from auxiliary.gui_base_methods import disable_mac_focus, set_image_to_label, set_image_to_button, return_to_menu, \
    hide_labels
from auxiliary.window_movement import DummyWindow
from gui_py_source.replay_select_window import Ui_replay_select_window
from management_database import ManagementGeneralLeaderboard


class ReplaySelectController(DummyWindow):
    def __init__(self, menu):
        DummyWindow.__init__(self)
        self.menu_handle = menu
        self.saved_games = ManagementGeneralLeaderboard.acquire_games_list()

        self.ui = Ui_replay_select_window()
        self.ui.setupUi(self)

        ### SET IMAGES
        set_image_to_label(self.ui.replay_icon_label, 'gamer.png')
        set_image_to_button(self.ui.forwards_button, 'returnright.png')
        set_image_to_button(self.ui.backwards_button, 'returnleft.png')
        set_image_to_button(self.ui.return_to_menu_button, 'returnleft.png')

        ### SET BUTTON EVENT HANDLERS
        self.ui.return_to_menu_button.clicked.connect(lambda: return_to_menu(self, self.menu_handle))
        self.ui.forwards_button.clicked.connect(lambda: self.page_forwards())
        self.ui.backwards_button.clicked.connect(lambda: self.page_forwards())

        ### ASSUME FOR NOW THAT ONLY FOUR GAMES CAN BE REPLAYED
        hide_labels([self.ui.backwards_button, self.ui.forwards_button])

        ### THIS WAY EXIT CLICKED DOESNT BUST THE WHOLE APP
        self.ui.exit_button.clicked.connect(lambda: return_to_menu(self, self.menu_handle))

        self.show()

    def page_backwards(self) -> None:
        pass

    def page_forwards(self) -> None:
        pass

    def signal_closing(self) -> None:
        self.menu_handle._is_replay_open = False

    def return_to_menu(self):
        self.menu_handle.show()
        self.menu_handle._is_replay_open = False
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ent = ReplaySelectController(QMainWindow())
    sys.exit(app.exec())