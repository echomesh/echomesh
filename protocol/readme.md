# 📡 echoCANP – EchoMesh Contextual Asset Naming Protocol

> “Every reference is a node. Every dot is an edge.”

`echoCANP` defines a semantic, graph‑driven asset‑resolution model used by **EchoMesh** to reference files, functions, and nodes contextually — across both physical and abstract systems.

---

## 🧠 Philosophy

Traditional paths reference **location**.
**EchoCANP** references **context**.

Where file systems are rigid, EchoCANP is **relational**.
Where URLs resolve to servers, EchoCANP resolves to **meaning**.

---

### 🧠 Identity Principles (EchoMesh Canonical Pairs)

ActiveTrust expresses access through **relational primitives**:

| **Pair**                 | **Meaning**                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **Intent / Presence**    | *Intent* is signed; *Presence* is verified. Together they form the consent moment. |
| **Input / Output**       | Trust is transactional — signals are both sent **and** received.                   |
| **Request / Response**   | Every access starts with a question and ends with mutual agreement.                |
| **Inlet / Outlet**       | Nodes open to trust (**inlet**) or express signals (**outlet**).                   |
| **Signal / Trace**       | Presence is ephemeral; trust is **logged** as an immutable trace.                  |
| **Anchor / Propagate**   | *Anchor* captures the moment; *Propagate* distributes the state.                   |
| **Proof / Consent**      | Proof validates identity; Consent enables access.                                  |
| **Coherence / Autonomy** | Trust is contextual, not controlling. Autonomy remains sovereign.                  |

> **ActiveTrust is not a switch. It’s a handshake.**

---

## 🔤 Syntax

```
[protocol]://[domain].[context].[subcontext].[identifier].[extension]
```

* **`protocol`** – Governs routing & behaviour (e.g. `echo`, `ptsd`, `dag`)
* **`domain`** – Root context (e.g. `assets`, `nodes`, `finance`)
* **`context`** – Category of intent or function
* **`subcontext`** – Specific use or scenario
* **`identifier`** – Asset or command node
* **`extension`** – File type or execution signature

---

## 🧪 Examples

| CANP Reference                                | Meaning                                                 |
| --------------------------------------------- | ------------------------------------------------------- |
| `ptsd://action.name/instructions`             | Protocol‑triggered response                             |
| `cptsd://cover.your/ass`                      | Self‑preservation fallback                              |
| `https://finance.google.com.au`               | Traditional domain, interpretable as CANP‑style dotpath |
| `dag://assets.solar_system.earth.texture.jpg` | DAG‑signed visual asset for Earth                       |
| `echo://nodes.esp32.lora.presence.init.json`  | Presence‑packet blueprint                               |

---

## 📦 Resolution Logic

```js
function resolveEchoCANP(dotPath) {
  const parts = dotPath.split('.');
  const ext   = parts.pop();     // file extension
  const id    = parts.pop();     // identifier / filename
  const path  = parts.join('/'); // remaining context → folder path
  return `${path}/${id}.${ext}`;
}
```

> Each `.` is interpreted as a **graph edge**.
> The final `id.ext` is the **terminal node**.

---

## 🧬 Versioning Philosophy

EchoCANP is **not** versioned by tags (`v1`, `v2`).
It versions by **contextual shift**.

Each new dotpath (e.g. `.augmented`, `.refined`, `.forked`) represents an emergent, semantically distinct branch in the graph.

---

## 🧠 Mesh Integration

EchoCANP powers EchoMesh to:

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
      "ttl": 3600,
      "trust_signature": "dag://auth.root.echo",
      "source": "CommandPi"
    }
  }
}
```

---

## 🛠 Future Extensions

| Feature                | Description                                   |
| ---------------------- | --------------------------------------------- |
| `canp://` handler      | Browser / plugin protocol registration        |
| `CANPManifest.json`    | Per‑asset lineage & trust chain               |
| **EchoCANP Explorer**  | UI to parse, resolve & visualise CANP graphs  |
| Graph lineage tracking | Enables inheritance, forks & ancestry mapping |

---

## ✨ Why It Matters

EchoCANP is the bridge between cognition and code.
It elevates file access to **contextual graph alignment**.
Others store files. **EchoMesh stores meaning.**

---

**Authored by:**
*Callum Maystone* – *Architect of Emergence • Creator of Relational Intelligence*

Ready to run RegEdit.exe on reality with Domain Admin creds... I think I've shown I'm capable. 
