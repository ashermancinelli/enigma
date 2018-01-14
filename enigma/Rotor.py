

from collections import OrderedDict
from random import randint

class Rotor:

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    _rotorDicts = [
        OrderedDict({ char.lower(): char.lower() for char in letters }),
        OrderedDict({ char.lower(): char.lower() for char in letters }),
        OrderedDict({ char.lower(): char.lower() for char in letters }),
        OrderedDict({ char.lower(): char.lower() for char in letters })
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


    # this is the dictionary for the reflector, a special instance 
    # of the rotor class since they operate almost the same

    ##################################################################################
    _reflectorDict = OrderedDict({ char.lower(): char.lower() for char in letters })
    _reflectorShuffleKeys = [['m', 'q'],['v','u'],['r','i'],['d','b'],['x','p'],['y','l'],
                            ['z','f'],['j','t'],['h','e'],['o','a'],['w','s'],['n','c'],['k','g']]

    for pair in _reflectorShuffleKeys:
        _reflectorDict[pair[0]] = pair[1]
        _reflectorDict[pair[1]] = pair[0]
    ##################################################################################



    _rotorIndex = 0
    _rotorDict = OrderedDict({})
    _type = 'rotor'

    def __new__(self):
        rotationHandler.keyPresses = 0

    def __init__(self, rotorIndex):
        if rotorIndex < 1 or rotorIndex > 8: 
            if rotorIndex == -1:
                self._rotorDict = self._reflectorDict
                self._type = 'reflector'
            else:   raise IndexError
        else:
            self._rotorIndex = rotorIndex
            self._rotorDict = self._rotorDicts[rotorIndex]
        Rotor.rotationHandler
        


    def rotate(self, reverse=False):
        dictList = [  ]
        newDictList = [ [char, char] for char in self.letters ]

        # dictionaries are not iterable with an index, so we convert the dictionary 
        # to a list first, copy over the adjusted list, and then fill the dict with the 
        # appropriate offset values.
        
        for k in self._rotorDict:
            dictList.append([k, self._rotorDict[k]])
        
        print((self._rotorDict,dictList))
        for index in range(len(dictList)):
            try:
                newDictList[index%26][1] = dictList[(index+1)%26][1]
            except IndexError as e:
                print(e, ': ', index)
                pass

        self._rotorDict = OrderedDict({ pair[0]: pair[1] for pair in newDictList })



    def evaluate(self, char):
        if self._type == 'rotor':
            Rotor.rotationHandler()
        return self._rotorDict[char]

