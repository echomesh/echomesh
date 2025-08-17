# EchoMesh GraphKey — Technical Definition

**Specification**: GraphKeySpec-v0.1
**Date**: 2025-06-06

---

## 1. Purpose

The **GraphKey** defines a portable, cryptographically signed, and context-aware identity structure for EchoMesh nodes.

Unlike traditional X.509 certificates, GraphKey introduces a **graph-encoded identity map**, locally stored and verified through:

* **Cryptographic signatures** (ECDSA / Ed25519).
* **mTLS overlay validation**.
* **Contextual lineage tracking** within a trust DAG.

This approach enables **decentralized, relational trust** across distributed systems.

---

## 2. File Format

* **File Name**: `graph.key`
* **Encoding**: UTF-8 JSON
* **Location**: Local to each deployed node
* **Signature**: ECDSA / Ed25519, SHA-512 fingerprint
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

| Field         | Type   | Description                                                           |
| ------------- | ------ | --------------------------------------------------------------------- |
| `graph_id`    | String | Global identifier of the identity graph (CANP format).                |
| `version`     | String | Schema version of the GraphKey specification.                         |
| `node`        | Object | Core identity attributes (ID, type, domain, capabilities, boot hash). |
| `edges[]`     | Array  | Trust relationships and contextual links to other nodes.              |
| `signature`   | Object | GraphKey signed by an upstream authority or peer node.                |
| `fingerprint` | String | Full graph hash signature for rapid verification.                     |

---

## 5. Comparison: GraphKey vs Traditional Certificates

| Feature            | X.509 Certificates | EchoMesh GraphKey                     |
| ------------------ | ------------------ | ------------------------------------- |
| Identity Structure | Flat, name-based   | Graph-based, contextual               |
| Trust Model        | Hierarchical CA    | Decentralized DAG                     |
| Validity           | Expiry date        | Graph lineage and hash integrity      |
| Validation         | Static public key  | Contextual trust propagation          |
| Storage            | PEM/DER file       | Local JSON (`graph.key`) or binary    |
| Revocation         | CRL / OCSP         | DAG edge pruning or lineage severance |

---

## 6. Integration Points

| Layer              | Function                                           |
| ------------------ | -------------------------------------------------- |
| **echoPresence**   | Signs and verifies initial node presence.          |
| **ActiveTrust**    | Validates graph lineage during runtime operations. |
| **mTLS Handshake** | Secures transport layer with encrypted identity.   |
| **CANPManifest**   | Links GraphKey to specific assets and contexts.    |
| **EchoRuntime**    | Uses fingerprint as the canonical presence hash.   |

---

## 7. Cryptographic Considerations

* **Signature Algorithms**:

  * ECDSA P-256
  * Ed25519
  * Optional Curve25519-X3DH (for key exchange).

* **Hash Algorithms**:

  * SHA-512 (default, full-graph digest).
  * SHA-256 (fallback for constrained devices).

* **Trust Inheritance**:

  * Edges can embed consent or subgraphs (certificate-style).

* **Revocation**:

  * Handled by pruning edges or removing lineage within the root trustgraph.

---

## 8. Verification Workflow

1. Node boots and loads local `graph.key`.
2. Extracts `.fingerprint` and `.edges`.
3. Validates local graph signature.
4. Validates edges against trust DAG (`trustgraph.json`).
5. Wraps transport in mTLS using `graph.key` as contextual identity.

---

## 9. Example: Presence Authentication

```text
Node requests to broadcast presence.  
→ Sends signed `graph.key` reference.  
→ Receiver checks edge: `trusts → CommandPi`.  
→ Valid edge + valid signature = authenticated presence.  
→ EchoMesh admits node into the cluster.  
```

---

## 10. Future Extensions

| Feature              | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `graph.keysig`       | Encrypted + signed binary wrapper.                       |
| `graph.key.enc`      | Fully encrypted payload for deployment in hostile zones. |
| `graph.key.inline`   | Inline signature embedded within CANP packets.           |
| `graph.keychain`     | Expanded edge lineage archive for trust inheritance.     |
| `graph.key.manifest` | Declares assets authorized by node identity.             |

---

## 11. Strategic Value

GraphKey provides enterprises with a **flexible, decentralized identity framework** that enhances:

* **Security**: Strong cryptographic primitives, tamper-resistant lineage.
* **Interoperability**: Seamless integration with EchoMesh, ActiveTrust, and CANP.
* **Governance**: Fine-grained trust control via DAG edge pruning.
* **Resilience**: Distributed verification eliminates reliance on central CAs.

