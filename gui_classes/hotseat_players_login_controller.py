from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QWidget

from auxiliary.window_movement import DummyWindow
from auxiliary.gui_base_methods import *
from database_management.credentials_manager import CredentialsManager
from gui_py_source.hotseat_player_count_window import *
from gui_classes.board_gui_controller import Board_gui
from gui_py_source.hotseat_players_login_window import Ui_hotseat_players_login_window
from player import Player


class HotseatPlayerLoginController(DummyWindow):
    def __init__(self, num: int, menu: QMainWindow):
        DummyWindow.__init__(self)

        # fields to pass to board_gui_controller
        self.players = []
        self.number_of_players = num
        self.current_game_board = None
        self.menu_handle = menu

        self.ui = Ui_hotseat_players_login_window()
        self.ui.setupUi(self)

        ### SET APPROPRIATE NUM PLAYERS WIDGET
        self._proper_players = ('players%d_page' % num)
        self._lay = self.findChild(QWidget, self._proper_players)
        self.ui.login_stacked_widget.setCurrentWidget(self._lay)

        self.setFocus()

        ### HIDE STATUS LABEL AS IT HAS ONE VALUE FOR NEGATIVE ALL LOGGED
        self.ui.start_game_status_label.setVisible(0)

        ### HIDE ALL LOGIN ERROR LABELS
        hide_labels(self.findChildren(QLabel, QRegularExpression('^wrong_cred_label_*')))

        ### SET IMAGES
        set_image_to_button(self.ui.start_game_button, 'swords.png')
        set_image_to_button(self.ui.return_to_menu_button, 'returnleft.png')
        set_image_to_label(self.ui.hotseat_icon_label, 'gamer.png')
        set_image_to_label(self.findChildren(QLabel, QRegularExpression('player_icon_label_*')), 'gamer.png')
        set_image_to_button(self.findChildren(QPushButton, QRegularExpression('.*_login_button')), 'edit.png')

        ### DISABLE FOCUS
        disable_mac_focus(self.findChildren(QLineEdit))

        ### HIDE PASSWORDS
        set_echomode(self.findChildren(QLineEdit, QRegularExpression('.*pass')))

        ### SET CURSOR TO MID FIELD
        set_cursor(self.findChildren(QLineEdit))
        ### SET CENTERED ALIGNMENT (SAME METHOD AS ABOVE)
        set_cursor(self.findChildren(QLabel, QRegularExpression('wrong_cred_label.*')))

        ### ADD BUTTON EVENT HANDLERS
        self.ui.exit_button.clicked.connect(lambda: quit_window(self))
        self.ui.start_game_button.clicked.connect(lambda: self.init_game())
        self.ui.return_to_menu_button.clicked.connect(lambda: return_to_menu(self, self.menu_handle))

        ### ADD LOGIN HANDLERS
        for _login_btn in self.findChildren(QPushButton, QRegularExpression('.*login_button')):
            # for each login button find corresponding (namewise) input fields
            # p[1-9]+of[1-9]+_login button to p[1-9]+of[1-9]_pass and p[1-9]+of[1-9]_login
            _pass_obj = find_object_by_substring(QLineEdit, name=_login_btn.objectName(), prefix='',
                                                 suffix='_login_button', root=self, new_pref=None, new_suff='_pass')

            _log_obj = find_object_by_substring(QLineEdit, name=_login_btn.objectName(), prefix='',
                                                suffix='_login_button', root=self, new_pref=None, new_suff='_login')

            # pass objects to function
            _login_btn.clicked.connect(
                lambda checked, passwd=_pass_obj, login=_log_obj: self.init_login(passwd, login)
            )
        ### SHOW GUI
        self.show()

    def init_login(self, passw: QLineEdit, log: QLineEdit) -> None:
        _passw, _log = passw.text(), log.text()
        # check if not empty
        if _passw != '' and _log != '':
            # verify supplied data, if correct set p[1-9]+of[1-9]+_logged_stacked as currentW.
            if CredentialsManager.verify_credentials(_log, _passw):
                print('correct creds')

                if not self.is_player_already_logged(_log):

                    # using one of names of passed objects to get reference to
                    _adequate_stacked_logged = find_object_by_substring(
                        QWidget, passw.objectName(), 'p', '_pass', self, 'player', '_stacked'
                    )

                    _successful_logged_widget = find_object_by_substring(
                        QWidget, passw.objectName(), 'p', '_pass', self, 'player', '_logged_stacked'
                    )

                    _player_name_label = find_object_by_substring(
                        QLabel, passw.objectName(), 'p', '_pass', self, 'player', '_name_label'
                    )

                    ### SET STACKED PAGE THAT INDICATES CORRECT AUTHORIZATION
                    _adequate_stacked_logged.setCurrentWidget(_successful_logged_widget)
                    ### ASSUME THAT ENTERED LOGIN IS PLAYER NAME
                    _player_name_label.setText(_log)

                    ### APPEND NEW PLAYER
                    self.players.append(self.create_player_object(_log))

                # player of such credentials has been authenticated
                else:
                    clear_input(passw, log)
                    _player_error_label = find_object_by_substring(
                        QLabel, passw.objectName(), 'p', '_pass', self, 'wrong_cred_label_', ''
                    )
                    _player_error_label.setText('gracz już zalogowany')
                    _player_error_label.setVisible(1)
                    ### SET FOCUS ON LOGIN INPUT FIELD
                    log.setFocus()

            # clear input if creds are incorrect
            else:
                clear_input(passw, log)
                _player_error_label = find_object_by_substring(
                    QLabel, passw.objectName(), 'p', '_pass', self, 'wrong_cred_label_', ''
                )
                _player_error_label.setText('wprowadzono złe dane')
                _player_error_label.setVisible(1)
                ### SET FOCUS ON LOGIN INPUT FIELD
                log.setFocus()
        else:
            print('uzupelnij oba pola')
            _player_error_label = find_object_by_substring(
                QLabel, passw.objectName(), 'p', '_pass', self, 'wrong_cred_label_', ''
            )
            _player_error_label.setText('uzupełnij oba pola')
            _player_error_label.setVisible(1)
            ### SET FOCUS ON LOGIN INPUT FIELD
            log.setFocus()

        ### CLEAR INPUT REGARDLESS OF IF STATEMENT
        print('pass %s log %s' % (_passw, _log))
        clear_input(passw, log)

    def create_player_object(self, name: str) -> Player:
        ### ASSUMING LOGIN IS AN UNIQUE ID
        return Player(name, [])

    # checks if player object of given name == login from db is already added to player pool for a game
    def is_player_already_logged(self, name: str) -> bool:
        _logged = [player.name for player in self.players]
        if name not in _logged:
            return False
        else:
            return True

    def init_game(self) -> None:
        if len(self.players) != self.number_of_players:
            self.ui.start_game_status_label.setVisible(1)
        else:
            self.start_game()

    def start_game(self) -> None:
        self.current_game_board = Board_gui(self.number_of_players, self.players, self.menu_handle)
        quit_window(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ent = HotseatPlayerLoginController(2, QMainWindow())
    sys.exit(app.exec())
