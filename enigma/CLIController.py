from EnigmaMachine import *

if __name__ == '__main__':

    em = EnigmaMachine([1,2],[['t', 's'], ['z', 'a'], ['e', 'n']], ['s','n'])
    
	
	
    while True:

        raw_pt = input("enter the plaintext to be encrypted\n>>>").lower()
        pt = ''
        for ch in raw_pt:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                pt += ch
            elif ch == ' ':
                pt += 'x'

        ct = ''
        for ch in pt:
            ct += em.evaluate(ch)

        print(ct)

        