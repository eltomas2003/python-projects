import random
secretNumber = random.randint(0,99)
tries = 3
while tries > 0:
    triesLeft = "You have "+ str(tries) + " tries left."
    print("Guess the secret number")
    print(triesLeft)
    numberGuess=int(input())
    if numberGuess == secretNumber:
        print("Congratulations!")
        exit()
    if numberGuess > secretNumber:
        print("secret number is lower")
        tries -= 1
    if numberGuess < secretNumber:
        print("Secret number is greater")
        tries -= 1
    
if tries == 0:
    print("Game Over!")
    print("The correct number was "+str(secretNumber))