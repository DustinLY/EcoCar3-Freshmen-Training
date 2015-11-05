""" This program will make a random int and ask the user to guess a number from 1 to 100 and will tell the user if their guess is too low or too high. 
A while loop makes the program run until the user quits by entering 0 or finishes the game and doesn't want to play again.
When the user correctly guesses the random number the game will ask if they wish to play again. Playing again will set the lower and higher guesses 
back to 0 and make a new random number. Most of the code is written in the try statement to prevent crashing. If a user enters a string the program 
would switch to the except statement which tells the user to enter valid input. I didn't use functions in this program because they give me errors 
mainly because of the scope of variables lower_guesses, higher_guesses, random_number, user_guess so I decided to start from scratch and when 
I didn't use functions it worked as expected."""
import random
low_guesses=0
high_guesses=0
random_number=random.randint(1,100)
loop=True
while loop:
  user_guess=raw_input("Guess a number between 1 and 100 or enter 0 to quit.\n")
  try:
    if int(user_guess)==random_number:
      print"You guessed correctly!\nGuesses that were too low: "+str(low_guesses)+"  too high: "+str(high_guesses)+"."
      play_again=raw_input("Do you want to play again? [1=yes, 2=no]  ")
      if play_again=="2":
        loop=False
      elif play_again=="1":
        low_guesses=0
        high_guesses=0
        random_number=random.randint(1,100)
    elif int(user_guess)>random_number and int(user_guess)>=1 and int(user_guess)<=100:
      print"Too high!"
      high_guesses=high_guesses+1
    elif int(user_guess)<random_number and int(user_guess)>=1 and int(user_guess)<=100:
      print"Too low!"
      low_guesses=low_guesses+1 
    elif user_guess=="0":
      print"Goodbye"
      loop=False
    else:
      print"Guess a number from 1 to 100 please."
  except:
    print"Invalid input please try again."
