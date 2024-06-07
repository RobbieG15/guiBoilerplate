# :Title: top_page_4.py
# :Description: Wrapper class for top_page_4
# :Created: 6/6/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
from PySide6.QtWidgets import QWidget

from frontend.ui.compiled.top_page_4 import Ui_Form


class TopPage4(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
