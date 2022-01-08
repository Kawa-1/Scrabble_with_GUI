from auxiliary.gui_base_methods import *
from auxiliary.window_movement import DummyWindow
from gui_classes.board_gui_controller import Board_gui
from gui_classes.hotseat_player_count_controller import HotseatPlayerCountController
from gui_classes.settings_window_controller import SettingsController
from gui_classes.sisi_mode_controller import SisiModeController
from gui_py_source.menu_window import *
from management_database import ManagementGeneralLeaderboard


class MenuWindowController(DummyWindow):
    def __init__(self, host_id):
        self.host_id = host_id
        self._is_hs_open = False
        self._is_si_open = False
        self._is_sett_open = False
        # self._is_rank_open = False
        DummyWindow.__init__(self)

        self.ui = Ui_menu_window()
        self.ui.setupUi(self)

        ### SET SHADOW / IMAGES
        set_image_to_label(self.ui.emoji_label, '3x.png')
        set_image_to_button(self.ui.hotseat_button, 'gamer.png')
        set_image_to_button(self.ui.help_button, 'edit.png')
        set_image_to_button(self.ui.logout_button, 'returnleft.png')
        set_image_to_button(self.ui.account_button, 'lookingglass.png')
        set_image_to_button(self.ui.vs_si_button, 'swords.png')

        ### ADD BUTTON EVENT HANDLERS
        self.ui.exit_button.clicked.connect(lambda: quit_window(self))
        self.ui.help_button.clicked.connect(lambda: Board_gui.clicked_help(self))
        self.ui.vs_si_button.clicked.connect(lambda: self.init_vs_si_game())
        self.ui.hotseat_button.clicked.connect(lambda: self.init_hotseat_game())
        self.ui.account_button.clicked.connect(lambda: self.open_account_settings())
        self.ui.logout_button.clicked.connect(lambda: self.open_logout_alert())

        ### SET TOP5
        self.fetch_and_set_players_score()

        ### CHANGE PLAYER LABELS' COLOR IN TOP5
        # find_object_by_substring()

        self.show()

    def init_vs_si_game(self) -> None:
        print('vssi game mode chosen')
        if not self._is_si_open:
            self._is_si_open = True
            SisiModeController(menu=self)
            self.hide()

    def init_hotseat_game(self) -> None:
        print('hotseat game mode chosen')
        if not self._is_hs_open:
            self._is_hs_open = True
            HotseatPlayerCountController(menu=self)
            # if it were to be left unhidden -> block any interactions
            self.hide()

    def open_account_settings(self) -> None:
        # TODO: add credentials manipulation
        print('account settings opened')
        if not self._is_sett_open:
            self._is_sett_open = True
            SettingsController(menu=self)
            # if it were to be left unhidden -> block any interactions
            self.hide()

    def open_logout_alert(self) -> None:
        # TODO: make it an actual alert
        self.close()
        from gui_classes.login_window_controller import LoginWindowController
        LoginWindowController()

    def fetch_and_set_players_score(self) -> None:
        _top5_scores = ManagementGeneralLeaderboard.get_general_leaderboard()

        for index, row in enumerate(_top5_scores, start=1):
            if index < 6:
                eval("self.ui.p{}_name_label".format(str(index))).setText(row[0])
                eval("self.ui.p{}_score_label".format(str(index))).setText(str(row[1]))
            else:
                break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = MenuWindowController('dummy host')
    sys.exit(app.exec())