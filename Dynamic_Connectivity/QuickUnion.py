
class QuickUnionUF:
    """Data structure for union find:
    An integer array to represent a tree of connected nodes
    id[i] is the parent of i and
    two nodes A and B are connected IFF they have the same root"""
    numArr = []
    length = 0
    def __init__(self, n):
        self.length = n
        for i in xrange(0,self.length):
            self.numArr.append(i)

    def Root(self, i):
        while(i != self.numArr[i]):
            i = self.numArr[i]
        return i

    def Union(self,a,b):
        #Make root of B a child of A
        self.numArr[self.Root(a)] = self.Root(b)

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
