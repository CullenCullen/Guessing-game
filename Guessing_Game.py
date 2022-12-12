#Guessing Game
#Author: Cullen Shortt
#Users will have to guess a number 1 -50. Once they get the answer, the program will
#let them know if their number is too high or too low. After guessing the correct number
#user will be shown how many tries it took them. 

import random #this imports the random class to use the method randint()

play = 'Y' #loop variable 
num = 1 #input variable 
correctnumber = random.randint(1,50) #this creates the random number
numguess = 0 #initilizes the number of guesses counter. 


while play != 'N' and play != 'n': #start of loop. Will terminate when user enters in 'N'
    num = int(input("Enter a guess 1-50, or 0 to quit: ")) #user prompt for input variable num
    if num > correctnumber and num <= 50: #checks if num is higher than correctnumber and in range
        print("Too high!")
        numguess += 1  #accumulator 
    elif num < correctnumber and num >= 1: #checks if num is less than correctnumber and in range
        print("Too Low!")
        numguess += 1 #accumulator 
    elif num < 0 or num > 50: #checks if num is out of range
        print("Guess must be between 1 and 50!")
        numguess += 1 #accumulator 
    elif num == correctnumber: #checks if num is the same as correctnumber
        numguess += 1 #accumulator
        print(f'That\'s it! You took {numguess} guesses to get the number.')
        print()
        play = input("Would you like to play again? (Y/N)") #terminates loop if user inputs N
    elif num == 0: #terminates loop if input is 0
        break

