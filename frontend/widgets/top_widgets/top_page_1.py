# :Title: top_page_1.py
# :Description: Wrapper class for top_page_1
# :Created: 6/6/2024
# :Last Modified: 6/11/2024
# :Author: Robert Greenslade

# Imports
from pathlib import Path

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QPlainTextEdit, QTextBrowser, QWidget

from backend.console_logging.console_logging import ConsoleLevel
from frontend.ui.compiled.top_page_1 import Ui_Form
from middleware.console_output import log as print


class TopPage1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Editor Init
        self.tab_count = 0
        self.file_paths: dict[str, int] = {}
        self.editors: dict[int, QPlainTextEdit] = {}
        self.editor_tab_widget.tabCloseRequested.connect(self.on_remove_tab_btn_click)

        # Viewer Widget Init
        self.html_viewer = QTextBrowser()
        self.viewer_widget_layout.addWidget(self.html_viewer)

        # Button Connections
        self.editor_tab_widget.currentChanged.connect(self.on_tab_change_btn_click)

    def on_tab_change_btn_click(self, index: int) -> None:
        """
        On Click event for the tab change in the editor.

        Args:
            index (int): The index to change to.
        """
        if self.editor_tab_widget.count() > 1:
            print(index, ConsoleLevel.DEBUG)
            self._update_viewer(self._get_file_path(index))

    def on_remove_tab_btn_click(self, index: int) -> None:
        """
        On Click event for the remove tab button.

        Args:
            index (int): The tab index to remove.
        """
        self.editor_tab_widget.removeTab(index)
        self._reconfig_dicts(
            index
        )  # Will not update fully if removing last tab, clear will cover it later
        self.tab_count -= 1
        if self.editor_tab_widget.count() > 0:
            self._update_viewer(
                self._get_file_path(self.editor_tab_widget.currentIndex())
            )
        else:
            self.clear()
            self.html_viewer.clear()

    def _update_viewer(self, file_path: str) -> bool:
        """
        Method to update the html viewer to the show the contents of the specified file path.

        Args:
            file_path (str): The html file to read into the viewer.
        """
        if not file_path.endswith(".html"):
            print("Only html files can be loaded", ConsoleLevel.WARNING)
            return False

        try:
            with open(Path(file_path), "r") as f:
                self.html_viewer.setHtml(f.read())
                return True
        except Exception as e:
            print(f"Could not load file into viewer.\n Error: {e}", ConsoleLevel.ERROR)
            return False

    def load_tab(self, file_path: str) -> bool:
        """
        Method to load a new html file into the editor.

        Args:
            file_path (str): The file path to load into the editor.

        Returns:
            bool: Whether or not the loading of the tab was successful.
        """
        if self.file_paths and file_path in self.file_paths:
            print(
                "File already loaded, switching to the tab instead", ConsoleLevel.DEBUG
            )
            self.editor_tab_widget.setCurrentIndex(self.file_paths[file_path])
            self._update_viewer(file_path)
            return False
        elif not file_path.endswith(".html"):
            print('"Only html files can be loaded", ConsoleLevel.WARNING')
            return False
        else:
            tab_editor = QPlainTextEdit()
            self.editor_tab_widget.addTab(tab_editor, Path(file_path).name)
            self.file_paths[file_path] = self.tab_count
            self.editors[self.tab_count] = tab_editor
            self.tab_count += 1
            try:
                with open(Path(file_path), "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        tab_editor.moveCursor(QTextCursor.End)
                        tab_editor.insertPlainText(f"{line}")
                print(file_path)
                self.editor_tab_widget.setCurrentIndex(self.file_paths[file_path])
                self._update_viewer(file_path)
                return True
            except Exception:
                print("Error reading and loading file", ConsoleLevel.ERROR)
                return False

    def _get_file_path(self, index: int) -> str:
        """
        Gets the file path associated with the tab index.

        Args:
            index (int): The tab to get the file path of.

        Returns:
            str: The file path associated with the tab index.
        """
        for key, value in self.file_paths.items():
            if value == index:
                return key

    def _reconfig_dicts(self, index: int) -> None:
        """
        Remake the dictionaries associating index and file paths.

        Args:
            index (int): The index that is being removed.
        """
        changed_paths: list[str, str] = []
        for key, value in self.file_paths.items():
            if value == index:
                changed_paths.append(key)
            if value > index:
                self.file_paths[key] = value - 1
                changed_paths.append(key)

        for i in range(0, len(changed_paths), 2):
            if i == len(changed_paths) - 1:
                break
            value = self.file_paths[changed_paths[i]]
            del self.file_paths[changed_paths[i]]
            self.file_paths[changed_paths[i + 1]] = value

        for key, value in self.editors.items():
            if key > index:
                self.editors[key - 1] = value
        del self.editors[self.editor_tab_widget.count()]
        print(self.file_paths, ConsoleLevel.DEBUG)

    def save(self) -> None:
        """
        Saves the current tab back out to the file and updates viewer.
        """
        curr_index = self.editor_tab_widget.currentIndex()
        if curr_index != -1:
            file_path = self._get_file_path(curr_index)
            with open(file_path, "w") as f:
                f.write(self.editors[curr_index].toPlainText())
            self._update_viewer(file_path)

    def clear(self) -> None:
        """
        Clears the entire top page and backend instance variables respectfully.
        """
        self.file_paths = {}
        self.editors = {}
        self.html_viewer.clear()
        self.editor_tab_widget.clear()
