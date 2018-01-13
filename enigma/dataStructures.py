#
#
# title: Enigma Project 
# contributors: Asher Mancinelli, Jude Battista, Alyssa La Fleur
# class: MA 362
# professor: Nate Moyer
# last updated: 1/12/18
#
#


# These are the default dictionaries for each rotor, and can be modified 
# by shuffling or adding new letters into the subsequent loops.
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

_rotorDicts = [
    { char.lower(): char.lower() for char in letters },
    { char.lower(): char.lower() for char in letters },
    { char.lower(): char.lower() for char in letters },
    { char.lower(): char.lower() for char in letters }
]

_shuffleKeys = [
    [['j','p'],['y','l'],['f','v'],['n','u'],['k','g'],['w','h'],['o','d'],['e','c'],['b','q'],['t','z'],['i','a'],['r','m'],['x','s']],
    [['o','q'],['y','m'],['a','g'],['i','j'],['s','r'],['v','k'],['z','u'],['b','t'],['c','e'],['w','h'],['n','l'],['f','p'],['d','x']],
    [['q','x'],['z','t'],['y','o'],['s','r'],['i','d'],['h','w'],['f','m'],['c','k'],['v','g'],['b','e'],['u','j'],['l','p'],['n','a']],
    [['q','h'],['l','t'],['v','n'],['p','b'],['k','a'],['d','z'],['r','m'],['f','y'],['e','w'],['u','o'],['i','x'],['g','j'],['s','c']]
]

for index in range(4):
    for pair in _shuffleKeys[index]:
        _rotorDicts[index][pair[0]] = pair[1]
        _rotorDicts[index][pair[1]] = pair[0]



class EnigmaMachine:

    rotors = []

    __init__(self, activeRotorIndeces, plugBoardPairs):

        # rotor index indicates which rotor will be in the enigma machine 
        # from right to left, as that is the order the signal would travel through
        # the actual enigma machine. An example of initializing an EnigmaMachine object
        # would be:
        #   em = EnigmaMachine([1, 5, 2], [['a', 't'], ['s', 'v'], ['l', 'k']])
        # In the example above, the rotors would be positioned with rotor 1 rightmost,
        # rotor 5 in the middle, and rotor 2 leftmost in a real enigma machine. The 
        # letters 'a' and 't' would be mapped to each other in the plugboard, as well 
        # as 's' and 'v', etc etc.
        for r in activeRotorIndeces:
            self.rotors.append(Rotor(r))
        

class Rotor:

    _rotorIndex = 0

    __init__(self, rotorIndex):
        if rotorIndex < 1 or rotorIndex > 8: raise IndexError
        self._rotorIndex = rotorIndex

class PlugBoard:

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    # the plug board is originally set up as a mapping from each letter to itself.
    plugBoardMapping = { char.lower(): char.lower() for char in PlugBoard.letters }  
    
    __init__(self, plugBoardPairs):
        for pair in plugBoardPairs:
            plugBoardMapping[pair[0]] = pair[1]
            plugBoardMapping[pair[1]] = pair[0]
    
    

