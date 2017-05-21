#!/usr/bin/python

# each "file scanned" becomes an array of Findings.
# each Report contains multiple arrays of Findings.

class Finding:
  def __init__(self,finding,filename,location,critical=False,description=""):
    self.finding = finding
    self.filename = filename
    self.location = location
    self.critical = critical
    self.description = description

class Report:
  def __init__(self):
    self.findings = {}

  def addFindings(self,filename,findinglist):
    if filename not in self.findings.keys():
      self.findings[filename] = findinglist
    else:
      self.findings[filename].append(findinglist)
