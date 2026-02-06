import time
from termcolor import colored
from time import perf_counter



def solve(board,fixedBoard):
    xPos = 0
    yPos = 0
    flagToGoBack = 0
    while yPos != 9:
        printBoard(board,fixedBoard,yPos,xPos)
        if xPos == 9:
            xPos = 0
            yPos += 1
        elif xPos == -1:
            xPos = 8
            yPos -= 1
        else:
            if fixedBoard[yPos][xPos] == 1: #This is a fixed space, dont change it
                if flagToGoBack == 1:
                    xPos -= 1
                else:
                    xPos += 1
            else: #Go wild
                if testNumber(board,yPos,xPos): #Something worked, we are good
                    xPos += 1 
                    flagToGoBack = 0
                else: #time to go back, we are sad
                    board[yPos][xPos] = 0
                    xPos -= 1
                    flagToGoBack = 1
    

def testNumber(board,yPos,xPos):
    start = board[yPos][xPos] + 1
    for num in range(start, 10):
        valid = True

        for x in range(9): #check the row
            if board[yPos][x] == num:
                valid = False #cant do this one
        
        for y in range(9): #check the col
            if board[y][xPos] == num:
                valid = False #cant do this one

        startY = yPos - (yPos % 3) #because it tells us which box we are in
        startX = xPos - (xPos % 3)

        for y in range(3):
            for x in range(3):
                if board[y + startY][x + startX] == num:
                    valid = False #cant do this one

        if valid == True: #This works
            board[yPos][xPos] = num
            return True
    return False
               
def learnFixedSpaces(board,fixedBoard):
    xPos = 0
    yPos = 0    
    while yPos != 9:
        if board[yPos][xPos] != 0:
            fixedBoard[yPos][xPos] = 1
            print(colored(fixedBoard[yPos][xPos], "red"),end="")
        else:
            print(fixedBoard[yPos][xPos],end="")
        xPos += 1
        if xPos == 9:
            print("")
            xPos = 0
            yPos += 1

def printBoard(board,fixedBoard,currentYPos,currentXPos):
    xPos = 0
    yPos = 0    
    while yPos != 9:
        if yPos == currentYPos and xPos == currentXPos and fixedBoard[yPos][xPos] == 1:
            print(colored(board[yPos][xPos], "magenta"),end="")  
        elif yPos == currentYPos and xPos == currentXPos:
            print(colored(board[yPos][xPos], "green"),end="")  
        elif fixedBoard[yPos][xPos] == 1:
            print(colored(board[yPos][xPos], "red"),end="")  
        else:
            print(board[yPos][xPos],end="")   
        xPos += 1
        if xPos == 9:
            print("")
            xPos = 0
            yPos += 1
    print("")

def sudoku():

    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    fixedBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    startTime = perf_counter()
    learnFixedSpaces(board,fixedBoard)
    solve(board,fixedBoard)
    endTime = perf_counter()
        
    print(f"Done in {endTime - startTime} seconds! ")


sudoku()