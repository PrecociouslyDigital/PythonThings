#!/usr/bin/python
import fileinput
charsets = [[0 for x in xrange(5)] for x in xrange(5)] 
def convertInto(plaintext, charset):
  message = [len(plaintext)]
  for x in range(0,len(plaintext)):
    for y in xrange(0,len(charset)):
      if plaintext[x] == charset[y]:
	message[x] = y
  return message
def convertOut(text, charset):
  message = ""
  for x in range(0,len(text)):
    for y in xrange(0,len(charset)):
      if text[x] == charset[y]:
	message += charset[y]
  return message
def encrypt(text, key, charset, mode):
  text = convertInto(text, charset)
  key = convertInto(key, charset)
  if mode == 1:
    multiplier = 1
  elif mode == 2:
    multiplier = 1
  else:
    multiplier = -1
  prevchar = 0
  for pos in range(0,len(text)):
    if mode % 2 == 0:
      prevchar = text[pos]
    text[pos] += key[pos%len(key)] * multiplier + prevchar * multiplier
  return convertOut(text, charset)
for line in fileinput.input("charset.txt"):
  charsets.append(line.split(" ", 2))
print "list of charsets"
for ewr in charsets:
  print str(ewr[0])
charset = raw_input("Which charset?")
for ewr in charsets:
  if ewr[0] == charset:
    charset = ewr[1]
print "charset is" + charset
supermode = raw_input("Activate super secure mode?\nSuper secure mode adds the value of the previous character to the next\nyes/no  ")
key = raw_input("key?")
message = raw_input("message?")
mode = raw_input("Encrypt or Decrypt?")
key.upper()
message.upper()
werw = 0
if mode == "encrypt":
  werw = 2
if supermode =="yes":
  werw += 1
print encrypt(message, key, charset, werw)