import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, cache_size=3):
        self.cache_size = cache_size
        self.current_size = 0
        self.storage = DoublyLinkedList()
        self.hashtable = dict()


    """
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    
    Also needs to move the key-value pair such that the pair 
    is considered most-recently used.
    """
    def get(self, key):
        if key not in self.hashtable.keys():
            return None

        self.storage.move_to_front(self.hashtable[key])

        return self.hashtable[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. 
    
    If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. 
    
    Additionally, in the case that the key already exists in 
    the cache, we simply want to overwrite the old value 
    associated with the key with the newly-specified value.
    """
    def set(self, key, value):
        if key in self.hashtable.keys():
            self.hashtable[key].value = value
            return

        if self.current_size == self.cache_size:
            node_to_remove = self.storage.remove_from_tail()
            self.hashtable = {key: node for key, node in self.hashtable.items()\
                              if node.value is not node_to_remove}
            self.storage.add_to_head(value)
            self.hashtable[key] = self.storage.head
        else:
            self.storage.add_to_head(value)
            self.hashtable[key] = self.storage.head
            self.current_size += 1


