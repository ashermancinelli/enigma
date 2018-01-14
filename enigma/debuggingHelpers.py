

class RotorMismatchError(Exception):
    def __str__(self):
        return "The number of rotors and the number of indices for the rotors does not match"