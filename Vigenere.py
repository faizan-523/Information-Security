def vigenere_Encryption(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    
    # Repeat key
    while len(key) < len(plaintext):
        key += key
    key = key[:len(plaintext)]

    ciphertext = ""
    j = 0  

    for i in range(len(plaintext)):
        if plaintext[i] == " ":  
            ciphertext += " "
        else:
            p = ord(plaintext[i]) - 65
            k = ord(key[j]) - 65
            c = (p + k) % 26
            ciphertext += chr(c + 65)
            j += 1
    return ciphertext


def vigenere_Decryption(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    
    while len(key) < len(ciphertext):
        key += key
    key = key[:len(ciphertext)]

    plaintext = ""
    j = 0

    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
        else:
            c = ord(ciphertext[i]) - 65
            k = ord(key[j]) - 65
            p = (c - k + 26) % 26
            plaintext += chr(p + 65)
            j += 1
    return plaintext


pt = input("Enter Plaintext: ")
k = input("Enter Key: ")

ct = vigenere_Encryption(pt, k)
print("Ciphertext:", ct)

decrypted_pt = vigenere_Decryption(ct, k)
print("Decrypted Plaintext:", decrypted_pt)
