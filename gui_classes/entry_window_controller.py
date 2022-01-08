from gui_classes.login_window_controller import LoginWindowController
from gui_py_source.entry_window import *
from menu_window_controller import *


class EntryWindowController(DummyWindow):

    def __init__(self):
        DummyWindow.__init__(self)

        self.ui = Ui_entryWindow()
        self.ui.setupUi(self)
        ### SET SHADOW / IMAGES
        set_image_to_label(self.ui.emoji_label, '3x.png')

        ### ADD BUTTON EVENT HANDLERS
        # closes QMainWindow
        self.ui.exitButton.clicked.connect(lambda: quit_window(self))
        # opens login window
        self.ui.triggerButton.clicked.connect(lambda: self.open_login())

        # show window
        self.show()

    def open_login(self):
        print('closing entry_window instance')
        LoginWindowController()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ent = EntryWindowController()
    sys.exit(app.exec())