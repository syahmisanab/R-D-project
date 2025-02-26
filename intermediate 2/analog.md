🎯 **Learning Objectives**
By completing this lesson, students will:

1. Understand the difference between digital and analog signals and why analog signals require conversion for Raspberry Pi.
2. Learn how the ADS1115 Analog-to-Digital Converter (ADC) works and how it extends Raspberry Pi's capabilities.
3. Gain confidence in connecting and reading data from analog sensors using ADS1115.
4. Develop basic troubleshooting and problem-solving skills when working with analog signals.

---

🔎 **Project Overview**

**Lesson Title:** "Understanding Analog Signals and ADS1115 on Raspberry Pi"  
**Duration:** 30–45 minutes  
**Goal:** By the end of this lesson, you will understand the basics of analog signals, the role of ADCs, and how to use the ADS1115 module to interface with analog sensors on a Raspberry Pi.

Modern microcontrollers like Arduino have built-in analog input pins, but Raspberry Pi lacks them. The ADS1115 ADC bridges this gap, allowing the Raspberry Pi to process analog signals for applications like sensors, potentiometers, and more.

---

🔧 **Materials & Equipment Checklist**

1. Raspberry Pi (Model 4 or any variant with Raspberry Pi OS installed)
2. ADS1115 Analog-to-Digital Converter module
3. Analog sensor (e.g., potentiometer, temperature sensor, or any voltage-based analog output device)
4. Jumper wires
5. Breadboard (optional but recommended)

**Tip:** Ensure your Raspberry Pi is powered and set up before beginning.

---

🛠 **Step-by-Step Instructions**

### **Step 1: Understanding Analog vs. Digital Signals**
1. **Digital Signals:** Represent data as discrete values (0 or 1), used by Raspberry Pi’s GPIO pins.
2. **Analog Signals:** Represent continuous values (e.g., varying voltages from a sensor) and require conversion for Raspberry Pi.
3. **Role of ADC:** Converts analog signals into a digital format readable by Raspberry Pi.

### **Step 2: What is ADS1115?**
1. ADS1115 is a 16-bit ADC module with four input channels.
2. It communicates with Raspberry Pi using the I2C protocol.
3. It allows reading of voltage-based sensors that output analog signals.

### **Step 3: Connecting ADS1115 to Raspberry Pi**
1. **Wiring Setup:**
   - Connect `VCC` on ADS1115 to `3.3V` on Raspberry Pi.
   - Connect `GND` on ADS1115 to `GND` on Raspberry Pi.
   - Connect `SCL` on ADS1115 to `SCL` on Raspberry Pi (`GPIO3` – Pin 5).
   - Connect `SDA` on ADS1115 to `SDA` on Raspberry Pi (`GPIO2` – Pin 3).
   - Connect an analog sensor (e.g., potentiometer) to `A0` input on ADS1115.

**Tip:** Ensure I2C is enabled on your Raspberry Pi (`sudo raspi-config` → Interfacing Options → I2C → Enable).

### **Step 4: Understanding ADS1115 Data Output**
1. The ADS1115 provides a 16-bit resolution output (values range from -32,768 to 32,767).
2. The output depends on the selected gain and reference voltage.
3. It can be configured to read single-ended or differential inputs.

### **Step 5: Practice & Experiment**
1. Connect different analog sensors and observe how the output changes.
2. Experiment with different gain settings to understand how they affect readings.
3. Try reading multiple channels simultaneously.

---

🤖 **Concepts (Simplified)**

1. **What is an ADC?**
   - An Analog-to-Digital Converter translates analog voltages into digital values.
2. **Why Raspberry Pi Needs ADS1115?**
   - Raspberry Pi lacks native analog input pins, so an external ADC is required.
3. **Common Analog Sensors that Require an ADC**
   - Potentiometers (voltage dividers)
   - Temperature sensors (e.g., LM35)
   - Light-dependent resistors (LDRs)
   - Pressure sensors

---

📝 **Activity Reflection & Questions**

1. **Analog vs. Digital:** Why can’t Raspberry Pi read analog values directly?
2. **ADS1115:** How does an ADC help bridge the gap between analog sensors and Raspberry Pi?
3. **Voltage Readings:** What happens when you adjust a potentiometer connected to ADS1115?
4. **Real-World Use Cases:** How do analog sensors play a role in robotics, weather monitoring, or medical devices?

---

🧠 **Mini Quiz (Test Your Understanding!)**

1. What type of signal does a potentiometer generate?
   a) Digital  
   b) Analog  
   c) Binary  

2. Why do we need ADS1115 for Raspberry Pi?
   a) To add more GPIO pins  
   b) To read analog signals  
   c) To control motors  

3. What communication protocol does ADS1115 use?
   a) SPI  
   b) UART  
   c) I2C  

4. What is the resolution of ADS1115?
   a) 8-bit  
   b) 10-bit  
   c) 16-bit  

**Answer Key (for instructor use):**  
1 – b, 2 – b, 3 – c, 4 – c  

---

🚀 **Challenges (Push Your Limits!)**

1. **Challenge 1:** Connect multiple analog sensors to ADS1115 and read values from different channels.
2. **Challenge 2:** Experiment with the gain settings of ADS1115 and observe how it affects readings.

---

📖 **Additional Resources**

- **Raspberry Pi Documentation (I2C & ADS1115)**
- **ADS1115 Datasheet**
- **Analog Sensors and ADCs (YouTube Tutorials)**

**Tip:** Understanding analog signals opens the door to projects in robotics, environmental monitoring, and IoT applications!

