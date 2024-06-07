# :Title: frontend.py
# :Description: Gather all frontend code into one window
# :Created: 5/30/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
from pathlib import Path

from backend.console_logging.console_logging import ConsoleLevel
from frontend.widgets.console_widget import ConsoleWidget
from frontend.widgets.main_window import MainWindow
from frontend.widgets.side_widgets.side_page_1 import SidePage1
from frontend.widgets.side_widgets.side_page_2 import SidePage2
from frontend.widgets.side_widgets.side_page_3 import SidePage3
from frontend.widgets.side_widgets.side_page_4 import SidePage4
from frontend.widgets.top_widgets.top_page_1 import TopPage1
from frontend.widgets.top_widgets.top_page_2 import TopPage2
from frontend.widgets.top_widgets.top_page_3 import TopPage3
from frontend.widgets.top_widgets.top_page_4 import TopPage4
from middleware.console_output import log as print
from middleware.console_output import set_console


class Frontend(MainWindow):
    """
    The wrapper class for the entire front end UI

    Args:
        QMainWindow (QMainWindow): Frontend inherits from QMainWindow
    """

    def __init__(self):
        # Main Window Init
        super().__init__()

        with open(Path("frontend").joinpath("dark_style.qss")) as dark_style_file:
            _dark_style = dark_style_file.read()
            self.setStyleSheet(_dark_style)

        # Console Widget Init
        self.console_widget = ConsoleWidget()
        self.bottom_widget_layout.addWidget(self.console_widget)
        set_console(self.console_widget)

        # Side Page Init
        self.side_page_1_widget = SidePage1()
        self.side_page_2_widget = SidePage2()
        self.side_page_3_widget = SidePage3()
        self.side_page_4_widget = SidePage4()
        self.side_page_1_layout.addWidget(self.side_page_1_widget)
        self.side_page_2_layout.addWidget(self.side_page_2_widget)
        self.side_page_3_layout.addWidget(self.side_page_3_widget)
        self.side_page_4_layout.addWidget(self.side_page_4_widget)

        #
        # Top Page Init
        self.top_page_1_widget = TopPage1()
        self.top_page_2_widget = TopPage2()
        self.top_page_3_widget = TopPage3()
        self.top_page_4_widget = TopPage4()
        self.top_page_1_layout.addWidget(self.top_page_1_widget)
        self.top_page_2_layout.addWidget(self.top_page_2_widget)
        self.top_page_3_layout.addWidget(self.top_page_3_widget)
        self.top_page_4_layout.addWidget(self.top_page_4_widget)

        # Button Connection
        self.page_1_btn.clicked.connect(self.on_page_1_btn_click)
        self.page_2_btn.clicked.connect(self.on_page_2_btn_click)
        self.page_3_btn.clicked.connect(self.on_page_3_btn_click)
        self.page_4_btn.clicked.connect(self.on_page_4_btn_click)

        # Test Log Display
        print("debug", ConsoleLevel.DEBUG)
        print("info")
        print("warning", ConsoleLevel.WARNING)
        print("error", ConsoleLevel.ERROR)
        print("critical", ConsoleLevel.CRITICAL)

        # Set Default Page
        self.on_page_1_btn_click()

    def on_page_1_btn_click(self) -> None:
        """
        Method for page 1 btn click.
        """
        self.side_widget.setCurrentIndex(0)
        self.top_widget.setCurrentIndex(0)
        self._adjust_tab_style(0)
        print("Switched to page 1", ConsoleLevel.DEBUG)

    def on_page_2_btn_click(self) -> None:
        """
        Method for page 2 btn click.
        """
        self.side_widget.setCurrentIndex(1)
        self.top_widget.setCurrentIndex(1)
        self._adjust_tab_style(1)
        print("Switched to page 2", ConsoleLevel.DEBUG)

    def on_page_3_btn_click(self) -> None:
        """
        Method for page 3 btn click.
        """
        self.side_widget.setCurrentIndex(2)
        self.top_widget.setCurrentIndex(2)
        self._adjust_tab_style(2)
        print("Switched to page 3", ConsoleLevel.DEBUG)

    def on_page_4_btn_click(self) -> None:
        """
        Method for page 4 btn click.
        """
        self.side_widget.setCurrentIndex(3)
        self.top_widget.setCurrentIndex(3)
        self._adjust_tab_style(3)
        print("Switched to page 4", ConsoleLevel.DEBUG)

    def _adjust_tab_style(self, tab_index: int) -> None:
        """
        Method for adjusting the style of the page buttons as they are clicked.

        Args:
            tab_index (int): The index of the currently active tab.
        """
        self._reset_button_style()
        pressed_style = """
            background-color: #808080;
            color: #31363F;
            border-radius: 4px;
            padding: 2px;
        """
        match tab_index:
            case 0:
                self.page_1_btn.setStyleSheet(pressed_style)
            case 1:
                self.page_2_btn.setStyleSheet(pressed_style)
            case 2:
                self.page_3_btn.setStyleSheet(pressed_style)
            case 3:
                self.page_4_btn.setStyleSheet(pressed_style)

    def _reset_button_style(self) -> None:
        """
        Method for resetting all page buttons to normal styling.
        """
        normal_style = """
            background-color: #31363F;
            color: #808080;
            border-radius: 4px;
            padding: 2px;
        """
        self.page_1_btn.setStyleSheet(normal_style)
        self.page_2_btn.setStyleSheet(normal_style)
        self.page_3_btn.setStyleSheet(normal_style)
        self.page_4_btn.setStyleSheet(normal_style)
