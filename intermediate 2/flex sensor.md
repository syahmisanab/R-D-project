# 📚 Lesson Plan: Using a Flex Bend Sensor with Raspberry Pi

## 🎯 Learning Objectives
By completing this lesson, students will:

1. Understand what a flex bend sensor is and how it works.
2. Learn how to interface a flex bend sensor with Raspberry Pi using an ADC.
3. Read and process analog data from the flex sensor using the ADS1115 ADC module.
4. Develop basic programming skills to capture and visualize flex sensor data.

---

## 🔎 Project Overview

**Lesson Title:** "Measuring Flex with a Bend Sensor on Raspberry Pi"
**Duration:** 30–45 minutes
**Goal:** Learn how a flex sensor works, how to interface it with a Raspberry Pi using the ADS1115, and how to process and interpret its readings.

A **flex bend sensor** is a type of variable resistor that changes its resistance when bent. The more the sensor bends, the higher the resistance, which can be read as an analog voltage. Since the Raspberry Pi lacks an analog input, we use an **ADS1115 Analog-to-Digital Converter (ADC)** to read the values.

---

## 🔧 Materials & Equipment Checklist

- Raspberry Pi (Model 4 or any variant with Raspberry Pi OS installed)
- ADS1115 Analog-to-Digital Converter module
- Flex Bend Sensor
- 10kΩ Resistor (for voltage divider circuit)
- Jumper wires
- Breadboard (optional but recommended)

**Tip:** Ensure your Raspberry Pi is powered and set up before beginning.

---

## 🛠 Step-by-Step Instructions

### **Step 1: Understanding the Flex Bend Sensor**

- A flex sensor is a variable resistor that changes its resistance when bent.
- It works as a **voltage divider** in a circuit.
- As the sensor bends, its resistance increases, altering the voltage output.
- This output is read by an ADC and interpreted by the Raspberry Pi.

### **Step 2: Wiring the Flex Sensor to the ADS1115**

1. **Create a voltage divider circuit:**
   - Connect one end of the flex sensor to **3.3V** on the Raspberry Pi.
   - Connect the other end to **A0** on ADS1115.
   - Place a **10kΩ resistor** between A0 and **GND**.

2. **Connect ADS1115 to Raspberry Pi:**
   - VCC → 3.3V
   - GND → GND
   - SDA → GPIO2 (Pin 3)
   - SCL → GPIO3 (Pin 5)

**Tip:** Enable I2C on Raspberry Pi using `sudo raspi-config` → Interfacing Options → I2C → Enable.

### **Step 3: Writing the Python Code**

```python
import Adafruit_ADS1x15
import time

# Initialize ADC
gain = 1  # Set gain for ADS1115
adc = Adafruit_ADS1x15.ADS1115()

print("Reading Flex Sensor Values...")

while True:
    value = adc.read_adc(0, gain=gain)  # Read A0 pin
    voltage = (value / 32767.0) * 3.3  # Convert to voltage
    print(f"Raw Value: {value}, Voltage: {voltage:.2f}V")
    time.sleep(0.5)
```

### **Step 4: Running the Code**

1. Save the script as `flex_sensor.py`.
2. Run the script using:
   ```bash
   python3 flex_sensor.py
   ```
3. Observe the sensor values change as you bend the sensor.

### **Step 5: Experiment & Analyze**

- Try different bending angles and observe how the output changes.
- Use the data to control an LED, servo motor, or log it for further analysis.
- Modify the script to store readings over time for graphing.

---

## 🤖 Concepts (Simplified)

### **What is a Flex Sensor?**
A sensor that changes resistance when bent, used in robotics, wearables, and motion tracking.

### **Why Use an ADC?**
Raspberry Pi cannot read analog signals directly, so we use an ADS1115 to convert the sensor's output into digital values.

### **Common Applications of Flex Sensors**
- Motion detection (e.g., gloves for sign language translation)
- Wearable devices
- Robotics and prosthetics

---

## 📝 Activity Reflection & Questions

1. **Flex Sensor Behavior:** How does the resistance of a flex sensor change when bent?
2. **Voltage Divider:** Why do we need a resistor in series with the flex sensor?
3. **I2C Communication:** What role does ADS1115 play in reading sensor values?

---

## 🧠 Mini Quiz (Test Your Understanding!)

1. What happens to the resistance of a flex sensor when it is bent?
   a) It increases
   b) It decreases
   c) It remains the same

2. Why do we need an ADS1115 for the flex sensor?
   a) Raspberry Pi has built-in analog inputs
   b) Raspberry Pi cannot read analog signals directly
   c) It is used for wireless communication

3. What is the function of a voltage divider in the flex sensor circuit?
   a) To increase the sensor's resistance
   b) To convert analog signals into digital ones
   c) To provide a readable voltage output for the ADC

**Answer Key:** 1 – a, 2 – b, 3 – c

---

## 🚀 Challenges (Push Your Limits!)

1. **Challenge 1:** Connect multiple flex sensors and read values from different channels.
2. **Challenge 2:** Modify the script to trigger an LED when the sensor bends beyond a threshold.
3. **Challenge 3:** Record sensor data and create a simple graph using Matplotlib.

---

## 📖 Additional Resources

- **Raspberry Pi Documentation (I2C & ADS1115)**
- **Flex Sensor Datasheet**
- **Python for Raspberry Pi (Official Guide)**

**Tip:** Understanding flex sensors opens doors to exciting projects in wearable tech, gaming, and robotics!

