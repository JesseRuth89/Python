#!/usr/bin/env python3
"""
NAME:
    printer_port_check.py
AUTHOR:
    Jesse Ruth (jr019593) -CWx
SYNOPSIS:
    Parses lpstat for defined printers and checks connectivity against -port [default 9100]
"""
import subprocess
import logging
import socket
import time
import concurrent.futures
import os
import argparse


def define_logging(default):
    # creating log in current working dir
    if default > 20:
        default = 10
    logging.basicConfig(
        filename='printer_port_check.log',
        # new log file each run
        filemode='w',
        level=default
    )


def define_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=9100, help='port used to check against, default 9100')
    parser.add_argument('-v', '--verbose', action='count', default=20, help='debug messages')
    return parser.parse_args()


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
    directory_path = os.getcwd()
    # get parser options
    args = define_parser()
    # set logging
    define_logging(args.verbose)
    print(f"Log file created {directory_path}/printer_port_check.log")
    print()

    logging.info('Printer check started')
    print('Gathering system printer(s)...')
    printers = gather_printers()
    print(f'{len(printers)} printer(s) defined on this system')
    print()

    # multi-threading port_check via executor
    print(f'Checking printers against port {args.port}')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        [executor.submit(port_check, printer, args.port) for printer in printers]
    print(f'Check {directory_path}/printer_port_check.log for results')
    print()
    logging.info('Printer check ended')


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Finished in: {round(end - start, 2)} second(s)')
    # debug this message
    logging.debug(f'Finished in: {round(end - start, 2)} second(s)')
