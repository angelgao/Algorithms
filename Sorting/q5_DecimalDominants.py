"""
Decimal Dominants
Given an array with N keys, find all values
that occur more than N/10 times.

Complexity: O(N)
"""

def Dominants(arr):
    vals = []
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max : max = i
        if i < min : min = i
    offset = min
    #create an array such that each index corresponds to a number
    buckets = [0] * (max - min + 1)

    for a in arr:
        buckets[a-offset] += 1
    n = len(arr) / 10
    for i in range(len(buckets)):
        if buckets[i] >= n: vals.append(i+offset)
    return vals

"""TESTS"""
arr = [-1,2,2,5,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
assert Dominants(arr) == [2,5]
