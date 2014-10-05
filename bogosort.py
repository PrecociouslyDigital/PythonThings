#!/usr/bin/python
from random import shuffle
count = int(raw_input("list size?"))
listed = []
for x in range(0,count): 
  listed.append(int(raw_input("item?")))
sortedList = sorted(listed)
print "We will now be idiots. In fact, I have an already sorted list to check against. I don't know why I'm doing this."
while listed != sortedList:
  shuffle(listed)
  print "Nope. " + str(listed) + " isn't sorted"
print "We finally got it. " + str(listed) + "is sorted"
