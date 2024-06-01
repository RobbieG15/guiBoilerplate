# :Title: recompile.py
# :Description: Compile all source ui to py files
# :Created: 5/30/2024
# :Last Modified: 5/30/2024
# :Author: Robert Greenslade

# Imports
from os import listdir, system
from pathlib import Path

# Gather all ui files to recompile
filenames = [x.strip(".ui") for x in listdir(Path(__file__).parent.joinpath("source"))]

# Recompile one at a time
for file in filenames:
    system(
        f'pyside6-uic {Path(__file__).parent.joinpath("source", file)}.ui -o {Path(__file__).parent.joinpath("compiled", file)}.py'
    )
