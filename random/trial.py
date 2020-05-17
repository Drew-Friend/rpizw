from random import randint

print("Rock, Paper Scissors!")
#for x in range(3):
    #print(3 - x)
print("input your answer")
com = randint(0, 2)             #0 is rock, 1 is paper, 2 is scissors
choice = input()
if choice == "rock" or choice == "scissors" or choice == "paper" or choice == "Rock" or choice == "Scissors" or choice == "Paper":
    if com == 0:
        if choice == "rock" or choice == "Rock":
            print("The computer also chose rock, it's a tie")
        if choice == "scissors" or choice == "Scissors":
            print("The computer chose rock, You Lose :(")
        if choice == "paper" or choice == "Paper":
            print("The computer chose rock, You Win!")
    if com == 1:
        if choice == "rock" or choice == "Rock":
            print("The computer chose paper, You Lose :(")
        if choice == "scissors" or choice == "Scissors":
            print("The computer chose paper, You Win!")
        if choice == "paper" or choice == "Paper":
            print("The computer also chose paper, it's a tie")
    if com == 2:
        if choice == "rock" or choice == "Rock":
            print("The computer chose scissors, You Win!")
        if choice == "scissors" or choice == "Scissors":
            print("The computer also chose scissors, it's a tie")
        if choice == "paper" or choice == "Paper":
            print("The computer chose scissors, You Lose :(")
else:
    print("invalid move")