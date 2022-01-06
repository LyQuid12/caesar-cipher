import string

real_msg = input("Input real message : ")
shift = int(input("Input shift : "))

if shift >= 26:
    raise TypeError("Shift cannot more than 25") 

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = real_msg.translate(table)

print(encrypted)
