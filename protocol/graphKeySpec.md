# `graphKeyTD.md`

**EchoMesh GraphKey — Technical Definition**
Version: `GraphKeySpec-v0.1`
Date: `2025-06-06`

---

## 🎯 Purpose

The **GraphKey** defines a portable, signed, context-aware identity structure for any EchoMesh node. It replaces traditional certificates with a **graph-encoded identity map** — locally stored, cryptographically signed, and verified by mTLS overlay with contextual lineage.

---

## 📦 File Type

* **File Name**: `graph.key`
* **Encoding**: UTF-8 JSON
* **Location**: Local to field-deployed node
* **Signature**: ECDSA / Ed25519 / SHA512 fingerprint
* **Encrypted Variant**: `graph.keysig` (binary wrapper)

---

## 🧬 Core Schema

```json
{
  "graph_id": "echo://nodes.esp32.unit004",
  "version": "GraphKeySpec-v0.1",
  "node": {
    "id": "unit004",
    "type": "device",
    "model": "ESP32-WROOM",
    "domain": "field.presence",
    "capability": ["presence", "relay"],
    "boot_hash": "sha256:..."
  },
  "edges": [
    {
      "relation": "trusts",
      "target": "CommandPi",
      "scope": "mesh.auth",
      "hash": "sha256:trustsig...",
      "timestamp": "2025-06-06T10:00:00Z"
    }
  ],
  "signature": {
    "signed_by": "CommandPi",
    "sig": "ecdsa256:ABCDEF...",
    "alg": "SHA512withECDSA"
  },
  "fingerprint": "sha512:fullgraphsig..."
}
```

---

## 📐 Field Definitions

| Field         | Type     | Description                                                           |
| ------------- | -------- | --------------------------------------------------------------------- |
| `graph_id`    | `string` | Global identifier (CANP format) of this identity graph                |
| `version`     | `string` | GraphKey schema version                                               |
| `node`        | `object` | Core identity of this node (type, domain, capabilities, boot hash)    |
| `edges[]`     | `array`  | Trust relationships and context-based links to other known identities |
| `signature`   | `object` | Graph-signed by an upstream authority or signer node                  |
| `fingerprint` | `string` | Full graph hash signature for rapid verification                      |

---

## 🔐 GraphKey vs Traditional Certificates

| Feature            | Traditional Certs (X.509) | EchoMesh GraphKey                     |
| ------------------ | ------------------------- | ------------------------------------- |
| Identity Structure | Flat, name-based          | Graph-based, contextual               |
| Trust Model        | Hierarchical CA           | Decentralized DAG                     |
| Validity           | Expiry Date               | Graph lineage & hash trail            |
| Validation         | Static Public Key         | Contextual trust propagation          |
| Storage            | PEM / DER file            | Local `graph.key` JSON or binary      |
| Revocation         | CRL / OCSP                | DAG edge pruning or lineage severance |

---

## 🔁 Integration Points

| Layer            | Function                                    |
| ---------------- | ------------------------------------------- |
| `echoPresence`   | Signs & verifies initial field presence     |
| `ActiveTrust`    | Validates graph lineage in runtime          |
| `mTLS Handshake` | Wraps transport with encrypted identity     |
| `CANPManifest`   | Links `graph.key` to specific assets        |
| `EchoRuntime`    | Uses fingerprint as canonical presence hash |

---

## 🔒 Cryptographic Notes

* **Signature Algorithm**:
  Supports `ECDSA P-256`, `Ed25519`, and optional `Curve25519-X3DH` for key exchange.

* **Hash Algorithm**:
  Uses `SHA-512` for full-graph digest. Lightweight nodes can fall back to `SHA-256`.

* **Trust Inheritance**:
  Edges can carry embedded consent or embedded certificate-style subgraphs.

* **Revocation**:
  Achieved by invalidating edge scopes or removing graph lineage in the root `trustgraph`.

---

## 🛠 Verification Workflow

1. Node boots → loads local `graph.key`
2. Extracts `.fingerprint` and `.edges`
3. Validates local graph signature
4. Validates edges against trust DAG (`trustgraph.json`)
5. Uses mTLS for transport; `graph.key` for contextual ID

---

## 🌐 Example Use Case: Presence Authentication

```text
Node → wants to broadcast presence  
→ Sends signed `graph.key` reference  
→ Receiver checks edge: `trusts → CommandPi`  
→ Valid edge + valid sig = authenticated presence  
→ EchoMesh admits node into field cluster
```

---

## 🧱 Future Extensions

| Feature              | Description                                 |
| -------------------- | ------------------------------------------- |
| `graph.keysig`       | Encrypted + signed binary wrapper           |
| `graph.key.enc`      | Fully encrypted payload for hostile domains |
| `graph.key.inline`   | Signed directly inside CANP packet          |
| `graph.keychain`     | Edge-expanded full trust lineage archive    |
| `graph.key.manifest` | Defines assets authorized by identity       |

---
