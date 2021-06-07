from PyQt6 import QtCore, QtGui, QtWidgets
from word import Word
from board import Board
from collections import defaultdict
from bag import Bag
from racks import Racks
from player import Player
from end_turn_pop import Ui_Form6
from leaderboard_pop import Ui_Form5
from kick_player import Ui_Form7
import game_over
from management_database import ManagementGeneralLeaderboard
from help import Ui_Form9


class Ui_Form4(object):
    def __init__(self, aux_number_of_players, aux_players):
        self.number_of_players = aux_number_of_players
        self.players = aux_players

    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.resize(867, 898)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(867, 898))
        Form.setMaximumSize(QtCore.QSize(867, 898))
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet("")

        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 661, 791))
        self.widget_4.setStyleSheet("background-color:\"lightgreen\"\n""")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.board_label_0_0 = QtWidgets.QLabel(self.widget)
        self.board_label_0_0.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_0_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_0.setObjectName("board_label_0_0")
        self.horizontalLayout.addWidget(self.board_label_0_0)
        self.board_label_0_1 = QtWidgets.QLabel(self.widget)
        self.board_label_0_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_1.setText("")
        self.board_label_0_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_1.setObjectName("board_label_0_1")
        self.horizontalLayout.addWidget(self.board_label_0_1)
        self.board_label_0_2 = QtWidgets.QLabel(self.widget)
        self.board_label_0_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_2.setText("")
        self.board_label_0_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_2.setObjectName("board_label_0_2")
        self.horizontalLayout.addWidget(self.board_label_0_2)
        self.board_label_0_3 = QtWidgets.QLabel(self.widget)
        self.board_label_0_3.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_0_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_3.setObjectName("board_label_0_3")
        self.horizontalLayout.addWidget(self.board_label_0_3)
        self.board_label_0_4 = QtWidgets.QLabel(self.widget)
        self.board_label_0_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_4.setText("")
        self.board_label_0_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_4.setObjectName("board_label_0_4")
        self.horizontalLayout.addWidget(self.board_label_0_4)
        self.board_label_0_5 = QtWidgets.QLabel(self.widget)
        self.board_label_0_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_5.setText("")
        self.board_label_0_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_5.setObjectName("board_label_0_5")
        self.horizontalLayout.addWidget(self.board_label_0_5)
        self.board_label_0_6 = QtWidgets.QLabel(self.widget)
        self.board_label_0_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_6.setText("")
        self.board_label_0_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_6.setObjectName("board_label_0_6")
        self.horizontalLayout.addWidget(self.board_label_0_6)
        self.board_label_0_7 = QtWidgets.QLabel(self.widget)
        self.board_label_0_7.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_0_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_7.setObjectName("board_label_0_7")
        self.horizontalLayout.addWidget(self.board_label_0_7)
        self.board_label_0_8 = QtWidgets.QLabel(self.widget)
        self.board_label_0_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_8.setText("")
        self.board_label_0_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_8.setObjectName("board_label_0_8")
        self.horizontalLayout.addWidget(self.board_label_0_8)
        self.board_label_0_9 = QtWidgets.QLabel(self.widget)
        self.board_label_0_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_9.setText("")
        self.board_label_0_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_9.setObjectName("board_label_0_9")
        self.horizontalLayout.addWidget(self.board_label_0_9)
        self.board_label_0_10 = QtWidgets.QLabel(self.widget)
        self.board_label_0_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_10.setText("")
        self.board_label_0_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_10.setObjectName("board_label_0_10")
        self.horizontalLayout.addWidget(self.board_label_0_10)
        self.board_label_0_11 = QtWidgets.QLabel(self.widget)
        self.board_label_0_11.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_0_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_11.setObjectName("board_label_0_11")
        self.horizontalLayout.addWidget(self.board_label_0_11)
        self.board_label_0_12 = QtWidgets.QLabel(self.widget)
        self.board_label_0_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_12.setText("")
        self.board_label_0_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_12.setObjectName("board_label_0_12")
        self.horizontalLayout.addWidget(self.board_label_0_12)
        self.board_label_0_13 = QtWidgets.QLabel(self.widget)
        self.board_label_0_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_0_13.setText("")
        self.board_label_0_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_13.setObjectName("board_label_0_13")
        self.horizontalLayout.addWidget(self.board_label_0_13)
        self.board_label_0_14 = QtWidgets.QLabel(self.widget)
        self.board_label_0_14.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_0_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_0_14.setObjectName("board_label_0_14")
        self.horizontalLayout.addWidget(self.board_label_0_14)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.board_label_1_0 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_0.setText("")
        self.board_label_1_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_0.setObjectName("board_label_1_0")
        self.horizontalLayout_2.addWidget(self.board_label_1_0)
        self.board_label_1_1 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_1.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_1_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_1.setObjectName("board_label_1_1")
        self.horizontalLayout_2.addWidget(self.board_label_1_1)
        self.board_label_1_2 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_2.setText("")
        self.board_label_1_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_2.setObjectName("board_label_1_2")
        self.horizontalLayout_2.addWidget(self.board_label_1_2)
        self.board_label_1_3 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_3.setText("")
        self.board_label_1_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_3.setObjectName("board_label_1_3")
        self.horizontalLayout_2.addWidget(self.board_label_1_3)
        self.board_label_1_4 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_4.setText("")
        self.board_label_1_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_4.setObjectName("board_label_1_4")
        self.horizontalLayout_2.addWidget(self.board_label_1_4)
        self.board_label_1_5 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_5.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_1_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_5.setObjectName("board_label_1_5")
        self.horizontalLayout_2.addWidget(self.board_label_1_5)
        self.board_label_1_6 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_6.setText("")
        self.board_label_1_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_6.setObjectName("board_label_1_6")
        self.horizontalLayout_2.addWidget(self.board_label_1_6)
        self.board_label_1_7 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_7.setText("")
        self.board_label_1_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_7.setObjectName("board_label_1_7")
        self.horizontalLayout_2.addWidget(self.board_label_1_7)
        self.board_label_1_8 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_8.setText("")
        self.board_label_1_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_8.setObjectName("board_label_1_8")
        self.horizontalLayout_2.addWidget(self.board_label_1_8)
        self.board_label_1_9 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_9.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_1_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_9.setObjectName("board_label_1_9")
        self.horizontalLayout_2.addWidget(self.board_label_1_9)
        self.board_label_1_10 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_10.setText("")
        self.board_label_1_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_10.setObjectName("board_label_1_10")
        self.horizontalLayout_2.addWidget(self.board_label_1_10)
        self.board_label_1_11 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_11.setText("")
        self.board_label_1_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_11.setObjectName("board_label_1_11")
        self.horizontalLayout_2.addWidget(self.board_label_1_11)
        self.board_label_1_12 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_12.setText("")
        self.board_label_1_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_12.setObjectName("board_label_1_12")
        self.horizontalLayout_2.addWidget(self.board_label_1_12)
        self.board_label_1_13 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_13.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_1_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_13.setObjectName("board_label_1_13")
        self.horizontalLayout_2.addWidget(self.board_label_1_13)
        self.board_label_1_14 = QtWidgets.QLabel(self.widget_2)
        self.board_label_1_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_1_14.setText("")
        self.board_label_1_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_1_14.setObjectName("board_label_1_14")
        self.horizontalLayout_2.addWidget(self.board_label_1_14)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.board_label_2_0 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_0.setText("")
        self.board_label_2_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_0.setObjectName("board_label_2_0")
        self.horizontalLayout_3.addWidget(self.board_label_2_0)
        self.board_label_2_1 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_1.setText("")
        self.board_label_2_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_1.setObjectName("board_label_2_1")
        self.horizontalLayout_3.addWidget(self.board_label_2_1)
        self.board_label_2_2 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_2.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_2_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_2.setObjectName("board_label_2_2")
        self.horizontalLayout_3.addWidget(self.board_label_2_2)
        self.board_label_2_3 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_3.setText("")
        self.board_label_2_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_3.setObjectName("board_label_2_3")
        self.horizontalLayout_3.addWidget(self.board_label_2_3)
        self.board_label_2_4 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_4.setText("")
        self.board_label_2_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_4.setObjectName("board_label_2_4")
        self.horizontalLayout_3.addWidget(self.board_label_2_4)
        self.board_label_2_5 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_5.setText("")
        self.board_label_2_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_5.setObjectName("board_label_2_5")
        self.horizontalLayout_3.addWidget(self.board_label_2_5)
        self.board_label_2_6 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_6.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_2_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_6.setObjectName("board_label_2_6")
        self.horizontalLayout_3.addWidget(self.board_label_2_6)
        self.board_label_2_7 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_7.setText("")
        self.board_label_2_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_7.setObjectName("board_label_2_7")
        self.horizontalLayout_3.addWidget(self.board_label_2_7)
        self.board_label_2_8 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_8.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_2_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_8.setObjectName("board_label_2_8")
        self.horizontalLayout_3.addWidget(self.board_label_2_8)
        self.board_label_2_9 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_9.setText("")
        self.board_label_2_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_9.setObjectName("board_label_2_9")
        self.horizontalLayout_3.addWidget(self.board_label_2_9)
        self.board_label_2_10 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_10.setText("")
        self.board_label_2_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_10.setObjectName("board_label_2_10")
        self.horizontalLayout_3.addWidget(self.board_label_2_10)
        self.board_label_2_11 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_11.setText("")
        self.board_label_2_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_11.setObjectName("board_label_2_11")
        self.horizontalLayout_3.addWidget(self.board_label_2_11)
        self.board_label_2_12 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_12.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_2_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_12.setObjectName("board_label_2_12")
        self.horizontalLayout_3.addWidget(self.board_label_2_12)
        self.board_label_2_13 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_13.setText("")
        self.board_label_2_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_13.setObjectName("board_label_2_13")
        self.horizontalLayout_3.addWidget(self.board_label_2_13)
        self.board_label_2_14 = QtWidgets.QLabel(self.widget_3)
        self.board_label_2_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_2_14.setText("")
        self.board_label_2_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_2_14.setObjectName("board_label_2_14")
        self.horizontalLayout_3.addWidget(self.board_label_2_14)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.board_label_3_0 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_0.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_3_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_0.setObjectName("board_label_3_0")
        self.horizontalLayout_4.addWidget(self.board_label_3_0)
        self.board_label_3_1 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_1.setText("")
        self.board_label_3_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_1.setObjectName("board_label_3_1")
        self.horizontalLayout_4.addWidget(self.board_label_3_1)
        self.board_label_3_2 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_2.setText("")
        self.board_label_3_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_2.setObjectName("board_label_3_2")
        self.horizontalLayout_4.addWidget(self.board_label_3_2)
        self.board_label_3_3 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_3.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_3_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_3.setObjectName("board_label_3_3")
        self.horizontalLayout_4.addWidget(self.board_label_3_3)
        self.board_label_3_4 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_4.setText("")
        self.board_label_3_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_4.setObjectName("board_label_3_4")
        self.horizontalLayout_4.addWidget(self.board_label_3_4)
        self.board_label_3_5 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_5.setText("")
        self.board_label_3_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_5.setObjectName("board_label_3_5")
        self.horizontalLayout_4.addWidget(self.board_label_3_5)
        self.board_label_3_6 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_6.setText("")
        self.board_label_3_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_6.setObjectName("board_label_3_6")
        self.horizontalLayout_4.addWidget(self.board_label_3_6)
        self.board_label_3_7 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_7.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_3_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_7.setObjectName("board_label_3_7")
        self.horizontalLayout_4.addWidget(self.board_label_3_7)
        self.board_label_3_8 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_8.setText("")
        self.board_label_3_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_8.setObjectName("board_label_3_8")
        self.horizontalLayout_4.addWidget(self.board_label_3_8)
        self.board_label_3_9 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_9.setText("")
        self.board_label_3_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_9.setObjectName("board_label_3_9")
        self.horizontalLayout_4.addWidget(self.board_label_3_9)
        self.board_label_3_10 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_10.setText("")
        self.board_label_3_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_10.setObjectName("board_label_3_10")
        self.horizontalLayout_4.addWidget(self.board_label_3_10)
        self.board_label_3_11 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_11.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_3_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_11.setObjectName("board_label_3_11")
        self.horizontalLayout_4.addWidget(self.board_label_3_11)
        self.board_label_3_12 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_12.setText("")
        self.board_label_3_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_12.setObjectName("board_label_3_12")
        self.horizontalLayout_4.addWidget(self.board_label_3_12)
        self.board_label_3_13 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_3_13.setText("")
        self.board_label_3_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_13.setObjectName("board_label_3_13")
        self.horizontalLayout_4.addWidget(self.board_label_3_13)
        self.board_label_3_14 = QtWidgets.QLabel(self.widget_5)
        self.board_label_3_14.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_3_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_3_14.setObjectName("board_label_3_14")
        self.horizontalLayout_4.addWidget(self.board_label_3_14)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.board_label_4_0 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_0.setText("")
        self.board_label_4_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_0.setObjectName("board_label_4_0")
        self.horizontalLayout_5.addWidget(self.board_label_4_0)
        self.board_label_4_1 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_1.setText("")
        self.board_label_4_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_1.setObjectName("board_label_4_1")
        self.horizontalLayout_5.addWidget(self.board_label_4_1)
        self.board_label_4_2 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_2.setText("")
        self.board_label_4_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_2.setObjectName("board_label_4_2")
        self.horizontalLayout_5.addWidget(self.board_label_4_2)
        self.board_label_4_3 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_3.setText("")
        self.board_label_4_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_3.setObjectName("board_label_4_3")
        self.horizontalLayout_5.addWidget(self.board_label_4_3)
        self.board_label_4_4 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_4.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_4_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_4.setObjectName("board_label_4_4")
        self.horizontalLayout_5.addWidget(self.board_label_4_4)
        self.board_label_4_5 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_5.setText("")
        self.board_label_4_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_5.setObjectName("board_label_4_5")
        self.horizontalLayout_5.addWidget(self.board_label_4_5)
        self.board_label_4_6 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_6.setText("")
        self.board_label_4_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_6.setObjectName("board_label_4_6")
        self.horizontalLayout_5.addWidget(self.board_label_4_6)
        self.board_label_4_7 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_7.setText("")
        self.board_label_4_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_7.setObjectName("board_label_4_7")
        self.horizontalLayout_5.addWidget(self.board_label_4_7)
        self.board_label_4_8 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_8.setText("")
        self.board_label_4_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_8.setObjectName("board_label_4_8")
        self.horizontalLayout_5.addWidget(self.board_label_4_8)
        self.board_label_4_9 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_9.setText("")
        self.board_label_4_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_9.setObjectName("board_label_4_9")
        self.horizontalLayout_5.addWidget(self.board_label_4_9)
        self.board_label_4_10 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_10.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_4_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_10.setObjectName("board_label_4_10")
        self.horizontalLayout_5.addWidget(self.board_label_4_10)
        self.board_label_4_11 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_11.setText("")
        self.board_label_4_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_11.setObjectName("board_label_4_11")
        self.horizontalLayout_5.addWidget(self.board_label_4_11)
        self.board_label_4_12 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_12.setText("")
        self.board_label_4_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_12.setObjectName("board_label_4_12")
        self.horizontalLayout_5.addWidget(self.board_label_4_12)
        self.board_label_4_13 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_13.setText("")
        self.board_label_4_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_13.setObjectName("board_label_4_13")
        self.horizontalLayout_5.addWidget(self.board_label_4_13)
        self.board_label_4_14 = QtWidgets.QLabel(self.widget_6)
        self.board_label_4_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_4_14.setText("")
        self.board_label_4_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_4_14.setObjectName("board_label_4_14")
        self.horizontalLayout_5.addWidget(self.board_label_4_14)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.board_label_5_0 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_0.setText("")
        self.board_label_5_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_0.setObjectName("board_label_5_0")
        self.horizontalLayout_6.addWidget(self.board_label_5_0)
        self.board_label_5_1 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_1.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_5_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_1.setObjectName("board_label_5_1")
        self.horizontalLayout_6.addWidget(self.board_label_5_1)
        self.board_label_5_2 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_2.setText("")
        self.board_label_5_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_2.setObjectName("board_label_5_2")
        self.horizontalLayout_6.addWidget(self.board_label_5_2)
        self.board_label_5_3 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_3.setText("")
        self.board_label_5_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_3.setObjectName("board_label_5_3")
        self.horizontalLayout_6.addWidget(self.board_label_5_3)
        self.board_label_5_4 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_4.setText("")
        self.board_label_5_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_4.setObjectName("board_label_5_4")
        self.horizontalLayout_6.addWidget(self.board_label_5_4)
        self.board_label_5_5 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_5.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_5_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_5.setObjectName("board_label_5_5")
        self.horizontalLayout_6.addWidget(self.board_label_5_5)
        self.board_label_5_6 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_6.setText("")
        self.board_label_5_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_6.setObjectName("board_label_5_6")
        self.horizontalLayout_6.addWidget(self.board_label_5_6)
        self.board_label_5_7 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_7.setText("")
        self.board_label_5_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_7.setObjectName("board_label_5_7")
        self.horizontalLayout_6.addWidget(self.board_label_5_7)
        self.board_label_5_8 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_8.setText("")
        self.board_label_5_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_8.setObjectName("board_label_5_8")
        self.horizontalLayout_6.addWidget(self.board_label_5_8)
        self.board_label_5_9 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_9.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_5_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_9.setObjectName("board_label_5_9")
        self.horizontalLayout_6.addWidget(self.board_label_5_9)
        self.board_label_5_10 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_10.setText("")
        self.board_label_5_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_10.setObjectName("board_label_5_10")
        self.horizontalLayout_6.addWidget(self.board_label_5_10)
        self.board_label_5_11 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_11.setText("")
        self.board_label_5_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_11.setObjectName("board_label_5_11")
        self.horizontalLayout_6.addWidget(self.board_label_5_11)
        self.board_label_5_12 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_12.setText("")
        self.board_label_5_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_12.setObjectName("board_label_5_12")
        self.horizontalLayout_6.addWidget(self.board_label_5_12)
        self.board_label_5_13 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_13.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_5_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_13.setObjectName("board_label_5_13")
        self.horizontalLayout_6.addWidget(self.board_label_5_13)
        self.board_label_5_14 = QtWidgets.QLabel(self.widget_7)
        self.board_label_5_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_5_14.setText("")
        self.board_label_5_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_5_14.setObjectName("board_label_5_14")
        self.horizontalLayout_6.addWidget(self.board_label_5_14)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.board_label_6_0 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_0.setText("")
        self.board_label_6_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_0.setObjectName("board_label_6_0")
        self.horizontalLayout_7.addWidget(self.board_label_6_0)
        self.board_label_6_1 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_1.setText("")
        self.board_label_6_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_1.setObjectName("board_label_6_1")
        self.horizontalLayout_7.addWidget(self.board_label_6_1)
        self.board_label_6_2 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_2.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_6_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_2.setObjectName("board_label_6_2")
        self.horizontalLayout_7.addWidget(self.board_label_6_2)
        self.board_label_6_3 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_3.setText("")
        self.board_label_6_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_3.setObjectName("board_label_6_3")
        self.horizontalLayout_7.addWidget(self.board_label_6_3)
        self.board_label_6_4 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_4.setText("")
        self.board_label_6_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_4.setObjectName("board_label_6_4")

        self.horizontalLayout_7.addWidget(self.board_label_6_4)
        self.board_label_6_5 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_5.setText("")
        self.board_label_6_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_5.setObjectName("board_label_6_5")
        self.horizontalLayout_7.addWidget(self.board_label_6_5)
        self.board_label_6_6 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_6.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_6_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_6.setObjectName("board_label_6_6")
        self.horizontalLayout_7.addWidget(self.board_label_6_6)
        self.board_label_6_7 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_7.setText("")
        self.board_label_6_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_7.setObjectName("board_label_6_7")
        self.horizontalLayout_7.addWidget(self.board_label_6_7)
        self.board_label_6_8 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_8.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_6_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_8.setObjectName("board_label_6_8")
        self.horizontalLayout_7.addWidget(self.board_label_6_8)
        self.board_label_6_9 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_9.setText("")
        self.board_label_6_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_9.setObjectName("board_label_6_9")
        self.horizontalLayout_7.addWidget(self.board_label_6_9)
        self.board_label_6_10 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_10.setText("")
        self.board_label_6_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_10.setObjectName("board_label_6_10")
        self.horizontalLayout_7.addWidget(self.board_label_6_10)
        self.board_label_6_11 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_11.setText("")
        self.board_label_6_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_11.setObjectName("board_label_6_11")
        self.horizontalLayout_7.addWidget(self.board_label_6_11)
        self.board_label_6_12 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_12.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_6_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_12.setObjectName("board_label_6_12")
        self.horizontalLayout_7.addWidget(self.board_label_6_12)
        self.board_label_6_13 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_13.setText("")
        self.board_label_6_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_13.setObjectName("board_label_6_13")
        self.horizontalLayout_7.addWidget(self.board_label_6_13)
        self.board_label_6_14 = QtWidgets.QLabel(self.widget_8)
        self.board_label_6_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_6_14.setText("")
        self.board_label_6_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_6_14.setObjectName("board_label_6_14")
        self.horizontalLayout_7.addWidget(self.board_label_6_14)
        self.verticalLayout.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_4)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.board_label_7_0 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_0.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_7_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_0.setObjectName("board_label_7_0")
        self.horizontalLayout_8.addWidget(self.board_label_7_0)
        self.board_label_7_1 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_1.setText("")
        self.board_label_7_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_1.setObjectName("board_label_7_1")
        self.horizontalLayout_8.addWidget(self.board_label_7_1)
        self.board_label_7_2 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_2.setText("")
        self.board_label_7_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_2.setObjectName("board_label_7_2")
        self.horizontalLayout_8.addWidget(self.board_label_7_2)
        self.board_label_7_3 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_3.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_7_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_3.setObjectName("board_label_7_3")
        self.horizontalLayout_8.addWidget(self.board_label_7_3)
        self.board_label_7_4 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_4.setText("")
        self.board_label_7_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_4.setObjectName("board_label_7_4")
        self.horizontalLayout_8.addWidget(self.board_label_7_4)
        self.board_label_7_5 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_5.setText("")
        self.board_label_7_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_5.setObjectName("board_label_7_5")
        self.horizontalLayout_8.addWidget(self.board_label_7_5)
        self.board_label_7_6 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_6.setText("")
        self.board_label_7_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_6.setObjectName("board_label_7_6")
        self.horizontalLayout_8.addWidget(self.board_label_7_6)
        self.board_label_7_7 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_7.setObjectName("board_label_7_7")
        self.board_label_7_7.setStyleSheet("background-color:\"lightpink\"\n""")
        self.horizontalLayout_8.addWidget(self.board_label_7_7)
        self.board_label_7_8 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_8.setText("")
        self.board_label_7_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_8.setObjectName("board_label_7_8")
        self.horizontalLayout_8.addWidget(self.board_label_7_8)
        self.board_label_7_9 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_9.setText("")
        self.board_label_7_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_9.setObjectName("board_label_7_9")
        self.horizontalLayout_8.addWidget(self.board_label_7_9)
        self.board_label_7_10 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_10.setText("")
        self.board_label_7_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_10.setObjectName("board_label_7_10")
        self.horizontalLayout_8.addWidget(self.board_label_7_10)
        self.board_label_7_11 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_11.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_7_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_11.setObjectName("board_label_7_11")
        self.horizontalLayout_8.addWidget(self.board_label_7_11)
        self.board_label_7_12 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_12.setText("")
        self.board_label_7_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_12.setObjectName("board_label_7_12")
        self.horizontalLayout_8.addWidget(self.board_label_7_12)
        self.board_label_7_13 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_7_13.setText("")
        self.board_label_7_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_13.setObjectName("board_label_7_13")
        self.horizontalLayout_8.addWidget(self.board_label_7_13)
        self.board_label_7_14 = QtWidgets.QLabel(self.widget_9)
        self.board_label_7_14.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_7_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_7_14.setObjectName("board_label_7_14")
        self.horizontalLayout_8.addWidget(self.board_label_7_14)
        self.verticalLayout.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_4)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.board_label_8_0 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_0.setText("")
        self.board_label_8_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_0.setObjectName("board_label_8_0")
        self.horizontalLayout_9.addWidget(self.board_label_8_0)
        self.board_label_8_1 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_1.setText("")
        self.board_label_8_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_1.setObjectName("board_label_8_1")
        self.horizontalLayout_9.addWidget(self.board_label_8_1)
        self.board_label_8_2 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_2.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_8_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_2.setObjectName("board_label_8_2")
        self.horizontalLayout_9.addWidget(self.board_label_8_2)
        self.board_label_8_3 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_3.setText("")
        self.board_label_8_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_3.setObjectName("board_label_8_3")
        self.horizontalLayout_9.addWidget(self.board_label_8_3)
        self.board_label_8_4 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_4.setText("")
        self.board_label_8_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_4.setObjectName("board_label_8_4")
        self.horizontalLayout_9.addWidget(self.board_label_8_4)
        self.board_label_8_5 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_5.setText("")
        self.board_label_8_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_5.setObjectName("board_label_8_5")
        self.horizontalLayout_9.addWidget(self.board_label_8_5)
        self.board_label_8_6 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_6.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_8_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_6.setObjectName("board_label_8_6")
        self.horizontalLayout_9.addWidget(self.board_label_8_6)
        self.board_label_8_7 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_7.setText("")
        self.board_label_8_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_7.setObjectName("board_label_8_7")
        self.horizontalLayout_9.addWidget(self.board_label_8_7)
        self.board_label_8_8 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_8.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_8_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_8.setObjectName("board_label_8_8")
        self.horizontalLayout_9.addWidget(self.board_label_8_8)
        self.board_label_8_9 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_9.setText("")
        self.board_label_8_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_9.setObjectName("board_label_8_9")
        self.horizontalLayout_9.addWidget(self.board_label_8_9)
        self.board_label_8_10 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_10.setText("")
        self.board_label_8_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_10.setObjectName("board_label_8_10")
        self.horizontalLayout_9.addWidget(self.board_label_8_10)
        self.board_label_8_11 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_11.setText("")
        self.board_label_8_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_11.setObjectName("board_label_8_11")
        self.horizontalLayout_9.addWidget(self.board_label_8_11)
        self.board_label_8_12 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_12.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_8_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_12.setObjectName("board_label_8_12")
        self.horizontalLayout_9.addWidget(self.board_label_8_12)
        self.board_label_8_13 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_13.setText("")
        self.board_label_8_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_13.setObjectName("board_label_8_13")
        self.horizontalLayout_9.addWidget(self.board_label_8_13)
        self.board_label_8_14 = QtWidgets.QLabel(self.widget_10)
        self.board_label_8_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_8_14.setText("")
        self.board_label_8_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_8_14.setObjectName("board_label_8_14")
        self.horizontalLayout_9.addWidget(self.board_label_8_14)
        self.verticalLayout.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.widget_4)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.board_label_9_0 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_0.setText("")
        self.board_label_9_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_0.setObjectName("board_label_9_0")
        self.horizontalLayout_10.addWidget(self.board_label_9_0)
        self.board_label_9_1 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_1.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_9_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_1.setObjectName("board_label_9_1")
        self.horizontalLayout_10.addWidget(self.board_label_9_1)
        self.board_label_9_2 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_2.setText("")
        self.board_label_9_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_2.setObjectName("board_label_9_2")
        self.horizontalLayout_10.addWidget(self.board_label_9_2)
        self.board_label_9_3 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_3.setText("")
        self.board_label_9_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_3.setObjectName("board_label_9_3")
        self.horizontalLayout_10.addWidget(self.board_label_9_3)
        self.board_label_9_4 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_4.setText("")
        self.board_label_9_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_4.setObjectName("board_label_9_4")
        self.horizontalLayout_10.addWidget(self.board_label_9_4)
        self.board_label_9_5 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_5.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_9_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_5.setObjectName("board_label_9_5")
        self.horizontalLayout_10.addWidget(self.board_label_9_5)
        self.board_label_9_6 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_6.setText("")
        self.board_label_9_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_6.setObjectName("board_label_9_6")
        self.horizontalLayout_10.addWidget(self.board_label_9_6)
        self.board_label_9_7 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_7.setText("")
        self.board_label_9_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_7.setObjectName("board_label_9_7")
        self.horizontalLayout_10.addWidget(self.board_label_9_7)
        self.board_label_9_8 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_8.setText("")
        self.board_label_9_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_8.setObjectName("board_label_9_8")
        self.horizontalLayout_10.addWidget(self.board_label_9_8)
        self.board_label_9_9 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_9.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_9_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_9.setObjectName("board_label_9_9")
        self.horizontalLayout_10.addWidget(self.board_label_9_9)
        self.board_label_9_10 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_10.setText("")
        self.board_label_9_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_10.setObjectName("board_label_9_10")
        self.horizontalLayout_10.addWidget(self.board_label_9_10)
        self.board_label_9_11 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_11.setText("")
        self.board_label_9_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_11.setObjectName("board_label_9_11")
        self.horizontalLayout_10.addWidget(self.board_label_9_11)
        self.board_label_9_12 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_12.setText("")
        self.board_label_9_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_12.setObjectName("board_label_9_12")
        self.horizontalLayout_10.addWidget(self.board_label_9_12)
        self.board_label_9_13 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_13.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_9_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_13.setObjectName("board_label_9_13")
        self.horizontalLayout_10.addWidget(self.board_label_9_13)
        self.board_label_9_14 = QtWidgets.QLabel(self.widget_11)
        self.board_label_9_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_9_14.setText("")
        self.board_label_9_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_9_14.setObjectName("board_label_9_14")
        self.horizontalLayout_10.addWidget(self.board_label_9_14)
        self.verticalLayout.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.board_label_10_0 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_0.setText("")
        self.board_label_10_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_0.setObjectName("board_label_10_0")
        self.horizontalLayout_11.addWidget(self.board_label_10_0)
        self.board_label_10_1 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_1.setText("")
        self.board_label_10_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_1.setObjectName("board_label_10_1")
        self.horizontalLayout_11.addWidget(self.board_label_10_1)
        self.board_label_10_2 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_2.setText("")
        self.board_label_10_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_2.setObjectName("board_label_10_2")
        self.horizontalLayout_11.addWidget(self.board_label_10_2)
        self.board_label_10_3 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_3.setText("")
        self.board_label_10_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_3.setObjectName("board_label_10_3")
        self.horizontalLayout_11.addWidget(self.board_label_10_3)
        self.board_label_10_4 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_4.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_10_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_4.setObjectName("board_label_10_4")
        self.horizontalLayout_11.addWidget(self.board_label_10_4)
        self.board_label_10_5 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_5.setText("")
        self.board_label_10_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_5.setObjectName("board_label_10_5")
        self.horizontalLayout_11.addWidget(self.board_label_10_5)
        self.board_label_10_6 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_6.setText("")
        self.board_label_10_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_6.setObjectName("board_label_10_6")
        self.horizontalLayout_11.addWidget(self.board_label_10_6)
        self.board_label_10_7 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_7.setText("")
        self.board_label_10_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_7.setObjectName("board_label_10_7")
        self.horizontalLayout_11.addWidget(self.board_label_10_7)
        self.board_label_10_8 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_8.setText("")
        self.board_label_10_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_8.setObjectName("board_label_10_8")
        self.horizontalLayout_11.addWidget(self.board_label_10_8)
        self.board_label_10_9 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_9.setText("")
        self.board_label_10_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_9.setObjectName("board_label_10_9")
        self.horizontalLayout_11.addWidget(self.board_label_10_9)
        self.board_label_10_10 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_10.setStyleSheet(
            "background-color:\"#ffdead\"\n""")
        self.board_label_10_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_10.setObjectName("board_label_10_10")
        self.horizontalLayout_11.addWidget(self.board_label_10_10)
        self.board_label_10_11 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_11.setText("")
        self.board_label_10_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_11.setObjectName("board_label_10_11")
        self.horizontalLayout_11.addWidget(self.board_label_10_11)
        self.board_label_10_12 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_12.setText("")
        self.board_label_10_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_12.setObjectName("board_label_10_12")
        self.horizontalLayout_11.addWidget(self.board_label_10_12)
        self.board_label_10_13 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_13.setText("")
        self.board_label_10_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_13.setObjectName("board_label_10_13")
        self.horizontalLayout_11.addWidget(self.board_label_10_13)
        self.board_label_10_14 = QtWidgets.QLabel(self.widget_12)
        self.board_label_10_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_10_14.setText("")
        self.board_label_10_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_10_14.setObjectName("board_label_10_14")
        self.horizontalLayout_11.addWidget(self.board_label_10_14)
        self.verticalLayout.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_4)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.board_label_11_0 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_0.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_11_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_0.setObjectName("board_label_11_0")
        self.horizontalLayout_12.addWidget(self.board_label_11_0)
        self.board_label_11_1 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_1.setText("")
        self.board_label_11_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_1.setObjectName("board_label_11_1")
        self.horizontalLayout_12.addWidget(self.board_label_11_1)
        self.board_label_11_2 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_2.setText("")
        self.board_label_11_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_2.setObjectName("board_label_11_2")
        self.horizontalLayout_12.addWidget(self.board_label_11_2)
        self.board_label_11_3 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_3.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_11_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_3.setObjectName("board_label_11_3")
        self.horizontalLayout_12.addWidget(self.board_label_11_3)
        self.board_label_11_4 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_4.setText("")
        self.board_label_11_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_4.setObjectName("board_label_11_4")
        self.horizontalLayout_12.addWidget(self.board_label_11_4)
        self.board_label_11_5 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_5.setText("")
        self.board_label_11_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_5.setObjectName("board_label_11_5")
        self.horizontalLayout_12.addWidget(self.board_label_11_5)
        self.board_label_11_6 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_6.setText("")
        self.board_label_11_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_6.setObjectName("board_label_11_6")
        self.horizontalLayout_12.addWidget(self.board_label_11_6)
        self.board_label_11_7 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_7.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_11_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_7.setObjectName("board_label_11_7")
        self.horizontalLayout_12.addWidget(self.board_label_11_7)
        self.board_label_11_8 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_8.setText("")
        self.board_label_11_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_8.setObjectName("board_label_11_8")
        self.horizontalLayout_12.addWidget(self.board_label_11_8)
        self.board_label_11_9 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_9.setText("")
        self.board_label_11_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_9.setObjectName("board_label_11_9")
        self.horizontalLayout_12.addWidget(self.board_label_11_9)
        self.board_label_11_10 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_10.setText("")
        self.board_label_11_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_10.setObjectName("board_label_11_10")
        self.horizontalLayout_12.addWidget(self.board_label_11_10)
        self.board_label_11_11 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_11.setStyleSheet(
            "background-color:\"#ffdead\"\n""")
        self.board_label_11_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_11.setObjectName("board_label_11_11")
        self.horizontalLayout_12.addWidget(self.board_label_11_11)
        self.board_label_11_12 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_12.setText("")
        self.board_label_11_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_12.setObjectName("board_label_11_12")
        self.horizontalLayout_12.addWidget(self.board_label_11_12)
        self.board_label_11_13 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_11_13.setText("")
        self.board_label_11_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_13.setObjectName("board_label_11_13")
        self.horizontalLayout_12.addWidget(self.board_label_11_13)
        self.board_label_11_14 = QtWidgets.QLabel(self.widget_13)
        self.board_label_11_14.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_11_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_11_14.setObjectName("board_label_11_14")
        self.horizontalLayout_12.addWidget(self.board_label_11_14)
        self.verticalLayout.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget_4)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.board_label_12_0 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_0.setText("")
        self.board_label_12_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_0.setObjectName("board_label_12_0")
        self.horizontalLayout_13.addWidget(self.board_label_12_0)
        self.board_label_12_1 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_1.setText("")
        self.board_label_12_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_1.setObjectName("board_label_12_1")
        self.horizontalLayout_13.addWidget(self.board_label_12_1)
        self.board_label_12_2 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_2.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_12_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_2.setObjectName("board_label_12_2")
        self.horizontalLayout_13.addWidget(self.board_label_12_2)
        self.board_label_12_3 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_3.setText("")
        self.board_label_12_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_3.setObjectName("board_label_12_3")
        self.horizontalLayout_13.addWidget(self.board_label_12_3)
        self.board_label_12_4 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_4.setText("")
        self.board_label_12_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_4.setObjectName("board_label_12_4")
        self.horizontalLayout_13.addWidget(self.board_label_12_4)
        self.board_label_12_5 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_5.setText("")
        self.board_label_12_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_5.setObjectName("board_label_12_5")
        self.horizontalLayout_13.addWidget(self.board_label_12_5)
        self.board_label_12_6 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_6.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_12_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_6.setObjectName("board_label_12_6")
        self.horizontalLayout_13.addWidget(self.board_label_12_6)
        self.board_label_12_7 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_7.setText("")
        self.board_label_12_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_7.setObjectName("board_label_12_7")
        self.horizontalLayout_13.addWidget(self.board_label_12_7)
        self.board_label_12_8 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_8.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_12_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_8.setObjectName("board_label_12_8")
        self.horizontalLayout_13.addWidget(self.board_label_12_8)
        self.board_label_12_9 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_9.setText("")
        self.board_label_12_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_9.setObjectName("board_label_12_9")
        self.horizontalLayout_13.addWidget(self.board_label_12_9)
        self.board_label_12_10 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_10.setText("")
        self.board_label_12_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_10.setObjectName("board_label_12_10")
        self.horizontalLayout_13.addWidget(self.board_label_12_10)
        self.board_label_12_11 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_11.setText("")
        self.board_label_12_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_11.setObjectName("board_label_12_11")
        self.horizontalLayout_13.addWidget(self.board_label_12_11)
        self.board_label_12_12 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_12.setStyleSheet(
            "background-color:\"#ffdead\"\n""")
        self.board_label_12_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_12.setObjectName("board_label_12_12")
        self.horizontalLayout_13.addWidget(self.board_label_12_12)
        self.board_label_12_13 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_13.setText("")
        self.board_label_12_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_13.setObjectName("board_label_12_13")
        self.horizontalLayout_13.addWidget(self.board_label_12_13)
        self.board_label_12_14 = QtWidgets.QLabel(self.widget_14)
        self.board_label_12_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_12_14.setText("")
        self.board_label_12_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_12_14.setObjectName("board_label_12_14")
        self.horizontalLayout_13.addWidget(self.board_label_12_14)
        self.verticalLayout.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(self.widget_4)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.board_label_13_0 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_0.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_0.setText("")
        self.board_label_13_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_0.setObjectName("board_label_13_0")
        self.horizontalLayout_14.addWidget(self.board_label_13_0)
        self.board_label_13_1 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_1.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_13_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_1.setObjectName("board_label_13_1")
        self.horizontalLayout_14.addWidget(self.board_label_13_1)
        self.board_label_13_2 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_2.setText("")
        self.board_label_13_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_2.setObjectName("board_label_13_2")
        self.horizontalLayout_14.addWidget(self.board_label_13_2)

        self.board_label_13_3 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_3.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_3.setText("")
        self.board_label_13_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_3.setObjectName("board_label_13_3")
        self.horizontalLayout_14.addWidget(self.board_label_13_3)
        self.board_label_13_4 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_4.setObjectName("board_label_13_4")
        self.horizontalLayout_14.addWidget(self.board_label_13_4)
        self.board_label_13_5 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_5.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_13_5.setText("")
        self.board_label_13_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_5.setObjectName("board_label_13_5")
        self.horizontalLayout_14.addWidget(self.board_label_13_5)
        self.board_label_13_6 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_6.setText("")
        self.board_label_13_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_6.setObjectName("board_label_13_6")
        self.horizontalLayout_14.addWidget(self.board_label_13_6)
        self.board_label_13_7 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_7.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_7.setText("")
        self.board_label_13_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_7.setObjectName("board_label_13_7")
        self.horizontalLayout_14.addWidget(self.board_label_13_7)
        self.board_label_13_8 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_8.setObjectName("board_label_13_8")
        self.horizontalLayout_14.addWidget(self.board_label_13_8)
        self.board_label_13_9 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_9.setStyleSheet("background-color:\"blue\"\n""")
        self.board_label_13_9.setText("")
        self.board_label_13_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_9.setObjectName("board_label_13_9")
        self.horizontalLayout_14.addWidget(self.board_label_13_9)
        self.board_label_13_10 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_10.setText("")
        self.board_label_13_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_10.setObjectName("board_label_13_10")
        self.horizontalLayout_14.addWidget(self.board_label_13_10)
        self.board_label_13_11 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_11.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_11.setText("")
        self.board_label_13_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_11.setObjectName("board_label_13_11")
        self.horizontalLayout_14.addWidget(self.board_label_13_11)
        self.board_label_13_12 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_12.setStyleSheet(
            "background-color:\"green\"\n""")
        self.board_label_13_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_12.setObjectName("board_label_13_12")
        self.horizontalLayout_14.addWidget(self.board_label_13_12)
        self.board_label_13_13 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_13.setStyleSheet("background-color:\"#ffdead\"\n""")
        self.board_label_13_13.setText("")
        self.board_label_13_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_13.setObjectName("board_label_13_13")
        self.horizontalLayout_14.addWidget(self.board_label_13_13)
        self.board_label_13_14 = QtWidgets.QLabel(self.widget_15)
        self.board_label_13_14.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_13_14.setText("")
        self.board_label_13_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_13_14.setObjectName("board_label_13_14")
        self.horizontalLayout_14.addWidget(self.board_label_13_14)
        self.verticalLayout.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.widget_4)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.board_label_14_0 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_0.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_14_0.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_0.setObjectName("board_label_14_0")
        self.horizontalLayout_15.addWidget(self.board_label_14_0)
        self.board_label_14_1 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_1.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_1.setText("")
        self.board_label_14_1.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_1.setObjectName("board_label_14_1")
        self.horizontalLayout_15.addWidget(self.board_label_14_1)
        self.board_label_14_2 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_2.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_2.setText("")
        self.board_label_14_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_2.setObjectName("board_label_14_2")
        self.horizontalLayout_15.addWidget(self.board_label_14_2)
        self.board_label_14_3 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_3.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_14_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_3.setObjectName("board_label_14_3")
        self.horizontalLayout_15.addWidget(self.board_label_14_3)
        self.board_label_14_4 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_4.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_4.setText("")
        self.board_label_14_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_4.setObjectName("board_label_14_4")
        self.horizontalLayout_15.addWidget(self.board_label_14_4)
        self.board_label_14_5 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_5.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_5.setText("")
        self.board_label_14_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_5.setObjectName("board_label_14_5")
        self.horizontalLayout_15.addWidget(self.board_label_14_5)
        self.board_label_14_6 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_6.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_6.setText("")
        self.board_label_14_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_6.setObjectName("board_label_14_6")
        self.horizontalLayout_15.addWidget(self.board_label_14_6)
        self.board_label_14_7 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_7.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_14_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_7.setObjectName("board_label_14_7")
        self.horizontalLayout_15.addWidget(self.board_label_14_7)
        self.board_label_14_8 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_8.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_8.setText("")
        self.board_label_14_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_8.setObjectName("board_label_14_8")
        self.horizontalLayout_15.addWidget(self.board_label_14_8)
        self.board_label_14_9 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_9.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_9.setText("")
        self.board_label_14_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_9.setObjectName("board_label_14_9")
        self.horizontalLayout_15.addWidget(self.board_label_14_9)
        self.board_label_14_10 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_10.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_10.setText("")
        self.board_label_14_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_10.setObjectName("board_label_14_10")
        self.horizontalLayout_15.addWidget(self.board_label_14_10)
        self.board_label_14_11 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_11.setStyleSheet(
            "background-color:\"lightblue\"\n""")
        self.board_label_14_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_11.setObjectName("board_label_14_11")
        self.horizontalLayout_15.addWidget(self.board_label_14_11)
        self.board_label_14_12 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_12.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_12.setText("")
        self.board_label_14_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_12.setObjectName("board_label_14_12")
        self.horizontalLayout_15.addWidget(self.board_label_14_12)
        self.board_label_14_13 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_13.setStyleSheet("background-color:\"green\"\n""")
        self.board_label_14_13.setText("")
        self.board_label_14_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_13.setObjectName("board_label_14_13")
        self.horizontalLayout_15.addWidget(self.board_label_14_13)
        self.board_label_14_14 = QtWidgets.QLabel(self.widget_16)
        self.board_label_14_14.setStyleSheet("background-color:\"red\"\n""")
        self.board_label_14_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.board_label_14_14.setObjectName("board_label_14_14")
        self.horizontalLayout_15.addWidget(self.board_label_14_14)
        self.verticalLayout.addWidget(self.widget_16)
        self.widget_18 = QtWidgets.QWidget(Form)
        self.widget_18.setGeometry(QtCore.QRect(661, 0, 211, 901))
        self.widget_18.setObjectName("widget_18")
        self.widget_18.setStyleSheet("background-color:\"lightblue\"\n""")

        self.how_many_points = QtWidgets.QLabel(self.widget_18)
        self.how_many_points.setGeometry(QtCore.QRect(40, 180, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.how_many_points.setFont(font)
        self.how_many_points.setObjectName("how_many_points")
        self.player_name = QtWidgets.QLabel(self.widget_18)
        self.player_name.setGeometry(QtCore.QRect(40, 150, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_name.setFont(font)
        self.player_name.setObjectName("player_name")
        self.currPlaying = QtWidgets.QLabel(self.widget_18)
        self.currPlaying.setGeometry(QtCore.QRect(40, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currPlaying.setFont(font)
        self.currPlaying.setObjectName("currPlaying")
        self.currPlaying.setText("Currently playing:")
        self.letters_left_TXT = QtWidgets.QLabel(self.widget_18)
        self.letters_left_TXT.setGeometry(QtCore.QRect(20, 720, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.letters_left_TXT.setFont(font)
        self.letters_left_TXT.setObjectName("letters_left_TXT")
        self.letters_left_TXT.setText("Letters left:")
        self.number_of_letters = QtWidgets.QLabel(self.widget_18)
        self.number_of_letters.setGeometry(QtCore.QRect(100, 720, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.number_of_letters.setFont(font)
        self.number_of_letters.setText("")
        self.number_of_letters.setObjectName("number_of_letters")
        self.logo = QtWidgets.QLabel(self.widget_18)
        self.logo.setGeometry(QtCore.QRect(6, 3, 201, 101))
        self.logo.setPixmap(QtGui.QPixmap('images/Scrabble-Logo-2_resized.png'))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.leaderboardButton = QtWidgets.QPushButton(self.widget_18)
        self.leaderboardButton.setGeometry(QtCore.QRect(50, 590, 111, 31))
        self.leaderboardButton.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.leaderboardButton.setObjectName("leaderboardButton")
        self.leaderboardButton.setText("Leaderboard")
        self.leaderboardButton.clicked.connect(self.clicked_leaderboard)

        self.helpButton = QtWidgets.QPushButton(self.widget_18)
        self.helpButton.setGeometry(QtCore.QRect(50, 650, 111, 31))
        self.helpButton.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.helpButton.setObjectName("helpButton")
        self.helpButton.setText("Help")
        self.helpButton.clicked.connect(self.clicked_help)

        self.clear = QtWidgets.QPushButton(self.widget_18)
        self.clear.setGeometry(QtCore.QRect(49, 300, 111, 31))
        self.clear.setObjectName("clear")
        self.clear.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.clear.clicked.connect(self.clicked_clear)

        self.confirm = QtWidgets.QPushButton(self.widget_18)
        self.confirm.setGeometry(QtCore.QRect(50, 240, 111, 31))
        self.confirm.setObjectName("confirm")
        self.confirm.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.confirm.setText("Confirm")
        self.confirm.clicked.connect(self.clicked_confirm)
        self.confirm.clicked.connect(self.safe_words)
        self.confirm.clicked.connect(self.check_to_kick_player)
        self.confirm.clicked.connect(self.change_player)
        # self.confirm.clicked.connect(self.kicked_player_pop)
        # self.confirm.clicked.connect(self.new_player_pop)

        self.frame = QtWidgets.QFrame(self.widget_18)
        self.frame.setGeometry(QtCore.QRect(30, 380, 151, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.change_letters = QtWidgets.QPushButton(self.frame)
        self.change_letters.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.change_letters.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.change_letters.setObjectName("change_letters")
        self.change_letters.setText("Change Letters")
        self.change_letters.clicked.connect(self.clicked_change_letters)
        self.change_letters.clicked.connect(self.clicked_clear)

        self.change_letters_confirm = QtWidgets.QPushButton(self.frame)
        self.change_letters_confirm.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.change_letters_confirm.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.change_letters_confirm.setObjectName("change_letters_confirm")
        self.change_letters_confirm.setText("Confirm")
        self.change_letters_confirm.clicked.connect(
            self.clicked_change_letters_confirm)
        # self.change_letters_confirm.clicked.connect(self.kicked_player_pop)
        # self.change_letters_confirm.clicked.connect(self.new_player_pop)

        self.change_letters_cancel = QtWidgets.QPushButton(self.frame)
        self.change_letters_cancel.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.change_letters_cancel.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.change_letters_cancel.setObjectName("change_letters_cancel")
        self.change_letters_cancel.setText("Cancel")
        self.change_letters_cancel.clicked.connect(
            self.clicked_change_letters_cancel)

        self.widget_17 = QtWidgets.QWidget(Form)
        self.widget_17.setGeometry(QtCore.QRect(0, 790, 661, 111))
        self.widget_17.setObjectName("widget_17")
        self.widget_17.setStyleSheet("background-color:\"lightblue\"\n""")

        self.pushButton1 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton1.setGeometry(QtCore.QRect(20, 10, 80, 81))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton1.clicked.connect(self.clicked_pushButton1)
        self.pushButton2 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton2.setGeometry(QtCore.QRect(115, 10, 80, 81))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton2.clicked.connect(self.clicked_pushButton2)
        self.pushButton3 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton3.setGeometry(QtCore.QRect(205, 10, 80, 81))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton3.clicked.connect(self.clicked_pushButton3)
        self.pushButton4 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton4.setGeometry(QtCore.QRect(295, 10, 80, 81))
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton4.clicked.connect(self.clicked_pushButton4)
        self.pushButton5 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton5.setGeometry(QtCore.QRect(385, 10, 80, 81))
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton5.clicked.connect(self.clicked_pushButton5)
        self.pushButton6 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton6.setGeometry(QtCore.QRect(475, 10, 80, 81))
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton6.clicked.connect(self.clicked_pushButton6)
        self.pushButton7 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton7.setGeometry(QtCore.QRect(565, 10, 80, 81))
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setStyleSheet("background-color:\"lightgrey\"\n""")
        self.pushButton7.clicked.connect(self.clicked_pushButton7)

        self.valid_move = False
        self.validity_rows_check = False
        self.validity_columns_check = False
        self.pass_first_move_check = 0
        #self.number_of_players = 4
        self.current_player = 0
        self.dict_players = {}
        self.new_letter = 0
        self.check_if_player_kicked = False
        self.number_players_start = self.number_of_players
        self.check_game_over = False

        self.letters_used = []
        self.coords_of_letters_used = []
        self.loaded_dictionary = Word.get_the_dictionary_for_words()

        self.managment_db = ManagementGeneralLeaderboard()
        self.board = Board()
        #self.bag = Bag()
        self.racks = Racks()
        self.letter_coordinates_dict = defaultdict(list)

        self.letter_to_board = ""

        self.players_to_db = {}  # do zrobienia na end game

        for i in range(self.number_of_players):
            self.dict_players[i] = self.racks.bag.generate_rack_for_player()
            self.dict_players[i].append(self.players[i].name)
            self.dict_players[i].append(self.players[i].score)
            self.dict_players[i].append(self.players[i].fails)
            self.dict_players[i].append(self.players[i].swapped)

        # self.letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
        #                     'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G',
        #                     'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M',
        #                     'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
        #                     'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V',
        #                     'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
        # random.shuffle(self.letter_list)
        # self.random_number = 0

        # self.dict_players = {}

        # for i in range(self.number_of_players):
        #     self.dict_players[i] = []
        #     for j in range(7):
        #         self.random_number = random.randint(0, len(self.letter_list)-1)
        #         self.dict_players[i].append(self.letter_list[self.random_number])
        #         self.letter_list.pop(self.random_number)
        #     self.dict_players[i].append(self.players_names[i])
        #     self.dict_players[i].append(0)

        print(self.dict_players)

        self.player_name.setText(self.dict_players[0][7])
        self.how_many_points.setText(str(self.dict_players[0][8]))

        self.pushButton1.setText(self.dict_players[0][0])
        self.pushButton2.setText(self.dict_players[0][1])
        self.pushButton3.setText(self.dict_players[0][2])
        self.pushButton4.setText(self.dict_players[0][3])
        self.pushButton5.setText(self.dict_players[0][4])
        self.pushButton6.setText(self.dict_players[0][5])
        self.pushButton7.setText(self.dict_players[0][6])

        self.number_of_letters.setText(str(self.racks.bag.get_size_of_bag()))

        self.actual_board = [['-' for i in range(15)] for j in range(15)]
        self.new_player_move_board = [
            ['-' for i in range(15)] for j in range(15)]
        self.check_in_which_move = [[0 for i in range(15)] for j in range(15)]
        self.board_labels = [[0 for i in range(15)] for j in range(15)]

        self.which_move = 1
        self.change_letters_check = 0

        self.pushButton1_check = 0
        self.pushButton2_check = 0
        self.pushButton3_check = 0
        self.pushButton4_check = 0
        self.pushButton5_check = 0
        self.pushButton6_check = 0
        self.pushButton7_check = 0

        self.pushButton1_used = 0
        self.pushButton2_used = 0
        self.pushButton3_used = 0
        self.pushButton4_used = 0
        self.pushButton5_used = 0
        self.pushButton6_used = 0
        self.pushButton7_used = 0

        self.buttons_to_change = {}
        self.number_buttons_to_change = 0

        self.dict_board_labels = {}

        self.players_sorted = []
        for i in range(self.number_of_players):
            self.players_sorted.append([self.dict_players[i][7], self.dict_players[i][8]])

        self.players_sorted.sort(key=lambda x: x[1])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        for i in range(15):
            for j in range(15):
                self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))] = \
                    [eval("self.board_label_" + str(i) + "_" + str(j)).text(),
                     eval("self.board_label_" + str(i) + "_" + str(j)).styleSheet(), i, j]

        for label in self.dict_board_labels:
            label.mousePressEvent = self.factory(
                label, self.dict_board_labels[label][2], self.dict_board_labels[label][3])

    def factory(self, label, i, j):
        def clicked_label(event):
            if self.change_letters_check == 0:
                if self.letter_to_board != "":
                    if label.styleSheet() != 'background-color:lightyellow':
                        label.setStyleSheet(
                            'background-color:lightyellow')
                        label.setText(self.letter_to_board)
                        self.new_player_move_board[i][j] = self.letter_to_board
                        self.check_in_which_move[i][j] = self.which_move

                        self.letters_used.append(self.letter_to_board)

                        self.coords_of_letters_used.append([i, j])

                        if self.pushButton1_check == 1:
                            self.pushButton1_used = 1
                            self.pushButton1.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton1_check = 0

                        if self.pushButton2_check == 1:
                            self.pushButton2_used = 1
                            self.pushButton2.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton2_check = 0

                        if self.pushButton3_check == 1:
                            self.pushButton3_used = 1
                            self.pushButton3.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton3_check = 0

                        if self.pushButton4_check == 1:
                            self.pushButton4_used = 1
                            self.pushButton4.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton4_check = 0

                        if self.pushButton5_check == 1:
                            self.pushButton5_used = 1
                            self.pushButton5.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton5_check = 0

                        if self.pushButton6_check == 1:
                            self.pushButton6_used = 1
                            self.pushButton6.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton6_check = 0

                        if self.pushButton7_check == 1:
                            self.pushButton7_used = 1
                            self.pushButton7.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton7_check = 0

        return clicked_label

    def clicked_confirm(self):
        if self.which_move == 1 or self.pass_first_move_check == 0:
            self.letter_coordinates_dict = self.board.place_letters(self.letters_used, self.coords_of_letters_used, self.new_player_move_board)
            self.valid_move, words_4_score = self.board.first_move(self.coords_of_letters_used, self.new_player_move_board, self.loaded_dictionary)
            if self.valid_move is True:
                self.pass_first_move_check = 1

        else:
            self.letter_coordinates_dict = self.board.place_letters(self.letters_used, self.coords_of_letters_used, self.new_player_move_board)
            self.validity_rows_check = self.board.check_validity_placement_rows(self.new_player_move_board)
            self.validity_columns_check = self.board.check_validity_placement_columns(self.new_player_move_board)

            if self.validity_rows_check is True and self.validity_columns_check is True:
                self.valid_move, words_4_score = self.board.check_words_from_board(self.loaded_dictionary, self.new_player_move_board)

        if self.valid_move is True and words_4_score != {}:
            self.dict_players[self.current_player][8] += self.board.get_score(words_4_score, self.new_player_move_board)
            self.players[self.current_player].score = self.dict_players[self.current_player][8]
            self.actual_board = self.new_player_move_board
            self.board.actual_board = self.actual_board
            self.board.create_sum_board_4_connection()

            self.dict_players[self.current_player][9] = 0
            del self.players[self.current_player].fails

            for i in range(15):
                for j in range(15):
                    self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))] = \
                        [eval("self.board_label_" + str(i) + "_" + str(j)).text(),
                        eval("self.board_label_" + str(i) + "_" + str(j)).styleSheet(), i, j]

        else:
            self.dict_players[self.current_player][9] += 1
            self.players[self.current_player].fails = 1

            for i in range(15):
                for j in range(15):
                    if self.check_in_which_move[i][j] == self.which_move:
                        self.new_player_move_board[i][j] = '-'
                        eval("self.board_label_" + str(i) + "_" + str(j)).setText(
                            self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))][0])

                        eval("self.board_label_" + str(i) + "_" + str(j)).setStyleSheet(
                            self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))][1])



        if self.valid_move is True:
            self.dict_players[self.current_player][10] = 0
            del self.players[self.current_player].swapped
            if self.pushButton1_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton1.setText(self.new_letter)
                self.dict_players[self.current_player][1] = self.new_letter

            if self.pushButton2_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton2.setText(self.new_letter) 
                self.dict_players[self.current_player][1] = self.new_letter

            if self.pushButton3_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton3.setText(self.new_letter)
                self.dict_players[self.current_player][2] = self.new_letter

            if self.pushButton4_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton4.setText(self.new_letter)
                self.dict_players[self.current_player][3] = self.new_letter

            if self.pushButton5_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton5.setText(self.new_letter)
                self.dict_players[self.current_player][4] = self.new_letter

            if self.pushButton6_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton6.setText(self.new_letter)
                self.dict_players[self.current_player][5] = self.new_letter

            if self.pushButton7_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.pushButton7.setText(self.new_letter)
                self.dict_players[self.current_player][6] = self.new_letter

        self.pushButton1_used = 0
        self.pushButton2_used = 0
        self.pushButton3_used = 0
        self.pushButton4_used = 0
        self.pushButton5_used = 0
        self.pushButton6_used = 0
        self.pushButton7_used = 0

        self.pushButton1_check = 0
        self.pushButton2_check = 0
        self.pushButton3_check = 0
        self.pushButton4_check = 0
        self.pushButton5_check = 0
        self.pushButton6_check = 0
        self.pushButton7_check = 0

        self.pushButton1.setStyleSheet('background-color:lightgrey')
        self.pushButton2.setStyleSheet('background-color:lightgrey')
        self.pushButton3.setStyleSheet('background-color:lightgrey')
        self.pushButton4.setStyleSheet('background-color:lightgrey')
        self.pushButton5.setStyleSheet('background-color:lightgrey')
        self.pushButton6.setStyleSheet('background-color:lightgrey')
        self.pushButton7.setStyleSheet('background-color:lightgrey')

        self.letter_to_board = ""

        self.valid_move = False

        self.number_of_letters.setText(str(self.racks.bag.get_size_of_bag()))
        self.letters_used.clear()
        self.coords_of_letters_used.clear()

        self.which_move += 1

        # tu trzeba zrobic sprawdzenie boardu i wtedy:
        # for i in range(15):
        #         for j in range(15):
        #                 self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))] = \
        #                 [eval("self.board_label_" + str(i) + "_" + str(j)).text(), eval("self.board_label_" + str(i) + "_" + str(j)).styleSheet()]

    def clicked_clear(self):
        self.letters_used.clear()
        self.coords_of_letters_used.clear()
        for i in range(15):
            for j in range(15):
                if self.check_in_which_move[i][j] == self.which_move:
                    self.new_player_move_board[i][j] = '-'
                    eval("self.board_label_" + str(i) + "_" + str(j)).setText(
                        self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))][0])

                    eval("self.board_label_" + str(i) + "_" + str(j)).setStyleSheet(
                        self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))][1])

                    if self.pushButton1_used == 1:
                        self.pushButton1_used = 0
                        self.pushButton1.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton1_check = 0

                    if self.pushButton2_used == 1:
                        self.pushButton2_used = 0
                        self.pushButton2.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton2_check = 0

                    if self.pushButton3_used == 1:
                        self.pushButton3_used = 0
                        self.pushButton3.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton3_check = 0

                    if self.pushButton4_used == 1:
                        self.pushButton4_used = 0
                        self.pushButton4.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton4_check = 0

                    if self.pushButton5_used == 1:
                        self.pushButton5_used = 0
                        self.pushButton5.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton5_check = 0

                    if self.pushButton6_used == 1:
                        self.pushButton6_used = 0
                        self.pushButton6.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton6_check = 0

                    if self.pushButton7_used == 1:
                        self.pushButton7_used = 0
                        self.pushButton7.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton7_check = 0

    def clicked_change_letters(self):
        self.change_letters_check = 1
        self.change_letters.setStyleSheet("background-color:\"red\"\n""")

    def clicked_change_letters_cancel(self):
        self.change_letters_check = 0
        self.change_letters.setStyleSheet("background-color:\"lightgrey\"\n""")

    def clicked_change_letters_confirm(self):
        if self.change_letters_check == 1:
            self.temp = 0

            if self.pushButton1_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton1_check = 0
                self.buttons_to_change[self.temp] = self.pushButton1
                self.temp += 1

            if self.pushButton2_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton2_check = 0
                self.buttons_to_change[self.temp] = self.pushButton2
                self.temp += 1

            if self.pushButton3_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton3_check = 0
                self.buttons_to_change[self.temp] = self.pushButton3
                self.temp += 1

            if self.pushButton4_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton4_check = 0
                self.buttons_to_change[self.temp] = self.pushButton4
                self.temp += 1

            if self.pushButton5_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton5_check = 0
                self.buttons_to_change[self.temp] = self.pushButton5
                self.temp += 1

            if self.pushButton6_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton6_check = 0
                self.buttons_to_change[self.temp] = self.pushButton6
                self.temp += 1

            if self.pushButton7_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton7_check = 0
                self.buttons_to_change[self.temp] = self.pushButton7
                self.temp += 1

            if self.number_buttons_to_change <= self.racks.bag.get_size_of_bag():
                for i in self.buttons_to_change:
                    # self.random_number = random.randint(
                    #     0, len(self.letter_list)-1)
                    # self.buttons_to_change[i].setText(
                    #     self.letter_list[self.random_number])

                    # self.letter_list.pop(self.random_number)
                    self.letter_to_swap = self.buttons_to_change[i].text()
                    aux_letter = self.racks.bag.swap_letters(self.letter_to_swap)
                    self.buttons_to_change[i].setText(aux_letter)
                    self.buttons_to_change[i].setStyleSheet(
                        "background-color:\"lightgrey\"\n""")

            self.change_letters.setStyleSheet(
                "background-color:\"lightgrey\"\n""")
            self.change_letters_check = 0
            self.which_move += 1
            self.number_of_letters.setText(str(self.racks.bag.get_size_of_bag()))

            self.dict_players[self.current_player][10] += 1
            self.players[self.current_player].swapped = 1

            self.safe_words()
            self.check_to_kick_player()
            self.change_player()

    def check_to_kick_player(self):
        letter_helper = self.dict_players[self.current_player]
        self.players[self.current_player].rack = [letter_helper[0], letter_helper[1], letter_helper[2], \
                                                  letter_helper[3], letter_helper[4], letter_helper[5], \
                                                  letter_helper[6]]
        if self.dict_players[self.current_player][9] == 2 or self.dict_players[self.current_player][10] == 3:

            self.name_kicked_player = self.dict_players[self.current_player][7]

            self.players_to_db[self.dict_players[self.current_player][7]] = self.dict_players[self.current_player][8]
            print(self.players_to_db)

            self.dict_players.pop(self.current_player)
            self.number_of_players -= 1

            self.check_if_player_kicked = True

        else:
            self.check_if_player_kicked = False

    def change_player(self):
        if self.racks.bag.get_size_of_bag() < 7:
            for key in self.dict_players:
                self.players_to_db[self.dict_players.get(key)[7]] = self.dict_players.get(key)[8]

            self.managment_db.insert_db(self.players_to_db)
            self.game_over()

        else:
            if self.check_if_player_kicked is True:
                for i in range(self.number_of_players + 1):
                    if i in self.dict_players:
                        pass

                    else:
                        for j in range(self.number_of_players - i):
                            self.dict_players[i+j] = self.dict_players.pop(i+j+1)

            if self.number_of_players == 1:
                print(self.dict_players)
                self.players_to_db[self.dict_players[0][7]] = self.dict_players[0][8]
                self.managment_db.insert_db(self.players_to_db)
                self.game_over()

            elif self.number_of_players != 0:
                self.players_sorted = []

                for i in range(self.number_of_players):
                    self.players_sorted.append([self.dict_players[i][7], self.dict_players[i][8]])

                self.players_sorted.sort(key=lambda x: x[1])

                if self.check_if_player_kicked is True:
                    self.kicked_player_pop()
                else:
                    self.new_player_pop()

                self.current_player = (self.which_move - 1) % self.number_of_players
                self.player_name.setText(self.dict_players[self.current_player][7])
                self.how_many_points.setText(str(self.dict_players[self.current_player][8]))
                letter_helper = self.dict_players[self.current_player]

                self.pushButton1.setText(letter_helper[0])
                self.pushButton2.setText(letter_helper[1])
                self.pushButton3.setText(letter_helper[2])
                self.pushButton4.setText(letter_helper[3])
                self.pushButton5.setText(letter_helper[4])
                self.pushButton6.setText(letter_helper[5])
                self.pushButton7.setText(letter_helper[6])


    def game_over(self):
        self.check_game_over = True
        self.players_sorted = []
        for key in self.players_to_db:
            self.players_sorted.append([key, self.players_to_db.get(key)])

        self.players_sorted.sort(key=lambda x: x[1])

        self.window4 = QtWidgets.QMainWindow()
        self.ui = game_over.Ui_Form8(self.players_sorted)
        self.ui.setupUi(self.window4)
        self.window4.show()
        self.form.hide()

    # def kicked_player_pop(self):
    #     self.window5 = QtWidgets.QMainWindow()
    #     self.ui = Ui_Form7(self.name_kicked_player)
    #     self.ui.setupUi(self.window5)
    #     self.window5.show()
    #     QtCore.QTimer.singleShot(3000, self.window5.close)
    #     self.kicked_player_check = True

    def kicked_player_pop(self):
        self.window5 = QtWidgets.QMainWindow()
        self.ui = Ui_Form7(self.name_kicked_player)
        self.ui.setupUi(self.window5)
        self.window5.show()
        QtCore.QTimer.singleShot(3000, self.window5.close)

        QtCore.QTimer.singleShot(3000, self.new_player_pop)

    def new_player_pop(self):

        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Form6(self.players_sorted, self.dict_players[self.current_player][7])
        self.ui.setupUi(self.window2)
        self.window2.show()
        QtCore.QTimer.singleShot(3000, self.window2.close)

    def clicked_leaderboard(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Form5(self.players_sorted)
        self.ui.setupUi(self.window3)
        self.window3.show()

    def clicked_help(self):
        self.window6 = QtWidgets.QMainWindow()
        self.ui = Ui_Form9()
        self.ui.setupUi(self.window6)
        self.window6.show()

    def safe_words(self):
        self.dict_players[self.current_player][0] = self.pushButton1.text()
        self.dict_players[self.current_player][1] = self.pushButton2.text()
        self.dict_players[self.current_player][2] = self.pushButton3.text()
        self.dict_players[self.current_player][3] = self.pushButton4.text()
        self.dict_players[self.current_player][4] = self.pushButton5.text()
        self.dict_players[self.current_player][5] = self.pushButton6.text()
        self.dict_players[self.current_player][6] = self.pushButton7.text()

        print(self.dict_players)

    def clicked_pushButton1(self):
        if self.pushButton1_used == 0:
            if self.change_letters_check == 1:
                if self.pushButton1_check == 0:
                    self.pushButton1.setStyleSheet('background-color:red')
                    self.pushButton1_check = 1

                else:
                    self.pushButton1.setStyleSheet('background-color:lightgrey')
                    self.pushButton1_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.pushButton1.setStyleSheet('background-color:red')
                    self.pushButton1_check = 1
                    self.letter_to_board = self.pushButton1.text()
                else:
                    self.pushButton1.setStyleSheet('background-color:lightgrey')
                    self.pushButton1_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton2(self):
        if self.pushButton2_used == 0:
            if self.change_letters_check == 1:
                if self.pushButton2_check == 0:
                    self.pushButton2.setStyleSheet('background-color:red')
                    self.pushButton2_check = 1

                else:
                    self.pushButton2.setStyleSheet('background-color:lightgrey')
                    self.pushButton2_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:

                    self.pushButton2.setStyleSheet('background-color:red')
                    self.pushButton2_check = 1
                    self.letter_to_board = self.pushButton2.text()
                else:
                    self.pushButton2.setStyleSheet('background-color:lightgrey')
                    self.pushButton2_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton3(self):
        if self.pushButton3_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton3_check == 0:
                    self.pushButton3.setStyleSheet('background-color:red')
                    self.pushButton3_check = 1

                else:
                    self.pushButton3.setStyleSheet('background-color:lightgrey')
                    self.pushButton3_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.pushButton3.setStyleSheet('background-color:red')
                    self.pushButton3_check = 1
                    self.letter_to_board = self.pushButton3.text()
                else:
                    self.pushButton3.setStyleSheet('background-color:lightgrey')
                    self.pushButton3_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton4(self):
        if self.pushButton4_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton4_check == 0:
                    self.pushButton4.setStyleSheet('background-color:red')
                    self.pushButton4_check = 1

                else:
                    self.pushButton4.setStyleSheet('background-color:lightgrey')
                    self.pushButton4_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.pushButton4.setStyleSheet('background-color:red')
                    self.pushButton4_check = 1
                    self.letter_to_board = self.pushButton4.text()
                else:
                    self.pushButton4.setStyleSheet('background-color:lightgrey')
                    self.pushButton4_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton5(self):
        if self.pushButton5_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton5_check == 0:
                    self.pushButton5.setStyleSheet('background-color:red')
                    self.pushButton5_check = 1

                else:
                    self.pushButton5.setStyleSheet('background-color:lightgrey')
                    self.pushButton5_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.pushButton5.setStyleSheet('background-color:red')
                    self.pushButton5_check = 1
                    self.letter_to_board = self.pushButton5.text()
                else:
                    self.pushButton5.setStyleSheet('background-color:lightgrey')
                    self.pushButton5_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton6(self):
        if self.pushButton6_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton6_check == 0:
                    self.pushButton6.setStyleSheet('background-color:red')
                    self.pushButton6_check = 1

                else:
                    self.pushButton6.setStyleSheet('background-color:lightgrey')
                    self.pushButton6_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.pushButton6.setStyleSheet('background-color:red')
                    self.pushButton6_check = 1
                    self.letter_to_board = self.pushButton6.text()
                else:
                    self.pushButton6.setStyleSheet('background-color:lightgrey')
                    self.pushButton6_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton7(self):
        if self.pushButton7_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton7_check == 0:
                    self.pushButton7.setStyleSheet('background-color:red')
                    self.pushButton7_check = 1

                else:
                    self.pushButton7.setStyleSheet('background-color:lightgrey')
                    self.pushButton7_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.pushButton7.setStyleSheet('background-color:red')
                    self.pushButton7_check = 1
                    self.letter_to_board = self.pushButton7.text()
                else:
                    self.pushButton7.setStyleSheet('background-color:lightgrey')
                    self.pushButton7_check = 0
                    self.letter_to_board = ""

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scrabble"))
        self.board_label_0_0.setText(_translate("Form", "TW"))
        self.board_label_0_3.setText(_translate("Form", "DL"))
        self.board_label_0_7.setText(_translate("Form", "TW"))
        self.board_label_0_11.setText(_translate("Form", "DL"))
        self.board_label_0_14.setText(_translate("Form", "TW"))
        self.board_label_1_1.setText(_translate("Form", "DW"))
        self.board_label_1_5.setText(_translate("Form", "TL"))
        self.board_label_1_9.setText(_translate("Form", "TL"))
        self.board_label_1_13.setText(_translate("Form", "DW"))
        self.board_label_2_2.setText(_translate("Form", "DW"))
        self.board_label_2_6.setText(_translate("Form", "DL"))
        self.board_label_2_8.setText(_translate("Form", "DL"))
        self.board_label_2_12.setText(_translate("Form", "DW"))
        self.board_label_3_0.setText(_translate("Form", "DL"))
        self.board_label_3_3.setText(_translate("Form", "DW"))
        self.board_label_3_7.setText(_translate("Form", "DL"))
        self.board_label_3_11.setText(_translate("Form", "DW"))
        self.board_label_3_14.setText(_translate("Form", "DL"))
        self.board_label_4_4.setText(_translate("Form", "DW"))
        self.board_label_4_10.setText(_translate("Form", "DW"))
        self.board_label_5_1.setText(_translate("Form", "TL"))
        self.board_label_5_5.setText(_translate("Form", "TL"))
        self.board_label_5_9.setText(_translate("Form", "TL"))
        self.board_label_5_13.setText(_translate("Form", "TL"))
        self.board_label_6_2.setText(_translate("Form", "DL"))
        self.board_label_6_6.setText(_translate("Form", "DL"))
        self.board_label_6_8.setText(_translate("Form", "DL"))
        self.board_label_6_12.setText(_translate("Form", "DL"))
        self.board_label_7_0.setText(_translate("Form", "TW"))
        self.board_label_7_3.setText(_translate("Form", "DL"))
        self.board_label_7_7.setText(_translate("Form", "*"))
        self.board_label_7_11.setText(_translate("Form", "DL"))
        self.board_label_7_14.setText(_translate("Form", "TW"))
        self.board_label_8_2.setText(_translate("Form", "DL"))
        self.board_label_8_6.setText(_translate("Form", "DL"))
        self.board_label_8_8.setText(_translate("Form", "DL"))
        self.board_label_8_12.setText(_translate("Form", "DL"))
        self.board_label_9_1.setText(_translate("Form", "TL"))
        self.board_label_9_5.setText(_translate("Form", "TL"))
        self.board_label_9_9.setText(_translate("Form", "TL"))
        self.board_label_9_13.setText(_translate("Form", "TL"))
        self.board_label_10_4.setText(_translate("Form", "DW"))
        self.board_label_10_10.setText(_translate("Form", "DW"))
        self.board_label_11_0.setText(_translate("Form", "DL"))
        self.board_label_11_3.setText(_translate("Form", "DW"))
        self.board_label_11_7.setText(_translate("Form", "DL"))
        self.board_label_11_11.setText(_translate("Form", "DW"))
        self.board_label_11_14.setText(_translate("Form", "DL"))
        self.board_label_12_2.setText(_translate("Form", "DW"))
        self.board_label_12_6.setText(_translate("Form", "DL"))
        self.board_label_12_8.setText(_translate("Form", "DL"))
        self.board_label_12_12.setText(_translate("Form", "DW"))
        self.board_label_13_1.setText(_translate("Form", "DW"))
        self.board_label_13_5.setText(_translate("Form", "TL"))
        self.board_label_13_9.setText(_translate("Form", "TL"))
        self.board_label_13_13.setText(_translate("Form", "DW"))
        self.board_label_14_0.setText(_translate("Form", "TW"))
        self.board_label_14_3.setText(_translate("Form", "DL"))
        self.board_label_14_7.setText(_translate("Form", "TW"))
        self.board_label_14_11.setText(_translate("Form", "DL"))
        self.board_label_14_14.setText(_translate("Form", "TW"))
        self.clear.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    test1 = Player("", [])
    test2 = Player("", [])
    test3 = Player("", [])
    # test4 = Player("", [])
    test1.name = "XD"
    test2.name = "elo"
    test3.name = "yo"
    # test4.name = "asd"
    test = [test1, test2, test3]
    ui = Ui_Form4(3, test)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
