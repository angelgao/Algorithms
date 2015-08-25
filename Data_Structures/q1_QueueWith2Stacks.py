"""
Queue with Two Stacks

Implement a queue with two stacks so that each queue
operation takes a constant amortized number of 
stack operations
"""

from ../stack import Stack

class Queue:
    def __init__(self):
        self.length = 0
        self.s1 = Stack()
        self.s2 = Stack()

    def Insert(self, elem):
        self.s1.Push(elem)
        self.length += 1

    def Remove(self):
        if self.s2.Is_Empty():
            #switch the entire stack over s2
            while not self.s1.Is_Empty(): 
                node = self.s1.Pop()
                self.s2.Push(node)
        elem = self.s2.Pop()
        self.length -= 1
        return str(elem)

    def Is_Empty(self):
        return self.length == 0
