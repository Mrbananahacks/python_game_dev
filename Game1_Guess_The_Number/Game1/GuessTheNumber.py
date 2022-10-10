'''
Created on 20 Apr 2022

@author: evane
'''
'''
1. Change the number range from 1 to 1.000.000
2. Game should ask us to guess a number
3. Give a clue if the number is higher or lower then the guess
4. Inform the player if he won

'''


from random import randint

start = 1

end = 1000

value = randint(start, end)

print("The computer chose a number between", start, "and", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    
    if guess <value:
        print("The number is Higher")
    elif guess > value:
        print("The number is Lower")

print("Congratulations!!! you've guessed the number. You Win! ")

    