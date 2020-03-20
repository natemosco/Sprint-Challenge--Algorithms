'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, index=0, count=0):
    index = index
    count = count
    if index == len(word) - 1
    return count
    if word[index] + word[index + 1] == "th":
        count += 1
        index += 2
        count_th(word, index, count)
    elif word[index] + word[index + 1] != "th":
        index += 1
        count_ths(word, index, count)
