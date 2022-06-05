import os
from shutil import which
from utils import logutils
from pathlib import *


def binpath(path:str):
    #Is it a full path?
    exists = os.path.exists(path)
    if exists is True: return path; pass

    #Is it in the path variable?
    if (which(path)):
        return which(path)
    else:
        logutils.fatal (f"Path {path} does not exist and not in the PATH variable.")

def templatepath():
    return str(Path(__file__).parent.parent.parent)