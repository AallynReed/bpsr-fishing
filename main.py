import sys
import os
from pathlib import Path

if getattr(sys, "frozen", False):
    cwd = os.getcwd()
    new_cwd = Path(sys.executable).parent
    os.chdir(new_cwd)
    if new_cwd not in sys.path:
        sys.path.append(new_cwd)

import ok

from src.config import config

if __name__ == '__main__':
    config = config
    ok = ok.OK(config)
    ok.start()
