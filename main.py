"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marek Ječmínka
email: jecminkam@seznam.cz
"""
import random

#def say_hi():
#    greeting = ["Hi there!",
#               50 * "-",
#               "I've generated a random 4 digit number for you.", 
#               "Let's play a bulls and cows game."]
#    
#    return print("\n".join(greeting))

def create_secret_number():
    secret_number = []    
    while len(secret_number) != 4:
        random_number = str(random.randint(1,9))
        if random_number in secret_number:
            continue
        else:
            secret_number.append(random_number)
    return "".join(secret_number)
    
greeting = ["Hi there!",
               50 * "-",
               "I've generated a random 4 digit number for you.", 
               "Let's play a bulls and cows game."]

print("\n".join(greeting))
