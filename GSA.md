# Graph System Authority – Runtime Stack

## 1. OS – Operating System
- **Ubuntu Server 24.04 LTSR**
- Provides stable execution layer for running graph substrates and executor services.

## 2. GS – Graph Substrate
- **Neo4j (bolt://)**
- Stores persistent graph of nodes, roles, context, history.
- Acts as source of truth for Field Executors.

## 3. FE – Field Executor
- **Active Graph Networks**
- Executes dynamic policies, propagates context-aware changes across graph.

## 4. CLI – Command Line Interface
- **ActiveShell (ASH)**
- Human/operator interface to interact with graph substrate and trigger field executions.

---

## Runtime Bindings Summary

| Abstract | Bound Implementation |
|----------|----------------------|
| OS       | Ubuntu 24.04 LTSR    |
| GS       | Neo4j (bolt://)      |
| FE       | Active Graph Network |
| CLI      | ActiveShell (ASH)    |