#!/usr/bin/env python

from sys import argv, exit
from lib.colorp import printc
from os.path import isdir, isfile

if __name__ == "__main__":
    if len(argv) < 2:
        printc("No arguments!", 31)
        exit(1)
    
    usepath = argv[1]
    if not isdir(usepath) and not isfile(usepath):
        printc(f"Unable to determine file type of {usepath}!", 31)

