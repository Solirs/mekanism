#!/usr/bin/env python
from utils import color, pathutils

class OpenRCgen():
    def __init__(self, template=None, *args, **kwargs):
        self.scrpath = "/etc/init.d/"
        self.template = pathutils.templatepath() + "/templates/openrc_initscript.txt"
        if template: self.template = template #I would love to use kwargs here but they dont resort to default value if kwarg is none...

    def OpenRCgen(self, scrpath: str) -> None:
        print(color.Colors().brgreen + "[+] Generating for OpenRC")
