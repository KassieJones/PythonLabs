import random

if __name__ == '__main__':
     cont = 'y'
     print'Welcome to the casino!'

     while cont.lower() == 'y':
        die_sides = input('How many sides should each die have?  ')

        die1 = random.randint(1, die_sides)
        die2 = random.randint(1, die_sides)

        print'Results:'
        print die1
        print die2

        cont = raw_input('Roll again?  y/n  ')

     print'Better luck next time!'