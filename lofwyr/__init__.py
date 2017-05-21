#!/usr/bin/python

import sys
import re
import glob
import rulesengine

class Engine:
  def __init__(self):
    pass

  def review(self,dirname):
    for filename in glob.iglob("%s/**/*" % dirname,recursive=True):
      print filename 
