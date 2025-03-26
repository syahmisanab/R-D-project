## Lesson 9: Controlling a Vibration Motor with Raspberry Pi

### 🎯 Learning Objectives
- Understand how a vibration motor works.
- Learn how to control a vibration motor using Raspberry Pi.
- Write a Python script to activate and deactivate a vibration motor using gpiozero.

---

### 🛠️ Materials & Equipment Checklist
- Raspberry Pi (any model, including Raspberry Pi 5)
- OiviO Pi Extension Board (No wiring needed)
- Vibration Motor (DC motor type)
- Power supply for Raspberry Pi
- Monitor, keyboard, and mouse (for setup)

---

### 🔍 Concept: How a Vibration Motor Works
A **vibration motor** is a small motor that produces vibrations instead of rotational motion. These motors are commonly used in mobile phones, game controllers, and alert systems.

- The Raspberry Pi cannot power the motor directly, so we use the **OiviO Pi Extension Board**, which provides an easy way to control it.
- We control the motor using a **GPIO pin**, turning it **ON** and **OFF** using Python.

---

### 🛠️ Components & Setup
**Pin Configuration:**  
- Vibration Motor → **GPIO 15**  

🔗 **Technical Sheet & Pin Reference:** OiviO Pi Technical Sheet  

---

## 🚀 Step-by-Step Guide
### Step 1: Open the Terminal & Create a Python File
1. Open the terminal on your Raspberry Pi.  
2. Navigate to your preferred directory:  
   ```bash
   cd ~
   ```  
3. Create a new Python script:  
   ```bash
   nano vibration_motor.py
   ```

---

### Step 2: Write the Python Code
#### 1. Import necessary libraries
```python
from gpiozero import OutputDevice
import time
```
✅ `OutputDevice` from `gpiozero` allows us to control the vibration motor.  
✅ `time.sleep()` is used to manage how long the motor stays on.  

---

#### 2. Define the Vibration Motor Pin
```python
vibration_motor = OutputDevice(15)
```
✅ Sets GPIO **15** as the output pin for the vibration motor.  

---

#### 3. Activate the Vibration Motor
```python
vibration_motor.on()
time.sleep(5)
vibration_motor.off()
```
✅ **Turns the motor ON for 5 seconds, then OFF.**  
✅ The **sleep() function** keeps the motor running for a specific time.  

---

### Step 3: Save & Run the Script
1. Save the file in nano:  
   - Press `CTRL + X`  
   - Press `Y` to confirm saving  
   - Press `Enter`  

2. Run the script:  
   ```bash
   python3 vibration_motor.py
   ```  

3. **Observe the vibration motor running for 5 seconds before stopping.**  

---

## 📝 Exercises
### Exercise 1: Short Pulses of Vibration
🔧 **Modify the script to make the vibration motor pulse ON and OFF every second, five times.**  

### Exercise 2: Vibration on Button Press
🔧 **Use a button (GPIO 17) to activate the vibration motor only when pressed.**  

### Exercise 3: Vibration with Motion Detection
🔧 **Combine a PIR motion sensor (GPIO 27) with the vibration motor so it vibrates when motion is detected.**  

---

## ❓ Quiz
1️⃣ **Which GPIO pin is used to control the vibration motor in our lesson?**  
   A) 17  
   B) 18  
   C) 15  
   D) 27  
   ✅ **Answer:** C) 15  

2️⃣ **What function is used to turn ON the vibration motor?**  
   A) motor.start()  
   B) motor.activate()  
   C) motor.on()  
   D) motor.begin()  
   ✅ **Answer:** C) motor.on()  

3️⃣ **What happens if we remove the sleep() function in the script?**  
   A) The motor will never turn off  
   B) The motor will turn off immediately  
   C) The Raspberry Pi will restart  
   D) The motor will run for 5 seconds  
   ✅ **Answer:** A) The motor will never turn off  

---

### 🤔 Activity Reflection & Questions
- How can we modify the script to change the vibration duration?  
- How can we use this in a real-world project (e.g., alerts, alarms, notifications)?  
- What other components can be combined with a vibration motor for interactive projects?  
