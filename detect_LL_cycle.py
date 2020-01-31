'''
Detect any cycle in a Linked List. Note that the head pointer may be 'None' if the list is empty. 

The function should return a Boolean value if the LL contains a cycle, or not.
'''

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def has_cycle(head):
    # We'll use fast and slow pointers for efficiently traversing LL
    fast = head
    slow = head

    # Fast pointer will traverse 2x speed of slow pointer
    # Keep iterating while fast.next is a valid node
    while fast.next:
        fast = fast.next.next
        slow = slow.next

        # Check if fast and slow refs are referring to same object
        if fast is slow:
            return True

    # If we reach end of loop, we've reached end of LL
    return False


