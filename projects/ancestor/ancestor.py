from pprint import pprint
from util import Queue


class Graph:
    '''Represent a graph as a dictionary
    of vertices mapping labels to edges.'''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist.')


def earliest_ancestor(ancestors, starting_node):
    '''
    `ancestors`: list of tuples (parent, child)
    `starting_node`: int of child node
    Returns earliest ancestor node, or -1 if none exist

    Design Notes
    > For parent-child relationships: is a LinkedPair DS fitting?
    > This is reverse DFS, would a Stack DS be fitting?
    '''
    # Build graph: Add vertices and edges 
    g = Graph()

    def last_ancestor(self, starting_vertex):
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create variable to track ancestor, default to -1 if no ancestor.
        ancestor = -1
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            #if 
            if bool(self.vertices[v]) is False and v != starting_vertex:
                ancestor = v
                # Then add all of its neighbors to the back of the queue
            for neighbor in self.vertices[v]:
                q.enqueue(neighbor)
        return ancestor
