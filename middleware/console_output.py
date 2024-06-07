# :Title: console_output.py
# :Description: additional middleware functions for console outputting
# :Created: 5/31/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
from sys import _getframe

from PySide6.QtCore import QObject

from backend.console_logging.console_logging import ConsoleLevel, ConsoleLogger


def log(msg: str, level: ConsoleLevel = ConsoleLevel.INFO) -> bool:
    """
    Wrapper log method that will be imported in any file that needs logging functionality

    Args:
        msg (str): The message the developer wants to display
        level (ConsoleLevel, optional): The level the msg fits under. Defaults to ConsoleLevel.INFO.

    Returns:
        bool: Whether or not the msg ended up printing
    """
    if level == ConsoleLevel.ERROR or level == ConsoleLevel.CRITICAL:
        msg = append_traceback(msg)
    return ConsoleLogger().log(msg, level)


def append_traceback(msg: str) -> str:
    """
    Adds a traceback to the msg

    Args:
        msg (str): the original message to print

    Returns:
        str: the new message with the additional traceback
    """
    msg += "\n  Traceback:"
    frame = _getframe(2)
    while frame:
        msg += f"\n    {frame.f_code.co_filename} - line {frame.f_lineno}"
        frame = frame.f_back
    return msg


def set_debug_mode(debug_mode: bool) -> None:
    """
    Setter for the debug mode (adds debug to levels)

    Args:
        debug_mode (bool): Whether debug mode is on or off
    """
    ConsoleLogger().set_debug_mode(debug_mode)


def set_console(console: QObject) -> None:
    """
    Setter for the self.console instance variable

    Args:
        console (QObject): The console to echo the msgs to
    """
    ConsoleLogger().set_console(console)
