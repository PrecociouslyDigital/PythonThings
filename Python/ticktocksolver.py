#!/usr/bin/python
import os
import sys
if sys.platform.startswith("win"):
	import winsound

secretz = [(1, 2), (2, 3), (8, 13), (4, 29), (130, 191), (343, 397), (652, 691), (858, 1009),
           (689, 2039), (1184, 4099), (2027, 7001), (5119, 10009), (15165, 19997), (15340, 30013),
           (29303, 70009), (42873, 160009), (158045, 200009)]
done = []
def beep():
	if sys.platform.startswith("linux"):
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1, 300))	
	elif sys.platform.startswith("win"):
		winsound.beep(300,1)
for i in xrange(100,2147483647):
	works = 1
	for (r,m) in secretz:
  		if (200009*i+158045)%m != r:
    			#print str(130*i+191) +  "doesn't work for" + str(r) + "," + str(m)
			works = 0
			break
		else:
			if m not in done:
				done.append(m)
				print str(200009*i+158045) + " mod " + str(m) + " is " + str(r) + " and all of the above"
				beep()

	if works == 1:
		print str(i) + "works"
		beep()
		break
print "Done!"
beep()
