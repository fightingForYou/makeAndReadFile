#!/bin/env python

"makeTextFile.py --create text file"
import os
ls = os.linesep

def makeFile():
  #get filename
  while True:
    fname = raw_input('input your file name:')
    if os.path.exists(fname):
      print '123'
    else:
      break
  all = []
  print "\nenter lines ('.'to quit)"

  while True:
    entry = raw_input('input what you want to save:')
    if entry == '.':
      break
    else:
      all.append(entry)
  fobj = open(fname, 'w')
  fobj.writelines(['%s%s' % (x, ls) for x in all])
  fobj.close()
  print 'Done'

def readFile():
  fname = raw_input("input the file name:")

  print

  try:
    fobj = open(fname, 'r')
  except IOError, e:
    print "file open error:", e
  else:
    for line in fobj:
      print line
    fobj.close() 
while True: 
  choice = raw_input("input m to make file , r to read file, or q to quit: ")
  if choice == 'm':
     makeFile()
  elif choice == 'r':
     readFile()
  elif choice == 'q':
     print "thanks to use"
     break
  else:
     print "please input the right word: w q or r"

