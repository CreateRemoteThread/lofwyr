#!/usr/bin/python

import lofwyr
import sys
import os
import getopt

def usage():
  print " [+] usage: %s [directoryName]" % sys.argv[0]

if __name__ == "__main__":
  try:
    opt,args = getopt.getopt(sys.argv[1:],"h",["help","repo=","report="])
  except getopt.GetoptError as err:
    print " [x] %s" % str(err)
    sys.exit(0)
  argRepo = None
  argReport = None
  argTarget = None
  for o,a in opt:
    if o in ("-h","--help"):
      usage()
      sys.exit(0)
    elif o == "--repo":
      argRepo = a
    elif o == "--report":
      argReport = a
    elif o == "--target":
      argTarget = a 
  parseEngine = lofwyr.Engine()
  reportObject = parseEngine.review(argRepo)
  if reportObject.isBuildBreaking():
    sys.exit(1)
  else:
    sys.exit(0)
