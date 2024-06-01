# :Title: frontend.py
# :Description: Gather all frontend code into one window
# :Created: 5/30/2024
# :Last Modified: 5/31/2024
# :Author: Robert Greenslade

# Imports
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from frontend.ui.compiled.console_widget import Ui_console_widget
from frontend.ui.compiled.frontend import Ui_MainWindow


class Frontend(QMainWindow):
    """
    The wrapper class for the entire front end UI

    Args:
        QMainWindow (QMainWindow): Frontend inherits from QMainWindow
    """

    def __init__(self):
        # Wrapper ui setup
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Console widget initialization
        console_widget = QWidget()
        console = Ui_console_widget()
        console.setupUi(console_widget)
        console_layout = QVBoxLayout()
        console_layout.addWidget(console_widget)
        self.ui.bottom_widget.setLayout(console_layout)
