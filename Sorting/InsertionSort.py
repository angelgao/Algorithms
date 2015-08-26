"""
Insertion Sort
Best : O(N) - for partially sorted arrays
Worst: O(N^2)

Note: 
This algorithm can be changed to ShellSort by 
changing the increment at which the swap happens.
It is faster because when we are sorting the array by 
increments of h, less swapping happens.
Then by gradually decreasing h until it reaches 1,
we make the array more and more partially sorted.
So when h decreases to 1, it is almost linear time to sort the array
"""


def InsertionSort(arr):
    n = len(arr)
    for i in range(0,n):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
             #swap i and j
             temp = arr[i]
             arr[i] = arr[j]
             arr[j] = temp
             i = j
             j = i - 1

"""Test"""
lst = [4,5,10,-1,0,111]
InsertionSort(lst)
assert lst == [-1,0,4,5,10,111]
