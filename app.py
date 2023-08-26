#!/usr/bin/env python3
import sys
from views import Window
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
