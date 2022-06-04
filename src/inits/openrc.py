#!/usr/bin/env python
from utils import color, pathutils

class OpenRCgen():
    def __init__(self, *args, **kwargs):
        self.scrpath = "/etc/init.d/"
        self.template = kwargs.get("custompath", pathutils.templatepath() + "/templates/openrc_initscript.txt")

    def OpenRCgen(self, scrpath: str) -> None:
        print(color.Colors().brgreen + "[+] Generating for OpenRC")
        print(self.template)
