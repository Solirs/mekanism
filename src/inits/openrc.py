#!/usr/bin/env python
from utils import color, pathutils, logutils
from preprocessor import preprocessor
import os
import sys
import stat

class OpenRCgen():
    def __init__(self, template=None, scrpath=None, *args, **kwargs):
        self.scrpath = "/etc/init.d/"
        self.template = pathutils.templatepath() + "/templates/openrc_initscript.txt"
        if template: self.template = template #I would love to use kwargs here but they dont resort to default value if kwarg is none...

    def OpenRCgen(self, scrpath: str, opath: str=None) -> None:
        logutils.good("[+] Generating for OpenRC")
        template_file = open(self.template, 'r')

        template = template_file.read()



        fin = preprocessor.proprocess_template(template, scrpath)
        service_name = pathutils.get_prog_name(scrpath)

        outpath = f"{self.scrpath}{service_name}"
        if opath is not None: outpath = opath

        logutils.good(f"[+] Template filling done ! Creating script in {outpath}")

        if os.path.exists(f'{outpath}'):
            logutils.red("!!! There is already a script at the path automatially generated by mekanism!!! ")
            ans = input("Owerwrite?: ")
            if ans.lower() not in ("y", "yes"):
                sys.exit(0)


        
        scr = open(f"{outpath}", 'w')

        logutils.good(f"[+] Writing generated script to {outpath}")
        scr.write(fin)
        scr.close()

        st = os.stat(f"{outpath}")
        os.chmod(f"{outpath}", st.st_mode | stat.S_IEXEC)


        logutils.good("[+] Init script written successfully! Would you like to check it out? [Y/n]")
        ans = input()

        if ans.lower() in ("y", "yes"):
            scr = open(f"{outpath}", 'r')
            print(scr.read())
        


        
