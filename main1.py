'''
1. choosing a random number between 1 and 100.
2. make function to set difficulty
3. let the user guess a number.
4. function to check user's guess against actual answer
5. track the number of turns and reduce by 1 if they get it wring.
6. repeat the guessing functionality if they get it wrong.
'''

import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
actual_answer = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def check_answer(user_guess, actual_answer):
    user_guess = int(input("Make a guess: "))
    if user_guess > actual_answer:
        print("Too high")
        print("guess again")
    elif user_guess < actual_answer:
        print("Too low")
        print("guess again")
    else:
        print(f"you are correct! The correct answer is {actual_answer}")


def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


turns = set_difficulty()
user_guess = 0
while user_guess != actual_answer:
    print(f"you have {turns} attempts remaining")
    check_answer(user_guess, actual_answer)
    turns -= 1
    if turns == 0:
        print(f"you are out of guess. You loss")
        break



