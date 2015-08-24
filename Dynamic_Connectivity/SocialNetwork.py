"""
Social Network Connectivity

Given a social network containing N members, and
a log file input of size M sorted by timestamp of when 
two members became friends. Determine the earliest time that
all members are connected (i.e. every member is a friend
of a friend... of a friend of a friend...)

Running time: MlogN or better
Space: proportional to N
"""

import sys

class QuickUnionUF:
    id = []
    size = []
    def __init__(self, length):
        self.length = length
        for i in range(0, length):
            self.id.append(i)
            self.size.append(1)

    def Root(self, a):
        while a != self.id[a] :
            a = self.id[a]
        return a

    # connects a and b, returns whether entire graph is connected
    def Union(self, a, b):
        i = self.Root(a)
        j = self.Root(b)
        if (self.size[a] > self.size[b]):
            self.id[j] = i
            self.size[i] += self.size[j]
            return self.size[i] == self.length
        else:
            self.id[i] = j
            self.size[j] += self.size[i]
            return self.size[j] == self.length

"""
Client which takes input as follows:
1. The number (N) of members <enter>
2. The number (M) of logs    <enter> 
2. A B where the two members A, B became friends <enter>
   until M lines or all members are connected
"""

len = int(raw_input()); #get number of members
UFObj = QuickUnionUF(len)
m = int(raw_input());   #get number of logs

if len <= 1: 
    print "Social Netork is all connected."
    sys.exit()

for i in range(0,m):
    line = raw_input()
    nums = line.split()     #num contains array of two numbers
    done = UFObj.Union(int(nums[0]), int(nums[1]))
    if done:
        print "Social Network is all connected."
        sys.exit()
