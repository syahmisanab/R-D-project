# 📡 PN532 NFC/RFID Module with Raspberry Pi

## 🎯 Learning Objectives
By completing this lesson, students will:

1. Understand the working principle of NFC and RFID technology.
2. Learn how the PN532 NFC module communicates with Raspberry Pi using I2C, SPI, or UART.
3. Read and write data using RFID/NFC tags.
4. Implement a simple RFID-based authentication system using Python.

---

## 🔎 Project Overview

**Lesson Title:** "Using PN532 NFC/RFID Module with Raspberry Pi"
**Duration:** 30–45 minutes  
**Goal:** Learn how to interface the PN532 module with Raspberry Pi and use it to read RFID/NFC tags.

NFC (Near Field Communication) is a short-range wireless technology used for authentication, payments, and data transfer. The **PN532 module** enables Raspberry Pi to read and write NFC/RFID tags, opening possibilities for security systems, access control, and contactless applications.

---

## 🔧 Materials & Equipment Checklist

1. **Raspberry Pi** (Model 4 or any variant with Raspberry Pi OS installed)
2. **PN532 NFC Module** (supports I2C, SPI, and UART communication)
3. **RFID/NFC Tags** (Mifare Classic, NTAG, etc.)
4. **Jumper Wires**
5. **Breadboard** (optional but recommended)

**Tip:** Ensure your Raspberry Pi is powered and connected to a display or SSH session before starting.

---

## 🛠 Step-by-Step Instructions

### **Step 1: Understanding NFC & RFID**

1. **RFID (Radio Frequency Identification):** Uses radio waves to transmit data between a reader and a tag.
2. **NFC (Near Field Communication):** A subset of RFID, allowing two-way communication between devices within a short range (usually <10 cm).
3. **PN532 Module:** A powerful NFC chip that supports:
   - Reading/Writing NFC tags.
   - Emulating NFC cards.
   - Peer-to-peer communication.

---

### **Step 2: Wiring PN532 to Raspberry Pi (I2C Mode)**

#### **PN532 Module Pins:**
- **VCC** → 3.3V (Raspberry Pi)
- **GND** → GND (Raspberry Pi)
- **SDA** → GPIO2 (Pin 3)
- **SCL** → GPIO3 (Pin 5)

**Tip:** Enable I2C on Raspberry Pi (`sudo raspi-config` → Interfacing Options → I2C → Enable).

---

### **Step 3: Installing Required Libraries**

```sh
sudo apt update
sudo apt install python3-pip
pip3 install adafruit-circuitpython-pn532
```

---

### **Step 4: Reading NFC Tags with Python**

```python
import time
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Configure PN532 to read NFC tags
pn532.SAM_configuration()

print("Waiting for an NFC card...")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid:
        print(f"Card detected! UID: {uid.hex()}")
    time.sleep(1)
```

---

### **Step 5: Understanding the Output**

1. The script continuously scans for NFC/RFID tags.
2. When a tag is detected, it prints the **UID (Unique Identifier)**.
3. This UID can be used for authentication, access control, or data retrieval.

---

## 🤖 Concepts (Simplified)

1. **What is NFC/RFID?**
   - Wireless technologies used for contactless identification and data transfer.

2. **Why use the PN532 Module?**
   - It allows Raspberry Pi to communicate with NFC tags and devices.

3. **Common Applications:**
   - Contactless payments
   - Smart locks and access control
   - Inventory tracking
   - IoT and automation

---

## 📝 Activity Reflection & Questions

1. **What is the main difference between NFC and RFID?**
2. **How does the PN532 module communicate with Raspberry Pi?**
3. **What happens when an NFC tag is scanned?**

---

## 🧠 Mini Quiz (Test Your Understanding!)

1. What type of technology does the PN532 module use?
   a) Bluetooth  
   b) NFC/RFID  
   c) Wi-Fi  

2. What is the primary function of an NFC tag?
   a) Store and transmit data wirelessly  
   b) Generate electricity  
   c) Act as a digital display  

3. What type of connection is used between the PN532 and Raspberry Pi in this lesson?
   a) SPI  
   b) UART  
   c) I2C  

**Answer Key:** 1 – b, 2 – a, 3 – c

---

## 🚀 Challenges (Push Your Limits!)

1. **Challenge 1:** Modify the script to trigger an LED when a specific NFC tag is detected.
2. **Challenge 2:** Store user data on an NFC tag and retrieve it using Raspberry Pi.
3. **Challenge 3:** Build a basic RFID-based attendance system.

---

## 📖 Additional Resources

- **PN532 Datasheet**
- **Adafruit PN532 Library Documentation**
- **NFC & RFID Tutorials (YouTube, Blogs)**

**Tip:** Learning NFC technology opens doors to exciting projects in security, automation, and smart devices!

---

Let me know if you need any modifications or more details! 🚀

