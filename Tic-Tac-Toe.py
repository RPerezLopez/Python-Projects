#tic tac toe game - Python

#this will lay out our board, and add an extra ' ' first so that players can choose 1-9 not 0-8.
board = [' ' for x in range(10)]

#This function will take in the poistion we want to place and insert a letter in it.
def insertLetter(letter, pos):
    board[pos] = letter

#This function will check if the space is free. By using the input player inserts and checking if it has a (' ').
def spaceIsFree(pos):
    return board[pos] == ' '

#This function prints our board. 
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |') 
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |') 
 
#This function here will check all possible outcomes on where a plater may win. diagonally, horizonatally or vertically. 
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

#This function will check to see if the player 1. input a number and not a work. 2. if the number is between 1 and 9. 3. if the space is free. IF any of those are False, we have functions to fix it.
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\', (1-9): ')
        #the 'Try' command lets you check a code for errors. 
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False 
                    insertLetter('X', move)
                else:
                    print("Space is already taken. Please try again")
            else:
                print('Please type a number within the Range')
        #This will print if the 'Try" function receives an error
        except:
            print('Please type a number between 1-9.')       

#This is the process the AI will use in order to be comp. 
def compMove():
    import time 
    print('Please wait while your competitor chooses his move.')
    time.sleep(2)

    #This will check for letters in board. if the space is blank and is between 1- 9.
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0


    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    conrnersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            conrnersOpen.append(i)

    if len(conrnersOpen) > 0:
        move = selectRandom(conrnersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move

#This function will be implemented in the compMove function to chose a move at random. Based on paramenters
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

#This will check if whether the board is Full or not. 
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to tic tac toe! First player to have three of the same letters connecting either diagonal, vertically or horizontally wins! Good luck. ')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s won this time, Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

main()
