"""
Problem:    Giving a string, and a pattern where each letter represents
            a specific word. Return whether the string matches the pattern.
"""

def Pattern(s, pattern):
    arr = s.split(" ")
    p = list(pattern)
    d = {}
    if len(arr) != len(p): return False

    for i in xrange(len(arr)):
        if p[i] in d:
            if arr[i] != d[p[i]]:
                return False
        else:
            d[p[i]] = arr[i]
    return True

""" INPUT """
s = raw_input()
pattern = raw_input()
print Pattern(s, pattern)


