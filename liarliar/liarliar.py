#liarliar.py
import sys

data = open('data.txt', 'r')
liars = {}
accuser = None
for line in data:
	columns = line.rstrip().split('   ')
	if (len(columns) == 2):
		accuser = columns[0]
		if (not(accuser in liars)):
			liars[accuser] = "false"
	elif (not(columns[0].isdigit())):
		person = columns[0]
		if (accuser and liars[accuser] == "false"):
			liars[person] = "true"
		else:
			liars[person] = "false"
	else:
		accuser = None

number_of_liars = liars.values().count("true")
print number_of_liars, len(liars)-number_of_liars
