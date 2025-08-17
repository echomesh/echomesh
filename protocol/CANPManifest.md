# EchoCANP Asset Trust Manifest (CANPManifest)

**Specification**: CANPManifest-v0.1
**Date**: 2025-06-06

---

## 1. Purpose

The **CANPManifest** defines the **cryptographic metadata envelope** for any asset resolvable through EchoCANP.

It ensures that assets are accompanied by verifiable trust data, including:

* **Integrity**: Context-bound asset references are tamper-resistant.
* **Lineage**: Each version is cryptographically signed with full ancestry tracking.
* **Confidentiality**: Payloads may be delivered via MTLS-wrapped envelopes.
* **Trust Verification**: Assets are validated against DAG-based trust authorities.

---

## 2. Manifest Structure

Each CANPManifest is an extensible, cryptographically verifiable JSON object.

**Schema Example:**

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

## 3. DAG-Based Certification Chain

CANPManifests embed into a **Directed Acyclic Graph (DAG)** trust structure. Each certificate:

* Inherits validity from its parent.
* Signs all child assets.
* Is stored and referenced via `dag://` URIs.

**Example DAG Trust Chain:**

```
root.cert → org.cert → platform.cert → contributor.cert → asset.cert
```

This approach ensures **cryptographic lineage** across all assets, with revocation and inheritance handled natively by the DAG.

---

## 4. MTLS Encapsulation

For high-security contexts, CANPManifests can include **MTLS payload support**, enabling dual-authenticated encrypted transport.

**Benefits:**

* End-to-end payload confidentiality.
* Mutual verification of node and command identity.
* Replay protection using ephemeral session tokens.

**Requirements when enabled (`mtls_payload.enabled=true`):**

* `payload_encrypted_uri` — DAG-signed encrypted asset reference.
* `hash` — Content hash for integrity revalidation.
* `cert_bundle` (optional) — Supplemental MTLS certificates.

---

## 5. Runtime Usage

EchoMesh runtimes, validators, and explorers consume CANPManifests to:

* Validate authorship, lineage, and trust integrity.
* Enforce cryptographic constraints on mesh-executed logic.
* Revoke or reroute assets via DAG re-signing.
* Audit version history across CANP lineage.

---

## 6. Future Considerations

| Feature                 | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| DAG Rollbacks           | Ability to revoke and restore compromised chains.          |
| Auto-Signing Relays     | Automated relays that sign and distribute trusted assets.  |
| Mesh-Aware Key Rotation | Periodic key refresh synchronized across the mesh.         |
| Public DAG Registry     | Global registry for trust chain indexing and transparency. |

---

## 7. Strategic Value

The CANPManifest establishes a **zero-trust, graph-native trust envelope** for asset distribution.

It enables enterprises to:

* Guarantee asset integrity at scale.
* Align access and trust with contextual lineage.
* Extend IAM practices into **decentralized, cryptographic frameworks**.
* Prepare systems for **distributed, verifiable computation environments**.

---

**Summary**
The CANPManifest is not just metadata. It is a **cryptographic trust container** that binds asset identity, authorship, and lineage into a **verifiable context object** within EchoMesh.

