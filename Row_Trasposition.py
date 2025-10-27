def row_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    
    key= [int(k) for k in key]

    col= len(key)
    rows = []
    for i in range(0, len(plaintext), col):
        part = plaintext[i:i+col]
        if len(part) < col:
            part += "X" * (col - len(part))
        rows.append(part) 

    ciphertext = ""
    for num in sorted(key):
        col= key.index(num)
        for row in rows:
            ciphertext += row[col]
    return ciphertext

plaintext = "INFORMATIONSECURITY"
key="31452"

print("Plaintext:", plaintext)

ciphertext = row_transposition_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

