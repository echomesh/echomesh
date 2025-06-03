## 🔐 **echoMesh Design Decision — Core Architecture Lock**

### ✅ **Network-Agnostic, Modular Mesh Protocol**

* Every node (ESP32, Pi, etc.) operates as an **independent, interoperable entity**.
* The mesh must work regardless of manufacturer — **LoRa, WiFi, UART, SPI, BLE all acceptable** at the link layer.
* Protocol flow is **agnostic to source hardware**, governed instead by the **packet sequence + channel interface model**.

---

### 🧱 **Layered Architecture**

#### **1. Physical Layer**

* **Primary Transport:** SX1262 LoRa @ 915MHz
* Optional uplink: WiFi, USB, Ethernet (via Pi Command Module)

#### **2. Network Layer: `echoL1`**

* Packet Structure: `(PID, Hash, Time, Payload)`
* Flow logic: Defined by 7-sequence interface routing table
* Channels and lanes standardised across nodes

#### **3. Compute Layer**

* ESP32s: **Decentralised processors**, capable of encryption, filtering, response
* Raspberry Pi: **Command Module**, acts as DAG root + uplink negotiator

#### **4. Storage Layer**

* Field: Onboard Flash or SPI Flash
* Command: MicroSD / USB / External drive
* Cloud Uplink: Optional via API, FTP, MQTT, or JSON stream

#### **5. DAG + ACL Security Model**

* Access controlled via signed DAG propagation
* **Device Identity = PID**
* **Trust = DAG-defined, TTL-constrained**
* ACLs are not static; they **evolve through interaction + verification**

---

### 📦 **Plug-and-Play Philosophy**

* **Each device has a local registry**:

  * Device type
  * Pin mapping
  * Capabilities
  * Trust flags
* Devices can be hot-swapped, repositioned, or redeployed with no hardcoded assumptions.

---

### 🧠 **Command Module (Pi) Responsibilities**

* Host echoOS / echoShell
* Visualise mesh topology
* Relay or store critical messages
* Perform bulk crypto / sync / uplink ops
* Maintain DAG state + respond to foreign PID queries

---

### 🛠️ Next Steps

* Build `echoOS` starter with local JSON registry + LoRa Rx
* Draft DAG format (node-based ACL prototype)
* Develop modular enclosure schema (magnet or clip-in preferred)
* Finalise registry format: `device.json`

