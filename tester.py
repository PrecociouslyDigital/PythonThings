#!/usr/bin/python
import fileinput
import random
charsets = []
wrongs = []
for line in fileinput.input(raw_input("file?\n")):
  line = line.split(" ",1)
  line[1] = line[1].rstrip("\n")
  charsets.append(line)
charsets.reverse()
#print charsets
surround = charsets.pop()
random.shuffle(charsets)
while charsets:
  test = charsets.pop()
  print surround[0] +" "+ test[0] +" "+ surround[1] +"\n"
  if test[1] == raw_input():
    print "Correct!\n"
  else:
    charsets.append(test)
    random.shuffle(charsets)
    if wrongs.count(test[1]) == 0:
      wrongs.append(test[1])
    print "Wrong: Correct answer was " + test[1]
    
print "Missed: " + str(wrongs)