
from PlugBoard import *
# from Rotor import *
from RotorByList import *

class EnigmaMachine:

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    _rotors = [] 
    _rotationsByRotor = []

    def __init__(self, activeRotorIndeces, plugBoardPairs, rotorStartingPositions):

        self.pb = PlugBoard(plugBoardPairs)

        # rotor index indicates which rotor will be in the enigma machine 
        # from right to left, as that is the order the signal would travel through
        # the actual enigma machine. An example of initializing an EnigmaMachine object
        # would be:
        #   em = EnigmaMachine([1, 5, 2], [['a', 't'], ['s', 'v'], ['l', 'k']], ['a','a','a'])
        # In the example above, the rotors would be positioned with rotor 1 rightmost,
        # rotor 5 in the middle, and rotor 2 leftmost in a real enigma machine. The 
        # letters 'a' and 't' would be mapped to each other in the plugboard, as well 
        # as 's' and 'v', etc etc.
        for ari in activeRotorIndeces:
            self._rotors.append(Rotor(ari))

        for r in self._rotors:
            self._rotationsByRotor.append(0)        

        self._totalRotations = 0

        # this is a special case of the Rotor class, where the reflector is 
        # defined. This acts essentially like a normal rotor would, but has its own 
        # dictionary defined. 
        self.reflector = Rotor(-1)

        for index in range(len(self._rotors)):
            for rotation in range(self.letters.index(rotorStartingPositions[index])):
                self._rotors[index].rotate()


        
    def rotationHandler(self):
        self._totalRotations += 1
        
        self._rotors[0].rotate()
        self._rotationsByRotor[0] += 1

        for index in range(len(self._rotors) - 1):
            while ( self._rotationsByRotor[index] // 26 ) > self._rotationsByRotor[ index + 1 ]:
                self._rotors[ index + 1 ].rotate()



    def evaluate(self, char):

        l = self.pb.evaluate(char)

        self.rotationHandler()
        
        for r in self._rotors:
            l = r.evaluate(l)
        
        l = self.reflector.evaluate(l)
        
        i = len(self._rotors) - 1
        
        while i >= 0:
            l = self._rotors[i].evaluate(l, reverse=True)
            i -= 1

        return self.pb.evaluate(l)
        
        