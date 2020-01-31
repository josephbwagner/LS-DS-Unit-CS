from detect_cycle import Node, has_cycle
# from skip_list import *


### Linked List Cycle Detector Code ###
head = Node(0, None)
node_1 = Node(1, None)
node_2 = Node(2, None)
node_3 = Node(3, None)
node_4 = Node(4, None)
node_5 = Node(5, None)
node_6 = Node(6, None)

head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6
node_6.next = node_4  # Tail node cyclically points to node_4

print(has_cycle(head))  # Print True if cycle is detected
