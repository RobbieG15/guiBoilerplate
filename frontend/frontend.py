# :Title: frontend.py
# :Description: Gather all frontend code into one window
# :Created: 5/30/2024
# :Last Modified: 6/11/2024
# :Author: Robert Greenslade

# Imports
from pathlib import Path

from PySide6.QtGui import QAction, QKeySequence

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

        # Menu Bar Init
        file_save_action = QAction("Save", self)
        self.menu_file.addAction(file_save_action)
        file_save_action.setShortcut(QKeySequence("Ctrl+S"))
        file_save_action.triggered.connect(self.on_save_action)

        # Editor Page Init
        self.side_page_1_widget.file_explorer_tree.itemDoubleClicked.connect(
            self._file_explorer_item_double_clicked
        )

        # Set Default Page
        self.on_page_1_btn_click()

    # ------------------------------------------------------------------------------------------------
    # ---------------------------------------- Frontend Shell ----------------------------------------
    # ------------------------------------------------------------------------------------------------

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

    def on_save_action(self) -> None:
        """
        The action to complete on each page when file -> save is initiated.
        """
        match self.side_widget.currentIndex():
            case 0:
                self.on_page_1_save()
            case 1:
                self.on_page_2_save()
            case 2:
                self.on_page_3_save()
            case 3:
                self.on_page_4_save()

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

    # ------------------------------------------------------------------------------------------------
    # ------------------------------------ Page One Functionality ------------------------------------
    # ------------------------------------------------------------------------------------------------

    def _file_explorer_item_double_clicked(self) -> None:
        """
        On double click event for the file explorer on page 1.
        """
        if len(self.side_page_1_widget.file_explorer_tree.selectedItems()) == 1:
            file_path = self.side_page_1_widget.get_full_file_path(
                self.side_page_1_widget.file_explorer_tree.currentItem()
            )
            if file_path.endswith(".html"):
                self.top_page_1_widget.load_tab(file_path)
            else:
                print("Only html files can be loaded", ConsoleLevel.WARNING)

    def on_page_1_save(self) -> None:
        """
        The save action corresponding to page 1.
        """
        self.top_page_1_widget.save()
        self.side_page_1_widget.save()

    # ------------------------------------------------------------------------------------------------
    # ------------------------------------ Page Two Functionality ------------------------------------
    # ------------------------------------------------------------------------------------------------

    def on_page_2_save(self) -> None:
        """
        The save action corresponding to page 2.
        """
        pass

    # ------------------------------------------------------------------------------------------------
    # ----------------------------------- Page Three Functionality -----------------------------------
    # ------------------------------------------------------------------------------------------------

    def on_page_3_save(self) -> None:
        """
        The save action corresponding to page 3.
        """
        pass

    # ------------------------------------------------------------------------------------------------
    # ----------------------------------- Page Four Functionality ------------------------------------
    # ------------------------------------------------------------------------------------------------

    def on_page_4_save(self) -> None:
        """
        The save action corresponding to page 4.
        """
        pass
