

from random import randint

class Rotor:

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    _possibleOffsets = [
        [24, 1, 4, 12, 9, 14, 6, 17, 8, 16, 7, 0, 23, 2, 21, 22, 19, 3, 11, 15, 25, 13, 18, 5, 10, 20],
        [20, 0, 4, 3, 9, 14, 17, 6, 24, 21, 25, 11, 8, 15, 18, 2, 5, 10, 16, 13, 19, 12, 22, 7, 23, 1],
        [5, 10, 18, 8, 14, 19, 12, 2, 3, 24, 20, 7, 21, 23, 0, 15, 17, 22, 25, 4, 13, 6, 1, 9, 16, 11],
        [7, 14, 20, 21, 23, 4, 6, 10, 15, 13, 24, 3, 2, 5, 16, 22, 11, 9, 1, 0, 19, 18, 12, 17, 8, 25],
        [11, 7, 3, 5, 0, 2, 14, 23, 6, 1, 19, 4, 25, 13, 16, 9, 21, 17, 18, 12, 10, 8, 22, 15, 24, 20],
        [17, 0, 11, 10, 20, 2, 6, 4, 12, 5, 22, 15, 23, 14, 24, 3, 13, 19, 21, 18, 8, 16, 7, 9, 25, 1],
        [2, 6, 17, 12, 19, 0, 3, 16, 10, 4, 20, 14, 9, 15, 22, 18, 24, 5, 8, 21, 7, 11, 1, 25, 23, 13],
        [2, 21, 1, 9, 5, 13, 8, 15, 22, 23, 19, 18, 3, 24, 12, 17, 10, 0, 6, 11, 25, 4, 16, 14, 20, 7],
    ]

    _reflectorOffsetList = [7, 22, 21, 12, 23, 2, 24, 13, 0, 4, 11, 9, 19, 10, 15, 14, 18, 16, 20, 8, 25, 5, 1, 6, 3, 17]

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
            self._rotorOffsetList = self._possibleOffsets[rotorIndex]


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
            
                

