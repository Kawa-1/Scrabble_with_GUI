from PyQt6 import QtWidgets
import sys
import menu

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = menu.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
