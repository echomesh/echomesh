# DA-CERT v0.1 — Directed Assertion Certificate

**Specification**: DA-CERT-v0.1
**Date**: 2025-06-06

---

## 1. Overview

The **Directed Assertion Certificate (DA-CERT)** defines a **local, cryptographically signed trust structure** for decentralized identity.

* Embedded at the hardware layer.
* Represented as a signed graph (nodes and edges).
* Enables verifiable delegation, presence, and routing across EchoMesh environments.

---

## 2. Certificate Structure

### 2.1 Header

```json
{
  "cert_id": "da-cert:graphkey:0001",
  "issued_at": "2025-06-06T09:21:00Z",
  "issuer_node": "echo:node/0000A1",
  "version": "0.1"
}
```

Defines certificate identifier, issuance time, issuer, and schema version.

---

### 2.2 Nodes

Each node represents a **key-bound identity or role** within the certificate.

```json
"nodes": {
  "0000A1": {
    "label": "Callum Node",
    "context": ["signer", "sovereign"],
    "key": "<base64_public_key>"
  },
  "0000A2": {
    "label": "Relay Unit",
    "context": ["device", "presence"],
    "key": "<base64_public_key>"
  }
}
```

---

### 2.3 Edges

Each edge represents a **signed trust derivation** between nodes.

```json
"edges": [
  {
    "from": "0000A1",
    "to": "0000A2",
    "type": "delegates",
    "scope": ["presence", "routing"],
    "timestamp": "2025-06-06T09:22:30Z",
    "signature": "<signature_of_payload_by_0000A1>"
  }
]
```

---

### 2.4 Context (Optional)

Optional system or situational metadata bound to the certificate.

```json
"context": {
  "firmware_hash": "sha256:abc123...",
  "location_hint": "AU-BRISBANE",
  "echo_version": "1.0.0"
}
```

---

### 2.5 Root Signature

The **top-level DAG signature** validates the entire certificate structure.

```json
"root_signature": {
  "signed_by": "0000A1",
  "hash": "sha256:final_merkle_root",
  "signature": "<root_signature_bytes>"
}
```

---

## 3. Validation Rules

* All node keys must be valid public keys.
* All edge signatures must be verifiable against the corresponding `from` node key.
* `root_signature.hash` must match the hash of the serialized graph content.
* Graph traversal must resolve without cycles.

---

## 4. Recommended Filename

Certificates should be stored in the format:

```
da-cert-<id>.json
```

Example:

```
da-cert-0001.json
```

---

## 5. Deployment

DA-CERTs may be embedded as trust anchors within:

* `echoL1` presence packets.
* Asset broadcast signatures.
* Trust assertion payloads.

---

## 6. Strategic Value

DA-CERT establishes a **lightweight, verifiable identity structure** suitable for distributed mesh environments, offering:

* Decentralized trust inheritance.
* Hardware-level identity embedding.
* Extensible DAG-based validation for edge networks.

