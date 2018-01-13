from EnigmaMachine import *

if __name__ == '__main__':
    em = EnigmaMachine([1,2,3],[['t', 's'], ['z', 'a'], ['e', 'n']])
    pt = 'noxiy'
    ct = ''
    for ch in pt:
        ct += em.evaluate(ch)
    print(ct)