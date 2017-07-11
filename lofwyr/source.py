#!/usr/bin/python

import sys
import re
import os, fnmatch
import imp
import lofwyr.report

def init_langdb():
  with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "lang.db"), "r") as f:
    data = f.readlines()
  
  langdb = {}
  for line in data:
    (extension, description, module) = line.rstrip().split(",")
    langdb[extension] = (description, module)
  return langdb

# simple grep
class SourceEngine:
  def __init__(self):
    self.langdb = init_langdb()
    self.scanmodules = {}
    self.report = lofwyr.report.Report()

  def review(self,dirname):
    for f in lofwyr.find_files(dirname,"*"):
      f_findings = []
      filex = open(f,"r")
      fdata = filex.read()
      maxLen = min(1024,len(fdata))
      if lofwyr.is_binary_string(fdata[0:maxLen]):
        pass
      else:
        for lang in self.langdb.keys():
          if fnmatch.fnmatch(f,lang):
            (desc,module) = self.langdb[lang]
            if module in self.scanmodules.keys():
              if self.scanmodules[module] != None:
                # print "scanning with module %s" % module
                f_findings += self.scanmodules[module].scan(fdata)
            else:
              try:
                self.scanmodules[module] = imp.load_source(module,os.path.join(os.path.dirname(os.path.realpath(__file__)),"%s.py" % module)).ScanEngine()
              except:
                self.scanmodules[module] = None
                continue
              f_findings += self.scanmodules[module].scan(fdata)
      filex.close()
      if len(f_findings) != 0:
        self.report.addFindings(f,f_findings)
    return self.report
    
if __name__ == "__main__":
  print " [!] this is not intended for direct use. please invoke start.py"
