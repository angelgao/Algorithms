"""
Selection in Two Arrays:

Given two sorted arrays a[],b[] of size N and M. Find the K-th
largest element.
Complexity: O(logP) where P = N + M
"""

def Select_rec(a,b,k):
    if len(a) == 0: return b[k]
    if len(b) == 0: return a[k]

    mid_a = len(a) / 2
    mid_b = len(b) / 2

    if mid_a + mid_b < k:
        if a[mid_a] > b[mid_b]:
            return Select_rec(a, b[mid_b+1:], k-mid_b-1)
        else:
            return Select_rec(a[mid_a+1:], b, k-mid_a-1)
    else:
        if a[mid_a] > b[mid_b]:
            return Select_rec(a[:mid_a], b, k)
        else:
            return Select_rec(a, b[:mid_b], k)

"""TEST"""
a = [0,1,2,3,4]
b= [6,7,10]
assert Select_rec(a,b,4) == 4
assert Select_rec(a,b,5) == 6

a = [0,1,2,3,4]
b= [2,3,4,6,7,10]
assert Select_rec(a,b,4) == 3
assert Select_rec(a,b,6) == 4


"""Older code that is more simple but handles less cases"""
def Select(a, b, k):
    if a[k] <= b[0] : return a[k]
    elif b[k] <= a[0] : return b[k]
    elif a[k] > b[0]:
        i = 0
        while(a[k] > b[i]):
            i += 1
            k -= 1
        return a[k]
    elif b[k] > a[0]:
        i = 0
        while(b[k] > a[i]):
            i += 1
            k -= 1
        return b[k]

"""TEST"""
a = [0,1,2,3,4]
b= [6,7,10]
assert Select(a,b,4) == 4

a = [0,1,2,3,4]
b= [2,3,4,6,7,10]
assert Select(a,b,4) == 3
