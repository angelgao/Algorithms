"""
Quick Sort:
Best : O(NlogN)
Worst: O(N^2) - a sorted/reversed sorted array
"""

def QuickSort(arr):
    #Should shuffle array to guarantee randomness
    Sort(arr, 0, len(arr)-1)

def Sort(arr, start, end):
    if (end <= start): return
    right = Partition(arr, start, end)
    Sort(arr, start, right-1)
    Sort(arr, right+1, end)

def Partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo
    j = hi
    while(True):
        while(arr[i] <= pivot): 
            i += 1
            if i == hi: break
        while(arr[j] >= pivot): 
            j -= 1
            if j == lo: break

        if i >= j : break       #check if ptrs cross

        arr[i], arr[j] = arr[j], arr[i]

    #swap lo and j
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

"""TEST"""
arr = [3,2,1,5,4]
QuickSort(arr)
assert arr == [1,2,3,4,5]

#duplicate keys
arr = [3,3,0,0, -1]
QuickSort(arr)
assert arr == [-1,0,0,3,3]
