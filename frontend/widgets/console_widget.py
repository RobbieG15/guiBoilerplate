# :Title: console_widget.py
# :Description: Wrapper class for console_widget
# :Created: 6/6/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
from PySide6.QtWidgets import QWidget

from frontend.ui.compiled.console_widget import Ui_console_widget


class ConsoleWidget(QWidget, Ui_console_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
