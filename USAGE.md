# Mekanism usage guide.

Mekanism has at least two required flags, the targeted init system (positional), and the program that your script or service will run.

for example:

`mekanism openrc -exec "ls"` 

Will create an openrc service that runs the command ls without flags.

There are common flags that you can use accross all init systems for example:

    -template [PATH] | Select the script or service template (Optional), default depends on your init system
    -o, --output [PATH] | Set output file (Optional), default depends on your init system
    -exec (path to program or program name if its in the PATH variable) | Set the program that your script or service will run (Required).

Specifying an init system is obligatory, meaning that
`mekanism -exec "ls"` will not work.

There are also a few init system specific flags.

Systemd:

    mode (positional) | Pick between user and root mode (more info at https://superuser.com/questions/1429433/what-is-the-difference-between-systemds-user-and-system-units-services), Optional and set to "user" by default.
    example: `mekanism systemd root -exec "ls"`



## Defaults

By default (-o flag not specified) openrc services are placed in /etc/init.d.

For systemd, if root mode is chosen then scripts are placed in /etc/systemd/system/, if user is chosen scripts are placed in ~/.config/systemd/user/

By default service files are named after their program's name.
For example `mekanism openrc -exec "ls"` > /etc/init.d/ls 

All the templates are in the templates directory and are named after their init system.