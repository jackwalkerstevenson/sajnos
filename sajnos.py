"""Replace 's' characters with long s 'ſ'

Arguments:
filename -- path/name of input file

Replaces 's' characters in a file with long s 'ſ' according to the
18th-century rules described on Wikipedia.
-replace s with ſ except:
-always round s at end of word (except abbreviations, but not handling this)
-always round s before apostrophe
-always round s adjacent to f

Output is a file with '_long' appended to the root of the filename.
"""
import sys
import string
import os


def replace(i, char):
    if char == 's':
        try:  # set previous char
            prev_char = line[i-1]
        except IndexError:
            prev_char = 'x'  # if first char, dummy previous char
        try:  # set next char
            next_char = line[i+1]
        except IndexError:
            next_char = ' '  # if last char, whitespace next char for s
        try:
            next_next_char = line[i+2]  # set two chars down
        except IndexError:
            # if no next-next, dummy space so terminal ' doesn't preserve s
            next_next_char = ' '
        # preserve s before and after 'f'
        if next_char == 'f' or prev_char == 'f':
            return char
        # preserve s before apostrophes in middle of words
        if next_char == "'" and next_next_char in string.ascii_letters:
            return char
        # replace s if not at end of word
        if next_char in string.ascii_letters:
            return replacement_char
        else:
            return char
    else:
        return char


filename = sys.argv[1]  # input corpus
root, ext = os.path.splitext(filename)
with open(filename, 'r') as f:
    corpus = f.readlines()
lines = []  # list of output lines

replacement_char = 'ſ'
for line in corpus:
    result = ''
    for i, char in enumerate(line):  # check each char for replacement
        result += (replace(i, char))
    lines.append(result)
with open(root + '_long' + ext, 'w') as f:
    f.writelines(lines)
