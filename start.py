#!/usr/bin/python

import lofwyr
import sys
import os
import getopt

def usage():
  print " [+] usage: %s [directoryName]" % sys.argv[0]

if __name__ == "__main__":
  if len(sys.argv) != 2:
    usage()
    sys.exit()
  else:
    parseEngine = lofwyr.Engine()
    parseEngine.review(sys.argv[1])
