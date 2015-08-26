"""
Selection Sort
Best : O(N^2)
Worst: O(N^2)

"""

def SelectionSort(lst):
    n = len(lst)
    for i in xrange(0,n):
        min = i
        for j in xrange(i,n):
            if lst[j] < lst[min]: min = j
        #swap i and min
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp


"""Test"""
lst = [4,5,10,-1,0,111]
SelectionSort(lst)
assert lst == [-1,0,4,5,10,111]
