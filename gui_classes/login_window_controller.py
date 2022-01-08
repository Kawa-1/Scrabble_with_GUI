from PyQt6.QtCore import QRegularExpression

from gui_py_source.login_window import *
from gui_classes.menu_window_controller import *
from database_management import credentials_manager


class LoginWindowController(DummyWindow):
    def __init__(self):
        DummyWindow.__init__(self)

        self.ui = Ui_login_window()
        self.ui.setupUi(self)

        ### SET WIDGET TO DISPLAY LOGIN FIELDS
        self.ui.login_reg_stacked.setCurrentWidget(self.ui.login_content)
        ### SET FOCUS FOR LOGIN INPUT FIELD
        self.setFocus()

        ### DARWIN EXCLUSIVE -> disable highlight around all input fields
        disable_mac_focus(self.findChildren(QLineEdit))

        ### SET SHADOW / IMAGES
        set_image_to_label(self.ui.emoji_label, '3x.png')

        ### SET BUTTON EVENT HANDLERS: OTHER
        self.ui.exit_button.clicked.connect(lambda: quit_window(self))

        ### SET BUTTON EVENT HANDLERS: LOGIN
        self.ui.login_button.clicked.connect(lambda: self.open_menu())
        self.ui.register_button.clicked.connect(lambda: self.init_register())

        ### SET BUTTON EVENT HANDLERS: REGISTER
        self.ui.init_login_button.clicked.connect(lambda: self.init_login())
        self.ui.init_register_button.clicked.connect(lambda: self.register_process())

        ### SET ECHOMODE-PASS TO PASS INPUT FIELDS
        set_echomode(self.findChildren(QLineEdit, QRegularExpression(".*password_input$")))

        ### show window
        self.show()

    def open_menu(self):
        _pass = self.ui.password_input.text()
        _login = self.ui.login_input.text()

        if _pass != '' and _login != '':
            # verify supplied data, if correct return open MenuWindow and quit LoginWindow
            # TODO: update MenuWindow(); pass credentials to MenuWindow constructor
            if credentials_manager.CredentialsManager.verify_credentials(_login, _pass):
                MenuWindowController(_login)
                quit_window(self)
            else:
                clear_input(self.ui.password_input, self.ui.login_input)
                self.ui.error_label.setText('niepoprawne dane')
        else:
            print('uzupelnij oba pola')
            self.ui.error_label.setText('uzupełnij oba pola')

    def init_register(self):
        clear_input(self.ui.password_input, self.ui.login_input)
        self.ui.error_register_label.clear()
        self.ui.login_reg_stacked.setCurrentWidget(self.ui.register_content)
        self.setFocus()

    def init_login(self):
        # clear input delivered to register fields when switching to login content
        clear_input(self.ui.reg_login_input, self.ui.reg_password_input)
        # clear error_reg label so that it wont display anyth. when init_register() called
        self.ui.error_register_label.clear()
        self.ui.login_reg_stacked.setCurrentWidget(self.ui.login_content)
        self.setFocus()

    def register_process(self):
        _pass = self.ui.reg_password_input.text()
        _login = self.ui.reg_login_input.text()

        if _pass != '' and _login != '':
            if credentials_manager.CredentialsManager.register_player(_login, _pass):
                clear_input(self.ui.reg_password_input, self.ui.reg_login_input)
                self.ui.error_register_label.setStyleSheet('color: rgb(62, 231, 41)')
                self.ui.error_register_label.setText('poprawnie zarejestrowano')
                self.setFocus()
            # such credentials exist in database; then:
            else:
                clear_input(self.ui.reg_password_input, self.ui.reg_login_input)
                self.ui.error_label.setStyleSheet('color: red')
                self.ui.error_register_label.setText('spróbuj inne dane')
        else:
            print('uzupelnij oba pola')
            self.ui.error_register_label.setText('uzupełnij oba pola')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = LoginWindowController()
    sys.exit(app.exec())