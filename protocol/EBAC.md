# EchoMesh Protocol Extension: EBAC (Edge-Based Access Control)

## 1. Overview

**Edge-Based Access Control (EBAC)** is the **native relational access model** of EchoMesh.
Unlike static identity and access management (IAM) frameworks, EBAC derives access rights **dynamically** from relationships within the mesh.

In EBAC:

* Nodes represent **entities** (users, resources, agents).
* Edges represent **permissions and trust relationships**.
* Access decisions are evaluated in **real time** from the active graph.

This approach provides a **context-aware, scalable, and self-evolving access fabric**.

---

## 2. Limitations of Traditional IAM Models

| Model                      | Description                      | Limitations                                  |
| -------------------------- | -------------------------------- | -------------------------------------------- |
| **RBAC** (Role-Based)      | Roles define permissions.        | Static, rigid, high administrative overhead. |
| **ABAC** (Attribute-Based) | Attributes define policies.      | Policy sprawl, difficult to audit at scale.  |
| **PBAC** (Policy-Based)    | Access rules encoded in logic.   | Complex, brittle, costly to maintain.        |
| **EBAC** (Edge-Based)      | **Relationships define access.** | **Dynamic, contextual, scalable.**           |

---

## 3. Protocol Function

In EBAC, permissions emerge directly from **edges in the graph**.

Example access edges:

```plaintext
[ Dr. Smith ] --(CAN_EDIT)--> [ Patient_001 ]
[ Admin_Y ] --(HAS_FULL_ACCESS)--> [ All_Patients ]
[ Researcher_X ] --(CAN_VIEW_DEIDENTIFIED)--> [ P001, P002, P003 ]
```

Each **edge** includes:

* Permission type (e.g., `CAN_EDIT`, `CAN_VIEW_DEIDENTIFIED`).
* Time-to-live (TTL) or decay logic.
* Contextual tags for scope (e.g., `research`, `clinical`).

---

## 4. Access Resolution Flow

When a node requests access:

1. Mesh evaluates **edges** between node and resource.
2. Validates edge state: permission type, TTL, context.
3. Grants or denies access in **real time**, without static role evaluation.

**Example: Access to Patient Record 002**

| Node          | Edge Relationship       | Access Result |
| ------------- | ----------------------- | ------------- |
| Dr. Smith     | `CAN_EDIT`              | ✅ Granted     |
| Researcher\_X | `CAN_VIEW_DEIDENTIFIED` | ✅ Granted     |
| Auditor\_Z    | `CAN_AUDIT`             | ✅ Granted     |
| Intern\_Y     | *No edge present*       | ❌ Denied      |

---

## 5. Access Fabric Concepts

* **Edges as Permissions** → Access modeled as graph relationships.
* **Edge TTL/Decay** → Permissions expire automatically over time.
* **Edge Mutation** → Access changes require only edge rewrites.
* **Multi-Vector Access** → A single node may hold multiple, differentiated edges to different resources.

---

## 6. Security and Integrity

EBAC enforces **zero-trust principles** by cryptographically securing edge states.

* **Encrypted Edge State** → All permissions are tamper-resistant.
* **Hash-Chained Logs** → Every change is signed and auditable.
* **Zero-Trust Native** → No assumption of trust; each access is revalidated.
* **Real-Time Propagation** → Edge changes broadcast across the mesh instantly.

---

## 7. Comparative Alignment

| Feature                | Traditional IAM  | EBAC (EchoMesh)       |
| ---------------------- | ---------------- | --------------------- |
| Access Source          | Roles / Policies | Graph Relationships   |
| Update Mode            | Manual Admin     | Auto-reactive         |
| Scalability            | Finite           | Effectively infinite  |
| Real-World Mapping     | Indirect         | Direct 1:1 relational |
| AI Contextual Matching | Minimal          | Native                |
| Encryption Backbone    | Optional         | Required (DAG-native) |

---

## 8. Strategic Value

EBAC introduces a **relational access model** aligned with how enterprises actually operate: through **relationships, trust, and presence**.

Benefits include:

* **Reduced IAM complexity** (no static roles/policies).
* **Real-time adaptability** to contextual changes.
* **Auditable trust lineage** via graph edges.
* **Seamless AI integration** for contextual access decisions.

---

## 9. Summary

EBAC represents the **access layer of EchoMesh**, providing a **dynamic, contextual, and scalable alternative** to RBAC, ABAC, and PBAC.

By treating **edges as permissions**, EBAC enables:

* Secure, zero-trust enforcement.
* Context-driven access alignment.
* Simplified governance at scale.

EBAC is not an extension of legacy IAM — it is **the native access fabric for relational intelligence systems**.

