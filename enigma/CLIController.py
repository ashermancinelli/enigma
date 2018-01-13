from Rotor import *
from PlugBoard import *
from EnigmaMachine import *

if __name__ == '__main__':
    em = EnigmaMachine([1,2,3],[['t', 's'], ['z', 'a'], ['e', 'n']])
    print(em.evaluate('a'))