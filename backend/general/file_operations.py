from pathlib import Path

from backend.general.console_logging import ConsoleLevel
from middleware.console_output import log as print


def read_file(file_path: Path | str) -> list[str]:
    try:
        if isinstance(file_path, Path):
            with open(file_path.as_posix(), "r") as f:
                return f.readlines()
        else:
            with open(file_path, "r") as f:
                return f.readlines()
    except OSError as os:
        print(f"{type(os)}: {os}", ConsoleLevel.ERROR)
    except Exception as e:
        print(f"Uncaught exeption occurred: {e}", ConsoleLevel.ERROR)
