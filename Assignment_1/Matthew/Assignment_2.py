import random

def main():

    compguess = random.randint(1, 100)
    largerguesses = 1
    smallguesses = 1

    loop = True
    while loop:

        userguess = int(raw_input('Pick a number between 1 - 100. '))

        if userguess < 0:
            return -1

        if (userguess > compguess):
            print 'Your guess is too high'

            largerguesses+=1

        elif (userguess < compguess):
            print 'Your guess is too low'

            smallguesses+=1

        elif (userguess == compguess):
            print 'You’ve guessed it right!'
            loop = False 
            print 'Total number of Large guesses >> ', largerguesses
            print 'Total number of Small guesses >> ', smallguesses
            print 'Total number of guesses ', largerguesses + smallguesses

if __name__ == '__main__':
    main()
