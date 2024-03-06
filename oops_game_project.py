from random import shuffle
# two useful variables for creating cards

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'

class Deck:
    """ this is the deck class. this object will create a deck of cards ti initiate play. 
    You ca then use thus Deck list of cards to split in half and give to the players. 
    It will use SUITE and RANKS to create the deck. It should also have a method for 
    splittin/cutting the deck in half and shuffling the deck."""
    
    #def __init__(self):
        #print("Creating New Ordered Deck!")
        #self.allcards = 

class Hand:
    """
    This is the Hand class. Each player has a hand, and ca remove cards
    from that hand . There should be an add and remove card method here.
    """
   
    pass

class Player:
    """
    This is the Player class, which takes in a name and an instance of a hand
    class object. the player can then play cards and check if they still have cards
    """

    pass


print("welcome to the war, let's play")