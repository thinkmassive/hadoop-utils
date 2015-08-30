#!/usr/bin/python

class AnsiGenerator(object):
  """
  AnsiGenerator - Dirt-simple class for generating strings with ANSI
  terminal escape codes.
  
  Usage:

  # Create a AnsiGenerator object
  ag = AnsiGenerator()

  # Produce and print some colored strings.  Combine attributes
  # by chaining them together.  Pass a string to the last
  # attribute to get the printable string:
  print ag.faint.on_blue.red("This is red text")
  print ag.bold.underline('foo')

  # Note you must pass the string to the last call in the chain.
  # This is right out and will produce an AttributeError:
  print ag.bold("My string").underline

  # You can also pre-create an AnsiGenerator with certain attributes.
  # Just don't pass a string to the last attribute and you will get
  # an AnsiGenerator loaded with those attributes
  bup = ag.bold.underline

  # AnsiGenerator objects are callable.  Just call it and pass the string
  # you want to print
  print bug('This is a test in bold underline')

  # or stack more attributes on it
  print bug.red('This is a test in bold underlined red')

  """
  ESCAPE = chr(033)
  ATTRS = {
     'clear':        0,
     'reset':        0,
     'bold':         1,
     'dark':         2,
     'faint':        2,
     'underline':    4,
     'underscore':   4,
     'blink':        5,
     'reverse':      7,
     'concealed':    8,
     'black':   30,   'on_black':    40,
     'red':     31,   'on_red':      41,
     'green':   32,   'on_green':    42,
     'yellow':  33,   'on_yellow':   43,
     'blue':    34,   'on_blue':     44,
     'magenta': 35,   'on_magenta':  45,
     'cyan':    36,   'on_cyan':     46,
     'white':   37,   'on_white':    47
  }

  def __init__(self, stack=[]):
    self._stack = stack

  def __call__(self, s):
    tmp_stack = list(self._stack)
    codes = ';'.join(map(lambda x: str(x), tmp_stack))
    return "{0}[{1}m{0}[K{2}{0}[m{0}[K".format(AnsiGenerator.ESCAPE, codes, s)

  def __getattr__(self, name):
    if name not in AnsiGenerator.ATTRS:
      raise AttributeError("ANSI attribute '{0}' not supported!".format(name))

    tmp_stack = list(self._stack)
    tmp_stack.append(AnsiGenerator.ATTRS[name])
    return AnsiGenerator(stack=tmp_stack)
