# SPDX-License-Identifier: MIT
from pathlib import Path
import runpy

demo_script = Path(__file__).resolve().parent / "demo_workspace" / "setup_demo_workspace.py"
runpy.run_path(str(demo_script), run_name="__main__")
