import os
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Load all private keys from 'keys' directory
key_dir = Path("keys/private")
private_keys = []

for filename in os.listdir(key_dir):
    if filename.endswith("_private.pem"):
        with open(key_dir / filename, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
            private_keys.append((filename, private_key))

# Open and parse the binary packet stream
with open("mesh_packet.bin", "rb") as f:
    packet_count = 0
    while True:
        # Read 4-byte length header
        length_bytes = f.read(4)
        if not length_bytes:
            break  # End of file

        length = int.from_bytes(length_bytes, byteorder="big")
        ciphertext = f.read(length)

        packet_count += 1
        print(f"\n🔍 Reading packet #{packet_count} (length: {length} bytes)")

        for key_name, private_key in private_keys:
            try:
                decrypted = private_key.decrypt(
                    ciphertext,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                print(f"✅ Decrypted with: {key_name}")
                print("📦 Message:")
                print(decrypted.decode())
                break  # No need to try other keys
            except Exception:
                print(f"❌ Failed with: {key_name}")
