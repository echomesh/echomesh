# EchoMesh – Field Report v0.6-α

![License](https://img.shields.io/badge/CC--BY--NC--SA%204.0-lightgrey)

<img src="https://github.com/user-attachments/assets/77623aa2-5930-45ec-87ae-1c2cd0e2533c" width="100" height="100" alt="EchoMesh logo"/>  

---

## Executive Summary

**EchoMesh** is a sovereign, lightweight communications capability designed to maintain human and system connectivity in environments where conventional infrastructure has failed or is unavailable. Built on **ESP32-SX1262 LoRa hardware** with solar/portable power options, EchoMesh provides a **field-resilient, policy-aligned alternative** to dependency on centralised or black-box communications platforms.

* **Origin:** Australia – independently developed Tier-1 capability
* **Mission:** Preserve operational continuity when towers or networks collapse
* **Status:** Operational; core mesh verified 2025-05-31

---

## System Architecture

### Core Stack

| Layer | Module    | Functionality                                                 |
| ----- | --------- | ------------------------------------------------------------- |
| L1    | RF        | LoRa 22 dBm (fallback BLE / Wi-Fi)                            |
| L2    | echoNet   | Self-forming mesh with adaptive lane tables                   |
| L3    | echoMSG   | Directed acyclic graph (DAG)-signed payloads ≤ 256 B          |
| L4    | echoVault | X25519 identities, AES-GCM envelopes, reputation-weighted ACL |
| L5    | echoMap   | Optional GPS beaconing for presence mapping                   |
| L6    | echoCtrl  | Command-line & WebSerial administration                       |

---

## Deployment Quickstart

```bash
git clone https://github.com/echomesh/echomesh
cd echomesh/firmware
pio run -t upload -e heltec_lora32
```

→ Device boots, broadcasts presence, and joins mesh within **< 5 seconds**.

---

## Field Metrics (May 2025)

| Metric                   | Result                |
| ------------------------ | --------------------- |
| Range (10 dBi antenna)   | 3.4 km NLOS           |
| Cold-boot mesh join      | 480 ms                |
| Current (Idle / TX)      | 19 mA / 110 mA        |
| Node deployment (30 May) | 35 clones (24 unique) |

---

## Use Cases

* **Disaster response pods**
* **Paramedic and strike teams**
* **Off-grid homesteads / remote operations**
* **Mutual-aid or resilience collectives**
* **Rapid-deployed sensor networks**
* **Mesh-native IoT ecosystems**

---

## Roadmap

* Streamlined CLI flasher
* Web-based echoMap interface
* Digitally signed OTA updates
* Federation bridge for cross-mesh interoperability

---

## Strategic Context

EchoMesh and the **Presence Mesh doctrine** represent an independent Australian scientific and engineering contribution to sovereign capability orchestration.

The system has been:

* **Designed in alignment** with **ADF** (Australian Defence Force) and **ITAR** compliance considerations
* **Structured to reduce strategic dependency** on opaque, foreign-sourced communications platforms
* **Optimised for field resilience**, ensuring telemetry and coordination remain intact even under degraded or contested network conditions

---

## Contact

* 📧 **Email:** [callum@echomesh.agency](mailto:callum@echomesh.agency)
* 📜 **License:** [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> *“When all you have left is your voice — let it echo.”*
