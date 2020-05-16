# Skip list: probabilistic data structure based on the Linked list
# Description of a skip list: https://brilliant.org/wiki/skip-lists/


class SkipNode(object):
    def __init__(self, elem=None):
        self.elem = elem

        # 'Square' representation (not list, station-like representation)
        self.prev = None
        self.next = None
        self.below = None
        self.above = None


class SkipList(object):
    def __init__(self, max_height):
        # Should have pointers to every single station in first node
        self.max_height = max_height
        self.head = [SkipNode() for i in range(max_height)]

        if len(self.head) > 1:
            # Connect all nodes, loop through all nodes in head
            for i in range(max_height):
                # For the ith node, connect it's 'below' to the i-1 node
                if i == 0:
                    self.head[i].above = self.head[i + 1]
                elif i == len(self.head) - 1:
                    self.head[i].below = self.head[i - 1]
                else:
                    self.head[i].above = self.head[i + 1]
                    self.head[i].below = self.head[i - 1]

    def search(self, target):
        '''
        Starts at the top node of the head
        If the next node along this line > target:
          Move down a layer, check next node along line again
          If the next node along line <= target:
                Move right to next node
                Stop criteria: target is found
        '''
        # Start at the last node in self.head
        start = self.head[-1]

        # If below exists go there
        while start.below:
            current = start.below
            # Go right if next < target
            while target >= current.next:
                current = current.next

        return current

    def insert(self, val):
        # Search the skip list for the largest value < val
            # Assuming the value doesn't exist in the list
        # Create a new node with the val and connect it to the found node
        # Add layers to this new node by flipping coins to determine # of layers
        # Connect layers to nodes in the same layers
        pass
