# 🔐 EchoMesh Protocol Extension: EBAC (Edge-Based Access Control)

## Overview

**Edge-Based Access Control (EBAC)** is the **relational access model** native to EchoMesh.  
It replaces static permission frameworks with **dynamic, graph-inferred access**.

Access rights are not assigned —  
they **emerge from relationships** between nodes in the mesh.

---

## ⚠️ Problem with Traditional IAM Models

| Model | Description | Limitations |
|-------|-------------|-------------|
| **RBAC** | Role-Based | Static, manual, rigid |
| **ABAC** | Attribute-Based | Complex policy sprawl |
| **PBAC** | Policy-Based | Logic overkill, brittle at scale |
| **EBAC** | **Edge-Based (Graph)** | 🔄 **Dynamic**, 🧠 **Contextual**, 🚀 **Scalable** |

---

## 🧬 Protocol Function

In EchoMesh, all nodes (users, resources, agents) are **vertices** in a DAG.  
**Edges define context-aware permissions** (e.g., `CAN_EDIT`, `CAN_VIEW_ANON`, `CAN_AUDIT`).

```graph
[ Dr. Smith ] --(CAN_EDIT)--> [ Patient_001 ]
[ Admin_Y ] --(HAS_FULL_ACCESS)--> [ All_Patients ]
[ Researcher_X ] --(CAN_VIEW_DEIDENTIFIED)--> [ P001, P002, P003 ]
```

---

## 🔎 Resolution Flow

When a node requests access:

1. Mesh checks for **active edges** between node and resource  
2. Edge includes **permission type, TTL, and context tags**  
3. Access is **granted/denied dynamically**, without role logic

---

## 🔄 Relationship Flow Example

### Access to Patient Record 002:

```plaintext
👨‍⚕️ Dr. Smith       → CAN_EDIT            → Patient_002 ✅
🔬 Researcher_X      → CAN_VIEW_DEIDENT    → Patient_002 ✅
👀 Auditor_Z         → CAN_AUDIT           → Patient_002 ✅
📕 Intern_Y          → NO EDGE             → Patient_002 ❌
```

---

## 🧱 Access Fabric Concepts

- **Edges as Permissions** → Relationships carry access state  
- **Edge TTL / Decay** → Permissions can expire organically  
- **Edge Mutation** → Updating access is a simple edge rewrite  
- **Multi-Vector Access** → Same node, different edges to different resources

---

## 🔐 DAG-Based Access Integrity

- **Encrypted Edge State** → Access graph is tamper-resistant  
- **Hash-Chained Permission Logs** → Every change is signed and auditable  
- **Zero-Trust Native** → Every edge is revalidated at time of use  
- **Real-Time Propagation** → New edges broadcast across mesh instantly

---

## 🧭 EchoMesh Alignment

| Feature | Traditional IAM | EBAC (EchoMesh) |
|---------|------------------|------------------|
| Access Source | Roles/Policies | Graph Relationships |
| Update Mode | Manual Admin | Auto-Reactive |
| Scale | Finite | Infinite |
| Real-World Mapping | Weak | 1:1 Relational |
| AI Alignment | Minimal | Native Contextual Matching |
| Encryption Backbone | Optional | Required (DAG-native) |

---

## 💥 Summary

**EBAC isn’t a feature — it’s the access layer the mesh was built for.**  
It reflects how the world actually works: through **relationships, trust, and presence.**

If RBAC is a door,  
ABAC is a lock,  
PBAC is a coded keypad...

Then EBAC is **the hand that already holds the key**.