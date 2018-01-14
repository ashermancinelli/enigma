from EnigmaMachine import *

if __name__ == '__main__':

    em = EnigmaMachine([1,2],[['t', 's'], ['z', 'a'], ['e', 'n']], ['a','a'])
    # em = EnigmaMachine([1], [], ['a','a','a'])
    
    while True:

        raw_pt = input("enter the plaintext to be encrypted\n>>>").lower()
        pt = ''
        for ch in raw_pt:
            if ch in 'abcdefghijklmnopqrstuv':
                pt += ch
            elif ch == ' ':
                pt += 'x'

        ct = ''
        for ch in pt:
            ct += em.evaluate(ch)

        print(ct)

        