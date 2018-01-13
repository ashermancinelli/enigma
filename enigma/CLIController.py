from EnigmaMachine import *

if __name__ == '__main__':

    em = EnigmaMachine([1,2,3],[['t', 's'], ['z', 'a'], ['e', 'n']], ['a','a','a'])
    pt = input("enter the plaintext to be encrypted\n>>>")
    ct = ''
    for ch in pt:
        ct += em.evaluate(ch)
    print(ct)