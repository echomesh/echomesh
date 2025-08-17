# EchoCANP – EchoMesh Contextual Asset Naming Protocol

## Executive Summary

**EchoCANP (Contextual Asset Naming Protocol)** provides a semantic, graph-driven asset resolution model designed for **context-aware referencing** across distributed systems. Unlike traditional file systems that focus on **location-based access**, EchoCANP resolves assets, functions, and nodes by **context and relational meaning**.

This capability allows enterprises to achieve **more resilient referencing, verifiable lineage tracking, and intent-driven access control** within the EchoMesh trust framework.

---

## Design Philosophy

* **Location vs. Context**: Traditional paths reference location (e.g., file systems, URLs). EchoCANP references **contextual meaning**.
* **Relational Model**: Every reference is a **node**; every dot (`.`) is an **edge**.
* **Dynamic Resolution**: Instead of resolving to servers or static files, EchoCANP resolves to **semantic structures**.

This enables enterprises to transition from **storage-centric data management** to **context-driven asset intelligence**.

---

## Syntax Model

**General Format**

```
[protocol]://[domain].[context].[subcontext].[identifier].[extension]
```

**Component Breakdown**

* **protocol** → Routing/behavior (e.g., `echo`, `dag`).
* **domain** → Root context (e.g., `assets`, `nodes`).
* **context** → Category of intent or function.
* **subcontext** → Specific use case or scenario.
* **identifier** → Asset or command node.
* **extension** → File type or resolution signature.

**Examples**

| Reference                                     | Meaning                           |
| --------------------------------------------- | --------------------------------- |
| `dag://assets.solar_system.earth.texture.jpg` | DAG-signed reference to an asset. |
| `echo://nodes.esp32.lora.presence.init.json`  | Presence packet structure.        |

---

## Resolution Logic

EchoCANP resolution interprets each `.` as a **graph edge**, with the final `id.ext` acting as the **terminal node**.

**Simplified Logic**

```javascript
function resolveEchoCANP(dotPath) {
  const parts = dotPath.split('.');
  const ext = parts.pop();
  const id = parts.pop();
  const path = parts.join('/');
  return `${path}/${id}.${ext}`;
}
```

---

## Versioning Approach

EchoCANP departs from static versioning (`v1`, `v2`) in favor of **semantic evolution**:

* **Contextual Shifts** → New branches reflect changes in context (e.g., `.augmented`, `.refined`).
* **Relational Divergence** → Each shift represents a **lineage fork**, preserving history and intent.
* **Immutable Anchors** → Trust anchors ensure integrity and provenance.

This enables enterprises to manage **evolutionary branches** of assets instead of overwriting history.

---

## ActiveShell Integration

EchoCANP is fully operable via **ActiveShell**, the runtime execution interface for EchoMesh.

**Example Commands**

```powershell
# Retrieve asset
Get-Asset solar_system.earth.texture

# View version history
Get-AssetHistory solar_system.earth.texture

# Set explicit version
Set-Asset solar_system.earth.texture -version 4

# Assign asset via external URI
Set-Asset solar_system.earth.texture -uri 'https://www.solarsystemscope.com/textures/download/8k_earth_daymap.jpg'

# Retrieve grouped assets
Get-AssetGroup -identity solar_system -Depth 2
```

*Note: Omitting `-Depth` retrieves the **entire subgraph**.*

---

## Mesh Integration

Within EchoMesh, EchoCANP is used to:

* Reference node blueprints.
* Load and resolve dependencies.
* Execute DAG manifests.
* Trigger protocol handlers.
* Maintain simulation lineage and audit trails.

---

## Registry Example

```json
{
  "registry": {
    "echo://assets.solar_system.earth.texture.jpg": {
      "resolved_path": "assets/solar_system/earth/texture.jpg",
      "affinity_scope": "field.rendering",
      "verified": true,
      "version": "initial",
      "source": "CommandPi"
    }
  }
}
```

---

## Roadmap and Extensions

| Feature                    | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| **`canp://` handler**      | Native protocol registration for browser/plugin use.    |
| **`CANPManifest.json`**    | Asset lineage, provenance, and trust chain metadata.    |
| **EchoCANP Explorer**      | UI for parsing, resolving, and visualizing CANP graphs. |
| **Graph lineage tracking** | Inheritance, forking, and ancestry mapping support.     |

---

## Strategic Value

EchoCANP elevates enterprise data management from **file storage** to **contextual meaning**. It introduces:

* **Resilient Referencing**: Context persists even if infrastructure changes.
* **Compliance-Ready Audit Trails**: Built-in lineage and trust anchors.
* **Dynamic Governance**: Integration with ActiveTrust for consent-driven access.

Where others store files, **EchoMesh stores meaning.**

---

## Alignment with ActiveTrust

EchoCANP operates natively within the **ActiveTrust framework**, ensuring asset resolution is inseparable from **intent verification** and **presence validation**.

**Canonical Identity Pairs** (as defined by ActiveTrust):

* Intent / Presence
* Input / Output
* Request / Response
* Inlet / Outlet
* Signal / Trace
* Anchor / Propagate
* Proof / Consent
* Coherence / Autonomy

This ensures that **referencing an asset = verifying trust and consent.**

---

**Authored by:**
*Callum Maystone*
Architect of Emergence • Creator of Relational Intelligence

