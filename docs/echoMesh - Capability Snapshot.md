# EchoMesh – Sovereign LoRa Mesh (v0.6)

**What problem it solves**  
> Push-button comms when infrastructure is down. No cellular, no cloud, still encrypted.

**Why it’s different**  
* Network-agnostic: SX1262 LoRa, Wi-Fi, BLE, UART (mix & match).  
* Self-healing DAG trust – nodes earn or lose authority in real-time.  
* Zero-touch: passive startup listens first, talks later.  
* Runs on $12 ESP32-SX1262 boards or a Pi zero command module.

**Field proof**  
| Metric | Result |
|--------|--------|
| Cold-boot mesh join | 480 ms (3-node test) |
| Passive EM GPIO detect | 0.7 V shift on REG-42 float |
| Range (915 MHz, 10 dBi) | 3.4 km NLOS suburban |
| Power draw idle/tx | 19 mA / 110 mA |

**Next milestone**  
– Tri-anchor geo-sync demo (ETA July 2025)  
– NV1-cleared code walk-through on request

**Ask**  
> 30-minute virtual brief & lab access for controlled range test.  
> Contact: callum@conicu.com.au +61449199361 (GitHub: @echomesh)
