'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) == 0:
        return 0
    else:
        if len(word) >= 2:
            pair = word[0:2]
            if pair == "th":
                return 1 + count_th(word[2:])
        if len(word) >= 3:
            triple = word[0:3]
            if triple[1:] == "th":
                return 1 + count_th(word[3:])

        return 0 + count_th(word[2:])
