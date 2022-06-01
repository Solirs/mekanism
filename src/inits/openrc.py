#!/usr/bin/env python

class OpenRCgen():
    def __init__(self):
        self.scrpath = "/etc/init.d"
        self.template = "placeholder"

    def OpenRCgen(self, scrpath: str) -> None:
        print("Generating for OpenRC")
