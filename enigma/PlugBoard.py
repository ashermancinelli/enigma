



from collections import OrderedDict

class PlugBoard:
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    def __init__(self, plugBoardPairs):
        
        # the plug board is originally set up as a mapping from each letter to itself.
        self.plugBoardMapping = OrderedDict({ char.lower(): char.lower() for char in self.letters })
        
        for pair in plugBoardPairs:
            self.plugBoardMapping[pair[0]] = pair[1]
            self.plugBoardMapping[pair[1]] = pair[0]

    def evaluate(self, char):
        return self.plugBoardMapping[char.lower()]
    