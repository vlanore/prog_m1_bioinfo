"""This script displays a bar plot of amino
acid counts in a fasta file"""

import read_fasta, matplotlib.pyplot, sys

sequence_list = read_fasta.read_fasta("data/example.fasta")

def count_letters(sequence):
    """Counts occurences of letters in sequence"""
    intermediate_result = {}
    for letter in sequence[1]:
        print(intermediate_result)
        letter_exists = letter in intermediate_result.keys()
        if not letter_exists:
            intermediate_result[letter] = 1
        else:
            intermediate_result[letter] += 1
    # intermediate_result = sorted(intermediate_result)
    return sorted(intermediate_result.items())

result = []
for sequence in sequence_list:
    count_dict = count_letters(sequence)
    letters = []
    counts = []
    for entry in count_dict:
        letters.append(entry[0])
        counts.append(entry[1])

    print(count_dict)
    print(letters)
    result.append((letters, counts))

matplotlib.pyplot.bar(result[0][0], result[0][1])
matplotlib.pyplot.bar(result[0][0], result[1][1], bottom=result[0][1])
matplotlib.pyplot.show()