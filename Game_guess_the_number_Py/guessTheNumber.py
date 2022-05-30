
    #When starting the game, a secret number between 1 and 100 is generated.
    #The game asks the user to enter a number.
    #The game will tell the user if the secret number is bigger or smaller than the guess.
    #As long as the user doesn't find the secret number, the game continues.
    #As soon as the user finds the secret number, the game stops and tells the user how many attempts it took to win. Make sure to use the right wording (attempt or attempts)
    #In case the user enters anything else than a number, the game should tell that to the user and quit gracefully.

import random
a = random.randint(1,100)
guess = int

number_of_guess = 0

while guess != a :
    #demander un nombre :
    guess = int(input("Enter a number between 1 and 100 :"))
    #est-ce que la donnée est exploitable ? :
    try:
        result = int(guess) 
    except:
        print("Couldn't convert your input to a valid number")
        quit()
    if guess > a : 
        print("the number is smaller")
    elif guess < a :
        print("the number is bigger")
    number_of_guess += 1
    
if number_of_guess == 1:
    print("you found the number in " + str(number_of_guess) + " attempt")
else :
    print("you found the number in " + str(number_of_guess) + " attempts")
