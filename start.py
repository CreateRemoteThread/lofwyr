#!/usr/bin/python

import lofwyr
import sys
import os
import getopt

def usage():
  print " [+] usage: %s [directory/weburl/host]" % sys.argv[0]
  sys.exit(0)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    usage()
  sorttype = lofwyr.sort(sys.argv[1])
  if sorttype in (lofwyr.WEB_TARGET, lofwyr.HOST_TARGET):
    print " [+] web target not implemented yet"
    sys.exit(0)
    report = sourceEngine.report.report()
  elif sorttype in (lofwyr.DIR_TARGET, lofwyr.FILE_TARGET):
    sourceEngine = lofwyr.source.SourceEngine
    report = sourceEngine.review(sys.argv[1])
  if report.isBuildBreaking():
    report.printReport()
    sys.exit(0)
  else:
    sys.exit(0) 

