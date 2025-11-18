from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"Hello i am Faizan"

signature = private_key.sign(
    message,
    hashes.SHA256(),
)

print("Original Message:", message)
print("Signature:", signature.hex())

try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256(),
    )
    print("Signature is Verified")
except Exception as e:
    print("Signature is Invalid:", e)