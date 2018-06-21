if __name__ == '__main__':

    print'Learn your squares and cubes!'
    cont = 'y'

    while cont.lower() == 'y':
        user_number = input('Enter an integer:  ')

        print 'Number       Squared     Cubed'
        print '======       =======     ======'

        for i in range(1, user_number+1):
            square = i*i
            cube = i*i*i
            print str(i) + '            ' + str(square) + '            ' + str(cube)

        cont = raw_input('Would you like to continue? y/n  ')

    print'Ok, goodbye!'