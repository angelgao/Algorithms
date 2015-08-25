"""
Detect cycle in a linked list

a) Determine whether a singly-linked data structure contains a cycle
   Running Time: O(N)

b) If a cycle exists, determine first node that participates in cycle
   Use a constant number of pointers to the list
   Running Time: O(N)

The structure of the linked list should not be modified
"""

from linkedList import LinkedList
from linkedList import Node

#Returns True if a cycle is found
def DetectCycle(lst):
    ptr1 = Node()
    ptr2 = Node()
    ptr1 = ptr2 = lst
    
    while ptr1 != None and ptr1.next != None and ptr2 != None and ptr2.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if ptr1 == ptr2:
            ptr1 = lst              #move ptr1 back to beginning 
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next    #increment both by 1 each time
            return ptr1             #return node where they met
    
    return False


"""
Tests
"""

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

lst1 = n1
lst1.next = n2
n2.next = n3
n3.next = n4

assert DetectCycle(lst1) is False

lst2 = n1
lst2.next = n2
n2.next = n3
n3.next = n2
assert DetectCycle(lst2) is n2
