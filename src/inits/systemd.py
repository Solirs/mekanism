#!/usr/bin/env python

class SystemDgen():
    def __init__(self):
        self.scrpath = "/etc/systemd/system/"
        self.template = "placeholder"
    def SystemDgen(self, scrpath: str):
        print("Generating for SystemD")
