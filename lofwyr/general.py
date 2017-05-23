#!/usr/bin/python

import re
import lofwyr.report

ruleset = []
ruleset.append( (re.compile("BEGIN RSA PRIVATE KEY"),True) )
ruleset.append( (re.compile("Password:"),True) )

class ScanEngine:
  def __init__(self):
    print " [!] general scan engine initializing"
    self.amazon_key = re.compile("")
    pass

  def scan(self,data):
    findings = []
    for (rule,criticality) in ruleset:
      result = rule.search(data)
      if result is not None:
        findings.append(lofwyr.report.Finding("Finding",critical=True))
    return findings
