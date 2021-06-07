#!/usr/bin/env python3
import os, shlex, subprocess

def gather_printers():
        output = subprocess.Popen(["lpstat", "-v"],
                                  universal_newlines=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        out, err = output.communicate()
        printers = []
        for line in out.splitlines():
                name = line.split()[3].split(":")[1].strip("//")
                try:
                        port = line.split()[3].split(":")[2]
                except IndexError:
                        # defaulting to 9100
                        # port is not defined for the socket
                        print(name)
                        port = 9100
                printers.append({"name": name, "port": int(port)})
        return printers
print(gather_printers())