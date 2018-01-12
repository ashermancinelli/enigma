#
#
# title: Enigma Project 
# contributors: Asher Mancinelli, Jude Battista, Alyssa La Fleur
# class: MA 362
# professor: Nate Moyer
# last updated: 1/12/18
#
#

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class enigma:

    __init__(self, activeRotors, plugBoard):
        
        for rotor in activeRotors:
            self.rotors.append(rotor)

class rotor:
class plugBoard:
    plugBoardMapping = { char: char for char in letters }  
    
    __init__(self, plugBoardList):
        for pair in plugBoardList:

