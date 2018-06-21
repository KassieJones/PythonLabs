if __name__ == '__main__':
    fact = 1
    cont = 'y'

    print'Welcome to the Factorial Calculator!'

    while cont.lower() == 'y':
        user_number = input('Enter and integer that is greater than 0 but less than 10:  ')

        for i in range(1, user_number+1):
            fact = fact * i

        print'The factorial of ' + str(user_number) + ' is ' + str(fact)
        cont = raw_input('Would you like to continue?  y/n  ')

    print'Ok, goodbye!'