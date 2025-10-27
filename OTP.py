def OTP_Encryption(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""

    for i in range(len(plaintext)):
            p = ord(plaintext[i]) - 65
            k = ord(key[i]) - 65
            c = (p + k) % 26
            ciphertext += chr(c + 65)
    return ciphertext

def OTP_Decryption(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""

    for i in range(len(ciphertext)):
            c = ord(ciphertext[i]) - 65
            k = ord(key[i]) - 65
            p = (c - k + 26) % 26
            plaintext += chr(p + 65)
    return plaintext

pt = input("Enter Plaintext: ")
k = input("Enter Key (same length as plaintext): ") 

if len(pt) != len(k):
    print("Error: Plaintext and Key must be of the same length!")
else:
    ct = OTP_Encryption(pt, k)
    print("Ciphertext:", ct)

    decrypted_pt = OTP_Decryption(ct, k)
    print("Decrypted Plaintext:", decrypted_pt)