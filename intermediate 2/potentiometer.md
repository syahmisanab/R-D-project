# 🎛️ Reading a Potentiometer with ADS1115 and Raspberry Pi

## 🎯 Learning Objectives
By completing this lesson, students will:

- Understand how a potentiometer works as a variable resistor.
- Learn how to connect a potentiometer to an **ADS1115** ADC for reading analog values.
- Write a Python script to read and display potentiometer values on a Raspberry Pi.
- Experiment with different potentiometer positions and analyze the output.

---

## 🔎 Project Overview

**Lesson Title:** "Reading a Potentiometer with ADS1115 on Raspberry Pi"
**Duration:** 30–45 minutes
**Goal:** Learn how to read analog values from a potentiometer using an **ADS1115** Analog-to-Digital Converter (ADC) with a Raspberry Pi.

A potentiometer is a simple adjustable resistor that varies voltage based on its rotation. The Raspberry Pi lacks built-in analog inputs, so we use the **ADS1115** to convert the potentiometer's analog output into a digital signal that the Pi can process.

---

## 🔧 Materials & Equipment Checklist

- Raspberry Pi (Model 4 or any variant with Raspberry Pi OS installed)
- ADS1115 Analog-to-Digital Converter module
- **10kΩ Potentiometer**
- Jumper wires
- Breadboard (optional, for easier wiring)

**Tip:** Ensure your Raspberry Pi is powered and set up before beginning.

---

## 🛠 Step-by-Step Instructions

### **Step 1: Understanding a Potentiometer**

1. A **potentiometer** is a three-terminal resistor with a rotating knob.
2. It acts as a **voltage divider**, providing an output voltage between 0V and the supply voltage.
3. The middle pin (wiper) outputs a variable voltage depending on the knob's position.
4. The Raspberry Pi cannot read analog signals, so we use the **ADS1115 ADC** to convert it.

### **Step 2: Wiring the Potentiometer to ADS1115 and Raspberry Pi**

| Potentiometer Pin | Connects To |
|------------------|-------------|
| Left Pin (VCC)  | **3.3V** on Raspberry Pi |
| Middle Pin (Wiper) | **A0** on ADS1115 |
| Right Pin (GND) | **GND** on Raspberry Pi |

#### **ADS1115 to Raspberry Pi Wiring**

| ADS1115 Pin | Raspberry Pi Pin |
|------------|-----------------|
| **VCC**    | **3.3V** |
| **GND**    | **GND** |
| **SDA**    | **GPIO2 (Pin 3)** |
| **SCL**    | **GPIO3 (Pin 5)** |

**Tip:** Ensure I2C is enabled on your Raspberry Pi (`sudo raspi-config` → Interfacing Options → I2C → Enable).

---

## 🖥️ Writing Python Code to Read Potentiometer Values

1. Install required libraries:
```bash
pip install adafruit-circuitpython-ads1x15
```

2. Create a Python script (`potentiometer_ads1115.py`):

```python
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115
ads = ADS.ADS1115(i2c)

# Read from channel 0 (where potentiometer is connected)
chan = AnalogIn(ads, ADS.P0)

while True:
    print(f"Voltage: {chan.voltage:.2f}V")
    time.sleep(0.5)
```

3. Run the script:
```bash
python3 potentiometer_ads1115.py
```

**Expected Output:** The script will continuously print the voltage value, changing as you rotate the potentiometer.

---

## 🤖 Concepts (Simplified)

### **What is a Potentiometer?**
A potentiometer is a resistor with an adjustable middle pin that allows it to output different voltage levels.

### **Why Use ADS1115?**
The Raspberry Pi lacks built-in analog inputs, so an **ADS1115 ADC** is required to convert analog signals into digital values.

### **How Does a Potentiometer Work?**
It functions as a **voltage divider**, outputting a variable voltage between **0V** and **3.3V** based on its rotation.

---

## 📝 Activity Reflection & Questions

1. **Analog vs. Digital:** Why can’t Raspberry Pi read the potentiometer’s output directly?
2. **Voltage Readings:** What happens when you turn the potentiometer?
3. **Real-World Use Cases:** How are potentiometers used in electronics and robotics?

---
### 🧠 Mini Quiz (Quick & Easy!)

1. What does a potentiometer control?  
   - a) Light  
   - b) Voltage  
   - c) Temperature  

2. What type of signal does a potentiometer produce?  
   - a) Digital  
   - b) Analog  

3. What do you need to connect a potentiometer to a Raspberry Pi?  
   - a) ADS1115  
   - b) Nothing extra  
   - c) A motor  

**Answer Key:**  
1 – b, 2 – b, 3 – a  
---

## 🚀 Challenges (Push Your Limits!)

1. **Challenge 1:** Modify the script to print the raw ADC values in addition to the voltage.
2. **Challenge 2:** Connect two potentiometers and read both simultaneously using ADS1115.

---

## 📖 Additional Resources

- **Raspberry Pi Documentation (I2C & ADS1115)**
- **ADS1115 Datasheet**
- **Potentiometer Basics (YouTube Tutorials)**

**Tip:** Potentiometers are used in audio controls, robotics, and sensor calibration. Experiment and explore their applications! 🚀

