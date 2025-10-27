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


plaintext = "INFORMATIONSECURITY"
key = "31452"

print("Plaintext:", plaintext)

ciphertext = "NASIROUXIMNRFTETOICY"
print("Ciphertext:", ciphertext)

decrypted_plaintext = row_transposition_decrypt(ciphertext, key)
print("Decrypted Plaintext:", decrypted_plaintext)
