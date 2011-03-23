#gattaca.py
import sys
import re
import itertools

#Opening the input file
data = open(sys.argv[1], 'r')

#Fetching the DNA string
dna_length = data.readline().rstrip()
dna = ''
while len(dna) < 100:
    dna = dna + data.readline().rstrip()

#Fetching the predictions
data.readline() #won't need the length of predictions

predictions = [re.split('\s*', l.rstrip()) for l in data.readlines()]

def create_range_for_prediction(prediction):
    return set(range(int(prediction[0]), int(prediction[1]) + 1))

def prediction_is_available(prediction, ranges_used):
    prediction_range = create_range_for_prediction(prediction)
    for range_used in ranges_used:
        if len(range_used.intersection(prediction_range)) > 0:
            return False
    return True

totals = []
for permutation in itertools.permutations(predictions):
    ranges_used = []
    i_total = 0
    for i in permutation:
        if prediction_is_available(i, ranges_used):
            i_total = i_total + int(i[2])
            ranges_used.append(create_range_for_prediction(i))
    totals.append(i_total)

print max(totals)
