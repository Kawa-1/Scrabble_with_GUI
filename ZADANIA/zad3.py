from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(189, 137)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton.clicked.connect(Form.close)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def clicked(self):
        aux = int(self.textEdit.toPlainText())
        self.window2 = QtWidgets.QMainWindow()
        if aux <= 5:
            self.ui = Ui_Form2()

        else:
            self.ui = Ui_Form3()

        self.ui.setupUi(self.window2)
        self.window2.show()
        
        # miejsce na zadanie 1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Click me!"))
        self.label.setText(_translate("Form", "Wpisz liczbę większą od 5"))


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(154, 72)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(154, 72))
        Form.setMaximumSize(QtCore.QSize(154, 72))
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet("background-color:\"red\"\n""")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Za mało"))


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(154, 72)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(154, 72))
        Form.setMaximumSize(QtCore.QSize(154, 72))
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)

        # miejsce na zadanie 1

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        # miejsce na zadanie 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
