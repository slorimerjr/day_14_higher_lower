#import data, logo
import random
from art import logo
from art import vs
from game_data import data

#pull 2 random items from the imported list
#name, follower_count, description, country i.e. print(choice_one["country"])

choice_a = random.choice(data)
choice_b = random.choice(data)

def find_answer():
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"

#end the game when user is wrong, print their final score, end the game.

def game():
    keep_playing = True
    while keep_playing == True:   
        score = 0
        keep_playing = True
        print(logo)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(vs)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
        answer = find_answer()
        print(f"Psst! The answer is {answer}!")
        guess = input("Who has more follower? A or B: ").lower()
        if guess == answer:
            score += 1
            print(f"You're right! Currenct score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            keep_playing = False 
game()
