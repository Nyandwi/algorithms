# Word Frequencies: Design a method to find the frequency of occurrences of any given word in a book. 
# What if we were running this algorithm multiple times?

# 1: Simple word querry
import string

def word_count(book, word):
    
    counts = 0
    
    book = book.translate(str.maketrans('', '', string.punctuation))
    book = book.lower().split()
    word = word.lower()
    
    for w in book:
        if w == word:
            counts += 1
    return counts


# 2: When to run the algorithm repetitively, use hashtables

def word_count_rep(book, word):
    
    """if we were running the algorithms multiple times..Save counts in hashtables"""
    
    dict_counts = {}
    
    book = book.translate(str.maketrans('', '', string.punctuation))
    book = book.lower().split()
    word = word.lower()
    
    for w in book:
        if w in dict_counts:
            dict_counts[w] += 1
        else:
            dict_counts[w] = 1
    
    return dict_counts[word]