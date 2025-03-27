# 📝 Lesson 12: Creating Patterns on an LED Matrix (MAX7219)  

## 🎯 Learning Objectives  
- Understand how an **8x8 LED matrix (MAX7219)** works.  
- Learn how to control the matrix using the **luma.led_matrix** library.  
- Display patterns like a cross, checkerboard, and spiral using Python.  

---

## 🛠️ Materials & Equipment Checklist  
- **Raspberry Pi**  
- **OiviO Pi Extension Board**  
- **MAX7219 8x8 LED Matrix Module**  
- **Power supply for Raspberry Pi**  
- **Monitor, keyboard, and mouse (for setup)**  

---

## 🔍 Concept: How an 8x8 LED Matrix Works  

An **LED matrix** consists of **64 LEDs** (8 rows × 8 columns). The **MAX7219** driver simplifies the control of individual LEDs using SPI (Serial Peripheral Interface).  

### How It Works:  
✅ The MAX7219 uses **SPI communication** (MOSI, SCLK, CS) to send data.  
✅ We send **ON/OFF commands** to each LED by addressing their positions.  
✅ By updating LEDs in a loop, we can create **scrolling text, animations, and patterns**.  

---

## 🛠️ Components & Setup  

### Pin Configuration (SPI Bus)  

| Component | Raspberry Pi GPIO |  
|-----------|------------------|  
| **DIN (MOSI)** | GPIO 10 |  
| **CS (Chip Select)** | GPIO 8 |  
| **CLK (Clock)** | GPIO 11 |  
| **GND** | GND |  
| **VCC** | 5V |  

🔗 **Technical Sheet & Pin Reference**: OiviO Pi Technical Sheet  

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
   nano led_matrix_patterns.py
   ```  

---

### **Step 2: Install Required Libraries**  
To control the MAX7219, we use the **luma.led_matrix** library. If you haven’t installed it, run:  
```bash
pip install luma.led_matrix
```  

---

### **Step 3: Write the Python Code**  

#### **1️⃣ Import Required Libraries**  
```python
#!/usr/bin/env python3
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time
```
✅ `max7219`: Controls the LED matrix.  
✅ `canvas`: Allows drawing on the LED matrix.  
✅ `spi, noop`: Handles SPI communication.  

---

#### **2️⃣ Initialize the LED Matrix**  
```python
# Initialize SPI communication
serial = spi(port=0, device=0, gpio=noop())

# Initialize the MAX7219 device (1 module, rotated 180°)
device = max7219(serial, cascaded=1, rotate=2)
```
✅ **SPI** (Serial Peripheral Interface) is used to communicate with the MAX7219.  
✅ `rotate=2` rotates the display for correct orientation.  

---

#### **3️⃣ Display a Simple Pattern (Corners + Center Pixel)**  
```python
def draw_specific_pixels():
    """Draw specific pixels on the matrix"""
    with canvas(device) as draw:
        draw.point((0, 0), fill="white")  # Top-left corner
        draw.point((7, 0), fill="white")  # Top-right corner
        draw.point((0, 7), fill="white")  # Bottom-left corner
        draw.point((7, 7), fill="white")  # Bottom-right corner
        draw.point((3, 3), fill="white")  # Center
    time.sleep(2)
```
✅ Uses `draw.point()` to turn **specific LEDs** ON.  

---

#### **4️⃣ Create a Cross Pattern**  
```python
def draw_cross():
    """Draw a cross on the matrix"""
    with canvas(device) as draw:
        # Horizontal line
        for x in range(8):
            draw.point((x, 3), fill="white")

        # Vertical line
        for y in range(8):
            draw.point((3, y), fill="white")
    time.sleep(2)
```
✅ Draws a **cross shape (X + Y center lines)** using loops.  

---

#### **5️⃣ Control LED Brightness**  
```python
def intensity_control():
    """Demonstrate intensity control"""
    print("Lowest intensity")
    device.contrast(1)  # Very low intensity
    with canvas(device) as draw:
        draw.rectangle((0, 0, 7, 7), fill="white")
    time.sleep(2)

    print("Medium intensity")
    device.contrast(128)  # Medium intensity
    with canvas(device) as draw:
        draw.rectangle((0, 0, 7, 7), fill="white")
    time.sleep(2)

    print("Highest intensity")
    device.contrast(255)  # Highest intensity
    with canvas(device) as draw:
        draw.rectangle((0, 0, 7, 7), fill="white")
    time.sleep(2)
```
✅ `device.contrast(value)` adjusts brightness (1 = dim, 255 = bright).  

---

#### **6️⃣ Run the Patterns Continuously**  
```python
def main():
    try:
        print("Drawing specific pixels...")
        draw_specific_pixels()

        print("Drawing cross...")
        draw_cross()

        print("Intensity control...")
        intensity_control()

    except KeyboardInterrupt:
        print("\nProgram stopped.")
    finally:
        # Clear the display
        with canvas(device) as draw:
            draw.rectangle((0, 0, 7, 7), fill="black")

if __name__ == '__main__':
    main()
```
✅ Runs each pattern in sequence.  
✅ Press **CTRL + C** to stop the script safely.  

---

## 📖 Additional Resources  
1. **Luma.LED_Matrix Documentation**: [https://luma-led-matrix.readthedocs.io](https://luma-led-matrix.readthedocs.io)  
2. **Official Raspberry Pi Projects**: [https://projects.raspberrypi.org/en](https://projects.raspberrypi.org/en)  
