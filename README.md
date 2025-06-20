![License](https://img.shields.io/badge/CC--BY--NC--SA%204.0-lightgrey)

<img src="https://github.com/user-attachments/assets/77623aa2-5930-45ec-87ae-1c2cd0e2533c" width="100" height="100" alt="image"/>


```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  E C H O M E S H   –   F I E L D   R E P O R T   v0.6-α       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Origin        : AU – “bush-built Tier-1 capability”
Mission       : Keep humans talking when towers die
Hardware      : ESP32-SX1262 915 MHz  /  Li-ion / solar
Status        : OPERATIONAL – core mesh verified 2025-05-31

┌─ CORE STACK ───────────────────────────────────────────────────┐
│ L1  RF       : LoRa 22 dBm (fallback BLE / Wi-Fi)              │
│ L2  echoNet  : Self-forming mesh, 7-sequence lane table        │
│ L3  echoMSG  : DAG-signed payloads  ≤ 256 B                    │
│ L4  echoVault: X25519 IDs, AES-GCM envelopes, rep-weighted ACL │
│ L5  echoMap  : GPS beacon (optional)                           │
│ L6  echoCtrl : CLI / WebSerial  → node admin                   │
└────────────────────────────────────────────────────────────────┘

┌─ QUICKSTART ───────────────────────────────────────────────────┐
│ $ git clone https://github.com/echomesh/echomesh              │
│ $ cd echomesh/firmware                                        │
│ $ pio run -t upload -e heltec_lora32                          │
│ → Boots, broadcasts presence, joins mesh in <5 s              │
└────────────────────────────────────────────────────────────────┘

┌─ FIELD METRICS (2025-05) ──────────────────────────────────────┐
│ Range (10 dBi)            3.4 km NLOS                         │
│ Cold-boot mesh join       480 ms                               │
│ Idle / TX current         19 mA / 110 mA                      │
│ Clones (30 May spike)     35 (24 unique)                      │
└────────────────────────────────────────────────────────────────┘

USE-CASES
  • Paramedic strike teams          • Off-grid homesteads
  • Mutual-aid collectives          • Disaster comms pods
  • Rapid-deployed sensor nets      • Mesh-native IoT

ROADMAP ► CLI flasher • Web echoMap • signed OTA • federation bridge

“ When all you have left is your voice — let it echo. ”

Contact  : callum@echomesh.agency   |  License : CC-BY-NC-SA 4.0

EchoMesh and the Presence Mesh doctrine represent an independent scientific contribution to sovereign capability orchestration. Designed in alignment with ADF and ITAR policy, it provides a structured alternative to complex black-box systems, reducing strategic dependency, and enabling field-resilient telemetry without compromising platform integrity.
