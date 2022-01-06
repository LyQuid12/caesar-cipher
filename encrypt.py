import string

def caesar_cipher_encrypt(text, shift):
    if shift >= 26:
        raise TypeError("Shift cannot more than 25")

    alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

    def shift_alphabet(alphabets):
        return alphabets[shift:] + alphabets[:shift]

    
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)

    table = str.maketrans(final_alphabet, final_shifted_alphabet)

    return text.translate(table)
