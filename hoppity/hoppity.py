#hoppityhop.py
import sys

def hoppity_hop(number):
	if (not(number % 3) and not(number % 5)):
		print "Hop"
	elif (not(number % 3)):
		print "Hoppity"
	elif (not(number % 5)):
		print "Hophop"

for i in range(1, int(sys.argv[1])):
        hoppity_hop(i)
