#breathalizer.py
import sys

def number_of_changes(word1, word2):
	if word1 == word2:
		return 0 
        
	length_diff = abs(len(word1) - len(word2))

	changes = 0
	removals = 0
	for i in range(0, len(word1)):
		j = 0 if (i - removals == 0) else i - removals

		if j < len(word2) and word1[i] != word2[j]:
		    if len(word1) <= len(word2) or removals >= length_diff:
		        changes = changes + 1
		    else:
		        j = i + removals + 1
		        if j < len(word1) and i < len(word2) and word1[j] == word2[i]:
		            removals = removals + 1
		        else:
		            changes = changes + 1

	return changes + length_diff

wall_post = open(sys.argv[1], 'r')
wall_post_words = map(lambda l: l.rstrip().split(" "), wall_post.readlines())

accepted_words_file = open('twl06.txt', 'r')
accepted_words = map(lambda l: l.rstrip(), accepted_words_file.readlines())

total_of_changes = 0
for word in wall_post_words[0]:
    word_changes = None
    for accepted_word in accepted_words:
		changes = number_of_changes(word.upper(), accepted_word)
		if word_changes is None or changes < word_changes:
			word_changes = changes

    total_of_changes = total_of_changes + word_changes

print total_of_changes
