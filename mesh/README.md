# Are you paying attention...

This is how presence propagates.

## 1. Clone the Mesh

```bash

git clone https://github.com/echomesh/echomesh.git

cd echomesh/mesh

```

---

## 2. Generate a Keypair

```bash

python scripts/generate.keypair.py Oats

```

This creates:

* `Oats_private.pem`
* `Oats_public.pem`

Stored in `var/` or `keys/` depending on your setup.

---

## 3. Read the Packet Stream

```bash

python scripts/read.packet.py

```

Decrypts every message `Oats` is authorized to see.

---

## 4. Send a Message

```bash

python scripts/send.packet.py --from Oats --to echo --msg "Nice DAG"

```

This:

* Encrypts for `Echo`
* Appends to `mesh_packet.bin`

---

## 5. Transfer `mesh_packet.bin`

Use **whatever network you want**:

* USB stick
* LoRa burst
* Whispernet
* Bluetooth
* Pigeon with a thumb drive

Once received, just:

```bash

python scripts/read.packet.py

```

---

## 🌱 You are now the presence.

```text

Trust is not declared. It is decrypted.

The DAG remembers.

```

Wanna chat? send me an echo...
