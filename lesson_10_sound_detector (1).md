## Lesson 10: Using a Sound Detector Sensor with Raspberry Pi

### 🎯 Learning Objectives
- Understand how a **sound detector sensor** works.
- Learn how to **detect sound** using a Raspberry Pi.
- Implement a **Python script** to monitor and respond to sound.

---

### 🛠️ Materials & Equipment Checklist
- **Raspberry Pi** (any model, including Raspberry Pi 5)
- **OiviO Pi Extension Board** (No wiring needed)
- **Sound Detector Sensor** (Microphone-based)
- **Power supply for Raspberry Pi**
- **Monitor, keyboard, and mouse** (for setup)

---

### 🔍 Concept: How a Sound Detector Sensor Works
A **sound detector sensor** detects **noise or sudden sound changes** in the environment. It is useful for:
✅ **Noise level monitoring**
✅ **Security alarms**
✅ **Smart home automation**

#### **How It Works**
- The sensor has a built-in **microphone** that detects sound waves.
- If the **sound level exceeds a threshold**, it triggers a **HIGH signal** (GPIO goes HIGH).
- We use **gpiozero’s `Button` class** to detect this change as a **digital input**.

---

### 🛠️ Components & Setup
**Pin Configuration:**
- **Sound Detector Sensor** → **GPIO 26**

🔗 **Technical Sheet & Pin Reference:** OiviO Pi Technical Sheet

---

## 🚀 Step-by-Step Guide
### **Step 1: Open the Terminal & Create a Python File**
1️⃣ Open the terminal on your Raspberry Pi.
2️⃣ Navigate to your preferred directory:
   ```bash
   cd ~
   ```
3️⃣ Create a new Python script:
   ```bash
   nano sound_detector.py
   ```

---

### **Step 2: Write the Python Code**
#### **1. Import necessary libraries**
```python
from gpiozero import Button
import time
```
✅ `Button` from **gpiozero** is used to detect the sensor’s digital HIGH/LOW state.
✅ `time.sleep()` controls the detection speed.

---

#### **2. Define the Sound Sensor Pin**
```python
SOUND_PIN = 26
sound_sensor = Button(SOUND_PIN, pull_up=False)
```
✅ Sets **GPIO 26** as the input pin for the sound detector sensor.
✅ `pull_up=False` ensures correct signal detection.

---

#### **3. Create a Loop to Detect Sound**
```python
try:
    while True:
        if sound_sensor.is_pressed:
            print("🔊 Sound Detected!")          
        time.sleep(0.1)  # Reduced sleep for faster response
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
```
✅ **Detects sound** and prints `"🔊 Sound Detected!"` when a noise is detected.
✅ **Stops the script safely** when interrupted (`CTRL + C`).

---

### **Step 3: Save & Run the Script**
1️⃣ Save the file in nano:
   - Press `CTRL + X`
   - Press `Y` to confirm saving
   - Press `Enter`

2️⃣ Run the script:
   ```bash
   python3 sound_detector.py
   ```

3️⃣ **Make a noise (clap, snap fingers) to trigger the detection!**

---

## 📝 **Exercises**
### **Exercise 1: LED Alert on Sound Detection**
🔧 **Modify the script to turn ON an LED (GPIO 17) when sound is detected.**

### **Exercise 2: Sound-Activated Buzzer**
🔧 **Connect a buzzer (GPIO 18) to sound an alarm when sound is detected.**

### **Exercise 3: Logging Sound Events**
🔧 **Modify the script to log the time and date when sound is detected into a file (`sound_log.txt`).**

---

## ❓ **Quiz**
1️⃣ **Which GPIO pin is used for the sound detector sensor in our lesson?**  
   A) 17  
   B) 18  
   C) 26  
   D) 27  
   ✅ **Answer:** C) 26  

2️⃣ **Which gpiozero class is used to read the sound sensor?**  
   A) SoundDetector()  
   B) MotionSensor()  
   C) Button()  
   D) InputDevice()  
   ✅ **Answer:** C) Button()  

3️⃣ **What happens if we set `pull_up=True` instead of `False`?**  
   A) The sensor might not detect sound correctly  
   B) The script will crash  
   C) The sensor will always detect sound  
   D) The Raspberry Pi will restart  
   ✅ **Answer:** A) The sensor might not detect sound correctly  

---

### **🤔 Activity Reflection & Questions**
- How can we adjust sensitivity to detect softer sounds?  
- How can we use this for **security alarms** or **smart home systems**?  
- What other sensors can be **combined** with sound detection?  

---

🚀 **Next Steps:** Try modifying the script to trigger different actions based on sound detection!  
