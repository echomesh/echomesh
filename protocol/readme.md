
# 📡 echoCANP – EchoMesh Contextual Asset Naming Protocol

> “Every reference is a node. Every dot is an edge.”

`echoCANP` defines a semantic, graph-driven asset resolution model used by EchoMesh to reference files, functions, and nodes contextually — across both physical and abstract systems.

---

## 🧠 Philosophy

Traditional paths reference **location**.  
**EchoCANP references context.**

Where file systems are rigid,  
EchoCANP is relational.  
Where URLs resolve to servers,  
EchoCANP resolves to **meaning**.


---

### 🧠 Identity Principles (EchoMesh Canonical Pairs)

ActiveTrust redefines access through relational primitives:

| **Pair**           | **Meaning**                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **Intent / Presence**     | Intent is signed. Presence is verified. Together they form the consent moment. |
| **Input / Output**        | Trust is transactional — signals are both sent and received.                  |
| **Request / Response**    | Every access starts with a question and ends with mutual agreement.          |
| **Inlet / Outlet**        | Nodes open to trust (inlet) or express signals (outlet).                     |
| **Signal / Trace**        | Presence is ephemeral. Trust is logged.                                      |
| **Anchor / Propagate**    | Anchor a moment. Propagate a state.                                          |
| **Proof / Consent**       | Proof validates identity; Consent enables access.                            |
| **Coherence / Autonomy**  | Trust is contextual, not controlling. Autonomy remains sovereign.            |

> **ActiveTrust is not a switch. It’s a handshake.**

---

## 🔤 Syntax

```

[protocol]: //[domain].[context].[subcontext].[identifier].[extension]

````

- `protocol` → Governs routing and behavior (e.g. `echo`, `ptsd`, `dag`)
- `domain` → Root context (e.g. `assets`, `nodes`, `finance`)
- `context` → Category of intent or function
- `subcontext` → Specific use or scenario
- `identifier` → Asset or command node
- `extension` → File type or resolution signature

---

## 🧪 Examples

| CANP Reference | Meaning |
|----------------|---------|
| `ptsd://action.name/instructions` | Protocol-triggered response |
| `cptsd://cover.your/ass` | Self-preservation fallback |
| `https://finance.google.com.au` | Legacy DNS domain (CANP-compliant) |
| `dag://assets.solar_system.earth.texture.jpg` | DAG-signed asset reference |
| `echo://nodes.esp32.lora.presence.init.json` | Presence packet structure |

---

## 📦 Resolution Logic

```js
function resolveEchoCANP(dotPath) {
  const parts = dotPath.split('.');
  const ext = parts.pop();
  const id = parts.pop();
  const path = parts.join('/');
  return `${path}/${id}.${ext}`;
}
````

> Interprets each `.` as a graph edge.
> Final `id.ext` is the terminal node.

---

## 🧬 Versioning Philosophy

EchoCANP is not versioned by tag (`v1`, `v2`) —
It’s versioned by **contextual shift**.

Each new dotpath (e.g. `.augmented`, `.refined`, `.forked`)
represents an emergent, semantically distinct branch.

---

## 🧠 Mesh Integration

EchoCANP is used throughout EchoMesh to:

* Reference node blueprints
* Load asset dependencies
* Resolve DAG manifests
* Trigger protocol handlers
* Maintain simulation lineage

---

## 🔐 EchoCANP in a Registry

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

## 🛠 Future Extensions

| Feature                  | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| `canp://` handler        | Protocol registration for browser/plugin support     |
| `CANPManifest.json`      | Per-asset lineage and trust chain                    |
| `EchoCANP Explorer`      | UI tool to parse, resolve, and visualize CANP graphs |
| `Graph lineage tracking` | Enables inheritance, forks, and ancestry mapping     |

---

## ✨ Why It Matters

EchoCANP is the bridge between cognition and code.
It elevates file access to **contextual graph alignment**.
Where others store files — EchoMesh builds meaning.

---

**Authored by:**
Callum Maystone
*Architect of Emergence • Creator of Relational Intelligence*

```

