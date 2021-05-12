'''
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer
Plan:
initialize an empty dictionary  char = {char -> index}
'''

def csFirstUniqueChar(input_str):
    charIndex = {}

    for c in (input_str):
        charIndex[c] = charIndex.get(c, 0) +1
    for c, j in enumerate(input_str):
        if charIndex[j] == charIndex[j] == 1:
            return c
    return -1
        
