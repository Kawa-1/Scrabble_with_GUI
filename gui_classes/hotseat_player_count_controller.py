from gui_classes.hotseat_players_login_controller import *


class HotseatPlayerCountController(DummyWindow):
    def __init__(self, menu):
        DummyWindow.__init__(self)
        self.menu_handle = menu

        self.ui = Ui_hotseat_player_count_window()
        self.ui.setupUi(self)

        ### SET IMAGES
        set_image_to_label(self.ui.hotseat_icon_label, 'gamer.png')
        set_image_to_button(self.ui.return_to_menu_button, 'returnleft.png')

        ### SET BUTTON EVENT HANDLERS
        self.ui.return_to_menu_button.clicked.connect(lambda: self.return_to_menu())
        self.ui.player2_button.clicked.connect(lambda: self.init_players_login(2))
        self.ui.player3_button.clicked.connect(lambda: self.init_players_login(3))
        self.ui.player4_button.clicked.connect(lambda: self.init_players_login(4))

        ### THIS WAY EXIT CLICKED DOESNT BUST THE WHOLE APP
        self.ui.exit_button.clicked.connect(lambda: self.return_to_menu())

        self.show()

    def init_players_login(self, num: int) -> None:
        try:
            # TODO: update w/ credentials handover
            HotseatPlayerLoginController(num, self.menu_handle)
            self.close()
        except Exception as e:
            print(e)

    def return_to_menu(self):
        self.menu_handle.show()
        self.menu_handle._is_hs_open = False
        self.close()

    def signal_closing(self):
        self.menu_handle._is_hs_open = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = HotseatPlayerCountController(QMainWindow)
    sys.exit(app.exec())