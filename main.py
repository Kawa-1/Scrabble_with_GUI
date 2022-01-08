from PyQt6 import QtWidgets
import sys
import menu
from gui_classes.login_window_controller import LoginWindowController

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = LoginWindowController()
    sys.exit(app.exec())