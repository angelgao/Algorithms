from linkedList import Node

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None #tail ptr to have O(1) insertion

    def is_empty(self):
        return (self.length == 0)

    def insert(self, elem):
        node = Node(elem)
        node.next = None
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove(self):
        elem = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0: self.tail = None
        return elem

