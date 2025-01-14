import random

subjects = [
    "I", "you", "Jim", "Helen", "Socrates", "skeletons",
    "a stick", "the undead", "Bilbo", "the youth",
    "all the children", "a unicorn", "several snakes",
    "Taylor Swift", "Hamlet", "an unkindness of ravens",
    "huge rats", "Kant", "Beauvoir", "they", 
    "the rest of them", "he", "she", "Pam", "a bunch",
]
verbs = [
    "opened", "smashed", "ate", "became", "climbed",
    "chose", "questioned", "grew", "squeezed", "read",
    "sought", "lifted", "outpaced", "surprised",
    "sauteed", "dissected", "displayed", "coughed up",
    "stole", "got rid of", "dispatched", "clung to",
]
objects = [
    "the closet", "her", "crumbs", "organs", "cheese",
    "the best ones", "a hippo", "the lot of them",
    "those assembled", "him", "platters", "the whiskey",
    "jumbo shrimp", "the strangest one", "the wind",
    "spoons galore", "a book", "a mirror", "a blessed spirit",
    "a path most perilous", "most", "a hungry caterpillar",
]

def rand_sub():
    """Returns a random grammatical subject"""
    return random.choice(subjects)

def rand_verb():
    """Returns a random verb"""
    return random.choice(verbs)

def rand_obj():
    """Returns a random grammatical object"""
    return random.choice(objects)

def rand_sen():
    """Returns a random subject-verb-object sentence"""
    s = rand_sub()
    v = rand_verb()
    o = rand_obj()
    sentence = " ".join([s.capitalize(), v, o]) + "."
    return sentence

def rand_par():
    """Returns a paragraph of random sentences"""
    n_sentences = random.randint(3, 5)
    paragraph = ""
    for i in range(0, n_sentences):
        paragraph += " " + rand_sen()
    return paragraph