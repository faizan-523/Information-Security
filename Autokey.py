def Autokey_Encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.upper().replace(' ', '')
    key = key.upper().replace(' ', '')
    
    full_key = key + plaintext
    ciphertext = ''

    for i in range(len(plaintext)):
        p = alphabet.index(plaintext[i])
        k = alphabet.index(full_key[i])
        c = (p + k) % 26
        ciphertext += alphabet[c]
    return ciphertext

def Autokey_Decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper().replace(' ', '')
    key = key.upper().replace(' ', '')
    
    full_key = key
    plaintext = ''

    for i in range(len(ciphertext)):
        c = alphabet.index(ciphertext[i])
        k = alphabet.index(full_key[i])
        p = (c - k + 26) % 26
        plaintext += alphabet[p]
        full_key += alphabet[p]
    return plaintext

plaintext = "DEFENDTHEEASTWALLOFTHECASTLE"
key = "FORTIFICATION"

print("Plaintext:", plaintext)
print("Key:", key)

cipher_text = Autokey_Encrypt(plaintext, key)
print("Ciphertext:", cipher_text)

decrypted_text = Autokey_Decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)