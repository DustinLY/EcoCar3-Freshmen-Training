import random
import math


def hello_World():
    print 'Hello World'


def greatest_Num(num1, num2):
    if num1 > num2:
        print num1
    else:
        print num2


def get_Greatest_Num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def roll_Dice():
    rolled_num = math.floor(random.randrange(1, 7))
    print rolled_num
    return rolled_num


def main():
    loop = True
    while loop:
        choice = raw_input('\n1. Print "Hello World"\n2. Print Greatest Number\n' +
                           '3. Roll a dice (get a number between 1 and 6)\n' +
                           '4. Exit Program\n>> ')
        if choice == '1':
            hello_World()
        elif choice == '2':
            num_one = raw_input('Enter the first number: ')
            num_two = raw_input('Enter the second number: ')
            greatest_Num(num_one, num_two)
        elif choice == '3':
            roll_Dice()
        elif choice == '4':
            loop = False
        else:
            print 'You did not enter a valid option. Try Again.'

if __name__ == '__main__':
    main()
