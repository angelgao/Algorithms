class PriorityQueue:
    """
    Uses a Python list as an attirute to contain
    the items in the queue.
    If the queue stores an object type, the object
    should have a specified __cmp__ method to determine
    priority.
    """
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0   #O(1)

    def insert(self, item):
        self.items.append(item)         #O(1)

    def remove(self):
        #remove according to priority
        max_index = 0
        for i in xrange(1, len(self.items)):
            # > will invoke cmp method
            if self.items[i] > self.items[max_index]: 
                max_index = i
        item = self.items[max_index]
        del self.items[max_index]
        return item


