

from random import randint

class Rotor:

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    _possibleOffsets = [
	[4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9],
	[0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4],
	[1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14],
	[4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1],
	[21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10],
	[9, 15, 6, 21, 14, 20, 12, 5, 24, 16, 1, 4, 13, 7, 25, 17, 3, 10, 0, 18, 23, 11, 8, 2, 19, 22],
	[13, 25, 9, 7, 6, 17, 2, 23, 12, 24, 18, 22, 1, 14, 20, 5, 0, 8, 21, 11, 15, 4, 10, 16, 3, 19],
	[5, 10, 16, 7, 19, 11, 23, 14, 2, 1, 9, 18, 15, 3, 25, 17, 0, 12, 4, 22, 13, 8, 20, 24, 6, 21],
    ]

    _reflectorOffsetList = [4,9,12,25,0,11,24,23,21,1,22,5,2,17,16,20,14,13,19,18,15,8,10,7,6,3]
	
    _rotations = 0
    _rotorOffsetList = []
    _type = 'rotor'

    def __init__(self, rotorIndex):

        if rotorIndex < 1 or rotorIndex > 8: 
            if rotorIndex == -1:
                self._rotorOffsetList = self._reflectorOffsetList
                self._type = 'reflector'
            else:   raise IndexError
        else:
            self._rotorOffsetList = self._possibleOffsets[rotorIndex - 1]


    def rotate(self):
        firstElement = self._rotorOffsetList[0]
        del self._rotorOffsetList[0]
        self._rotorOffsetList.append(firstElement)


    def evaluate(self, char, reverse=False):
		
        char = char.lower()

        if reverse:
            return self.letters[self._rotorOffsetList.index(self.letters.index(char))]

        else:
            return self.letters[self._rotorOffsetList[self.letters.index(char)]]
            
                

