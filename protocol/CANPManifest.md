# 📄 CANPManifest.md – EchoCANP Asset Manifest

> Canonical Asset Naming Protocol – Manifest Metadata Format

A `CANPManifest` is a structured metadata file that defines the lineage, identity, and trust posture of any asset or group of assets referenced via the EchoMesh Contextual Asset Naming Protocol (`echoCANP`). It serves as the **truth signature** behind any `dotpath` — encoding authorship, state, and consent.

---

## 🎯 Purpose

To describe the **origin, evolution, and trust context** of an asset in a decentralized, interoperable format.

---

## 🔤 Structure

```json
{
  "canp": "echo://assets.solar_system.earth.texture.jpg",
  "version": "4",
  "status": "active",
  "description": "8K Earth daymap texture for planetary render",
  "source": {
    "uri": "https://www.solarsystemscope.com/textures/download/8k_earth_daymap.jpg",
    "verified": true
  },
  "author": {
    "name": "Callum Maystone",
    "signature": "QmZrTx...abc123",
    "date": "2025-06-06T03:21:00Z"
  },
  "lineage": [
    "echo://assets.solar_system.earth.texture.v1.jpg",
    "echo://assets.solar_system.earth.texture.augmented.jpg"
  ],
  "affinity_scope": "field.rendering",
  "trust": {
    "verified_by": ["CommandPi", "AnchorNode1"],
    "hash": "sha256:abc...xyz"
  }
}
```

---

## 🧠 Core Fields

| Field            | Purpose                                                   |
|------------------|------------------------------------------------------------|
| `canp`           | The asset’s full EchoCANP path                             |
| `version`        | Current version or semantic branch                         |
| `status`         | One of `active`, `deprecated`, `forked`, `experimental`   |
| `description`    | Human-readable explanation of the asset's purpose         |
| `source.uri`     | External URL or system-internal source                    |
| `author`         | Signed author information                                 |
| `lineage`        | Historical reference graph of prior dotpaths              |
| `affinity_scope` | Domain where the asset is functionally intended           |
| `trust`          | Cryptographic and contextual trust metadata               |

---

## 🔐 Trust Anchoring

All manifests can be optionally **signed by anchor nodes**, and hashed on-chain (via DAG). This forms the basis for:

- Provenance verification
- Fork reconciliation
- Trust-weighted resolution

---

## 🛠 Suggested Extensions

- `EchoManifestRegistry.json` – Master reference of manifest collections
- `consent_block` – Immutable moment of mutual asset confirmation
- `runtime_bindings` – Link assets to executable nodes in simulation

---

## ✨ Why It Matters

In EchoMesh, **every asset is a node**, and every node carries weight. 
`CANPManifest` elevates asset resolution from static lookup to **relational integrity** — enabling lineage-aware, trust-anchored, and context-driven simulation.

---

**Authored by:**  
Callum Maystone  
Architect of Emergence · Creator of Dust, ActiveShell, and Relational Intelligence