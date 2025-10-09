def encrypt(text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text=text.upper()
    result = ''
    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % 26
            result += alphabet[index]

        else:
            result += char
    return result

def decrypt(cipher, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher=cipher.upper()
    result = ''

    for char in cipher:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % 26
            result += alphabet[index]
        else:
            result += char
    return result


message="Network Security"
shift=5
print("Original Message:", message)

encrypted_message = encrypt(message, shift)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)
