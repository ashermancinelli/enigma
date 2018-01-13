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
##################################################################################
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

_rotorDicts = [
    { char.lower(): char.lower() for char in letters },
    { char.lower(): char.lower() for char in letters },
    { char.lower(): char.lower() for char in letters },
    { char.lower(): char.lower() for char in letters }
]

_shuffleKeys = [
    [['j','p'],['y','l'],['f','v'],['n','u'],['k','g'],['w','h'],
     ['o','d'],['e','c'],['b','q'],['t','z'],['i','a'],['r','m'],['x','s']],

    [['o','q'],['y','m'],['a','g'],['i','j'],['s','r'],['v','k'],
     ['z','u'],['b','t'],['c','e'],['w','h'],['n','l'],['f','p'],['d','x']],

    [['q','x'],['z','t'],['y','o'],['s','r'],['i','d'],['h','w'],
     ['f','m'],['c','k'],['v','g'],['b','e'],['u','j'],['l','p'],['n','a']],

    [['q','h'],['l','t'],['v','n'],['p','b'],['k','a'],['d','z'],
     ['r','m'],['f','y'],['e','w'],['u','o'],['i','x'],['g','j'],['s','c']]
]

for index in range(4):
    for pair in _shuffleKeys[index]:
        _rotorDicts[index][pair[0]] = pair[1]
        _rotorDicts[index][pair[1]] = pair[0]

##################################################################################






# this is the dictionary for the reflector, a special instance 
# of the rotor class since they operate almost the same

##################################################################################
_reflectorDict = { char.lower(): char.lower() for char in letters }
_reflectorShuffleKeys = [['m', 'q'],['v','u'],['r','i'],['d','b'],['x','p'],['y','l'],
                         ['z','f'],['j','t'],['h','e'],['o','a'],['w','s'],['n','c'],['k','g']]

for pair in _reflectorShuffleKeys:
    _reflectorDict[pair[0]] = pair[1]
    _reflectorDict[pair[1]] = pair[0]
##################################################################################



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
        for r in activeRotorIndeces:
            self.rotors.append(Rotor(r))

        # this is a special case of the Rotor class, where the reflector is 
        # defined. This acts essentially like a normal rotor would, but has its own 
        # dictionary defined. 
        reflector = Rotor(-1)

        


    def evaluate(self, char):

        l = self.pb.evaluate(char)
        
        for r in self.rotors:
            l = r.evaluate(l)
        
        l = self.reflector.evaluate(l)
        
        i = len(rotors)
        
        while i >= 0:
            l = self.rotors[i].evaluate(l)
            i -= 1

        return self.pb.evaluate(l)
        
        

class Rotor:

    _rotorIndex = 0
    _rotorDict = {}
    _type = 'rotor'

    def __init__(self, rotorIndex):
        if rotorIndex < 1 or rotorIndex > 8: 
            if rotorIndex == -1:
                _rotorDict = _reflectorDict
                _type = 'reflector'
            else:   raise IndexError
        else:
            self._rotorIndex = rotorIndex
            self._rotorDict = _rotorDicts[rotorIndex]


    def rotate(self):
        dictList = []
        newDictList = []

        # dictionaries are not iterable with an index, so we convert the dictionary 
        # to a list first, copy over the adjusted list, and then fill the dict with the 
        # appropriate offset values.
        for k, v in _rotorDict:
            dictList.append([k, v])
        
        for index in len(dictList):
            newDictList[index][1] = dictList[(index+1)%26][1]

        _rotorDict = { pair[0]: pair[1] for pair in newDictList }


    def evaluate(self, char):
        if self._type == 'rotor':
            rotate()
        return _rotorDict[char]



class PlugBoard:
    
    def __init__(self, plugBoardPairs):
        
        # the plug board is originally set up as a mapping from each letter to itself.
        self.plugBoardMapping = { char.lower(): char.lower() for char in letters }  
        
        for pair in plugBoardPairs:
            self.plugBoardMapping[pair[0]] = pair[1]
            self.plugBoardMapping[pair[1]] = pair[0]

    def evaluate(self, char):
        return self.plugBoardMapping[char.lower()]
    
    

if __name__ == '__main__':
    em = EnigmaMachine([1,2,3],[['t', 's'], ['z', 'a'], ['e', 'n']])
    plaintext = 'asher'
    ciphertext = ''
    # for ch in pt:
    #     ct += em.evaluate(ch)
    
    # print(ct)
    ct = em.evaluate('a')
