# computer thinking of a number

# user guesses 

# computer says too high or too low

# user guesses again

def play_game():
    # think of what we need to keep track of
    number_to_guess = 4
    #TODO: make this number a new, randomly generated number each time the function runs
    user_guess = int(input("Guess a number between 1 and 100: "))
    #TODO: limit the number of guesses to 8
    # compare user_guess to the number
    # if number too high or too low, guess again
    # if the guess is the number, print message, end game
    while user_guess != number_to_guess:
        if user_guess > number_to_guess:
            print("Too high! Guess again.")
        elif user_guess < number_to_guess:
            print("Too low! Guess again,")
        user_guess = int(input("Guess a number between 1 and 100: "))
    print("You're right! Good job!")

play_game()
