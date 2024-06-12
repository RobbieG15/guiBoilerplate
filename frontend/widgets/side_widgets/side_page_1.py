# :Title: side_page_2.py
# :Description: Wrapper class for side_page_2
# :Created: 6/6/2024
# :Last Modified: 6/11/2024
# :Author: Robert Greenslade


# Imports
from os import listdir
from os.path import isdir, isfile, join
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QTreeWidgetItem, QWidget

from backend.console_logging.console_logging import ConsoleLevel
from frontend.ui.compiled.side_page_1 import Ui_Form
from middleware.console_output import log as print


class SidePage1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.root = self.file_explorer_tree.invisibleRootItem()

        self.working_directory_change_btn.clicked.connect(self._on_change_btn_click)

    def _on_change_btn_click(self) -> bool:
        """
        On change event method for the working directory file selection.

        Returns:
            bool: Whether or not the event executed successfully.
        """
        directory_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        if not directory_path:
            print("Directory was not specified, cannot import", ConsoleLevel.DEBUG)

            return False

        self.working_directory_line_edit.setText(directory_path)

        self.file_explorer_tree.clear()
        self._populate_tree(directory_path)

        return True

    def _populate_tree(
        self, directory_path: str, parent: QTreeWidgetItem = None
    ) -> None:
        """
        Method to add the files and directories recursively from inside the working directory.

        Args:
            directory_path (str): The working directory file path
            parent (QTreeWidgetItem, optional): The widget item to set as the parent. Defaults to None.
        """
        only_files = [
            f for f in listdir(directory_path) if isfile(join(directory_path, f))
        ]
        for child_file in only_files:
            if ".html" not in child_file:
                continue
            item = QTreeWidgetItem([child_file])
            item.setText(0, child_file)
            if parent:
                parent.addChild(item)
            else:
                self.root.addChild(item)
        only_dirs = [
            f for f in listdir(directory_path) if isdir(join(directory_path, f))
        ]
        for child_dir in only_dirs:
            print(child_dir)
            item = QTreeWidgetItem([child_dir])
            if parent:
                parent.addChild(item)
                self._populate_tree(Path(directory_path).joinpath(child_dir), item)
            else:
                self.root.addChild(item)
                self._populate_tree(Path(directory_path).joinpath(child_dir), item)

    def get_full_file_path(self, item: QTreeWidgetItem) -> str:
        """
        Method to get the full file path of a given widget item in the file explorer tree.

        Args:
            item (QTreeWidgetItem): The item to get the file path of.

        Returns:
            str: The file path of the item as a string.
        """
        full_path = Path(self.working_directory_line_edit.text())
        if item.parent() is None:
            partial = item.text(0)
        else:
            partial = Path(self.get_full_file_path(item.parent())).joinpath(
                item.text(0)
            )
        return str(full_path.joinpath(partial))

    def save(self) -> None:
        """
        The save event for the side widget on page 1. At the moment, nothing to save.
        """
        pass
