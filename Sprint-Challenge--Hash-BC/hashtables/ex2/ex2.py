#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    # Hash tickets: source is key, dest is value
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    # Populate `route`
    for ticket in range(length):
        if ticket == 0:
            start = hash_table_retrieve(ht, "NONE")
            route[ticket] = start
        else:
            # Get dest (value) of previous route
            route[ticket] = hash_table_retrieve(ht, route[ticket-1])

    print(route)
    return route
