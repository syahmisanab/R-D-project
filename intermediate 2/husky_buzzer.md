# 🎵 Tag-Based Melody Player with HuskyLens and Raspberry Pi

## 🎯 Learning Objectives
By the end of this lesson, students will:

1. Understand how to interface a HuskyLens AI Camera with a Raspberry Pi using I2C.
2. Learn how to detect tags using HuskyLens and trigger different melodies.
3. Gain experience working with GPIO to control a buzzer for sound output.
4. Develop confidence in integrating computer vision with physical computing projects.

---

## 🔎 Project Overview

**Lesson Title:** "Tag-Controlled Melody Player with HuskyLens"  
**Duration:** 45–60 minutes  
**Goal:** Create an interactive music box that plays different melodies when specific tags are detected.

In this project, students will use a **HuskyLens AI Camera** to recognize tags. When a tag is detected, a Raspberry Pi will trigger a corresponding melody on a buzzer. This project combines AI-powered object recognition, GPIO control, and sound generation to create a simple yet engaging interactive system.

---

## 🔧 Materials & Equipment Checklist

1. Raspberry Pi (any model with I2C support)
2. HuskyLens AI Camera
3. I2C connection cables
4. Buzzer (Piezo or active buzzer module)
5. Jumper wires
6. Tags pre-learned on HuskyLens
7. Breadboard (optional for easy wiring)

**Tip:** Before starting, ensure your HuskyLens is set to **Tag Recognition mode** and pre-learn at least two tags.

---

## 🛠 Step-by-Step Instructions

### **Step 1: Wiring the Components**

#### **Connect HuskyLens to Raspberry Pi via I2C:**
- **HuskyLens VCC** → **Raspberry Pi 3.3V**
- **HuskyLens GND** → **Raspberry Pi GND**
- **HuskyLens SDA** → **Raspberry Pi SDA (GPIO2, Pin 3)**
- **HuskyLens SCL** → **Raspberry Pi SCL (GPIO3, Pin 5)**

#### **Connect Buzzer to Raspberry Pi:**
- **Buzzer Positive (+)** → **GPIO17 (Pin 11)**
- **Buzzer Negative (-)** → **GND**

**Tip:** Use `i2cdetect -y 1` in the terminal to verify HuskyLens is detected before proceeding with the code.

---

### **Step 2: Installing Required Libraries**

Run the following commands in the Raspberry Pi terminal to install necessary libraries:

```bash
pip install huskylib RPi.GPIO
```

Ensure `I2C` is enabled using:

```bash
sudo raspi-config
```
Navigate to **Interfacing Options > I2C > Enable**

---

### **Step 3: Writing the Python Code**

```python
import time
import board
import busio
import RPi.GPIO as GPIO
from huskylib import HuskyLensLibrary

# Initialize HuskyLens on I2C
hl = HuskyLensLibrary("I2C", address=0x32)

# Set up buzzer
buzzer_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define melodies for each tag
melodies = {
    1: [261, 293, 329, 349],  # Melody for Tag 1
    2: [392, 440, 493, 523]   # Melody for Tag 2
}

def buzz(frequency, duration):
    if frequency == 0:
        time.sleep(duration)
        return
    period = 1.0 / frequency
    delay = period / 2
    cycles = int(duration * frequency)
    for _ in range(cycles):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(delay)

def play_melody(melody):
    for note in melody:
        buzz(note, 0.2)
        time.sleep(0.05)

while True:
    try:
        results = hl.learnedBlocks()
        if results:
            tag_id = results[0].ID
            print(f"Detected Tag ID: {tag_id}")
            if tag_id in melodies:
                play_melody(melodies[tag_id])
            else:
                print("No melody assigned to this tag.")
        else:
            print("No tags detected.")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.5)
```

---

### **Step 4: Training the HuskyLens to Recognize New Tags**

1. Set HuskyLens to **Tag Recognition Mode**.
2. Hold a new tag in front of the camera.
3. Press the **learning button** on HuskyLens to register the tag.
4. Assign a melody to the new tag in the Python script.

**Tip:** Label each tag with its assigned melody to keep track easily.

---

### **Step 5: Running the Program**

1. Save the script as `tag_melody.py`
2. Run the script using:
   ```bash
   python3 tag_melody.py
   ```
3. Place a tag in front of HuskyLens and observe the buzzer playing the assigned melody!

**Tip:** If the buzzer isn’t producing sound, double-check the wiring and ensure the tag is correctly recognized by HuskyLens.

---

## 🤖 Discussion & Key Takeaways

1. **How does HuskyLens detect tags?**
   - HuskyLens uses its built-in Tag Recognition algorithm to detect and classify tags.
2. **Why do we use I2C instead of UART for HuskyLens?**
   - I2C allows multiple devices to communicate on the same bus, making it easier to integrate with Raspberry Pi.
3. **How does the buzzer produce different tones?**
   - The buzzer's frequency determines the pitch of the sound, allowing us to create melodies.

---

## 🔥 Bonus Challenge

- Modify the script to add more tags and melodies.
- Use a **servo motor** instead of a buzzer to create a simple access control system.
- Display tag names on an **OLED screen** when detected.

---

## 📖 Additional Resources

- [HuskyLens Official Documentation](https://www.dfrobot.com/product-1922.html)
- [RPi.GPIO Library](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
- [I2C on Raspberry Pi](https://www.raspberrypi.org/documentation/hardware/raspberrypi/i2c/README.md)

---

## 🎥 Video Demonstration

*Add video here*

Let me know if you need any modifications! 🚀

