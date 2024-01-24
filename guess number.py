import random


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print("Your guess is correct")


def set_difficulty():
    level = input("Choose the difficulty? 'easy' or 'hard'")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


easy_level_turns = 10
hard_level_turns = 5


def game():
    print("Welcome to number guessing game.")
    print("I'm thinking of the number between 1 and 100.")
    answer = random.randint(1, 100)


    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempt to guess the right number")
        guess = int(input("Make a guess"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses")
            return
        elif guess != answer:
            print("Guess again")

game()
