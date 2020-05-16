"""
A ring buffer is a non-growable buffer with a fixed size.
When the ring buffer is full and a new element is inserted,
the oldest element in the ring buffer is overwritten with the newest element.

RingBuffer has two methods, `append` and `get`. 
The append method adds elements to the buffer. 
The get method returns all of the elements in the buffer in a list in their given order. 
It should not return any None values in the list even if they are present in the ring buffer.
"""

class RingBuffer:

  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity


  def append(self, item):
    storage_length = len([item for item in self.storage if item != None])
    
    if storage_length == self.capacity:
        self.storage[self.current] = item
        self.current += 1
    else:
        ind = self.storage.index(None)
        self.storage[ind] = item


  def get(self):
    return [item for item in self.storage if item != None]