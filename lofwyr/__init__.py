#!/usr/bin/python

import sys
import re
import os, fnmatch
import imp
import socket

textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# initial sort

WEB_TARGET=1
FILE_TARGET=2
DIR_TARGET=3
HOST_TARGET=4
UNKNOWN_TARGET=-1

def sort(in_arg):
  if ("http:" in in_arg) or ("https:" in in_arg):
    return WEB_TARGET
  if os.path.isfile(in_arg):
    return FILE_TARGET
  if os.path.isdir(in_arg):
    return DIR_TARGET
  try:
    socket.gethostbyname(in_arg)
    return HOST_TARGET
  except:
    return UNKNOWN_TARGET

def find_files(directory, pattern):
  for root, dirs, files in os.walk(directory):
    for basename in files:
      if fnmatch.fnmatch(basename, pattern):
        filename = os.path.join(root, basename)
        yield filename

if __name__ == "__main__":
  print " [!] this is not intended for direct use. please invoke start.py"
