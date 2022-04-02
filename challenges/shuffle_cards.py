# Write a function to shuffle a deck of cards. 
# It must be a perfect shuffle-in other words, each of the 52! permutations of the deck has to be equally likely. 
# Assume that you are given a random number generator which is perfect.

import random

def shuffle_cards(cards):
    """
    Given a card of elements, 
    shuffle the cards. 
    Solution: iterate through the card, swapping each element with a random element
    """
    
    for i in range(len(cards)):
        
        rand = random.randint(0,i)
        
        # temp = cards[rand]
        # cards[rand] = cards[i] 
        # cards[i] = temp

        cards[i], cards[rand] = cards[rand], cards[i]
        
    return cards

print(shuffle_cards([1,2,3,4,5]))