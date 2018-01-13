
from PlugBoard import *
from Rotor import *


class EnigmaMachine:

    rotors = []

    def __init__(self, activeRotorIndeces, plugBoardPairs):

        self.pb = PlugBoard(plugBoardPairs)

        # rotor index indicates which rotor will be in the enigma machine 
        # from right to left, as that is the order the signal would travel through
        # the actual enigma machine. An example of initializing an EnigmaMachine object
        # would be:
        #   em = EnigmaMachine([1, 5, 2], [['a', 't'], ['s', 'v'], ['l', 'k']])
        # In the example above, the rotors would be positioned with rotor 1 rightmost,
        # rotor 5 in the middle, and rotor 2 leftmost in a real enigma machine. The 
        # letters 'a' and 't' would be mapped to each other in the plugboard, as well 
        # as 's' and 'v', etc etc.
        r1 = Rotor(activeRotorIndeces[0])
        r2 = Rotor(activeRotorIndeces[1])
        r3 = Rotor(activeRotorIndeces[2])
        self.rotors = [r1, r2, r3]
        if len(activeRotorIndeces) > 3:
            r4 = Rotor(activeRotorIndeces[3])
            self.rotors.append(r4)
        if len(activeRotorIndeces) > 4:
            r5 = Rotor(activeRotorIndeces[4])
            self.rotors.append(r5)

        # this is a special case of the Rotor class, where the reflector is 
        # defined. This acts essentially like a normal rotor would, but has its own 
        # dictionary defined. 
        self.reflector = Rotor(-1)

        


    def evaluate(self, char):

        l = self.pb.evaluate(char)
        
        for r in self.rotors:
            l = r.evaluate(l)
        
        l = self.reflector.evaluate(l)
        
        i = len(self.rotors) - 1
        
        while i >= 0:
            l = self.rotors[i].evaluate(l)
            i -= 1

        return self.pb.evaluate(l)
        
        