import random
secretNumber = random.randint(1,3)
print("rock, paper, scissors")
userSelection = int(input("1. Rock 2. Paper 3. Scissors"))
win = "You win"
lose = "You lose"
def rockPaper():
    if secretNumber == 1:
        return "rock"
    if secretNumber == 2:
        return "paper"
    if secretNumber == 3:
        return "Scissors"
def rockPaperPlayer():
    if userSelection == 1:
        return "rock"
    if userSelection == 2:
        return "paper"
    if userSelection == 3:
        return "Scissors"
bothSelections = "the computer choose "+rockPaper()+". You choose " + rockPaperPlayer()
if secretNumber == 1 and userSelection == 2:
    print(bothSelections)
    print(win)
if secretNumber == 1 and userSelection == 3:
    print(bothSelections)
    print(lose)
if secretNumber == 2 and userSelection == 1:
    print(bothSelections)
    print(lose)
if secretNumber == 2 and userSelection == 3:
    print(bothSelections)
    print(win)
if secretNumber == 3 and userSelection == 1:
    print(bothSelections)
    print(win)
if secretNumber == 3 and userSelection == 2:
    print(bothSelections)
    print(lose)
if secretNumber == userSelection:
    print(bothSelections)
    print("Draw")
    