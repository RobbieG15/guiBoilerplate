# :Title: frontend.py
# :Description: Gather all frontend code into one window
# :Created: 5/30/2024
# :Last Modified: 6/1/2024
# :Author: Robert Greenslade

# Imports
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from backend.console_logging.console_logging import ConsoleLevel
from frontend.ui.compiled.console_widget import Ui_console_widget
from frontend.ui.compiled.frontend import Ui_MainWindow
from middleware.console_output import log, set_console


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
        self.setStyleSheet("background-color: grey;")
        self.ui.setupUi(self)

        # Console widget initialization
        self.console_widget = QWidget()
        console = Ui_console_widget()
        console.setupUi(self.console_widget)
        console_layout = QVBoxLayout()
        console_layout.addWidget(self.console_widget)
        self.ui.bottom_widget.setLayout(console_layout)
        set_console(console)

        # Test
        log("debug msg", ConsoleLevel.DEBUG)
        log("info msg", ConsoleLevel.INFO)
        log("warning msg", ConsoleLevel.WARNING)
        log("error msg", ConsoleLevel.ERROR)
        log("critcial msg", ConsoleLevel.CRITICAL)

        # Page setup
