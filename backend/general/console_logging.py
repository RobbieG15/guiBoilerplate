# :Title: console_logging.py
# :Description: console logging for the entire project
# :Created: 5/31/2024
# :Last Modified: 6/1/2024
# :Author: Robert Greenslade

# Imports
from datetime import datetime
from enum import Enum
from logging import (
    CRITICAL,
    DEBUG,
    ERROR,
    INFO,
    WARNING,
    Filter,
    Formatter,
    Logger,
    LogRecord,
    StreamHandler,
    getLogger,
)
from sys import stderr, stdout

from colorama import Fore, Style
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QTextCursor

from data.classes.singleton import Singleton


class LevelFilter(Filter):
    """
    Filtering class for the logging level handlers

    Args:
        Filter (logging.Filter): LevelFilter inherits from Filter
    """

    def __init__(self, level):
        self.__level = level

    def filter(self, record: LogRecord) -> bool:
        """
        The override method of filtering the levels

        Args:
            record (LogRecord): The level to filter

        Returns:
            bool: Whether or not to display this level on the handler
        """
        return record.levelno == self.__level


class ConsoleLevel(Enum):
    """
    Enum to keep track of the log levels because logging doesn't support

    Args:
        Enum (Enum): ConsoleLevel inherits from Enum
    """

    DEBUG = DEBUG
    """ All messages that wil only be available to devs in debug mode """
    INFO = INFO
    """ Normal messages that would be default print statements """
    WARNING = WARNING
    """ Messages that won't harm the user, but might give unexpected behavior """
    ERROR = ERROR
    """ Error messages provided with a traceback """
    CRITICAL = CRITICAL
    """ Enhanced error messages that could put the state of the program in jeopardy """


class ConsoleLogger(Singleton):
    """
    The Console Logger that will be used throughout the project files

    Args:
        Singleton (Singleton): ConsoleLogger inherits from Singleton class
    """

    def __init__(self) -> None:
        if hasattr(self, "_instantiated"):
            return
        self._instantiated: bool = True
        """ Whether or not the console logger has already been created """
        self.logger: Logger = None
        """ The logger that will be used to display msgs to user """
        self.levels: set[ConsoleLevel] = None
        """ The levels the user has selected to show. """
        self.console: QObject = None
        """ The console in the ui to print to """

        self.setup_logger()
        self.enable_all()

    def set_console(self, console: QObject) -> None:
        """
        Setter for the self.console instance variable

        Args:
            console (QObject): The console to echo the msgs to
        """
        self.console = console

    def set_debug_mode(self, debug_mode: bool) -> None:
        """
        Setter for the debug mode (adds debug to levels)

        Args:
            debug_mode (bool): Whether debug mode is on or off
        """
        if debug_mode:
            self.levels.add(ConsoleLevel.DEBUG)
        elif not debug_mode and ConsoleLevel.DEBUG in self.levels:
            self.levels.remove(ConsoleLevel.DEBUG)

    def log(self, msg: str, level: ConsoleLevel = ConsoleLevel.INFO) -> bool:
        """
        Method to print the log messages to the supported output streams

        Args:
            msg (str): message the developer wants to print
            level (ConsoleLevel, optional): the level the message is. Defaults to ConsoleLevel.INFO.

        Returns:
            bool: Whether or not the message printed
        """
        if level in self.levels:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            match level:
                case ConsoleLevel.DEBUG:
                    self.logger.debug(msg)
                    self._show_in_console(f"{time} - DEBUG - {msg}\n", Qt.cyan)
                case ConsoleLevel.INFO:
                    self.logger.info(msg)
                    self._show_in_console(f"{time} - INFO - {msg}\n", Qt.white)
                case ConsoleLevel.WARNING:
                    self.logger.warning(msg)
                    self._show_in_console(f"{time} - WARNING - {msg}\n", Qt.yellow)
                case ConsoleLevel.ERROR:
                    self.logger.error(msg)
                    self._show_in_console(f"{time} - ERROR - {msg}\n", Qt.red)
                case ConsoleLevel.CRITICAL:
                    self.logger.critical(msg)
                    self._show_in_console(f"{time} - CRITICAL - {msg}\n", Qt.red)
            return True
        return False

    def _show_in_console(self, msg: str, color) -> None:
        if self.console:
            old_color = self.console.console_text.textColor()
            self.console.console_text.moveCursor(QTextCursor.End)
            self.console.console_text.setTextColor(color)
            self.console.console_text.insertPlainText(msg)
            self.console.console_text.setTextColor(old_color)

    def enable_all(self) -> None:
        """
        Function to enable all levels of output logging except debug.
        Debug is enabled through command line args in main.
        """
        self.levels = set(
            [
                ConsoleLevel.INFO,
                ConsoleLevel.WARNING,
                ConsoleLevel.ERROR,
                ConsoleLevel.CRITICAL,
            ]
        )

    def setup_logger(self) -> None:
        """
        Method to instantiate the self.logger with all requirements and functionality
        """
        # Delete old logger if needed
        if self.logger:
            del self.logger

        # Initiating the logger
        self.logger = getLogger("Logger")
        self.logger.setLevel(DEBUG)

        # Handlers
        debug_handler = StreamHandler(stdout)
        debug_handler.setLevel(DEBUG)
        info_handler = StreamHandler(stdout)
        info_handler.setLevel(INFO)
        warning_handler = StreamHandler(stdout)
        warning_handler.setLevel(WARNING)
        error_handler = StreamHandler(stderr)
        error_handler.setLevel(ERROR)
        critical_handler = StreamHandler(stderr)
        critical_handler.setLevel(CRITICAL)

        # Formatters
        debug_formatter = Formatter(
            f"{Fore.BLUE}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        info_formatter = Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        warning_formatter = Formatter(
            f"{Fore.YELLOW}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        error_formatter = Formatter(
            f"{Fore.RED}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        critical_formatter = Formatter(
            f"{Fore.RED}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Set handler formatters
        debug_handler.setFormatter(debug_formatter)
        info_handler.setFormatter(info_formatter)
        warning_handler.setFormatter(warning_formatter)
        error_handler.setFormatter(error_formatter)
        critical_handler.setFormatter(critical_formatter)

        # Add filters
        debug_handler.addFilter(LevelFilter(DEBUG))
        info_handler.addFilter(LevelFilter(INFO))
        warning_handler.addFilter(LevelFilter(WARNING))
        error_handler.addFilter(LevelFilter(ERROR))
        critical_handler.addFilter(LevelFilter(CRITICAL))

        # Add Handlers
        self.logger.addHandler(debug_handler)
        self.logger.addHandler(info_handler)
        self.logger.addHandler(warning_handler)
        self.logger.addHandler(error_handler)
        self.logger.addHandler(critical_handler)
