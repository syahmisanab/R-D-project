# Lesson 13: Displaying Text on an LCD 1602

## 🎯 Learning Objectives
- Understand how an LCD 1602 (16x2 character display) works.
- Learn how to interface the LCD with Raspberry Pi using I2C communication.
- Write a Python script to display text on the LCD screen.

## 🛠️ Materials & Equipment Checklist
- Raspberry Pi
- OiviO Pi Extension Board
- 1602 LCD with I2C module
- Power supply for Raspberry Pi
- Jumper wires
- Monitor, keyboard, and mouse (for setup)

---

## 🔍 Concept: How an LCD 1602 Works
The LCD 1602 is a **16x2 character display** that allows us to show text. It uses the **Hitachi HD44780** controller and can be controlled with an **I2C adapter**, which reduces the number of GPIO pins needed.

### ✅ How It Works
- I2C (**Inter-Integrated Circuit**) communication is used to send commands.
- The LCD has an **I2C address** (usually **0x27** or **0x3F**).
- We send **ASCII character codes** to display text.

---

## 🛠️ Components & Setup

### Pin Configuration (I2C Bus)
| Component | Raspberry Pi GPIO |
|-----------|-----------------|
| **SDA (Data)** | GPIO 2 (SDA) |
| **SCL (Clock)** | GPIO 3 (SCL) |

🔗 **Technical Sheet & Pin Reference:** [OiviO Pi Technical Sheet]

---

## 🚀 Step-by-Step Guide

### Step 1: Enable I2C on Raspberry Pi
```bash
sudo raspi-config
```
- Go to **Interfacing Options → I2C** and **Enable** it.
- Restart your Raspberry Pi:
```bash
sudo reboot
```

---

### Step 2: Check the I2C Address
```bash
sudo apt install -y i2c-tools
i2cdetect -y 1
```
- The LCD should appear as **0x27** or **0x3F**.

---

## Step 3: Write the Python Code

### 1️⃣ Import Required Libraries
```python
import time
import smbus2
import signal
```

### 2️⃣ Define I2C Address & Bus
```python
LCD_ADDR = 0x27  
bus = smbus2.SMBus(1)
```

### 3️⃣ LCD Command & Control Bits
```python
LCD_CHR = 1  # Data mode
LCD_CMD = 0  # Command mode
LCD_BACKLIGHT = 0x08  # Backlight ON
ENABLE = 0b00000100  # Enable bit
```

### 4️⃣ Function to Send Data to LCD
```python
def lcd_byte(bits, mode):
    high_bits = mode | (bits & 0xF0) | LCD_BACKLIGHT
    low_bits = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT
    bus.write_byte(LCD_ADDR, high_bits)
    bus.write_byte(LCD_ADDR, high_bits | ENABLE)
    time.sleep(0.0005)
    bus.write_byte(LCD_ADDR, high_bits & ~ENABLE)
    bus.write_byte(LCD_ADDR, low_bits)
    bus.write_byte(LCD_ADDR, low_bits | ENABLE)
    time.sleep(0.0005)
    bus.write_byte(LCD_ADDR, low_bits & ~ENABLE)
```

### 5️⃣ Initialize the LCD
```python
def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Display ON, Cursor OFF
    lcd_byte(0x28, LCD_CMD)  # 2-line mode, 5x8 font
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)
```

### 6️⃣ Function to Display Text on LCD
```python
def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)  # Move to first line
    for char in text:
        lcd_byte(ord(char), LCD_CHR)
```

### 7️⃣ Clearing the LCD
```python
def lcd_clear():
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)
```

### 8️⃣ Handling Ctrl+C (Keyboard Interrupt)
```python
def signal_handler(sig, frame):
    print("\nClearing LCD and exiting...")
    lcd_clear()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)
```

### 9️⃣ Running the Main Program
```python
if __name__ == "__main__":
    lcd_init()
    lcd_display("Autobotic")
    
    try:
        while True:
            time.sleep(1)  # Keep script running
    except KeyboardInterrupt:
        pass
```

---

## Step 4: Run the Script
```bash
nano lcd_display.py
python3 lcd_display.py
```
- The LCD should display:
```
Autobotic
```

---

## 🤔 Activity Reflection & Questions
1️⃣ What happens if you change `"Autobotic"` to another text?  
2️⃣ How can you display text on the **second row** of the LCD?  
3️⃣ Can you modify the script to **scroll text** across the LCD?
