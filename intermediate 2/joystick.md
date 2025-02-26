# 🕹️ Joystick Module with Raspberry Pi

## 🎯 Learning Objectives
By completing this lesson, students will:

1. Understand how a joystick module works and how it provides both analog and digital signals.
2. Learn how to interface a joystick with a Raspberry Pi using an ADC (ADS1115) for analog readings.
3. Read and interpret joystick movement data to control outputs such as servos or game functions.
4. Develop confidence in working with both digital and analog inputs on Raspberry Pi.

---

## 🔎 Project Overview

**Lesson Title:** "Interfacing a Joystick Module with Raspberry Pi"
**Duration:** 30–45 minutes
**Goal:** Learn how to use a joystick module with Raspberry Pi to detect movement and button presses.

Joysticks are commonly used in gaming and robotics. They consist of two potentiometers (one for X-axis and one for Y-axis) and a button. Since Raspberry Pi lacks analog input pins, an external ADC (ADS1115) is required to read the joystick’s position.

---

## 🔧 Materials & Equipment Checklist

1. Raspberry Pi (Model 4 or any variant with Raspberry Pi OS installed)
2. ADS1115 Analog-to-Digital Converter module
3. Joystick module (XY joystick with a push button)
4. Jumper wires
5. Breadboard (optional but recommended)
6. Python installed on Raspberry Pi

**Tip:** Ensure your Raspberry Pi is powered and set up before beginning.

---

## 🛠 Step-by-Step Instructions

### **Step 1: Understanding the Joystick Module**

1. **X-axis and Y-axis:**
   - The joystick has two potentiometers for X and Y movement.
   - Each potentiometer provides an **analog** voltage output, requiring an ADC.

2. **Push Button:**
   - Pressing the joystick down activates a built-in **digital switch**.
   - This button can be read directly by a Raspberry Pi GPIO pin.

---

### **Step 2: Wiring the Joystick to Raspberry Pi (via ADS1115)**

#### **Joystick Pins:**
- **VCC** → 3.3V (Raspberry Pi)
- **GND** → GND (Raspberry Pi)
- **VRX (X-axis)** → A0 (ADS1115)
- **VRY (Y-axis)** → A1 (ADS1115)
- **SW (Button)** → Any GPIO pin (e.g., GPIO17 / Pin 11)

#### **ADS1115 to Raspberry Pi:**
- **VCC** → 3.3V
- **GND** → GND
- **SDA** → GPIO2 (Pin 3)
- **SCL** → GPIO3 (Pin 5)

**Tip:** Ensure I2C is enabled on your Raspberry Pi (`sudo raspi-config` → Interfacing Options → I2C → Enable).

---

### **Step 3: Reading Joystick Data in Python**

```python
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# Initialize I2C and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
x_axis = AnalogIn(ads, ADS.P0)
y_axis = AnalogIn(ads, ADS.P1)

# Button setup
button_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    x_val = x_axis.value  # Read X-axis
    y_val = y_axis.value  # Read Y-axis
    button = GPIO.input(button_pin)  # Read button state
    
    print(f'X: {x_val}, Y: {y_val}, Button: {"Pressed" if button == 0 else "Not Pressed"}')
    time.sleep(0.1)
```

---

### **Step 4: Understanding the Output**

1. The joystick's X and Y positions will return values between **0 and 65535** (16-bit resolution from ADS1115).
2. The center position should be around **32767**.
3. Moving the joystick fully left/right or up/down will change the values accordingly.
4. The button state will be **0 (Pressed)** or **1 (Not Pressed)**.

---

## 🤖 Concepts (Simplified)

1. **How a Joystick Works**
   - Two potentiometers measure movement along X and Y axes.
   - A push button provides a digital on/off signal.

2. **Why We Need ADS1115**
   - Raspberry Pi lacks analog input pins, so an ADC is required to read joystick movement.

3. **Common Uses for Joysticks**
   - Controlling robots, games, and servos.
   - Navigating menus in embedded systems.

---

## 📝 Activity Reflection & Questions

1. **How does a joystick provide position data?**
2. **Why do we need an ADC to read the joystick movement?**
3. **What happens when you press the joystick button?**

---

## 🧠 Mini Quiz (Test Your Understanding!)

1. What type of signal does a joystick’s movement generate?
   a) Digital
   b) Analog
   c) Binary

2. Why do we need an ADS1115 to use a joystick with Raspberry Pi?
   a) To convert analog signals to digital
   b) To add more GPIO pins
   c) To power the joystick

3. What happens when you press the joystick button?
   a) It generates an analog voltage
   b) It sends a digital signal (0 or 1)
   c) It changes joystick movement

**Answer Key:** 1 – b, 2 – a, 3 – b

---

## 🚀 Challenges (Push Your Limits!)

1. **Challenge 1:** Use the joystick to control an LED’s brightness (via PWM) based on X-axis movement.
2. **Challenge 2:** Move a servo motor using the joystick’s position.
3. **Challenge 3:** Use the joystick to navigate a simple game on Raspberry Pi.

---

## 📖 Additional Resources

- **ADS1115 Datasheet**
- **Raspberry Pi GPIO Documentation**
- **Joystick Interfacing Tutorials (YouTube, Blogs)**

**Tip:** Learning how to use a joystick will help in robotics, game development, and interactive projects!

---

Let me know if you need any modifications or more details! 🚀

