from util import Queue


with open('words_alpha.txt', 'r') as f:
    words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    '''
    Return all words from word_list that are
    exactly 1 letter different.
    '''
    # Time complexity: O(num_words * len_of_begin_word)
    # Space complexity: O()
    letters = ['a','b','c','d','e','f','g','h',\
            'i','j','k','l','m','n','o','p',\
            'q','r','s','t','u','v','x','y','z']
    neighbors = []
    letter_list = list(word)
    # For each word in word list
    for i in range(len(letter_list)):
        # Check each other letter
        for letter in letters:
            temp_word = list(word)
            temp_word[i] = letter
            w = ''.join(temp_word)
            # See if word is in the set
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


def word_ladder_path(begin_word, end_word):
    q = Queue()
    q.enqueue([begin_word])
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            if v == end_word:
                return path
            visited.add(v)
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None


print(word_ladder_path("hit", "cog"))
print(word_ladder_path("sail", "boat"))
print(word_ladder_path("africa", "turkey"))
