#!/usr/local/bin/python2.7
import morse

try:
  assert '... --- ... ... --- ...' == morse.alpha_to_morse('s o s s o s')
  print 'alpha_to_morse() OK'
except:
  print 'alpha_to_morse() FAIL'

try:
  assert 'S O S S O S' == morse.morse_to_alpha('... --- ... ... --- ...')
  print 'morse_to_alpha() OK'
except:
  print 'morse_to_alpha() FAIL'
