from gui_classes.hotseat_players_login_controller import *
from gui_py_source.sisi_mode_window import Ui_sisi_mode_window


class SisiModeController(DummyWindow):
    def __init__(self, menu):
        DummyWindow.__init__(self)
        self.menu_handle = menu

        self.ui = Ui_sisi_mode_window()
        self.ui.setupUi(self)

        disable_mac_focus([self.ui.hard_si_button])

        ### SET IMAGES
        set_image_to_label(self.findChildren(QLabel, QRegularExpression('si_icon*')), 'swords.png')
        set_image_to_button(self.ui.sisi_game_button, 'returnright.png')
        set_image_to_button(self.ui.return_to_menu_button, 'returnleft.png')

        ### SET BUTTON EVENT HANDLERS
        self.ui.return_to_menu_button.clicked.connect(lambda: self.return_to_menu())
        self.ui.player_button.clicked.connect(
            lambda: self.ui.game_mode_stacked.setCurrentWidget(self.ui.player_si_level_select_page)
        )
        self.ui.simulate_button.clicked.connect(
            lambda: self.ui.game_mode_stacked.setCurrentWidget(self.ui.sisi_level_select_page)
        )
        self.ui.hard_si_button.clicked.connect(lambda: self.start_player_si_game('hard'))
        self.ui.easy_si_button.clicked.connect(lambda: self.start_player_si_game('easy'))
        self.ui.sisi_game_button.clicked.connect(lambda: self.start_sisi_game())

        ### THIS WAY EXIT CLICKED DOESNT BUST THE WHOLE APP
        self.ui.exit_button.clicked.connect(lambda: return_to_menu(self, self.menu_handle))

        self.show()

    @staticmethod
    def start_player_si_game(ai: str) -> None:
            print('%s %s' % ('player', ai))
            # ### GET CURRENT PLAYER ID
            # _player = Player(self.menu_handle.host_id, [])
            # _ai = AI(ai)
            # Board_gui(2, [_player, _ai], self.menu_handle)

    def verify_checkboxes(self) -> bool:
        _s1_checkboxes = [checkbox for checkbox in self.findChildren(QCheckBox, QRegularExpression('s1_*')) if checkbox.isChecked()]
        _s2_checkboxes = [checkbox for checkbox in self.findChildren(QCheckBox, QRegularExpression('s2_*')) if checkbox.isChecked()]

        if len(_s1_checkboxes) % 2 or len(_s2_checkboxes) % 2:
            uncheck_all([*_s1_checkboxes, *_s2_checkboxes])
            return False
        elif not len(_s1_checkboxes) % 2 and not len(_s2_checkboxes) % 2:
            return True
        else:
            print('idk co to robi')
            return False

    def start_sisi_game(self) -> None:
        if self.verify_checkboxes():
            print('sisi +')

    def signal_closing(self) -> None:
        self.menu_handle._is_si_open = False

    def return_to_menu(self):
        self.menu_handle.show()
        self.menu_handle._is_si_open = False
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = SisiModeController(QMainWindow())
    sys.exit(app.exec())