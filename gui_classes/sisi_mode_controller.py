from typing import Union

from gui_classes.hotseat_players_login_controller import *
from gui_py_source.sisi_mode_window import Ui_sisi_mode_window
from player import Player
import random


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
        # self.ui.medium_si_button.clicked.connect(lambda: self.start_player_si_game('medium'))
        self.ui.sisi_game_button.clicked.connect(lambda: self.start_sisi_game())

        ### THIS WAY EXIT CLICKED DOESNT BUST THE WHOLE APP
        self.ui.exit_button.clicked.connect(lambda: return_to_menu(self, self.menu_handle))

        self.show()

    def start_player_si_game(self, ai: str) -> None:
            _names = ("David", "Mati", "Jerzy", "Jeff", "Joe", "Alice", "Robert", "Leokadia", "Kamil", "Barbara")
            name = _names[random.randint(0, len(_names)-1)] + "_AI" + str(random.randint(0,20))
            print('%s %s' % ('player', ai))
            # ### GET CURRENT PLAYER ID
            _player = Player(self.menu_handle.host_id, [])
            _ai = Player(name, [], True, ai.upper())
            self.hide()
            # self.close()
            self.signal_closing()
            Board_gui(2, [_player, _ai], self.menu_handle)

    def verify_checkboxes(self) -> [bool, list]:
        _s1_checkboxes = [checkbox for checkbox in self.findChildren(QCheckBox, QRegularExpression('si1_*')) if checkbox.isChecked()]
        _s2_checkboxes = [checkbox for checkbox in self.findChildren(QCheckBox, QRegularExpression('si2_*')) if checkbox.isChecked()]

        if len(_s1_checkboxes) == 1 and len(_s2_checkboxes) == 1:
            return [True, [*_s1_checkboxes, *_s2_checkboxes]]
        else:
            uncheck_all([*_s1_checkboxes, *_s2_checkboxes])
            return [False, []]

    def start_sisi_game(self) -> None:
        _verified, _checkboxes = self.verify_checkboxes()
        if _verified:
            _names = ("David", "Mati", "Jerzy", "Jeff", "Joe", "Alice", "Robert", "Leokadia", "Kamil", "Barbara")
            print('sisi +')
            _name1 = _names[random.randint(0, len(_names)-1)] + "_AI" + str(random.randint(0,20))
            _name2 = _names[random.randint(0, len(_names)-1)] + "_AI" + str(random.randint(0,20))
            ### GET AI
            _ai_mode = [chbox.objectName().split("_")[1] for chbox in _checkboxes]
            _ai1 = Player(_name1, [], True, _ai_mode[0].upper())
            _ai2 = Player(_name2, [], True, _ai_mode[1].upper())
            self.hide()
            # self.close()
            self.signal_closing()
            Board_gui(2, [_ai1, _ai2], self.menu_handle)


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