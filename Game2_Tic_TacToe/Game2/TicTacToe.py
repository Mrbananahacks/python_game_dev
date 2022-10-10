'''
Created on 21 Apr 2022

@author: evane
'''

'''
1. Display the game board with 9 positions for x and y
2. Make sure the board is empty
3. Provide numbers for each cell so the players can refer to it.
4. Provide error message for placing a symbol in a filled cell
5. If player has 3 symbols in a line display you win message
'''


theBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

boardKeys = []

#print(boardKeys)

for key in theBoard:
    boardKeys.append(key)
    
#print(boardKeys)

def printBoard(board):
    
    print(board['7'] + '/' + board['8'] + '/' +board['9'])
    print('-+-+-')
    
    print(board['4'] + '/' + board['5'] + '/' +board['6'])
    print('-+-+-')
    
    print(board['1'] + '/' + board['2'] + '/' +board['3'])
    print('-+-+-')
    
#printBoard(theBoard)


def game():
    
    turn = 'X'
    count = 0
    
    for i in range(10):
        
        printBoard(theBoard)
        
        print("It is turn of " + turn +" Specify the place you want to go")
        
        move = input()
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1
        else:
            print("Sorry this cell location is filled. Please choose another one.")
            
            continue
        
        if count >= 5:
            
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
            if theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "Won the game")
                
                break
            
        if count == 9:
            print("\nGame Over\n")
            print("The game is tie!")
            
            
        if turn == "X":
            turn="O"
        else:
            turn="X"
    # this21 part restarts the game with user input       
    restart = input("Do you want to restart the Game? (y/n)")
            
            
    if restart =='y' or restart == 'Y':
        for key in boardKeys:
            theBoard[key] = ' '
        game()
            
            

if __name__ == "__main__":
    game()
                 
    
        
