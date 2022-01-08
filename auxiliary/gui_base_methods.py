import os

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QFile, QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QMainWindow, QCheckBox
from platform import system
from multipledispatch import dispatch
import re
from PyQt6.uic.properties import QtGui
from typing import List


def quit_window(window) -> None:
    window.close()


### IMAGE SETTERS
@dispatch(QLabel, str)
def set_image_to_label(widget: QLabel, image: str) -> None:
    _file = '{}{}{}'.format(os.getcwd(), '/images/', image)
    _pixmap = QPixmap(_file)
    _pixmap.scaled(
        widget.width(),
        widget.height(),
        Qt.AspectRatioMode.KeepAspectRatio
    )
    widget.setPixmap(_pixmap)
    widget.setScaledContents(True)


@dispatch(list, str)
def set_image_to_label(labels, image: str) -> None:
    _file = '{}{}{}'.format(os.getcwd(), '/images/', image)
    _pixmap = QPixmap(_file)
    for widget in labels:
        _pixmap.scaled(
            widget.width(),
            widget.height(),
            Qt.AspectRatioMode.KeepAspectRatio
        )
        widget.setPixmap(_pixmap)
        widget.setScaledContents(True)


@dispatch(QPushButton, str)
def set_image_to_button(button: QPushButton, image: str) -> None:
    _file = '{}{}{}'.format(os.getcwd(), '/images/', image)
    button.setIcon(QIcon(_file))
    button.setIconSize(QSize(button.width(), button.height()))


@dispatch(list, str)
def set_image_to_button(elements, image: str) -> None:
    _file = '{}{}{}'.format(os.getcwd(), '/images/', image)
    for button in elements:
        button.setIcon(QIcon(_file))
        button.setIconSize(QSize(button.width(), button.height()))


def clear_input(*argv: QLineEdit) -> None:
    for each in argv:
        each.setText('')


def uncheck_all(arg1: list, *argv: QCheckBox):
    for each in arg1:
        each.isChecked = False
    for each in argv:
        each.isChecked = False


def disable_mac_focus(arg1: list,  *argv: QLineEdit) -> None:
    if system() == 'Darwin':
        for each in arg1:
            each.setAttribute(Qt.WidgetAttribute.WA_MacShowFocusRect, 0)
        for each in argv:
            each.setAttribute(Qt.WidgetAttribute.WA_MacShowFocusRect, 0)


def set_echomode(arg1: list, *argv: QLineEdit) -> None:
    for each in arg1:
        each.setEchoMode(QLineEdit.EchoMode.Password)
    for each in argv:
        each.setEchoMode(QLineEdit.EchoMode.Password)


def set_cursor(arg1: list, *argv: QLineEdit) -> None:
    for each in arg1:
        each.setAlignment(Qt.Alignment.AlignCenter)
    for each in argv:
        each.setAlignment(Qt.Alignment.AlignCenter)


def hide_labels(arg1: list, *argv: QLabel) -> None:
    for each in arg1:
        each.setVisible(0)
    for each in argv:
        each.setVisible(0)


def find_object_by_substring(
        obj: QtWidgets,
        name: str,
        prefix: str,
        suffix: str,
        root: QMainWindow,
        new_pref: str,
        new_suff: str) -> QtWidgets:

    # name stripped of prefix and suffix
    _str = re.sub(('^' + prefix), '', name)
    _str = re.sub((suffix + '$'), '', _str)

    if new_pref is None and new_suff is not None:
        return root.findChild(obj, (_str + new_suff))

    elif new_pref is not None and new_suff is None:
        return root.findChild(obj, (new_pref + _str))

    elif new_pref is not None and new_suff is not None:
        return root.findChild(obj, (new_pref + _str + new_suff))

    else:
        return root.findChild(obj, _str)


def return_to_menu(source: QMainWindow, menu: QMainWindow) -> None:
    menu.show()
    menu._is_hs_open = False
    source.close()


def board_to_string(board: list) -> str:
    _string = ''
    for i in range(15):
        for j in range(15):
            _string += board[i][j]
    return _string


def string_to_board(string: str) -> list:
    """
    get string from db and convert it to board to pass to gui
    char at string[i+j] corresponds to board[i][j] letter tile
    """
    _list = []
    for i in range(len(string)):
        if i % 15 == 0:
            sub = string[i:i + 15]
            lst = []
            for j in sub:
                lst.append(j)
            _list.append(lst)
    return _list
