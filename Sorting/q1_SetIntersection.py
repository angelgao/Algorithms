"""
Intersection of Two Sets

Given two arrays a[] and b[], each containing
N distinct 2D points in the plane, design a 
subquadratic algorithm to count the number of
points that are contained in both arrays
"""

from InsertionSort import InsertionSort

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, other):
        if self.x > other.x : return 1
        elif self.x < other.x : return -1
        else: return 0

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

def Intersection(a,b):
    InsertionSort(a);
    InsertionSort(b);
    n = i = j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            n += 1
            i += 1
            j += 1
    return n

""" TESTS """
#No Intersection
a1 = [Point(1,2), Point(2,3), Point(5,4)]
b1 = [Point(0,0), Point(4,5)]
assert Intersection(a1, b1) == 0

#Intersection non-sorted
a2 = [Point(4,3), Point(0,0), Point(5,5)]
b2 = [Point(0,0), Point(4,3), Point(1,1), Point(2,10)]
assert Intersection(a2,b2) == 2

#All the same
a3 = [Point(1,1), Point(2,2), Point(3,3)]
b3 = [Point(3,3), Point(1,1), Point(2,2)]
assert Intersection(a3,b3) == 3
