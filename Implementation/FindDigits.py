"""
Problem:    Given an integer N. Find the digits in this
            number that exactly divide N and display their
            count.
            If a digit appears twice, it is counted twice

Input:      First line contains T (num test cases)
            Followed by T lines of integers N

Output:     For each test case, display the count of digits.
"""

def CountDigits(n):
    count = 0
    arr_n = list(str(n))
    for i in arr_n:
        if int(i) != 0:
            if n % int(i) == 0:
                count += 1

    return count

""" Input """
t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    print CountDigits(n)
