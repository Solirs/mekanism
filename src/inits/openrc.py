#!/usr/bin/env python
from utils import color, pathutils
import preprocessor


class OpenRCgen():
    def __init__(self, template=None, *args, **kwargs):
        self.scrpath = "/etc/init.d/"
        self.template = pathutils.templatepath() + "/templates/openrc_initscript.txt"
        if template: self.template = template #I would love to use kwargs here but they dont resort to default value if kwarg is none...

    def OpenRCgen(self, scrpath: str) -> None:
        print(color.Colors().brgreen + "[+] Generating for OpenRC" + color.Colors().reset)
        print("Command is " + scrpath)
        template_file = open(self.template, 'r')

        template = template_file.read()

        fin = preprocessor.preprocessor.proprocess_template(template, scrpath)
        print(color.Colors().brgreen + f"[+] Template filling done ! Creating script in {self.scrpath}{preprocessor.preprocessor.get_prog_name(scrpath)}" + color.Colors().reset)
        



        

        
        #Now the fun begins.

        
