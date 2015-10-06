"""
Problem: Given a string, return whether the brackets match.

Input:   String
Output:  T/F
"""

def Brackets(s):
    s_arr = list(s)
    sum = 0
    for i in s_arr:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
            if sum < 0: return False

    return sum == 0

str = raw_input()
print Brackets(str)
