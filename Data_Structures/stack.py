from linkedList import LinkedList
from linkedList import Node

class Stack:
    def __init__(self, top=None):
        self.top = top #top is reference to linked list

    def Push(self, node):
        node.next = self.top
        self.top = node

    def Pop(self):
        node = self.top
        self.top = node.next
        return str(node)

