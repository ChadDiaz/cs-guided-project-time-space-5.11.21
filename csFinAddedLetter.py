'''
You are given two strings, str_1 and str_2, where str_2 is generated by randomly shuffling str_1 and then adding one letter at a random position.

Write a function that returns the letter that was added to str_2.

Examples:

csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef") -> "f"
csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
csFindAddedLetter(str_1 = "bf", str_2 = "bfb") -> "b"

Notes:

str_1 and str_2 both consist of only lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string
1: a=10  b=20
2: a=10  b=20  c=30
1 total - 30
2 total - 60
str 2 - str 1 = 30 = c   
'''

def csFindAddedLetter(str_1, str_2):
    smallString = str_1
    largeString = str_2

    smallStringTotal = 0
    largeStringTotal = 0
    i = 0

    while(i < len(smallString)):
        smallStringTotal += ord(smallString[i])
        largeStringTotal += ord(largeString[i])
        i += 1
    
    largeStringTotal += ord(largeString[i])

    intChar = largeStringTotal - smallStringTotal
    return chr(intChar)

