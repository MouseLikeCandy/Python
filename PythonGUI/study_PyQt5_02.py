# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：study_PyQt5_01.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/10/8 15:34 
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.resize(200, 50)
        self.setWindowTitle("PyQt5")
        self.label = QLabel(self)
        self.label.setText("Hello World")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50, 20)


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
