#!/usr/bin/python

import sys
import re
import os, fnmatch
import imp
# import general
# import importlib

# a = imp.load_source('general','lofwyr/general.py').ScanEngine()

def find_files(directory, pattern):
  for root, dirs, files in os.walk(directory):
    for basename in files:
      if fnmatch.fnmatch(basename, pattern):
        filename = os.path.join(root, basename)
        yield filename

def init_langdb():
  f = open("lang.db","r")
  data = f.readlines()
  langdb = {}
  for line in data:
    (extension, description, module) = line.rstrip().split(",")
    langdb[extension] = (description, module)
  return langdb

class Engine:
  def __init__(self):
    self.langdb = init_langdb()
    self.scanmodules = {}

  def review(self,dirname):
    for f in find_files(dirname,"*.*"):
      filex = open(f,"r")
      fdata = filex.read()
      for lang in self.langdb.keys():
        if fnmatch.fnmatch(f,lang):
          (desc,module) = self.langdb[lang]
          if module in self.scanmodules.keys():
            if self.scanmodules[module] != None:
              self.scanmodules[module].scan(fdata)
          else:
            try:
              self.scanmodules[module] = imp.load_source(module,"lofwyr/%s.py" % module).ScanEngine()
            except:
              print " [!] module %s not implemented" % (module)
              self.scanmodules[module] = None
              continue
            self.scanmodules[module].scan(fdata)
      filex.close()    
