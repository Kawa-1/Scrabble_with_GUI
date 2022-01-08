from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QWidget

from auxiliary.window_movement import DummyWindow
from auxiliary.gui_base_methods import *
from database_management import credentials_manager
from database_management.credentials_manager import CredentialsManager
from gui_py_source.settings_window import Ui_settings_window


class SettingsController(DummyWindow):
    def __init__(self, menu: QMainWindow):
        DummyWindow.__init__(self)
        self.menu_handle = menu
        # copy host id from menu controller
        # use as a reference to db (primary key)
        # self._host_id = self.menu_handle.host_id

        self.ui = Ui_settings_window()
        self.ui.setupUi(self)

        ### SET USERNAME
        self.ui.player_name_label.setText(self.menu_handle.host_id)

        ### SET IMAGES
        set_image_to_label(self.ui.icon_label, 'gamer.png')
        set_image_to_button(self.ui.return_to_menu_button, 'returnleft.png')

        ### DISABLE FOCUS
        disable_mac_focus(self.findChildren(QLineEdit))

        ### HIDE PASSWORDS
        set_echomode(self.findChildren(QLineEdit, QRegularExpression('.*pass')))

        ### SET CURSOR TO MID FIELD
        set_cursor(self.findChildren(QLineEdit))

        ### HIDE ERROR LABEL
        hide_labels([self.ui.error_label])

        ### SET BUTTON METHODS
        self.ui.change_pass_button.clicked.connect(lambda: self.init_pass_change())
        self.ui.return_to_menu_button.clicked.connect(lambda: self.return_to_menu())

        ### THIS WAY EXIT CLICKED DOESNT BUST THE WHOLE APP
        self.ui.exit_button.clicked.connect(lambda: self.return_to_menu())

        self.show()

    def init_pass_change(self) -> None:
        _old_pass, _new_pass = self.ui.old_pass_lineedit.text(), self.ui.new_pass_lineedit.text()

        if self.ui.new_pass_lineedit != '' and self.ui.old_pass_lineedit != '':
            # case when login//pass mismatch occurs
            if not CredentialsManager.change_password(self.menu_handle.host_id, _old_pass, _new_pass):
                self.ui.error_label.setText('Błędne hasło')
                self.ui.error_label.setVisible(1)
            # successful login
            else:
                self.ui.error_label.setText('Poprawnie zmieniono hasło')
                self.ui.error_label.setVisible(1)
                self.ui.error_label.setStyleSheet('color: green;')
                clear_input(self.ui.old_pass_lineedit, self.ui.new_pass_lineedit)

        else:
            self.ui.error_label.setText('Uzupełnij oba pola')
            self.ui.error_label.setVisible(1)

    def return_to_menu(self) -> None:
        self.menu_handle.show()
        self.menu_handle._is_sett_open = False
        self.close()

    def signal_closing(self) -> None:
        self.menu_handle._is_sett_open = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = SettingsController(QMainWindow())
    sys.exit(app.exec())


