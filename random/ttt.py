import array

squares = array.array('u',['_','_','_','_','_','_','_','_','_'])
inProgress = True
choosing = True

def printSquare():                              #display the board
    #row 1
    print(squares[0], end =" "),
    print(squares[1], end =" " ),
    print(squares[2] ),
    #row 2
    print(squares[3], end =" " ),
    print(squares[4], end =" " ),
    print(squares[5] ),
    #row 3
    print(squares[6], end =" " ),
    print(squares[7], end =" " ),
    print(squares[8] )

def moveCheck(choice):                          #check validity of move
    if choice > 0 and choice < 10 and squares[choice-1] == "_":
        return True
    else:
        return False

def winCheck(player):                           #check if someone won
    if squares[4] == player:
        if squares[0] == player and squares[8] == player:           #\ diagonal
            return True
        elif squares[2] == player and squares[6] == player:         #/ diagonal
            return True
        elif squares[1] == player and squares[7] == player:         #middle column
            return True
        elif squares[3] == player and squares[5] == player:         #middle row
            return True
    if squares[6] == player:
        if squares[0] == player and squares[3] == player:           #first column
            return True
        elif squares[7] == player and squares[8] == player:         #bottom row
            return True
    if squares[2] == player:
        if squares[5] == player and squares[8] == player:           #final column
            return True
        elif squares[0] == player and squares[1] == player:         #top row
            return True
    else:
        return False


while inProgress == True:
    print("Player 1, select square")
    choosing = True
    pX = int(input())
    while choosing:
        if moveCheck(pX):
            squares[pX-1] = 'X'
            choosing = False
        else:
            print("Player 1, please select a valid square")
            pX = int(input())
            continue
    printSquare()
    if winCheck('X'):
        winner = 'X'
        break

    print("Player 2, select square")
    choosing = True
    pO = int(input())
    while choosing:
        if moveCheck(pO):
            squares[pO-1] = 'O'
            choosing = False
        else:
            print("Player 2, please select a valid square")
            pO = int(input())
            continue
    printSquare()
    if winCheck('O'):
        winner = 'O'
        break

print(winner, end =" "),
print("wins!")
inProgress = False