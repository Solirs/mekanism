import os
from shutil import which
from utils import logutils
from pathlib import *


def get_prog_name(cmd: str):
    if "/" in cmd.split()[0]:
        return cmd.split()[0].split("/")[-1]


def binpath(path:str): #This just resolves the full path of the program to execute if its in the PATH var.
    #Is it a full path?
    prog = path.split()[0]
    exists = os.path.exists(prog)
    if exists is True: return path; pass

    #Is it in the path variable?
    if (which(prog)):
        flags = ("".join(path.split()[1:])) #Error if directly put in brackets
        return f"{which(prog).rstrip()} {flags}"
    else:
        logutils.fatal (f"Path {path} does not exist and not in the PATH variable.")

def templatepath():
    return str(Path(__file__).parent.parent.parent)