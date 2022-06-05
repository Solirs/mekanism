import sys
from utils import color


def fatal(msg: str):
    print(color.Colors().red +"FATAL: " + msg + color.Colors().reset)
    sys.exit(1)

def red(msg: str):
    print(color.Colors().red + msg + color.Colors().reset)

def good(msg: str):
    print(color.Colors().brgreen + msg + color.Colors().reset)