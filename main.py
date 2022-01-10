from PyQt6 import QtWidgets
import sys
import menu
from gui_classes.login_window_controller import LoginWindowController
from management_database import ManagementGeneralLeaderboard

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = LoginWindowController()
    ManagementGeneralLeaderboard.delete_empty_games_onstart()
    sys.exit(app.exec())