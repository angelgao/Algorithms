"""
Permuation

Given two integer arrays of size N, design a
subquadratic algorithm to determine whether one
is a permutation of the other.
(ie. they contain exactly same entries, but possibly
different order)
"""
from InsertionSort import InsertionSort

def Permutation(a,b):
    if len(a) != len(b): return False
    InsertionSort(a)
    InsertionSort(b)
    
    for i in range(0, len(a)):
        if a[i] != b[i]: return False

    return True

""" TESTS """

a1 = [1,2,3,4]
b1 = [1,2,3]
assert Permutation(a1,b1) == False

a2 = [1,2,3,4]
b2 = [4,3,2,1]
assert Permutation(a2,b2) == True

a3 = [0,4,3,0]
b3 = [3,4,0,0]
assert Permutation(a3,b3) == True
