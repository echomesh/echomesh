# Appendix: EchoStack Runtime Protocol

## Executive Summary

The **EchoStack Runtime Protocol** is the execution layer for relational intelligence systems. It integrates **contextual memory, dynamic execution, decentralized propagation, and contextual asset resolution** into a single, trust-anchored framework.

Where traditional runtime environments focus on data processing, EchoStack focuses on **context enactment**, providing enterprises with a secure, scalable, and verifiable foundation for distributed intelligence.

---

## Core Components

EchoStack unifies four key layers into a cohesive runtime stack:

| Layer                 | Component         | Purpose                                                               |
| --------------------- | ----------------- | --------------------------------------------------------------------- |
| **Substrate**         | Dust              | Immutable, trust-anchored memory layer for relational structures.     |
| **Runtime Interface** | ActiveShell (ASh) | Execution layer for graph construction, querying, and transformation. |
| **Mesh Network**      | EchoMesh          | Decentralized, presence-aware propagation and trust signaling.        |
| **Resolution Engine** | echoCANP          | Contextual asset naming and semantic resolution via dotpath syntax.   |

Together, these components form a **distributed relational intelligence engine**.

---

## Dust – Contextual Memory Layer

**Dust** serves as the trusted memory substrate. It provides:

* Graph-encoded relationships and historical deltas.
* Hierarchical JSON + DAG anchoring for versioning and timestamping.
* Graph-anchored references (no traditional file paths).

**Example Entry:**

```json
{
  "id": "solar_system.earth.texture.jpg",
  "version": "refined",
  "stored_at": "assets/solar_system/earth/texture.jpg",
  "trust_anchor": "BananoBlock#44310"
}
```

---

## ActiveShell (ASh) – Execution Interface

**ActiveShell** extends native PowerShell capabilities for relational graph management.

**Core Commands**

* `Create-ActiveGraph`
* `Add-Node`, `Set-Node`, `Get-Node`, `Delete-Node`
* `Create-Edge`, `Set-Edge`, `Get-Edge`, `Delete-Edge`
* `Export-Graph`, `Import-Graph`

**Asset Operations**

* `Get-Asset`
* `Set-Asset`
* `Get-AssetHistory`
* `Get-AssetGroup`

**Example Usage:**

```powershell
Add-Node -NodeName "PharmacyC" -Type "Pharmacy" -Domain "Healthcare"
Create-Edge -Source "PatientA" -Target "PharmacyC" -Relationship "GetsMedsFrom"
Get-Asset solar_system.earth.texture
```

---

## EchoMesh – Propagation Protocol

**EchoMesh** manages decentralized trust and presence propagation.

Features include:

* Node-declared **Intent** and **Presence** verification.
* Signed and logged signal transmissions with traceability.
* Governance tiers (e.g., `field_civilian`, `op_civic`, `tactical_node`).

**Canonical Identity Pairs:**

* Intent / Presence
* Input / Output
* Anchor / Propagate
* Proof / Consent
* Signal / Trace

---

## echoCANP – Contextual Asset Naming Protocol

**echoCANP** resolves assets and identities based on graph context.

**Syntax:**

```
[protocol]://[domain].[context].[subcontext].[identifier].[extension]
```

**Example:**

```
dag://assets.solar_system.earth.texture.jpg
```

**Resolution Logic (simplified):**

```javascript
function resolveEchoCANP(dotPath) {
  const parts = dotPath.split('.');
  const ext = parts.pop();
  const id = parts.pop();
  const path = parts.join('/');
  return `${path}/${id}.${ext}`;
}
```

Each **dot** represents a graph edge.
Each **terminal node** resolves to an asset.

---

## Full Runtime Example

```powershell
Create-ActiveGraph -GraphName "SimNet"
Set-Asset nodes.esp32.lora.presence.init.json `
  -uri "https://github.com/echomesh/assets/init_packet.json"
Invoke-EchoPresence -NodeID "esp32-Node-7" -Scope "medops.mesh"
Anchor-State -From "CommandPi" -StateID "op_civic.v1"
```

---

## Summary

EchoStack provides enterprises with a **runtime model for relational intelligence**. It:

* Stores trusted context (**Dust**)
* Executes structural operations (**ASh**)
* Propagates intent and presence (**EchoMesh**)
* Resolves meaning and identity (**echoCANP**)

By anchoring runtime execution in trust, presence, and context, EchoStack enables a **next-generation approach to distributed intelligence systems**.
