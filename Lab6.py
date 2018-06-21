VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

if __name__ == '__main__':
    cont = 'y'

    print'Welcome to the Pig Latin Translator!'

    while cont.lower() == 'y':
        sentence = raw_input("Enter a line to be translated: ")
        sentence_lower = sentence.lower()
        words = sentence_lower.split(' ')

        for word in words:
            if word[0] in VOWELS:
                print word + "way",
            else:
                print word[1:] + word[0] + "ay",

        cont = raw_input('\nTranslate another line?  y/n  ')

    print'Ok, goodbye!'