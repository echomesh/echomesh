# EchoMesh GraphKey — Technical Definition

**Specification**: GraphKeySpec-v0.1
**Date**: 2025-06-06

---

## 1. Purpose

The **GraphKey** defines a portable, cryptographically signed, context-aware identity structure for EchoMesh nodes.

It replaces traditional X.509 certificates with a **graph-encoded identity map** that is:

* Locally stored.
* Cryptographically verifiable.
* Validated via mTLS overlay with contextual lineage.

This provides a decentralized, DAG-based trust model suitable for distributed systems.

---

## 2. File Format

* **File Name**: `graph.key`
* **Encoding**: UTF-8 JSON
* **Location**: Local to field-deployed nodes
* **Signature**: ECDSA / Ed25519 / SHA-512 fingerprint
* **Encrypted Variant**: `graph.keysig` (binary wrapper)

---

## 3. Core Schema

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

## 4. Field Definitions

| Field         | Type   | Description                                                       |
| ------------- | ------ | ----------------------------------------------------------------- |
| `graph_id`    | String | Global identifier (CANP format) for this identity graph.          |
| `version`     | String | GraphKey schema version.                                          |
| `node`        | Object | Core identity attributes (type, domain, capabilities, boot hash). |
| `edges[]`     | Array  | Trust relationships and context-based links to other identities.  |
| `signature`   | Object | GraphKey signature from upstream authority or peer node.          |
| `fingerprint` | String | Full graph hash signature for rapid verification.                 |

---

## 5. Comparison: GraphKey vs Traditional Certificates

| Feature            | X.509 Certificates | EchoMesh GraphKey              |
| ------------------ | ------------------ | ------------------------------ |
| Identity Structure | Flat, name-based   | Graph-based, contextual        |
| Trust Model        | Hierarchical CA    | Decentralized DAG              |
| Validity           | Expiry date        | Graph lineage & hash integrity |
| Validation         | Static public key  | Contextual trust propagation   |
| Storage            | PEM / DER file     | JSON (`graph.key`) or binary   |
| Revocation         | CRL / OCSP         | DAG edge pruning / lineage cut |

---

## 6. Integration Points

| Layer            | Function                                     |
| ---------------- | -------------------------------------------- |
| `echoPresence`   | Signs and verifies initial node presence.    |
| `ActiveTrust`    | Validates lineage during runtime.            |
| `mTLS Handshake` | Wraps transport in encrypted identity.       |
| `CANPManifest`   | Links `graph.key` to assets and context.     |
| `EchoRuntime`    | Uses fingerprint as canonical presence hash. |

---

## 7. Cryptographic Notes

* **Signature Algorithms**: ECDSA P-256, Ed25519, optional Curve25519-X3DH.
* **Hashing**: SHA-512 (default full-graph digest). SHA-256 supported for constrained nodes.
* **Trust Inheritance**: Edges may embed consent or subgraph certificates.
* **Revocation**: Managed by invalidating edge scopes or removing lineage from the trustgraph.

---

## 8. Verification Workflow

1. Node boots and loads local `graph.key`.
2. Extracts `.fingerprint` and `.edges`.
3. Validates local signature.
4. Validates edges against the trust DAG (`trustgraph.json`).
5. Uses mTLS for transport; applies `graph.key` as contextual ID.

---

## 9. Example Use Case — Presence Authentication

```text
Node requests to broadcast presence.  
→ Sends signed `graph.key` reference.  
→ Receiver checks edge: `trusts → CommandPi`.  
→ Valid edge + valid signature = authenticated presence.  
→ EchoMesh admits node into field cluster.  
```

---

## 10. Future Extensions

| Feature              | Description                                  |
| -------------------- | -------------------------------------------- |
| `graph.keysig`       | Encrypted + signed binary wrapper.           |
| `graph.key.enc`      | Fully encrypted payload for hostile domains. |
| `graph.key.inline`   | Signature embedded directly in CANP packets. |
| `graph.keychain`     | Expanded trust lineage archive.              |
| `graph.key.manifest` | Defines asset authorization scope.           |

---

## 11. Strategic Value

GraphKey provides a **decentralized, cryptographic identity model** for distributed systems. It enhances:

* **Security**: Strong signatures, DAG-based lineage validation.
* **Interoperability**: Seamless integration with EchoMesh, CANP, and ActiveTrust.
* **Governance**: Fine-grained revocation via DAG pruning.
* **Resilience**: Removes reliance on central certificate authorities.

