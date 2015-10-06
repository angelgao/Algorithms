"""
Problem:    Given two strings A, B. Find if there is a
            substring that appears in both A and B.

Input:      First line will contain number of tests (t),
            Then followed by t tests with each word on a new line.

Output:     YES / NO
"""

def TwoStrings(a, b):
    set_a = set(list(a))
    set_b = set(list(b))
    return len(set.intersection(set_a,set_b))

t = int(raw_input())
for i in xrange(t):
    a = raw_input()
    b = raw_input()
    if TwoStrings(a,b) == 0:
        print "NO"
    else:
        print "YES"
