#!/usr/bin/python
import random
def convert(a,b):
  total = []
  add = a%b
  if a<=1:
    total.append(a)
    return total
  else:
    total.extend(convert(a//b,b))
    total.append(add)
    return total
def format(given):
  if given[0] == 1:
    coefficient = ''
  else:
    coefficient = str(given[0])
  total = coefficient + "x^" + str(len(given)-1)
  for i in range(1,len(given)-2):
    if given[i] != 0:
      if given[i] == 1:
	coefficient = ''
      else:
	coefficient = str(given[i])
      total += "+" + coefficient + "x^" + str(len(given) - i - 1)
  if given[len(given) - 2] != 0:
      if given[len(given) - 2] == 1:
	coefficient = ''
      else:
	coefficient = str(given[len(given) - 2])
      total += "+" + coefficient + "x^" + str(len(given) - i - 1)
  i = given.pop()
  if i != 0:
    total += "+" + str(i)
  return total
print "Have your polynomial ready?"
print "Remember, the coefficients must be positive and integers"
base = int(raw_input("Can you tell me what f(1) is?"))
random.seed()
base = random.randint(0,14) + base
working = int(raw_input("Can you tell me what f(" + str(base) + ") is?"))
print(convert(working, base))
output = format(convert(working, base))
print output
raw_input("okay?")
