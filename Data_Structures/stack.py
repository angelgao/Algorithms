from linkedList import LinkedList
from linkedList import Node

class Stack:
    def __init__(self, top=None):
        self.top = top #top is reference to linked list
        self.length = 0

    def Push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.length += 1

    def Pop(self):
        node = self.top
        self.top = node.next
        self.length -= 1
        return str(node)

    def Is_Empty(self):
        return self.length == 0

