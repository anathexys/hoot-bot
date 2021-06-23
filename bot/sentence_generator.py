from random import choice

class SentenceGenerator():
    '''Returns a generated sentence. Currently POC.'''
    list_of_sentences = [
        'you understand the reality of life on this server: you are all puppets to an almighty sadistic dungeon master.',
        'you delve too much into the number crunching in relation with atmospheric modelling and end up to 42.000 due to a rounding error.',
        'you get convinced that an orgonite crystal will neutralize your second covid-19 jab.',
        'well, yes, but actually no.',
        'you attend a seminar given by a known fruity guru and try to find a hidden truth in the pips of a cucumber.',
        'the library in you grandfather house is so large it lets you enter the L-space. You end up unable to find that copy of Hamlet without all the \'e\'.',
        'you find yourself tied -- alone -- to a tramway tracks. Luckily, the person operating the switch chose the other tracks. Unluckily, the creator of the tramway dilemma forgot about the third rail.',
        'mandatory corporate events lead by your n+∞ (aka, his Fabiengness) are really not good for your sanity.',
        'you try to connect to the server hosting the coffee machine and end up with a 418 error.'
    ]
    
    def __init__(self):
        pass
    
    def get_sentence(self):
        return choice(self.list_of_sentences)