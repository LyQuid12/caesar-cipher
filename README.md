# caesar-cipher
A simple Caesar Cipher encryption made using Python


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
