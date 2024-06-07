# :Title: main.py
# :Description: execute entire project in one spot
# :Created: 5/30/2024
# :Last Modified: 6/6/2024
# :Author: Robert Greenslade

# Imports
import sys
from argparse import ArgumentParser
from os import system
from pathlib import Path

from PySide6.QtWidgets import QApplication

from middleware.console_output import log as print
from middleware.console_output import set_debug_mode

if __name__ == "__main__":
    # Command line arguments for development
    parser = ArgumentParser()
    parser.add_argument(
        "--build", help="build project into an executable", action="store_true"
    )
    parser.add_argument(
        "--update_ui",
        help="recreate compiled ui files from source ui",
        action="store_true",
    )
    parser.add_argument(
        "--debug",
        help="allow debug msgs to be printed during execution",
        action="store_true",
    )
    parser.add_argument(
        "--nolaunch", help="Run main and exit before launching gui", action="store_true"
    )
    args = parser.parse_args()

    if args.build:
        print("Building Started")
        system(
            'pyinstaller --onefile main.py --specpath "build/" --distpath "build/dist" --noconfirm --clean'
        )
        print("Building Complete")
    if args.update_ui:
        print("Updating Started")
        system(f'python {Path("frontend").joinpath("ui", "recompile.py")}')
        print("Updating Complete")
    if args.debug:
        set_debug_mode(True)
        print("Debug Mode Active")

    # Keep this right before gui initialization
    if args.nolaunch:
        print("Main reached gui initialization, exiting")
        exit()

    # Main app, only need one of these in entire project
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Initialize the entire frontend (import needs to be down here to avoid ui compile issues)
    from frontend.frontend import Frontend

    frontend = Frontend()
    frontend.show()

    # Start the event loop.
    app.exec()
