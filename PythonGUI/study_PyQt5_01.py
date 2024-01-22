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


def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100, 100, 200, 50)
   b.move(50, 20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()