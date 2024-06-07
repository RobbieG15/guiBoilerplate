# :Title: side_page_3.py
# :Description: Wrapper class for side_page_3
# :Created: 6/6/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
from PySide6.QtWidgets import QWidget

from frontend.ui.compiled.side_page_3 import Ui_Form


class SidePage3(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
