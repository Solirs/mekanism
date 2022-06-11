# Mekanism

Mekanism is a simple program that generates init scripts and services.
It's designed for compatibility across UNIX like systems and does not use any non built-in module according to the [python 3.10.5 module index](https://docs.python.org/3/py-modindex.html). Meaning that you don't even need to configure pip to use it.

It's currently WIP and in a semi-usable state. As it lacks some features and polishing.


It currently supports:

    OpenRC,
    SystemD.

I plan to add support to the following:

    Runit,
    SysVinit,
    FreeBSD,
    OpenBSD.

Readme WIP
