
class UF:
    """Data structure for union find:
    An integer array where a and b are connected IFF
    they have the same index"""
    numArr = []
    length = 0
    def __init__(self, n):
        self.length = n
        for i in xrange(0,self.length):
            self.numArr.append(i)

    def Union(self,a,b):
        firIndex = self.numArr[a]
        secIndex = self.numArr[b]
        for i in xrange(0,self.length):
            if self.numArr[i] == firIndex:
                self.numArr[i] = secIndex

    def Connected(self,a,b):
        return self.numArr[a] == self.numArr[b]


"""Reads input from stdin then either connects the two 
elements or tells user they are connected"""

len = int(raw_input()); #get number of elements
UFObj = UF(len)

while True:
    line = raw_input()
    if line == '': break    #stop reading on "enter" 
    nums = line.split()     #num contains array of two numbers
    if UFObj.Connected(int(nums[0]), int(nums[1])):
        print "%s and %s are connected!" % (nums[0], nums[1])
    else:
        UFObj.Union(int(nums[0]), int(nums[1]))
