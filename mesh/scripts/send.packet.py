import json
import uuid
import argparse
from datetime import datetime
from pathlib import Path
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Setup CLI
# Setup CLI
parser = argparse.ArgumentParser(description="Send encrypted mesh packet.")
parser.add_argument("--to", required=True, help="Recipient node name (used as key name prefix)")
parser.add_argument("--from", dest="from_node", required=True, help="Sender node name (informational only)")
parser.add_argument("--msg", required=True, help="Message content")
parser.add_argument("--bin", default="mesh_packet.bin", help="Output file (default: mesh_packet.bin)")
args = parser.parse_args()

# Resolve key path
pub_key_path = Path(f"/keys/public/{args.to}_public.pem")
if not pub_key_path.exists():
    print(f"🚫 Public key for {args.to} not found at {pub_key_path}")
    exit(1)

# Load recipient's public key
with open(pub_key_path, "rb") as key_file:
    recipient_key = serialization.load_pem_public_key(key_file.read())

# Construct packet
message = {
    "packet_id": str(uuid.uuid4()),
    "to": args.to,
    "from": args.from_node,
    "timestamp": datetime.utcnow().isoformat(),
    "data": args.msg
}

plaintext = json.dumps(message).encode()

# Encrypt packet
ciphertext = recipient_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Append to .bin with length header
with open(args.bin, "ab") as f:
    f.write(len(ciphertext).to_bytes(4, byteorder="big"))
    f.write(ciphertext)

print(f"✅ Encrypted message sent to {args.to} and appended to {args.bin}")
