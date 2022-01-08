# Form implementation generated from reading ui file 'NextPlayerPopOut.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from player import Player

class Ui_Form6(object):
    def __init__(self, aux_players_sorted, aux_current_player_name):
        self.players_sorted = aux_players_sorted
        self.current_player_name = aux_current_player_name
        # elf.check_if_popout = check

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(299, 292)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("background-color:\"lightgreen\"\n"
"")
        self.nextPlabel = QtWidgets.QLabel(Form)
        self.nextPlabel.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextPlabel.setFont(font)
        self.nextPlabel.setObjectName("nextPlabel")
        self.playerNamelabel = QtWidgets.QLabel(Form)
        self.playerNamelabel.setGeometry(QtCore.QRect(20, 60, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerNamelabel.sizePolicy().hasHeightForWidth())
        self.playerNamelabel.setSizePolicy(sizePolicy)
        self.playerNamelabel.setMinimumSize(QtCore.QSize(200, 30))
        self.playerNamelabel.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playerNamelabel.setFont(font)
        self.playerNamelabel.setText("")
        self.playerNamelabel.setObjectName("playerNamelabel")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 129, 261, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.secondPnamelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.secondPnamelabel.setObjectName("secondPnamelabel")
        self.gridLayout.addWidget(self.secondPnamelabel, 1, 0, 1, 1)
        self.thirdPnamelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.thirdPnamelabel.setObjectName("thirdPnamelabel")
        self.gridLayout.addWidget(self.thirdPnamelabel, 2, 0, 1, 1)
        self.firstPnamelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstPnamelabel.setObjectName("firstPnamelabel")
        self.gridLayout.addWidget(self.firstPnamelabel, 0, 0, 1, 1)
        self.fourthPnamelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fourthPnamelabel.setObjectName("fourthPnamelabel")
        self.gridLayout.addWidget(self.fourthPnamelabel, 3, 0, 1, 1)
        self.firstPscorelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstPscorelabel.setObjectName("firstPscorelabel")
        self.gridLayout.addWidget(self.firstPscorelabel, 0, 1, 1, 1)
        self.secondPscorelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.secondPscorelabel.setObjectName("secondPscorelabel")
        self.gridLayout.addWidget(self.secondPscorelabel, 1, 1, 1, 1)
        self.thirdPscorelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.thirdPscorelabel.setObjectName("thirdPscorelabel")
        self.gridLayout.addWidget(self.thirdPscorelabel, 2, 1, 1, 1)
        self.fourthPscorelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fourthPscorelabel.setObjectName("fourthPscorelabel")
        self.gridLayout.addWidget(self.fourthPscorelabel, 3, 1, 1, 1)

        self.number_of_players = len(self.players_sorted)

        self.playerNamelabel.setText(self.current_player_name)

        self.firstPnamelabel.setText(self.players_sorted[self.number_of_players - 1][0])
        self.firstPscorelabel.setText(str(self.players_sorted[self.number_of_players - 1][1]))

        self.secondPnamelabel.setText(self.players_sorted[self.number_of_players - 2][0])
        self.secondPscorelabel.setText(str(self.players_sorted[self.number_of_players - 2][1]))

        if self.number_of_players == 3:
            self.thirdPnamelabel.setText(self.players_sorted[self.number_of_players - 3][0])
            self.thirdPscorelabel.setText(str(self.players_sorted[self.number_of_players - 3][1]))

        if self.number_of_players == 4:
            self.thirdPnamelabel.setText(self.players_sorted[self.number_of_players - 3][0])
            self.thirdPscorelabel.setText(str(self.players_sorted[self.number_of_players - 3][1]))
            self.fourthPnamelabel.setText(self.players_sorted[self.number_of_players - 4][0])
            self.fourthPscorelabel.setText(str(self.players_sorted[self.number_of_players - 4][1]))

        #QtCore.QTimer.singleShot(5, Form.close())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scrabble"))
        self.nextPlabel.setText(_translate("Form", "Next player:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_Form6()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
