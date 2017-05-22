#!/usr/bin/python

import re
import lofwyr.report

class ScanEngine:
  def __init__(self):
    print " [!] general scan engine initializing"
    self.amazon_key = re.compile("AKIA(0-9A-Za-z+?)")
    pass

  def scan(self,data):
    result = self.amazon_key.search(data)
    if(result.key())
    # print result
    return []
