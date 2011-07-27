#dancebattle.py
import sys, re, itertools

data = open(sys.argv[1], 'r')
total_of_moves = int(data.readline())
total_of_turns = int(data.readline())

total_of_possible_turns = 0
for c in itertools.combinations_with_replacement(range(total_of_moves), 2):
    total_of_possible_turns += 1 

print "Total de combinacoes possiveis", total_of_possible_turns

winner = False 
used_turns = []
used_moves = []
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

    if (len(used_turns) + total_of_moves - len(used_moves)) % 2 == 0:
        winner = True
except:
    if len(used_turns) % 2 == 0:
        winner = True

if winner:
    print "Win"
else:
    print "Lose"

print "Used moves: ", len(used_moves)
