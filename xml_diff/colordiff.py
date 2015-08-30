#!/usr/bin/python

from difflib import SequenceMatcher
from ansigenerator import AnsiGenerator

ADDTEXT = AnsiGenerator().green.bold
DELETETEXT = AnsiGenerator().red.bold
FILLTEXT = AnsiGenerator().on_yellow.bold

def color_diff_strings(a, b):
  sm = SequenceMatcher(isjunk=lambda x: False, a=a, b=b, autojunk=False)

  outa = ''
  outb = ''

  for op in sm.get_opcodes():
    opcode = op[0]
    a1 = op[1]
    a2 = op[2]
    b1 = op[3]
    b2 = op[4]
    if opcode == 'replace':
      outa += DELETETEXT(a[a1:a2])
      outb += ADDTEXT(b[b1:b2])

    if opcode == 'delete':
      outa += DELETETEXT(a[a1:a2])
      outb += FILLTEXT(' ' * (a2-a1))

    if opcode == 'insert':
      outa += FILLTEXT(' ' * (b2-b1))
      outb += ADDTEXT(b[b1:b2])

    if opcode == 'equal':
      outa += a[a1:a2]
      outb += b[b1:b2]

  return (outa, outb)
