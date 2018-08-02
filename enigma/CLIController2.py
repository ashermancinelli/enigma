from EnigmaMachine import *
import copy

def keepGoing(chars):
    cont = input("{} [y/n]".format(chars)).lower()
    if cont == 'y':
        return True
    elif cont == 'n':
        return False
    else:
        keepGoing(chars)



def makePublicEM():
    listOfRotorIndeces = []
    index = input("\tPlease enter the indeces of the rotors you would like to use, separated by commas. \n\t[Options include 1 through 3, you may not use any rotor more than once.]\n>>>")
    listOfRotorIndeces = index.split(',')
    for i in range(len(listOfRotorIndeces)):
        listOfRotorIndeces[i] = int(listOfRotorIndeces[i])
    print('Please enter the initial setting you would like each of the rotors to have by entering a character for each rotor:')
    rotorStartingPositions = []
    for i in listOfRotorIndeces:
        rotorStartingPositions.append(input('Starting position for rotor with index {}:\n>>>'.format(i)).lower())
        
    return EnigmaMachine(listOfRotorIndeces, [], rotorStartingPositions) 



def makeNavyEM():
    listOfRotorIndeces = []
    index = input("\tPlease enter the indeces of the rotors you would like to use, separated by commas. \n\t[Options include 1 through 5, you may not use any rotor more than once.]\n>>>")
    listOfRotorIndeces = index.split(',')
    for i in range(len(listOfRotorIndeces)):
        listOfRotorIndeces[i] = int(listOfRotorIndeces[i])
    numberOfPlugboarPairs = int(input('Please enter the number of plugboard pairs you would like to use in your enigma machine (maximum of 13).\n>>>'))
    print('Please enter the letters you would like to pair together one pair at a time, seperated by a comma. You may not use the same letter twice.')
    plugboardPairs = []
    for i in range(numberOfPlugboarPairs):
        inp = input('Pair {}:\n>>>'.format(i + 1)).lower()
        plugboardPairs.append(inp.split(','))

    print('Please enter the initial setting you would like each of the rotors to have by entering a character for each rotor:')
    rotorStartingPositions = []
    for i in listOfRotorIndeces:
        rotorStartingPositions.append(input('Starting position for rotor with index {}:\n>>>'.format(i)).lower())
        
    return EnigmaMachine(listOfRotorIndeces, plugboardPairs, rotorStartingPositions) 


def mainLoop(em):
    fresh_em = copy.copy(em)
    pt = input('Enter the plaintext to be encrypted:\n>>>').lower()
    checked_pt = ''
    for ch in pt:
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            checked_pt += ch
        elif ch == ' ':
            checked_pt += 'x'

    ct = ''
    for ch in checked_pt:
        ct += em.evaluate(ch)

    print(ct)
    if keepGoing('Would you like to reset this enigma machie to its original configuration?'):
        mainLoop(fresh_em)
    if keepGoing('Would you like to continue with this enigma machine configuration?'):
        mainLoop(em)




if __name__ == '__main__':
    while True:
        print("""
        Welcome to the MA362 Enigma Machine Emulator!
        
        Please choose one of the following options by typing the letter in brackets. \n\tThe description of each command is given to the right of the bracketed character:
        [N] Initialize a WWII German Navy grade M1/M2 Enigma Machine.
        [P] Initialize a WWII German Public use Enigma Machine""")
        command = input('>>>').lower()
        if command == 'n':
            em = makeNavyEM()
        elif command == 'p':
            em = makePublicEM()

        mainLoop(em)

        if not keepGoing('Would you like to continue using this program?'):
            exit()
