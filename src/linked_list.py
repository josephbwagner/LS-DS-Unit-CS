class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, set_head=None):
        self.head = set_head

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def remove(self, value):
        # If we have no head: print error, return
        if not self.head:
            print("ERROR: Value not found")
        # If head has target value
        # Remove head by pointing to head.next
        elif self.head.value == value:
            self.head = self.head.next
        else:
            parent = self.head
            current = self.head.next

            while current:
                if current.value == value:
                    parent.next = current.next
                    return
            print("ERROR: Value not found")

    def contains(self, value):
        current_node = self.head
        while (current_node):
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    def print(self):
        ll_str = ''
        current = self.head
        while (current):
            ll_str += current.value
            current = current.next

        print(ll_str)
        return
