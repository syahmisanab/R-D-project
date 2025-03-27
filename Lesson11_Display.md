# 🎯 Lesson 11: Displaying Numbers on a 4-Digit 7-Segment Display  

## **Learning Objectives**  
- Understand how a **4-digit 7-segment display** works.  
- Learn how to interface the **HT16K33-based display** with a Raspberry Pi using I2C.  
- Write a Python script to **display a fixed number ("1234")**.  

---

## 🛠️ Materials & Equipment Checklist  
- Raspberry Pi  
- **OiviO Pi Extension Board** (No wiring needed)  
- **4-digit 7-segment display (HT16K33 driver)**  
- Power supply for Raspberry Pi  
- Monitor, keyboard, and mouse (for setup)  

---

## 🔍 Concept: How a 4-Digit 7-Segment Display Works  
A **7-segment display** consists of **LED segments** arranged to form numbers. By turning different segments **ON** or **OFF**, we can display numbers and some letters.  

### **How It Works:**  
✅ The **HT16K33 driver chip** simplifies control using **I2C (Inter-Integrated Circuit)**.  
✅ **No need for complex GPIO wiring**—we only use **SDA (GPIO 2) and SCL (GPIO 3)** for communication.  
✅ We send data to the display in **4-digit format** (e.g., "1234").  

---

## 🛠️ Components & Setup  
### **Pin Configuration (I2C Bus)**  
| Component  | Raspberry Pi GPIO |
|------------|------------------|
| SDA (Data) | GPIO 2           |
| SCL (Clock) | GPIO 3           |

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
   nano display_number.py
   ```  

---

### **Step 2: Write the Python Code**  

#### **1. Import Necessary Libraries**  
```python
import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4
```
✅ **busio** manages I2C communication.  
✅ **Seg7x4** from Adafruit allows us to control the 7-segment display.  

---

#### **2. Initialize I2C Communication and Display**  
```python
# Initialize I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the 4-digit 7-segment display
display = Seg7x4(i2c)
```
✅ The **HT16K33 driver** is set up using I2C on the Raspberry Pi.  

---

#### **3. Display the Number "1234"**  
```python
# Display the number "1234"
display.print("1234")

# Keep the display ON for 10 seconds
time.sleep(10)

# Clear the display before exiting
display.fill(0)
```
✅ The **print() function** sends "1234" to the display.  
✅ The **fill(0)** function clears the display when the script ends.  

---

### **Step 3: Save & Run the Script**  
1️⃣ **Save the file in nano:**  
   - Press **CTRL + X**  
   - Press **Y** to confirm saving  
   - Press **Enter**  

2️⃣ **Run the script:**  
   ```bash
   python3 display_number.py
   ```  
3️⃣ The display should show **"1234"** for **10 seconds** before turning off.  

---

## 📝 Exercises  

### **Exercise 1: Display a Custom Number**  
Modify the script to **display "5678"** instead of "1234".  

### **Exercise 2: Countdown from 9999 to 0000**  
Modify the script to **count down from 9999 to 0000**, with a **1-second delay per step**.  

### **Exercise 3: Interactive Number Update**  
Use a **button (GPIO 17)** to **increase the displayed number** by **1** each time the button is pressed.  

### **Exercise 4: Display Sensor Values**  
Use a **temperature sensor** and display the **current temperature** on the 7-segment display.  

---

## ❓ Quiz  

1️⃣ **Which communication protocol does the HT16K33 driver use?**  
   A) SPI  
   B) UART  
   C) I2C  
   D) PWM  
   ✅ Answer: **C) I2C**  

2️⃣ **Which function is used to display a number on the 7-segment display?**  
   A) `display.show()`  
   B) `display.write()`  
   C) `display.print()`  
   D) `display.display()`  
   ✅ Answer: **C) display.print()**  

3️⃣ **What happens if we don’t call `fill(0)` at the end of the script?**  
   A) The display will clear automatically  
   B) The last number will remain displayed  
   C) The Raspberry Pi will restart  
   D) The display will blink  
   ✅ Answer: **B) The last number will remain displayed**  

---

## 🤔 **Activity Reflection & Questions**  
- How can we modify the script to **show different numbers**?  
- How can we make the numbers **change dynamically**?  
- How can we use **buttons or sensors** to update the display?  

---

## 🚀 **Challenges (Push Your Limits!)**  

### **Challenge 1: Stopwatch Display**  
Use a **button** to start and stop a **count-up timer** on the display.  

### **Challenge 2: Real-Time Clock Display**  
Modify the script to **show the current time (HHMM format)** using Python’s **datetime module**.  

### **Challenge 3: Sensor-Based Alert System**  
Use a **motion sensor** to display "**ALRT**" when movement is detected.  

---

## 📖 **Additional Resources**  
1️⃣ Official Raspberry Pi Projects:  
🔗 [https://projects.raspberrypi.org/en](https://projects.raspberrypi.org/en)  
