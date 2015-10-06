"""
Problem:    Given a word w, rearrange its letters to find the word
            s such that s is lexicographically greater than w. In
            the case that there are multiple, find the lowest.

Input:      An integer t for num of test cases, followed by t words.

Output:     The corresponding s

Note:       This function uses the next_permutation algorithm
"""


def FindWord(word):
    w = list(word)      # Convert string to list to be mutable

    # Find longest non-decreasing suffix
    for i in reversed(range(len(w))):
        if w[i-1] < w[i]: break

    if i == 0: return "no answer"     # Already highest permutation
    else: pivot = i -1

    for i in reversed(range(pivot, len(w))):
        if w[i] > w[pivot]: break
    
    # Swap pivot with i
    w[i], w[pivot] = w[pivot], w[i]

    # Reverse suffix
    w[pivot+1:] = reversed(w[pivot+1:])

    # Turn back into a string
    return "".join(w)


"""
Collect Input, and call function
"""
t = int(raw_input())
for i in range(t):
    word = raw_input()
    print FindWord(word)
