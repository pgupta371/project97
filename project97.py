import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess the Number between 1-9")
while(chances<5):
    guess = int(input("Enter Your Guess "))
    if(guess == number):
        print("You Won!")
        break
    elif(guess<number):
        print("Guess a Higher Number than ", guess)

    else:
        print("Guess a Lower Number than ", guess)

    chances += 1
if(not chances<5):
    print("You Lost the Correct Number was ", number)