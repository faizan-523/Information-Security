def Caesor_Encrypt(text, shift):
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

def Caesar_Decrypt(cipher, shift):
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

def matrix(key):
    key = key.upper().replace("J", "I")
    matrix=""
    for ch in key:
        if ch not in matrix and ch.isalpha():
            matrix += ch

    for ch in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if ch not in matrix:
            matrix += ch

    return [list (matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix,ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i,j
    return None

def Playfair_Encrypt(plaintext,matrix):
    text=plaintext.upper().replace("J","I")
    pairs=[]
    i=0
    while i < len(text):
        a=text[i]
        b=text[i+1] if i+1 < len(text) else 'X'
        if a==b:
            pairs.append((a,'X'))
            i+=1
        else:
            pairs.append((a,b))
            i+=2
            
    cipher=""
    for a,b in pairs:
                r1, c1= find_position(matrix,a)
                r2, c2= find_position(matrix,b)
                if r1==r2:
                    cipher+=matrix[r1][(c1+1)%5]
                    cipher+=matrix[r2][(c2+1)%5]
                elif c1==c2:
                    cipher+=matrix[(r1+1)%5][c1]
                    cipher+=matrix[(r2+1)%5][c2]
                else:
                    cipher+=matrix[r1][c2]
                    cipher+=matrix[r2][c1]
    return cipher
        
def Playfair_Decrypt(ciphertext,matrix):
    plain=""
    for i in range(0,len(ciphertext),2): 
        a,b=ciphertext[i],ciphertext[i+1]
        r1,c1=find_position(matrix,a)
        r2,c2=find_position(matrix,b)

        if r1==r2:
            plain+=matrix[r1][(c1-1)%5]  
            plain+=matrix[r2][(c2-1)%5]

        elif c1==c2:
            plain+=matrix[(r1-1)%5][c1] 
            plain+=matrix[(r2-1)%5][c2]

        else:
            plain+=matrix[r1][c2]  
            plain+=matrix[r2][c1]
    return plain

def vigenere_Encryption(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    
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


def row_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = [int(k) for k in key]

    col = len(key)
    rows = []
    
    for i in range(0, len(plaintext), col):
        part = plaintext[i:i+col]
        if len(part) < col:
            part += "X" * (col - len(part))
        rows.append(part)

    ciphertext = ""
    for num in sorted(key):
        col_index = key.index(num)
        for row in rows:
            ciphertext += row[col_index]
    return ciphertext


def row_transposition_decrypt(ciphertext, key):
    key = [int(k) for k in key]
    col = len(key)
    row_count = len(ciphertext) // col

    table = [[""] * col for _ in range(row_count)]
    index = 0

    for num in sorted(key):
        col_index = key.index(num)
        for r in range(row_count):
            table[r][col_index] = ciphertext[index]
            index += 1

    plaintext = ""
    for r in range(row_count):
        for c in range(col):
            plaintext += table[r][c]

    return plaintext.rstrip("X")

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


while True:
    print("\n===== MENU =====")
    print("1. Caesar Cipher")
    print("2. Playfair Cipher")
    print("3. Vigenere Cipher")
    print("4. Row Transposition Cipher")
    print("5. One-Time Pad (OTP)")
    print("6. Autokey Cipher")
    print("7. Exit")

    choice = input("\nEnter choice (1-7): ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift: "))
        enc = Caesor_Encrypt(text, shift)
        dec = Caesar_Decrypt(enc, shift)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == "2":
        text = input("Enter text: ")
        key = input("Enter key: ")
        m = matrix(key)
        enc = Playfair_Encrypt(text, m)
        dec = Playfair_Decrypt(enc, m)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == "3":
        text = input("Enter text: ")
        key = input("Enter key: ")
        enc = vigenere_Encryption(text, key)
        dec = vigenere_Decryption(enc, key)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == "4":
        text = input("Enter text: ")
        key = input("Enter numeric key (e.g. 3 1 4 2): ").split()
        enc = row_transposition_encrypt(text, key)
        dec = row_transposition_decrypt(enc, key)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == "5":
        text = input("Enter text (same length as key): ")
        key = input("Enter key (same length): ")
        enc = OTP_Encryption(text, key)
        dec = OTP_Decryption(enc, key)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == "6":
        text = input("Enter text: ")
        key = input("Enter key: ")
        enc = Autokey_Encrypt(text, key)
        dec = Autokey_Decrypt(enc, key)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
