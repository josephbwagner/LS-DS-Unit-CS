#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    # `weights` is a List of weights (insert into ht)
    # `length` is len(weights)
    # `limit` is the value we're trying to sum to
    # If not None, return sorted Tuple with len() == 2
    if length <= 1:
        return None
 
    ht = HashTable(16)
    # Insert weights as keys and indices as values
    for ind, val in enumerate(weights):
        hash_table_insert(ht, val, ind)

    # Loop through keys (weights) and retrieve
    # key of limit-weight if it exists
    for weight in weights:
        remaining = limit - weight

        if hash_table_retrieve(ht, remaining):
            answer_1 = hash_table_retrieve(ht, weight)
            answer_2 = hash_table_retrieve(ht, remaining)
            if answer_1 > answer_2:
                print(answer_1, answer_2)
                return (answer_1, answer_2)
            else:
                print(answer_2, answer_1)
                return (answer_2, answer_1)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
