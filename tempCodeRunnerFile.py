plaintext = "INFORMATIONSECURITY"
key="31452"

print("Plaintext:", plaintext)

ciphertext = row_transposition_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)