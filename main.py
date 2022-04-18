#import data, logo
import random
from art import logo
from art import vs
from game_data import data

#pull 2 random items from the imported list
#name, follower_count, description, country i.e. print(choice_one["country"])
choice_a = random.choice(data)
choice_b = random.choice(data)
score = 0
keep_playing = 0

def find_answer():
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"

def check_answer(guess):
    if guess == find_answer():
        return score + 1
        print(f"You're right! Currenct score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        return keep_playing + 1
        return 

while keep_playing == 0:
    print(logo)
    #print information on the 2 items imported
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    #allow the user to choose one or the other
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    #give the user points for each correctly chosen
    guess = input("Who has more follower? A or B: ").lower()
    check_answer(guess)

#end the game when user is wrong, print their final score, end the game.

def game():
    while guess! = answer:
        print(logo)
        #print information on the 2 items imported
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        #allow the user to choose one or the other
        print(vs)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
        #give the user points for each correctly chosen
        guess = input("Who has more follower? A or B: ").lower()
        check_answer(guess)