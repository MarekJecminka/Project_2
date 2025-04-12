"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marek Ječmínka
email: jecminkam@seznam.cz
"""
import random

def say_hi():
     return "\n".join(["Hi there!",
                        50 * "-",
                        "I've generated a random 4 digit number for you.", 
                        "Let's play a bulls and cows game."])

def create_secret_number():
    secret_number = []    
    while len(secret_number) != 4:
        random_number = str(random.randint(1,9))
        if random_number in secret_number:
            continue
        else:
            secret_number.append(random_number)
    return "".join(secret_number)

def get_valid_user_guess():
    def duplicates(number_to_check):
        not_duplicates = []
        duplicates = []
        for item in number_to_check:
            if not item in not_duplicates:
                not_duplicates.append(item)
            else:
                duplicates.append(item)
        
        return len(duplicates) != 0

    print(50 * "-")
    valid_user_number = ""
    while True:
        user_number = input("Enter a number: ")
        if len(user_number) != 4:
            print("Your number is not 4 digit. Type 4 digit number next time!")
        elif not user_number.isdigit():
            print("You did not type digits! Enter digits next time!")
        elif user_number[0] == "0":
            print("Numbers can not start with zero. Type digits that do not start with zero next time!")
        elif duplicates(user_number):
            print("Number contains duplicates. Type unique number next time!")
        else:
            valid_user_number += user_number
            break
    
    return valid_user_number

print(say_hi())

passed_user_number = get_valid_user_guess()
passed_secret_number = create_secret_number()

number_of_guesses = 1

while passed_user_number != passed_secret_number:
    print(">>>", passed_user_number)
    bulls = []
    cows = []

    for index, item in enumerate(passed_user_number):
        if item == passed_secret_number[index]:
            bulls.append(item)
        elif item in passed_secret_number and item not in bulls:
            cows.append(item)
    
    print(f"{len(bulls)} bull{"s" if len(bulls) > 1 else ""}, {len(cows)} cow{"s" if len(cows) > 1 else ""}")
    
    passed_user_number = get_valid_user_guess()
    number_of_guesses += 1
else:
    print(">>>", passed_user_number)
    print(f"Correct, you've guessed the right number\nin {number_of_guesses} guess{"es" if number_of_guesses > 1 else ""}!")
    print(50 * "-" + "\nThat's amazing!")
