from itertools import permutations

# Constants for word length and fixed letters positions
WORD_LENGTH = 5
FIXED_LETTERS = {'O': 2, 'A': 4}

# Given letters and fixed letters at specified positions
available_letters = ['A', 'R', 'R', 'G', 'E', 'L', 'Y']
fixed_letters = {'O', 'A'}

# Generate all unique permutations of the available letters
letter_permutations = set(permutations(available_letters, WORD_LENGTH - len(FIXED_LETTERS)))

# Check each permutation for fixed letters in the specified positions and form words
scrabble_words = []
for perm in letter_permutations:
    word = list(perm)
    for letter, position in FIXED_LETTERS.items():
        word.insert(position, letter)
    if len(word) == WORD_LENGTH:
        scrabble_words.append(''.join(word))

print(f"Possible {WORD_LENGTH}-letter words with fixed letters at specified positions:")
print(scrabble_words)
