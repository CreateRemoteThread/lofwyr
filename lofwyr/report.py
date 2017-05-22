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

  def isBuildBreaking(self):
    print self.findings
    for filename in self.findings.keys():
      for finding in self.findings[filename]:
        if finding.critical == True:
          return True
    return False

  def printReport(self):
    print "This is my report. Do with it what you will."
