from utils import color, logutils, pathutils

def get_prog_flags(cmd: str):
    return "".join(cmd.split()[1:]).rstrip()


def proprocess_template(template: str, cmd: str):
    logutils.good("[+] Filling template...")
    progname = pathutils.get_prog_name(cmd)
    flags = get_prog_flags(cmd)
    final = template.replace("$MK_SVNAME", progname).replace("$MK_EXECCMD", f'"{cmd.split()[0]}"').replace("$MK_FLAGS", flags)
    
    return final
    

