#!/usr/local/bin/python2.7
import morse

try:
  assert '...---... ...---...' == morse.alpha_to_morse('sos sos')
  print 'alpha_to_morse() OK'
except:
  print 'alpha_to_morse() FAIL'
