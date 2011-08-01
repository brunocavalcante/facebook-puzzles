#liarliar.py
import sys

data = open(sys.argv[1], 'r')
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

total_liars = liars.values().count("true")
total_nonliars = abs(len(liars) - total_liars)
print max(total_liars, total_nonliars), min(total_liars, total_nonliars)
