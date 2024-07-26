import random

print("Welcome to my game, I will think of a number between 1 and 100. try and guess what the number is")
playerName = input("What is your name? ")
print("Hello {} it is {} to meet you".format(playerName, "nice"))

computerNumber = random.randrange(1,101)
playing = True
guesses = 0
while playing:
    print("please guess a number between 1 and 100")
    playerNumber = input("what is your guess? ")

    playerNumber = int(playerNumber)
    guesses = guesses + 1
    if playerNumber == computerNumber:
        print("that is correct")
        playing = False

    elif guesses == 8:
        print("You ran out of guesses")
        playing = False

    if playerNumber < computerNumber:
        print("that is too low")

    if playerNumber > computerNumber:
        print("that is too high")



print("it took you {} guesses".format(guesses))