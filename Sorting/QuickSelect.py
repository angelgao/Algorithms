"""
Quick Select
Problem: Given an array of numbers, find the N largest element
         in the array.

Implementation: Using partition from QuickSort, and only traverse
                to the side of the parition where N can be.

Complexity: Best - O(N) on average, Worst - O(N^2)

"""

def Partition(arr, start, end):
    pivot = arr[start]
    i = start
    j = end
    while (True):
        while(arr[i] <= pivot):
            i += 1
            if i == end: break
        while(arr[j] >= pivot): 
            j -= 1
            if j == start: break

        if (i >= j): break
        arr[i], arr[j] = arr[j], arr[i] #swap i and j
    
    arr[start], arr[j] = arr[j], arr[start]
    return j


"""
input:  An array of ints
Output: The nth largest element
"""
def Select(arr, n):
    lo = 0
    hi = len(arr) - 1
    while ( hi > lo):
        j = Partition(arr, lo, hi)
        if (n > j): lo = j + 1
        elif (n < j): hi = j - 1
        else: return arr[n]
    return arr[n]

"""TEST"""
arr = [0,4,2,0,1]
assert Select(arr, 0) == 0
assert Select(arr, 1) == 0
assert Select(arr, 2) == 1
assert Select(arr, 3) == 2
assert Select(arr, 4) == 4
