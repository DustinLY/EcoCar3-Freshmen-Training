#Assignment_2
###What to do
#####This is the old "I'm thinking of a number between…". 
  When you run the program, the computer randomly generates a number.
  Then, the user is to guess the number.
  Upon guessing wrong, the program gives him/her a hint as to whether the guess is too high or too low.
  Once the number has been guessed, the game is over.

Create a command line Python program to input, keep track of, and check user's attempts to guess a randomly generated number.
The input portion of the program will be a continuous loop, only breaking out of it when the user either guesses 
the correct number, or by entering -1 to signify giving up. After each guess, the user will be informed of his guess being
too high, too low, or exactly correct. Upon exiting the loop, the user is given feedback of their guesses (amount guessed 
too low, amount guessed too high, total amount of guesses).
You'll need to generate a random number to be guessed by the user.

Example of how this program's output should look after it runs:

    >>> Guess the number I'm thinking of, from 1-100: 16
    >>> Your guess is larger than the random value. Next guess: 
    >>> 8
    >>> Your guess is larger than the random value. Next guess: 
    >>> 4
    >>> Your guess is smaller than the random value. Next guess: 
    >>> 6
    >>> You've guessed correct!
    >>> Total number of guesses: 4
    >>> Smaller Guesses: 1
    >>> Larger Guesses: 2

#####Break large problems into smaller pieces!
  Sometimes it is useful for beginners to complete a smaller, simpler program before tackling the full project.
  Start with an easy program that only completes part of the project.
  Name your project 'Assignment_2'. Always use variable and function names that clearly describe what you are creating.

#####Please Design First
  Dividing a larger problem into smaller sub-problems is an important technique in computer programming.

It is a good practice to design your software before you write the code.
Here are some design tasks you should complete before you start:
-  Write out a list of variables you think you will need (e.g. int totalGuesses; // count of many guesses altogether scores)
-  Flow chart (or Pseudo code) the selection statement(s) to decide if the guess was too high, too low, or the equivalent number
-  Flow chart (or Pseudo code) the loop, include the check for -1 input and update of variables
-  In other words, have some idea about HOW you are going to solve the problem, BEFORE you try to solve the problem.
  
**Please use functions to write this game. Do not attempt this program without the use of functions.**
If possible, try to create a class for the game. We can go over classes in python during the Thursday meeting if you want to use classes.
