# EchoMesh – Asset Register (Preliminary Visual Parse)

*Version 0.1 | Prepared by YouMatter Systems | Date: 2025-06-06*

---

## 1. Current Asset Inventory

| Row | Item Description                                  | Category     | Notes / Technical Detail             |
| --- | ------------------------------------------------- | ------------ | ------------------------------------ |
| 1   | Large Breadboard Set (Faystar)                    | Prototyping  | Triple board, integrated power rails |
| 2   | Small White Breadboard                            | Prototyping  | Secondary/backup unit                |
| 3   | Jaycar “Learn to Solder” Kit                      | Training Kit | Through-hole soldering practice      |
| 4   | Arduino Sensor Kit                                | Sensor Pack  | Temperature, IR, light, etc.         |
| 5   | Duinotech Compass Soldering Iron                  | Tool         | Standard soldering unit              |
| 6   | Solder Wire Roll                                  | Consumable   | Composition (Sn/Pb vs Pb-free) TBD   |
| 7   | Flux Pen / Marker                                 | Tool         | Likely flux delivery tool            |
| 8   | Duinotech 1.27” Color OLED Display                | Display      | SPI/I²C miniature display            |
| 9   | Raspberry Pi GPIO Shroud                          | Protection   | Dust/short protection for headers    |
| 10  | Duinotech Digital Humidity & Temperature Sensor   | Sensor       | Likely DHT11/DHT22                   |
| 11  | Duinotech Sound Sensor                            | Sensor       | Microphone + op-amp board            |
| 12  | Duinotech IR Sensor                               | Sensor       | IR receiver/emitter module           |
| 13  | Duinotech Light Sensor                            | Sensor       | Photodiode module                    |
| 14  | Duinotech Motion Sensor                           | Sensor       | Passive Infrared (PIR)               |
| 15  | Duinotech Gas Sensor                              | Sensor       | MQ-series type                       |
| 16  | Jaycar Autoranging Digital Multimeter             | Tool         | Battery-operated DMM                 |
| 17  | Jumper Wire Assortment (M-F, F-F)                 | Wiring       | Pre-stripped header wires            |
| 18  | USB–UART Module (FTDI-compatible)                 | Adapter      | Serial bridge for MCU programming    |
| 19  | ProtoBoards (x2) – Black w/ Gold Pads             | Prototyping  | Solder prototyping boards            |
| 20  | Raspberry Pi-Compatible RTC Module                | Time Module  | Real-Time Clock w/ battery backup    |
| 21  | ESP32 Development Board                           | MCU          | Wi-Fi/Bluetooth capable, LoRa absent |
| 22  | Arduino Uno (or compatible clone)                 | MCU          | Standard entry-level board           |
| 23  | Wire Stripper / Crimper Tool                      | Tool         | Manual cable preparation             |
| 24  | 7” HDMI Touch Screen (Duinotech)                  | Display      | USB + HDMI input                     |
| 25  | 7” HDMI Touch Screen (Pelican Case loadout)       | Display      | Field-ready deployment set           |
| 26  | LoRa Antenna Kit w/ Pigtail                       | Comms Module | RP-SMA + u.FL connectors             |
| 27  | Mixed Components (resistors, capacitors, headers) | Components   | General prototyping parts            |
| 28  | Duinotech Leonardo Micro Board                    | MCU Board    | Compact USB-enabled MCU              |
| 29  | Ribbon Cable Pack (10-pin, multi-colour)          | Wiring       | Dupont header type                   |

---

## 2. Recommended Asset Register Schema

For full enterprise-grade asset tracking, the following fields should be added to the register:

| Column Name          | Description                                  |
| -------------------- | -------------------------------------------- |
| **Asset ID**         | Unique identifier assigned by asset register |
| **Item Description** | Human-readable equipment label               |
| **Category**         | Equipment classification (Sensor, Tool, MCU) |
| **Serial Number**    | Manufacturer or custom-assigned serial ID    |
| **Unique ID / MAC**  | Hardware identifier (e.g. ESP32 MAC, RTC ID) |
| **Assigned Node**    | Logical assignment (EchoNode.00, EchoRoot)   |
| **Status**           | Active / Spare / Faulty / Development        |
| **Location**         | Storage or deployment location               |
| **Custodian**        | Assigned owner / responsible engineer        |
| **Notes**            | Additional operational or technical remarks  |

---

## 3. Next Steps

1. **Serialisation:** Assign asset IDs and capture hardware serial/MACs.
2. **Categorisation:** Confirm final category taxonomy for consistent reporting.
3. **Integration:** Import register into configuration management or CMDB system (ServiceNow / Snipe-IT).
4. **Lifecycle Tracking:** Define asset status states (procurement → active → retired).
5. **Field Readiness:** Mark items packaged/deployed vs retained in lab.
