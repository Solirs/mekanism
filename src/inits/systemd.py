#!/usr/bin/env python

from utils import color, pathutils

class SystemDgen():
    def __init__(self, template=None, *args, **kwargs):
        self.scrpath = "/etc/systemd/system/"
        self.template = pathutils.templatepath() + "/templates/systemd_service.txt" 
        if template: self.template = template #I would love to use kwargs here but they dont resort to default value if kwarg is none...
    def SystemDgen(self, scrpath: str):
        print(color.Colors().brgreen +  "[+] Generating for SystemD" + color.Colors().reset)
        template_file = open(self.template, 'r')

        template = template_file.read()
