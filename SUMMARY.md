# EchoMesh – Documentation Index  
*A living map of every spec, diagram, example and test.*

## 0 — Project-level
- [README](README.md) — elevator pitch & build badges  
- [CHANGELOG](CHANGELOG.md) — semantic-version log  
- [CONTRIBUTING](CONTRIBUTING.md) — branch naming, commit format, CLA

## 1 — Architecture Overview
- [EchoMesh Stack](docs/overview/echomesh_stack.md)
- [Protocol Matrix](docs/overview/protocol_matrix.md)
- [Mermaid Gallery](docs/overview/diagrams.md)

## 2 — Protocols (`/docs/protocols`)
| Code | Document | Purpose |
|------|----------|---------|
| **NTSP** | [Network Time-Sync Protocol](docs/protocols/NTSP.md) | tick / pulse-echo / `TΔ` |
| **DCA-G** | [Distributed Cert-Authority (Graph)](docs/protocols/DCA-G.md) | role & scope certs |
| **DOTP** | [Distributed Object Transfer](docs/protocols/DOTP.md) | payload framing & retries |
| **DRAP** | [DAG-Referenced Asset](docs/protocols/DRAP.md) | provenance & lineage |
| **DMCP** | [Dynamic Mesh Config](docs/protocols/DMCP.md) | role hopping & quorum |
| **SEMP** | [State Exchange & Mesh Presence](docs/protocols/SEMP.md) | heartbeat & liveness |
| **FoEC-Vet** | [Vetting / Reaction Depth](docs/protocols/FoEC-Vet.md) | NV1 → NV2 → PV model |
| **NTSP-Examples** | [Time-Sync JSON vectors](examples/ntsp/t_delta.json) | reference packets |

## 3 — Algorithms (`/docs/algorithms`)
- [Graph-Shard Merge](docs/algorithms/merge.md)
- [Multi-Packet Echo Correction](docs/algorithms/echo_merge.md)

## 4 — Firmware (`/firmware/esp32`)
- [`src/`](firmware/esp32/src) — PlatformIO sources  
- [`include/`](firmware/esp32/include) — protocol headers  
- [`docs/`](firmware/esp32/docs) — HAL notes & pin maps

## 5 — Examples (`/examples`)
- `ntsp/` — sync logs & JSON schemas  
- `dca/` — YAML cert bundles  
- `dotp/` — sample payloads w/ CRC mismatch cases  

## 6 — Tests (`/test`)
- Unit: protocol parsers, CRC, cert verify  
- Integration: dual-node loopback, LoRa over-air  
- CI: GitHub Action matrix

## 7 — Assets (`/docs/assets`)
- Auto-rendered Mermaid → PNG  
- High-res white-board photos (original refs)

---

### How to extend
1. Add a page? → create the Markdown then reference it here.  
2. Add a diagram? → place the `.mmd` in `docs/overview/` (or protocol folder) and the PNG in `docs/assets/`.  
3. Keep this index alphabetized / section-ordered so new contributors never get lost.

*Locked & loaded — next up: populate **NTSP.md**.* 🚀