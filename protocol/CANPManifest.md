# 📄 CANPManifest.md — EchoCANP Asset Trust Manifest

> **Encapsulating Trust. Declaring Intent. Defining Lineage.**

The `CANPManifest` defines the **cryptographic metadata envelope** for any EchoCANP-resolvable asset.
It encapsulates **versioning, certification, origin metadata**, and optional **MTLS-wrapped payloads** using a DAG-based certificate chaining mechanism.

---

## 🔐 Purpose

CANPManifests act as **trust-bound signatures** for assets and instructions resolved via EchoCANP, ensuring:

- Integrity of context-bound asset references
- Cryptographically signed authorship and version lineage
- Secure delivery via encapsulated Mutual TLS (MTLS) envelopes
- Verification against DAG-signed trust authorities

---

## 🧬 Manifest Structure

Each manifest is an extensible, cryptographically verifiable object:

```json
{
  "canp": "echo://assets.solar_system.earth.texture.jpg",
  "resolved_path": "assets/solar_system/earth/texture.jpg",
  "version": "3.1.forked",
  "author": {
    "id": "callum.maystone",
    "signature": "0xBCF1...0A3D",
    "certificate_dag": "dag://trust.youmatter.origin.cert.0xA59"
  },
  "issued": "2025-06-06T02:00:00Z",
  "expiry": "2026-06-06T02:00:00Z",
  "mtls_payload": {
    "enabled": true,
    "hash": "sha256:1AFC...0931",
    "payload_encrypted_uri": "dag://mtls.envelope.asset.earth-texture"
  },
  "affinity_scope": "field.rendering",
  "trust_flags": ["verified", "dag-certified", "encrypted"]
}
```

---

## 🔗 DAG-Based Certification Chain

EchoMesh uses a **Directed Acyclic Graph (DAG)** model to track and verify asset trust lineage. Each certificate in the chain is itself a node in the DAG, forming a cryptographically signed ancestry map.

### Example DAG Trust Chain

```
root.cert -> org.cert -> platform.cert -> contributor.cert -> asset.cert
```

Each cert:
- Inherits from its parent
- Signs all child references
- Is stored and referenced via `dag://` URIs

---

## 🔐 MTLS Encapsulation

MTLS payloads are optionally supported by enabling **dual-authenticated transport encryption**. This provides:

- **Payload confidentiality**
- **Mutual verification** of node and command identity
- **Secure replay protection** using ephemeral session tokens

When `mtls_payload.enabled = true`, the CANPManifest must include:

- `payload_encrypted_uri` — a DAG-signed encrypted resource
- `hash` — content hash for local revalidation
- `cert_bundle` (optional) — MTLS certificate bundle for out-of-band validation

---

## 🧠 Usage

EchoMesh runtimes, validators, and explorers consume CANPManifests to:

- Validate asset lineage and authorship
- Enforce trust constraints on mesh-executed logic
- Dynamically reroute or revoke assets via DAG re-signing
- Audit and trace versions across CANP lineage

---

## 🧩 Future Considerations

| Feature | Description |
|--------|-------------|
| DAG Rollbacks | Ability to revoke and rollback compromised asset chains |
| Auto-Signing Relay | Relays that automatically sign trusted asset emissions |
| Mesh-Aware Key Rotation | Periodic cryptographic material updates across mesh |
| Public DAG Registry | Global trust chain indexing & transparency portal |

---

## ✨ Summary

The `CANPManifest` provides an extensible trust container for every EchoCANP asset — securing identity, enforcing lineage, and preparing EchoMesh to support zero-trust, distributed computation environments.

> A manifest is not just metadata. It is **context, compressed into cryptographic form.**