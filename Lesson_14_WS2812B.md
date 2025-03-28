# 📚 LESSON 14: Controlling a WS2812B LED Strip  

## 🎯 Learning Objectives  
By the end of this lesson, you will:  
✅ Understand how a **WS2812B (NeoPixel) LED strip** works.  
✅ Learn how to interface the LED strip with **Raspberry Pi using the OiviO Pi Extension Board**.  
✅ Write a **Python script** to control the LED strip.  

---

## 🛠️ Materials & Equipment Checklist  
- ✅ **Raspberry Pi**  
- ✅ **OiviO Pi Extension Board**  
- ✅ **WS2812B LED Strip (NeoPixel)**  
- ✅ **Power supply for Raspberry Pi**  
- ✅ **Monitor, keyboard, and mouse (for setup)**  

---

## 🛠️ Components & Setup  

### **Pin Configuration (WS2812B Data Pin)**  

| **Component**  | **Raspberry Pi GPIO (OiviO Pi Extension Board)** |
|---------------|-----------------------------------|
| **WS2812B Data**  | **GPIO 18 (PWM0) - Pin 12**  |
| **Power (5V)** | **5V - Pin 2 or Pin 4**  |
| **Ground (GND)** | **GND - Pin 6**  |

🔗 **Technical Sheet & Pin Reference:** [OiviO Pi Technical Sheet]  

---

## 🔍 Concept: How WS2812B Works  

The **WS2812B LED strip**, also known as **NeoPixel**, is a type of addressable RGB LED strip. Each LED can be controlled individually using a **single data pin**.  

✅ **How It Works:**  
- Each LED has a **tiny microcontroller** inside that controls its color.  
- The Raspberry Pi sends color data to the first LED, which then passes the data to the next one, and so on.  
- We use the **Adafruit NeoPixel library** to control the LEDs with Python.  

✅ **Why Use WS2812B?**  
✔ Only **one GPIO pin** is needed for multiple LEDs.  
✔ Supports **cool lighting effects** like color waves, rainbow cycles, and animations.  
✔ Each LED can have **independent brightness and color settings**.  

---

## 🚀 Step-by-Step Guide  

### **Step 1: Install Required Libraries**  
Before running the code, install the **Adafruit NeoPixel library**:  

```bash
pip install adafruit-circuitpython-neopixel
```

---

### **Step 2: Write the Python Code**  

📜 **Save the following script as** `neopixel.py`:  

---

### **1️⃣ Import Necessary Libraries**  
```python
import time
import board
import neopixel
```
✅ **time**: Used for adding delays between color changes.  
✅ **board**: Helps define the Raspberry Pi's GPIO pins.  
✅ **neopixel**: The library that controls the LED strip.  

---

### **2️⃣ LED Strip Configuration**  
```python
LED_PIN = board.D18  # GPIO 18 (OiviO Pi Extension Board)
NUM_LEDS = 8         # Change this to the number of LEDs in your strip
BRIGHTNESS = 0.5     # Brightness level (0.0 - 1.0)
ORDER = neopixel.GRB # Color order for WS2812B
```
✅ **LED_PIN**: The GPIO pin used to send data to the LED strip (**GPIO 18 - Pin 12**).  
✅ **NUM_LEDS**: The number of LEDs in the strip (change if needed).  
✅ **BRIGHTNESS**: Controls the brightness level of the LEDs. A value of `1.0` is full brightness.  
✅ **ORDER**: Defines the color sequence (**GRB is standard for WS2812B**).  

---

### **3️⃣ Initialize the LED Strip**  
```python
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER)
```
✅ This creates a **NeoPixel object** that allows us to control the LEDs.  
✅ `auto_write=False` means we need to call `pixels.show()` to update the LEDs.  

---

### **4️⃣ Define a Function to Cycle Colors**  
```python
def color_cycle(wait=0.5):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
    for color in colors:
        pixels.fill(color)
        pixels.show()
        time.sleep(wait)
```
✅ The function cycles through **red, green, and blue** colors.  
✅ `pixels.fill(color)`: Fills the entire LED strip with the selected color.  
✅ `pixels.show()`: Updates the LEDs to display the new color.  
✅ `time.sleep(wait)`: Adds a short delay before changing to the next color.  

---

### **5️⃣ Main Loop to Run the Animation**  
```python
try:
    while True:
        color_cycle()
```
✅ **while True** keeps the script running indefinitely.  
✅ Calls `color_cycle()` repeatedly to create a looping animation.  

---

### **6️⃣ Graceful Exit on Keyboard Interrupt**  
```python
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))  # Turn off LEDs on exit
    pixels.show()
    print("
LEDs turned off. Exiting...")
```
✅ If the user **presses Ctrl+C**, this ensures:  
✔ The **LEDs turn off**.  
✔ The **program exits cleanly** with a message.  

---

### **Step 3: Run the Code**  

1️⃣ Open the terminal and navigate to your script folder:  
   ```bash
   cd /path/to/your/script/
   ```  
2️⃣ Run the script with **sudo** (required for GPIO access):  
   ```bash
   sudo python3 neopixel.py
   ```  
3️⃣ Press **Ctrl+C** to stop the script. The LEDs will **turn off automatically**.  
