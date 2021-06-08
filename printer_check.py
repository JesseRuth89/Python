#!/usr/bin/env python3
import subprocess
import socket
import time
import concurrent.futures


def gather_printers() -> list:
    output = subprocess.Popen(["lpstat", "-v"],
                              universal_newlines=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    # execute lpstat
    out, err = output.communicate()
    printers = []
    # for each line gather name and port
    for line in out.splitlines():
        try:
            name = line.split()[3].split(":")[1].strip("//")
            printers.append(name)
        except:
            print(f'****Check into {line}****')
    return printers


def port_check(address):
    s = socket.socket()
    s.settimeout(0.2)
    try:
        s.connect((address, 9100))
        # return f'Connected to {address} on port 9100'
    except OSError:
        return f'Failed to connect to {address}'


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(port_check, printer) for printer in gather_printers()]
        for result in concurrent.futures.as_completed(results):
            print(result.result())

    end = time.perf_counter()
    print(f'Finished in: {round(end - start, 2)} second(s)')
