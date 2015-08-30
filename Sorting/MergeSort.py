"""
Merge Sort
Best:  O(NlogN)
Worst: O(NlogN)
"""

def merge(arr1, arr2):
    m_arr = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if (i >= len(arr1)):
            m_arr.extend(arr2[j:])
            break
        elif(j >= len(arr2)):
            m_arr.extend(arr1[i:])
            break
        elif arr1[i] < arr2[j] :
            m_arr.append(arr1[i])
            i += 1
        else:
            m_arr.append(arr2[j])
            j += 1
    return m_arr

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    s_arr1 = MergeSort(arr1)
    s_arr2 = MergeSort(arr2)
    return merge(s_arr1, s_arr2)

"""TEST"""
arr = [3,1,2]
s_arr = MergeSort(arr)
assert s_arr == [1,2,3]

arr = [0, -1, 0, 5, 10, 111, -243]
s_arr = MergeSort(arr)
assert s_arr == [-243, -1, 0, 0, 5, 10, 111]
