from dataclasses import dataclass

@dataclass
class Colors():
    red: str = "\u001b[31m"
    brgreen: str = "\u001b[32;1m"
    reset: str = "\u001b[0m"
