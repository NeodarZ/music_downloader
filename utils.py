import sys
import logging


def read_file(filename):
    lines = []

    if filename.is_dir():
        logging.fatal(f'{filename} is a folder instead of a file!')
        sys.exit(1)
    elif not filename.is_file():
        filename.touch()
    with open(filename) as filehandler:
        for line in filehandler.readlines():
            lines.append(line.strip())

    return lines

def write_file(filename, data):
    with open(filename, 'a') as filehandler:
        filehandler.write(data+'\n')