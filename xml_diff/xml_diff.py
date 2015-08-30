#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET
from colordiff import color_diff_strings

class HadoopProperty(object):
  def __init__(self, name, value, final):
    self._name = name
    self._value = value
    self._final = final

  @property
  def name(self):
    return self._name

  @property
  def value(self):
    return self._value

  @property
  def final(self):
    return self._final

a = {}
b = {}

tree = ET.parse(sys.argv[1])
root = tree.getroot()
for child in root:
  name = child.find('name').text
  value = child.find('value').text
  final = child.findtext('final', 'false').lower()
  if name in a:
    print "WARNING: {0} appears more than once in {1}".format(name, sys.argv[1])
  a[name] = HadoopProperty(name, value, final)

tree = ET.parse(sys.argv[2])
root = tree.getroot()
for child in root:
  name = child.find('name').text
  value = child.find('value').text
  final = child.findtext('final', 'false').lower()
  if name in b:
    print "WARNING: {0} appears more than once in {1}".format(name, sys.argv[2])
  b[name] = HadoopProperty(name, value, final)

for name in a:
  if name not in b:
    print "Only in L: {0} -> {1}".format(name, a[name].value)

for name in b:
  if name not in a:
    print "Only in R: {0} -> {1}".format(name, b[name].value)

for name in a:
  if name in b:
    out_text = ""
    if a[name].final != b[name].final:
      out_text += " Finality differs:\tL:{0} R:{1}\n".format(a[name].final, b[name].final)
    if a[name].value != b[name].value:
      (diffa,diffb) = color_diff_strings(a[name].value, b[name].value)
      out_text += " L:\t{0}\n R:\t{1}\n".format(diffa, diffb)
    if out_text:
      print "Diff {0}:\n{1}".format(name, out_text)
