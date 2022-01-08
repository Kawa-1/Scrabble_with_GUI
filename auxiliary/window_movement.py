from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt


# introduce window dragging mechanism; overriding Qt methods
# works just fine

class DummyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self._old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButtons.LeftButton:
            # self._old_pos = event.position()
            self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButtons.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        # delta = event.position() - self._old_pos
        delta = event.globalPosition().toPoint() - self._old_pos
        self.move(self.pos() + delta)
        self._old_pos = event.globalPosition().toPoint()
        event.accept()

