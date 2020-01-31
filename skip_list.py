# Skip list: probabilistic data structure based on the Linked list
# Description of a skip list: https://brilliant.org/wiki/skip-lists/

### Design Notes ###
#
# Is a node, a single node, or a collection of all layers per index?
# aka "station representation"
# If we opt for station repr. we could represent it as a
# list of pointers to the next station.


class SkipNode(object):
    def __init__(self, elem=None):
        self.elem = elem

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

    def search(self):
        pass

    def delete(self):
        pass
