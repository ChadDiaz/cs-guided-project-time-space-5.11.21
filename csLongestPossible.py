"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"

csLongestPossible("abc", "abc") -> "abc"
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string

Understand:
(a) (aeeddf)
---> "aedf"

Plan:
initialize an empty list    output = []

"""

def csLongestPossible(str_1, str_2):
    """
    str_1 = a d b b b e f f 
    newString1 = a d b e f

    str_2 = i i u y t r e e
    newString2 = i u y t r e
    """
    uniString1 = set(str_1)
    uniString2 = set(str_2)
    uniString1.update(uniString2)
    

    finalString = list(uniString1)
    finalString.sort()

    return "".join(finalString)

    
