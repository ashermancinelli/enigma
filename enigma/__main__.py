'''
Main file to be run when running the directory or zipfile
'''


from CLIController2 import *

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



