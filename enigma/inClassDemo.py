from EnigmaMachine import *

if __name__ == '__main__':

    em = EnigmaMachine([ 1 ],[['t', 's'], ['z', 'a'], ['e', 'n'], ['b', 'l'], ['f', 'o'], ['w', 'h'], ['c', 'g'], ['d', 'r'], ['i', 'q'], ['p', 'v'], ['j', 'm'], ['k', 'u'], ['x', 'y']], ['a'])

    print('Initial Mapping: ', em._rotors[0]._rotorOffsetList)
	
	
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
            print('Rotor Mapping: ', em._rotors[0]._rotorOffsetList)
 

        print(ct)

        
