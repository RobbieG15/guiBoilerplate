# :Title: main_window.py
# :Description: Wrapper class for main_window
# :Created: 6/6/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
from PySide6.QtWidgets import QMainWindow

from frontend.ui.compiled.frontend import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setupUi(self)
