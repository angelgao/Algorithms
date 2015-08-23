
class QuickUnionUF:
    """Data structure for union find:
    Two integer array to represent a tree of connected nodes and its size
    numArr[i] is the parent of i and size[i] is its size.
    two nodes A and B are connected IFF they have the same root"""
    numArr = []
    size = []
    length = 0
    def __init__(self, n):
        self.length = n
        for i in xrange(0,self.length):
            self.numArr.append(i)
            self.size.append(1)

    def Root(self, i):
        while(i != self.numArr[i]):
            self.numArr[i] = self.numArr[self.numArr[i]] #path compression
            i = self.numArr[i]
        return i

    def Union(self,a,b):
        i = self.Root(a)
        j = self.Root(b)
        #always merge the smaller tree as a child of the bigger
        if self.size[i] < self.size[j]:
            self.size[j] += self.size[i] #update size
            self.numArr[i] = j
        else:
            self.size[i] += self.size[j] #update size
            self.numArr[j] = i

    def Connected(self,a,b):
        #Check that a and b have the same root
        return self.Root(a) == self.Root(b)


"""CLIENT SUITE FOR UNION FIND"""
"""Reads input from stdin then either connects the two 
elements or tells user they are connected"""

len = int(raw_input()); #get number of elements
UFObj = QuickUnionUF(len)

while True:
    line = raw_input()
    if line == '': break    #stop reading on "enter" 
    nums = line.split()     #num contains array of two numbers
    if UFObj.Connected(int(nums[0]), int(nums[1])):
        print "%s and %s are connected!" % (nums[0], nums[1])
    else:
        UFObj.Union(int(nums[0]), int(nums[1]))
