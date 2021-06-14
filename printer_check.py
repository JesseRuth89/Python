#!/usr/bin/env python3
import subprocess
import logging
import socket
import time
import concurrent.futures
import os


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
        logging.debug(f'Printer being parsed:{line}')
        try:
            name = line.split()[3].split(":")[1].strip("//")
            logging.debug(f'Printer being appended:{name}')
            printers.append(name)
        except:
            logging.warning(f'Unable to parse {line}')
    return printers


def port_check(address, port):
    s = socket.socket()
    s.settimeout(.5)
    try:
        s.connect((address, port))
        logging.info(f'Connected to {address} over {port}')
    except OSError:
        logging.warning(f'Failed to connect to {address} over {port}')


def main():
    # creating log in current working dir
    logging.basicConfig(
        filename='printer_check.log',
        # new log file each run
        filemode='w',
        level=logging.DEBUG
    )
    logging.info('Printer check started')
    print('Gathering system printer(s)...')
    # printers = gather_printers()
    port = 22
    printers = ['shsohapp1', 'shsohapp2', 'shsohapp3', 'baycflapp1', 'baycfldb4']
    print(f'{len(printers)} printer(s) defined on this system')

    # multi-threading port_check via executor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        [executor.submit(port_check, printer, port) for printer in printers]

    logging.info('Printer check ended')
if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Finished in: {round(end - start, 2)} second(s)')
    # debug this message
    logging.debug(f'Finished in: {round(end - start, 2)} second(s)')
