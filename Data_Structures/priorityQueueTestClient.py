from priorityQueue import PriorityQueue
class Golfer:
    """
    A class with a defined cmp method for priority queue
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)

    def __cmp__(self, other):
        if self.score < other.score: return 1 #lower score is better
        if self.score > other.score: return -1
        return 0 #if equal, return 0

""" Test Client """

tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phile Mickelson", 72)
hal = Golfer("Hal Sutton", 69)

pq = PriorityQueue()
pq.insert(tiger)
pq.insert(phil)
pq.insert(hal)

while not pq.is_empty(): print pq.remove()

#OUTPUT:
#   Tiger Woods    : 61
#   Hal Sutton     : 69
#   Phil Mickelson : 72
