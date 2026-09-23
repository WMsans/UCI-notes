from pathlib import Path
import sys


# Make modules in the "src" directory visible to the modules in the "tests" directory.
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
