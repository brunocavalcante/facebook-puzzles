#dancebattle.py
import sys, re

data = open(sys.argv[1], 'r')
total_of_moves = int(data.readline())
total_of_turns = int(data.readline())

winner = False 
used_turns = []
used_moves = []
i = 1
try:
    for line in data.readlines():
        turn = re.split('\s*', line.rstrip())
        if len(used_turns) > 0 and turn[0] != used_turns[-1][0]:
            print "Invalid turn: 1st move should be == to last turn's move"
            raise
        for used_turn in used_turns:
            if len(set(turn).intersection(set(used_turn))) == 2:
                print "Repeated move."
                raise
        for move in turn:
            if move not in used_moves:
                used_moves.append(move) 
        used_turns.append(turn)
        i += 1
except:
    if i % 2 == 0:
        winner = True

if not winner:
    if (i + total_of_moves - len(used_moves)) % 2 == 0:
        winner = True

if winner:
    print "Win"
else:
    print "Lose"

print "Used moves: ", len(used_moves)
