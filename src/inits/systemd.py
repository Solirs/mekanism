#!/usr/bin/env python

from utils import color, pathutils

class SystemDgen():
    def __init__(self, *args, **kwargs):
        self.scrpath = "/etc/systemd/system/"
        self.template = kwargs.get("custompath", pathutils.templatepath() + "/templates/systemd_service.txt")
    def SystemDgen(self, scrpath: str):
        print(color.Colors().brgreen +  "[+] Generating for SystemD")
