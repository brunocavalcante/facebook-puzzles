#dancebattle.py
import sys, re, itertools

data = open(sys.argv[1], 'r')
total_of_moves = int(data.readline())
total_of_turns = int(data.readline())

winner = False 
used_turns = []
used_moves = []
try:
    for line in data.readlines():
        turn = re.split('\s*', line.rstrip())
        turn[0] = int(turn[0])
        turn[1] = int(turn[1])
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

    turns = []
    for c in itertools.combinations_with_replacement(range(total_of_moves), 2):
        turns.append(list(c))

    while len(used_turns) < len(turns):
        found_combination = False
        for t in turns:
            t_inverted = [t[1], t[0]]
            if t not in used_turns and t_inverted not in used_turns and used_turns[-1][1] in t:
                found_combination = True
                if t[0] == used_turns[-1][1]:
                    used_turns.append(t)
                else:
                    used_turns.append(t_inverted)
                break
        if not found_combination:
            print "No play available."
            raise
except:
    if len(used_turns) % 2 == 1:
        winner = True

if winner:
    print "Win"
else:
    print "Lose"

print "Plays: ", used_turns
print "Used moves: ", len(used_moves)
