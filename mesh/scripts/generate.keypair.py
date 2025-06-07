import os
import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Get name from command-line argument, or use default
key_name = sys.argv[1] if len(sys.argv) > 1 else "<INSERT NAME HERE>"
# key_name = "meshlogon"  # ❌ this overrides the above line

# Ensure the directory exists
os.makedirs("keys", exist_ok=True)

# Generate keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Write private key
with open(f"keys/public/{key_name}_private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Write public key
with open(f"keys/private/{key_name}_public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print(f"🔑 Generated keys: keys/private/{key_name}_private.pem and keys/private/{key_name}_public.pem")
