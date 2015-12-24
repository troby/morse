#!/usr/local/bin/python2.7
import re

a2m = {
  'A': '.-',     'B': '-...',   'C': '-.-.', 
  'D': '-..',    'E': '.',      'F': '..-.',
  'G': '--.',    'H': '....',   'I': '..',
  'J': '.---',   'K': '-.-',    'L': '.-..',
  'M': '--',     'N': '-.',     'O': '---',
  'P': '.--.',   'Q': '--.-',   'R': '.-.',
  'S': '...',    'T': '-',      'U': '..-',
  'V': '...-',   'W': '.--',    'X': '-..-',
  'Y': '-.--',   'Z': '--..',   '9': '----.',
  '0': '-----',  '1': '.----',  '2': '..---',
  '3': '...--',  '4': '....-',  '5': '.....',
  '6': '-....',  '7': '--...',  '8': '---..',

}


m2a = {
    '---': 'O',   '--.': 'G',   '-...': 'B',
   '-..-': 'X',   '.-.': 'R',   '--.-': 'Q',
   '--..': 'Z',   '.--': 'W',  '..---': '2',
     '.-': 'A',    '..': 'I',   '-.-.': 'C',
   '..-.': 'F',  '-.--': 'Y',      '-': 'T',
      '.': 'E',  '.-..': 'L',    '...': 'S',
    '..-': 'U', '.----': '1',  '-----': '0',
    '-.-': 'K',   '-..': 'D',  '----.': '9',
  '-....': '6',  '.---': 'J',   '.--.': 'P',
  '....-': '4',    '--': 'M',     '-.': 'N',
   '....': 'H', '---..': '8',   '...-': 'V',
  '--...': '7', '.....': '5',  '...--': '3',
}

def alpha_to_morse(msg):
  string=''
  for char in msg.strip():
    if re.match(' ', char):
      continue
    string += a2m[char.upper()]
    string += ' '
  return string.strip()

def morse_to_alpha(msg):
  string=''
  seq=msg.strip().split(' ')
  for char in seq:
    string += m2a[char]
    string += ' '
  return string.strip()

def main():
  msg = raw_input('MESSAGE: ')
  if re.match('^[A-Z ]+$', msg.upper()):
    print alpha_to_morse(msg)
  elif re.match('^[\.\- ]+$', msg.upper()):
    print morse_to_alpha(msg)
  else:
    print 'mixed chars detected: enter only alphanumeric, or morse code'
	
if __name__ == "__main__":
  main()
