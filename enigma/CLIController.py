from EnigmaMachine import *

if __name__ == '__main__':

    em = EnigmaMachine([ 1, 2, 6 ],[['t', 's'], ['z', 'a'], ['e', 'n'], ['b', 'l'], ['f', 'o']], ['s','n', 'k'])
    print("This enigma machine is configured with rotors I, II, and VI, a configured plugboard, and the rotors initially set to s, n, and k. Happy encrypting, sailor!") 
    
	
	
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

        
