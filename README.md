# Caesar Cipher

A simple Caesar Cipher encryption made using Python.
For the packages versions can be seen [here](https://github.com/EterNomm/Whitehat/blob/main/examples/caesar_cipher.py) (Using [Whitehat](https://pypi.org/project/whitehat) packages)

Example :
- Encrypt
```py
import encrypt

text = "LyQuid"
encrypted = caesar_cipher_encrypt(text, 12)
print(encrypted)

# output : XkCgup
```

- Decrypt
```py
import encrypt

text = "XkCgup"
decrypted = caesar_cipher_decrypt(text, 12)
print(decrypted)

# output : LyQuid
```
