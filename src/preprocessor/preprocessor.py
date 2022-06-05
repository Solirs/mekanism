from utils import color

def get_prog_name(cmd: str):
    if "/" in cmd.split()[0]:
        return cmd.split()[0].split("/")[-1]



def proprocess_template(template: str, cmd: str):
    print(color.Colors().brgreen + "[+] Filling template..." + color.Colors().reset)
    progname = get_prog_name(cmd)
    final = template.replace("$MK_SVNAME", progname).replace("$MK_EXECCMD", f'''"{cmd}"''')
    return final
    

