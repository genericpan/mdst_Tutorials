"""
Intro to python exercises shell code
"""

def is_odd(x):
    if x%2==1:
        return True
    return False


def is_palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i]!=word[len(word)-i-1]:
            return False
    return True
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    list1 = list()
    for i in numlist:
        if i%2==1:
            list1.append(i)
    return list1
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    dictionary=dict()
    word=text.split()
    for stringin in word:
        if stringin in dictionary:
            dictionary[stringin]+=1
        else:
            dictionary[stringin]=1
    return dictionary
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
print(only_odds([1, 2, 3, 4, 5, 6]))
    
