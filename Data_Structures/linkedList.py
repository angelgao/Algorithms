class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_list(self):
        if self.head != None:
            self.head.print_node()
        else:
            print "None"

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return str(self.cargo)

    def print_node(self):
        node = self
        while node:
            print node,
            node = node.next
        print



