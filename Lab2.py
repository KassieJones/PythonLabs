if __name__ == '__main__':
    cont = 'y'

    print'Welcome to the Room Detail Generator'

    while cont.lower() == 'y':
        length = input('Enter Length:  ')
        width = input('Enter Width:  ')
        print 'Your room is ' + str(length) + 'x' + str(width)
        area = length * width
        perimeter = (2*length) + (2*width)
        print 'Your area is ' + str(area) + ', and your perimeter is ' + str(perimeter)+ '.'
        cont = raw_input('Would you like to continue? y/n')

    print'Ok, goodbye!'