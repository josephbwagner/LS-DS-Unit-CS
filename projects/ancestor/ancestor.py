from pprint import pprint
from util import Stack

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
    g = Graph()

    # Add vertices and edges to Graph object
    for parent, child in ancestors:
        if parent not in g.vertices:
            g.add_vertex(parent)
        if child not in g.vertices:
            g.add_vertex(child)
        g.add_edge(parent, child)

    pprint(g.vertices)

    s = Stack()
    s.push(starting_node)

    while s.size() > 0:
        v = s.pop()
        sentry = v
        for vertex in g.vertices:
            if v in g.vertices[vertex]:
                print(f'Pushing vertex/parent to stack: {vertex}')
                s.push(vertex)

        if s.size() == 0:
            return v

    return -1




    # # Determine parent of `starting_node`
    # # or return -1 if no parent exists
    # current_parent = None
    # for vertex in g.vertices:
    #     if starting_node in g.vertices[vertex]:
    #         print(f'starting_node is child of: {vertex}')
    #         current_parent = vertex
    # if current_parent is None:
    #     return -1

    # # Traverse parent nodes until none remain
    # while True:
    #     # To detect change
    #     sentry_var = current_parent
    #     print(f'sentry: {sentry_var}, current_parent: {current_parent}')

    #     # Find all parents
    #     parents = []
    #     for vertex in g.vertices:
    #         if current_parent in g.vertices[vertex]:
    #             parents.append(vertex)
    #             # current_parent = vertex
        
    #     # Find 
    #     for vertex in parents:


    #     # Termination condition
    #     if current_parent == sentry_var:
    #         print(f'Earliest ancestor found: {current_parent}')
    #         return current_parent
