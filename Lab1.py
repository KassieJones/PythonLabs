if __name__ == '__main__':
    user_number = input('Please enter a number between 1 and 100')
    print'You entered:  ', user_number

    if user_number%2 != 0:
        if user_number <= 60:
            print 'Odd'
        else:
            print "Odd and over 60"
    else:
        if user_number >= 2 and user_number <=25:
            print 'Even and less than 25'
        elif user_number >= 26 and user_number <= 60:
            print 'Even'
        elif user_number > 60:
            print 'Even and over 60'