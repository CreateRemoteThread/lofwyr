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
    sys.exit(1)
  else:
    parseEngine = lofwyr.Engine()
    report = parseEngine.review(sys.argv[1])
    if report.isBuildBreaking():
      sys.exit(1)
    else:
      sys.exit(0)
