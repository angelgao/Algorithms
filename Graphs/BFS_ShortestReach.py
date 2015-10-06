"""
Problem:    Given an undirected graph consisting of 
            N nodes and a start position S. Find the
            shortest distances between each node and S.

Input:      First line is T, denoting num of test cases
            Each test case has two integers,
            N = num of nodes in the graph
            M = num of edges in the graph
            The next M lines consists of integers x y
            where an edge exists
            Last line is S, denoting start position

Output:     For each test case, a single line consisting of
            N-1 space separated integers, denoting the shortest
            distance to each node.
"""

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def addEdge(self, other):
        self.edges.append(other)

class Graph:
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.nodes = [0] * numNodes
        for i in xrange(numNodes):
            n = Node(i)
            self.nodes[i] = n
    
    def ShortestDist(self, start):
        arr = [-1] * self.numNodes
        arr[start] = 0
        q = deque([self.nodes[start]])
        while q:
            v = q.popleft()
            for edge in v.edges:
                if arr[edge.value] == -1:
                    # Unexplored
                    arr[edge.value] = arr[v.value] + 6
                    q.append(edge)
        return arr


""" Input """
t = int(raw_input())
for i in xrange(t):
    l = raw_input().split()
    N = int(l[0])            # Num of nodes in graph
    M = int(l[1])            # Num of edges in graph

    graph = Graph(N)

    for j in xrange(M):
        s = raw_input().split()
        x = int(s[0]) - 1
        y = int(s[1]) - 1
        graph.nodes[x].addEdge(graph.nodes[y])
        graph.nodes[y].addEdge(graph.nodes[x])

    
    s = int(raw_input()) - 1
    arr = graph.ShortestDist(s)

    for i in xrange(len(arr)):
        if s != i: print arr[i],
    print ""

