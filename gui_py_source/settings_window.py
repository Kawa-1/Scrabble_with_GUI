# Form implementation generated from reading ui file '/Users/mzieba/Documents/szkola/code/Scrabble_with_GUI/templates/settings_window.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_settings_window(object):
    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(591, 698)
        self.centralwidget = QtWidgets.QWidget(settings_window)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.menu_frame.setGeometry(QtCore.QRect(140, 60, 311, 461))
        self.menu_frame.setStyleSheet("QFrame {\n"
"    border-radius: 7px;\n"
"    color: rgb(62, 231, 41);\n"
"    background-color: rgb(40, 109, 50);\n"
"}\n"
"")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.name_label = QtWidgets.QLabel(self.menu_frame)
        self.name_label.setGeometry(QtCore.QRect(-40, 20, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.exit_button = QtWidgets.QPushButton(self.menu_frame)
        self.exit_button.setGeometry(QtCore.QRect(290, 7, 14, 14))
        self.exit_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 40, 54);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.exit_button.setText("")
        self.exit_button.setCheckable(False)
        self.exit_button.setDefault(False)
        self.exit_button.setFlat(False)
        self.exit_button.setObjectName("exit_button")
        self.return_to_menu_button = QtWidgets.QPushButton(self.menu_frame)
        self.return_to_menu_button.setGeometry(QtCore.QRect(140, 410, 41, 32))
        self.return_to_menu_button.setStyleSheet("QPushButton{\n"
"    background-color: transparent;\n"
"image: url(:/newPrefix/images/returnleft.png);\n"
"}\n"
"")
        self.return_to_menu_button.setText("")
        self.return_to_menu_button.setObjectName("return_to_menu_button")
        self.frame = QtWidgets.QFrame(self.menu_frame)
        self.frame.setGeometry(QtCore.QRect(45, 110, 221, 281))
        self.frame.setStyleSheet("QWidget {\n"
"background-color: rgb(22, 60, 27);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.player_name_label = QtWidgets.QLabel(self.frame)
        self.player_name_label.setGeometry(QtCore.QRect(70, 15, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.player_name_label.setFont(font)
        self.player_name_label.setStyleSheet("QLabel {\n"
"    \n"
"    color: rgb(62, 232, 41);\n"
"}")
        self.player_name_label.setObjectName("player_name_label")
        self.icon_label = QtWidgets.QLabel(self.frame)
        self.icon_label.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.icon_label.setStyleSheet("QLabel {\n"
"    \n"
"    image: url(:/newPrefix/images/gamer.png);\n"
"}")
        self.icon_label.setText("")
        self.icon_label.setObjectName("icon_label")
        self.settings_label = QtWidgets.QLabel(self.frame)
        self.settings_label.setGeometry(QtCore.QRect(-30, -40, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.settings_label.setFont(font)
        self.settings_label.setStyleSheet("QLabel {\n"
"    color: rgb(226, 224, 158);\n"
"\n"
"}")
        self.settings_label.setObjectName("settings_label")
        self.game_mode_desc_2 = QtWidgets.QTextBrowser(self.frame)
        self.game_mode_desc_2.setGeometry(QtCore.QRect(10, 65, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.game_mode_desc_2.setFont(font)
        self.game_mode_desc_2.setStyleSheet("QWidget{\n"
"    \n"
"    color: rgb(204, 204, 143);\n"
"}")
        self.game_mode_desc_2.setObjectName("game_mode_desc_2")
        self.old_pass_lineedit = QtWidgets.QLineEdit(self.frame)
        self.old_pass_lineedit.setGeometry(QtCore.QRect(90, 130, 113, 21))
        self.old_pass_lineedit.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(111, 254, 112);\n"
"    color: black;\n"
"\n"
"}")
        self.old_pass_lineedit.setObjectName("old_pass_lineedit")
        self.new_pass_lineedit = QtWidgets.QLineEdit(self.frame)
        self.new_pass_lineedit.setGeometry(QtCore.QRect(90, 170, 113, 21))
        self.new_pass_lineedit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(52, 119, 53);\n"
"    color: black;\n"
"    \n"
"}")
        self.new_pass_lineedit.setObjectName("new_pass_lineedit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 133, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 173, 71, 16))
        self.label_2.setObjectName("label_2")
        self.change_pass_button = QtWidgets.QPushButton(self.frame)
        self.change_pass_button.setGeometry(QtCore.QRect(60, 230, 100, 32))
        self.change_pass_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 128, 249);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.change_pass_button.setObjectName("change_pass_button")
        self.error_label = QtWidgets.QLabel(self.frame)
        self.error_label.setGeometry(QtCore.QRect(0, 200, 221, 20))
        self.error_label.setStyleSheet("QLabel {\n"
"    color: red;\n"
"}")
        self.error_label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.frame.raise_()
        self.name_label.raise_()
        self.exit_button.raise_()
        self.return_to_menu_button.raise_()
        settings_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings_window)
        QtCore.QMetaObject.connectSlotsByName(settings_window)

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "MainWindow"))
        self.name_label.setText(_translate("settings_window", "<html><head/><body><p><span style=\" font-weight:700;\">Scrabble</span></p><p><br/></p></body></html>"))
        self.player_name_label.setText(_translate("settings_window", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; font-style:italic;\">*player*</span></p></body></html>"))
        self.settings_label.setText(_translate("settings_window", "<html><head/><body><p><span style=\" font-size:18pt;\">Ustawienia</span></p><p><br/></p></body></html>"))
        self.game_mode_desc_2.setHtml(_translate("settings_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:14pt; font-weight:700; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">zmień hasło</span></p></body></html>"))
        self.label.setText(_translate("settings_window", "stare hasło"))
        self.label_2.setText(_translate("settings_window", "nowe hasło"))
        self.change_pass_button.setText(_translate("settings_window", "zatwierdź"))
        self.error_label.setText(_translate("settings_window", "błędne haslo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings_window = QtWidgets.QMainWindow()
    ui = Ui_settings_window()
    ui.setupUi(settings_window)
    settings_window.show()
    sys.exit(app.exec())
