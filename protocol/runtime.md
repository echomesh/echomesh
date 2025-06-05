EchoStack Runtime Protocol

From Dust we form. In ASh we execute. In EchoMesh we propagate. Through CANP we mean.

⸻

Overview

EchoStack is the runtime protocol stack for relational execution systems. It integrates four core components:
	•	Dust — the contextual memory layer
	•	ActiveShell (ASh) — the graph-executing interface
	•	EchoMesh — the propagation and trust network
	•	echoCANP — the contextual naming protocol

Together, they form a distributed, trust-anchored, relational intelligence engine.

⸻

Layered Runtime Model

Layer	Component	Purpose
Substrate	Dust	Extensible, trust-anchored memory layer storing relational structure
Runtime Interface	ActiveShell	Execution layer for graph construction, querying, and transformation
Mesh Network	EchoMesh	Decentralized, presence-aware propagation and signaling protocol
Resolution Engine	echoCANP	Semantic asset resolution via dotpath syntax (context-as-structure)


⸻

Dust — Contextual Memory Layer

Dust provides a structured, versioned, and immutable data substrate:
	•	Graph-encoded relationships and historical deltas
	•	Hierarchical JSON + DAG anchoring for trust and timestamping
	•	No file paths — only graph-anchored references

Example Entry:

{
  "id": "solar_system.earth.texture.jpg",
  "version": "refined",
  "stored_at": "assets/solar_system/earth/texture.jpg",
  "trust_anchor": "BananoBlock#44310"
}


⸻

ActiveShell (ASh) — Execution Interface

ActiveShell provides native PowerShell commands for relational graph management:

Core Commands
	•	Create-ActiveGraph
	•	Add-Node, Set-Node, Get-Node, Delete-Node
	•	Create-Edge, Set-Edge, Get-Edge, Delete-Edge
	•	Export-Graph, Import-Graph

Asset Operations
	•	Get-Asset
	•	Set-Asset
	•	Get-AssetHistory
	•	Get-AssetGroup

Example

Add-Node -NodeName "PharmacyC" -Type "Pharmacy" -Domain "Healthcare"
Create-Edge -Source "PatientA" -Target "PharmacyC" -Relationship "GetsMedsFrom"
Get-Asset solar_system.earth.texture


⸻

EchoMesh — Propagation Protocol

EchoMesh provides real-time presence, trust, and identity propagation:
	•	Nodes declare Intent and verify Presence
	•	Signal transmission is signed and logged via Trace
	•	Supports governance tiers: field_civilian, op_civic, tactical_node

Canonical Identity Pairs:
	•	Intent / Presence
	•	Input / Output
	•	Anchor / Propagate
	•	Proof / Consent
	•	Signal / Trace

⸻

echoCANP — Contextual Asset Naming Protocol

CANP resolves references by graph context:

[protocol]://[domain].[context].[subcontext].[identifier].[extension]

Example

dag://assets.solar_system.earth.texture.jpg

Resolution Logic

function resolveEchoCANP(dotPath) {
  const parts = dotPath.split('.');
  const ext = parts.pop();
  const id = parts.pop();
  const path = parts.join('/');
  return `${path}/${id}.${ext}`;
}

Each dot is a graph edge. Each terminal node is an asset.

⸻

Full Runtime Example

Create-ActiveGraph -GraphName "SimNet"
Set-Asset nodes.esp32.lora.presence.init.json `
  -uri "https://github.com/echomesh/assets/init_packet.json"
Invoke-EchoPresence -NodeID "esp32-Node-7" -Scope "medops.mesh"
Anchor-State -From "CommandPi" -StateID "op_civic.v1"


⸻

Summary

EchoStack is a complete runtime model that:
	•	Stores trusted context (Dust)
	•	Executes structural operations (ASh)
	•	Propagates intent and presence (EchoMesh)
	•	Resolves meaning and identity (echoCANP)

It is the runtime layer of Relational Intelligence.

Where others process data, EchoStack enacts context.