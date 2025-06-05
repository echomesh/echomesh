## `DA-CERT v0.1` — **Directed Assertion Certificate**

A local, signed trust structure for decentralized identity, embedded at the hardware layer.

---

### 1. **Header**

```json
{
  "cert_id": "da-cert:graphkey:0001",
  "issued_at": "2025-06-06T09:21:00Z",
  "issuer_node": "echo:node/0000A1",
  "version": "0.1"
}
```

---

### 2. **Nodes**

Each node represents a key-bound identity or role.

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

### 3. **Edges**

Each edge is a signed trust derivation between nodes.

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

### 4. **Context (Optional)**

System or situational metadata bound to the cert.

```json
"context": {
  "firmware_hash": "sha256:abc123...",
  "location_hint": "AU-BRISBANE",
  "echo_version": "1.0.0"
}
```

---

### 5. **Root Signature**

Top-level DAG signature.

```json
"root_signature": {
  "signed_by": "0000A1",
  "hash": "sha256:final_merkle_root",
  "signature": "<root_signature_bytes>"
}
```

---

## ✅ Validation Rules

* All node keys must be valid public keys.
* All edge signatures must be verifiable against `from` node key.
* `root_signature.hash` must match hash of serialized graph content.
* Graph traversal must resolve without cycles.

---

## 📁 Recommended Filename

```bash
da-cert-0001.json
```

---

## 📡 Deployment

Embed DA Cert hash or full cert in:

* `echoL1` presence packets
* Asset broadcast signatures
* Trust assertion payloads

