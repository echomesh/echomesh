# EchoMesh Presence Propagation — Quickstart Guide

**Specification**: Presence-Propagation-v0.1
**Date**: 2025-06-06

---

## 1. Clone the Mesh Repository

```bash
git clone https://github.com/echomesh/echomesh.git
cd echomesh/mesh
```

This retrieves the latest EchoMesh runtime components and supporting scripts.

---

## 2. Generate a Keypair

```bash
python scripts/generate.keypair.py Oats
```

This command generates a new node identity keypair:

* `Oats_private.pem`
* `Oats_public.pem`

Keys are stored under `var/` or `keys/`, depending on configuration.

---

## 3. Read the Packet Stream

```bash
python scripts/read.packet.py
```

Decrypts and displays all messages authorized for the specified node.
Decryption is validated against the node’s private key.

---

## 4. Send a Message

```bash
python scripts/send.packet.py --from Oats --to echo --msg "Nice DAG"
```

This command:

* Encrypts the message for the destination node (`Echo`).
* Appends the packet to `mesh_packet.bin`.

---

## 5. Transfer the Packet File

The `mesh_packet.bin` file is the portable carrier for mesh communications. It may be transmitted across **any transport medium**, including:

* USB or removable storage
* Low-power radio (LoRa)
* Local mesh relays (Bluetooth, Wi-Fi Direct)
* Air-gapped transfers

On the receiving node, simply execute:

```bash
python scripts/read.packet.py
```

to decrypt and process incoming messages.

---

## 6. Presence Validation

Within EchoMesh, **presence is not declared — it is verified**.
Decrypted packets serve as proof of:

* Node identity.
* Trust lineage within the DAG.
* Cryptographic authorization to participate in the mesh.

**Principle:**

> Trust is not assumed. Trust is decrypted.
> The DAG provides memory, integrity, and verification.

---

## Summary

This quickstart demonstrates the minimal workflow required to:

1. Join the mesh (keypair generation).
2. Authenticate presence (packet reading).
3. Propagate messages (packet sending + transfer).

EchoMesh presence propagation enables **secure, verifiable communication** across distributed environments — from low-bandwidth field operations to enterprise-scale mesh networks.

