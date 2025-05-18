🎯 Learning Objectives
- Understand how an LCD 1602 (16x2 character display) works.
- Learn how to interface the LCD with Raspberry Pi using I2C communication.
- Write a Python script to display text on the LCD screen.

---
🛠️ Materials & Equipment Checklist
- Raspberry Pi
- OiviO Pi Extension Board
- Power supply for Raspberry Pi
- Monitor, keyboard, and mouse (for setup)

---
🔍 Concept: How an LCD 1602 Works
The LCD 1602 is a 16x2 character display that allows us to show text. It uses the Hitachi HD44780 controller and can be controlled with an I2C adapter, which reduces the number of GPIO pins needed.

✅ How It Works
- I2C (Inter-Integrated Circuit) communication is used to send commands.
- The LCD has an I2C address (usually 0x27 or 0x3F).
- We send ASCII character codes to display text.

What is I2C


---
🛠️ Components & Setup

Pin Configuration (I2C Bus)
Component
Raspberry Pi GPIO
SDA (Data)
GPIO 2 (SDA)
SCL (Clock)
GPIO 3 (SCL)

🔗 Technical Sheet & Pin Reference: [OiviO Pi Technical Sheet]

---
🚀 Step-by-Step Guide

Step 1: Enable I2C on Raspberry Pi
sudo raspi-config
- Go to Interfacing Options → I2C and Enable it.
- Restart your Raspberry Pi:
sudo reboot

---
Step 2: Check the I2C Address
sudo apt install -y i2c-tools
i2cdetect -y 1
- The LCD should appear as 0x27 or 0x3F.

---
Step 3: Write the Python Code

1.  Import Required Libraries
import time
import smbus2
import signal
  - time → Used for adding delays to ensure smooth LCD operation.
  - smbus2 → Enables I2C communication between the Raspberry Pi and the LCD.
  - signal → Handles the Ctrl+C keyboard interrupt, allowing the script to exit gracefully.

2.  Define I2C Address & Bus
LCD_ADDR = 0x27  
bus = smbus2.SMBus(1)
  - LCD_ADDR = 0x27 → Specifies the I2C address of the LCD (it may be 0x3F on some models).
  - smbus2.SMBus(1) → Opens I2C Bus 1 on the Raspberry Pi to communicate with the LCD.
  
3. LCD Command & Control Bits
LCD_CHR = 1  # Data mode
LCD_CMD = 0  # Command mode
LCD_BACKLIGHT = 0x08  # Backlight ON
ENABLE = 0b00000100  # Enable bit
  - LCD_CHR = 1 → Used when sending character data to the display.
  - LCD_CMD = 0 → Used when sending commands (e.g., clearing the screen).
  - LCD_BACKLIGHT = 0x08 → Keeps the LCD’s backlight ON.
  - ENABLE = 0b00000100 → This bit is required to latch data onto the LCD.
  
4. Function to Send Data to LCD
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
  - This function sends either commands or text to the LCD.
  - Since the LCD operates in 4-bit mode, it splits the data into high bits and low bits before sending.
  - The ENABLE bit is toggled to inform the LCD when data is ready to be read.
5. Initialize the LCD
def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Display ON, Cursor OFF
    lcd_byte(0x28, LCD_CMD)  # 2-line mode, 5x8 font
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)
  - This function configures the LCD at startup.
  - 0x33 and 0x32 → Set 4-bit mode.
  - 0x06 → Moves the cursor to the right after writing text.
  - 0x0C → Turns ON the display without a blinking cursor.
  - 0x28 → Configures the display to 2-line mode with 5x8 font size.
  - 0x01 → Clears the LCD screen.
  
6. Function to Display Text on LCD
def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)  # Move to first line
    for char in text:
        lcd_byte(ord(char), LCD_CHR)
  - 0x80 → Moves the cursor to the first row, first column.
  - The function loops through each character in the text, converts it into an ASCII value, and sends it to the LCD.
  
7. Clearing the LCD
def lcd_clear():
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)
  - This function clears the entire LCD screen by sending 0x01.
  
8. Handling Ctrl+C (Keyboard Interrupt)
def signal_handler(sig, frame):
    print("\nClearing LCD and exiting...")
    lcd_clear()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)
  - Ensures the LCD is cleared before exiting the script.
  - When the user presses Ctrl+C, the lcd_clear() function runs.
9. Running the Main Program
def run_lcd_demo():
    """Run a simple LCD demo: display 'Autobotic' and keep running."""
    lcd_init()
    lcd_display("Autobotic")

    try:
        while True:
            time.sleep(1)  # Keep script running
    except KeyboardInterrupt:
        pass

# run code
run_lcd_demo()
- Initializes the LCD using lcd_init().
- Displays the text "Autobotic" using lcd_display().
- The script keeps running until Ctrl+C is pressed, which stops the script gracefully.

10. Full code 
import time
import smbus2
import signal

LCD_ADDR = 0x27  
bus = smbus2.SMBus(1)

LCD_CHR = 1  # Data mode
LCD_CMD = 0  # Command mode
LCD_BACKLIGHT = 0x08  # Backlight ON
ENABLE = 0b00000100  # Enable bit

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
    
def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Display ON, Cursor OFF
    lcd_byte(0x28, LCD_CMD)  # 2-line mode, 5x8 font
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)
    
def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)  # Move to first line
    for char in text:
        lcd_byte(ord(char), LCD_CHR)
def lcd_clear():
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)
    
def signal_handler(sig, frame):
    print("\nClearing LCD and exiting...")
    lcd_clear()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run_lcd_demo():
    """Run a simple LCD demo: display 'Autobotic' and keep running."""
    lcd_init()
    lcd_display("Autobotic")

    try:
        while True:
            time.sleep(1)  # Keep script running
    except KeyboardInterrupt:
        pass

# run code
run_lcd_demo()

---
Function Examples

1. Multiple Line Display
def lcd_display_lines(line1, line2=""):
    """Display text on two LCD lines"""
    lcd_byte(0x80, LCD_CMD)  # First line
    for char in line1:
        lcd_byte(ord(char), LCD_CHR)
    
    lcd_byte(0xC0, LCD_CMD)  # Second line
    for char in line2:
        lcd_byte(ord(char), LCD_CHR)
  - Purpose: Shows text on two lines of the LCD
  - Example: Display date on first line, time on second line
  - Useful for: Showing two pieces of information simultaneously
2. Text Scrolling
def lcd_scroll_text(text, delay=0.3):
    """Scroll text across the LCD screen"""
    text = text + " " * 16  # Add padding
    for i in range(len(text) - 15):
        lcd_clear()
        lcd_byte(0x80, LCD_CMD)
        for char in text[i:i+16]:
            lcd_byte(ord(char), LCD_CHR)
        time.sleep(delay)
  - Purpose: Makes long text scroll across the LCD screen
  - Example: Displays a long message that moves from right to left
  - Useful for: Showing longer messages on a small display
3. Sensor Data Display
import random
def display_temperature():
    """Display temperature from a sensor"""
    temp = round(random.uniform(20.0, 35.0), 1)
    lcd_display(f"Temp: {temp}°C")
  - Purpose: Shows sensor readings on the LCD
  - Example: Displays temperature (simulated in this code, but can be replaced with real sensor data)
  - Useful for: Monitoring environmental conditions
4. Date and Time Display
from datetime import datetime
def display_datetime():
    """Show current date and time"""
    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")
    
    lcd_display_lines(date_str, time_str)
  - Purpose: Shows current date and time
  - Example: Displays date (DD/MM/YYYY) on first line, time (HH:MM) on second line
  - Useful for: Creating a simple clock or timestamp display
5. Blinking Text
def lcd_blink_text(text, blinks=3):
    """Create a blinking text effect"""
    for _ in range(blinks):
        lcd_display(text)
        time.sleep(0.5)
        lcd_clear()
        time.sleep(0.5)
  - Purpose: Makes text blink on and off
  - Example: Repeatedly shows and hides a message
  - Useful for: Drawing attention to important information or creating visual alerts
6. IP Address Display
import socket
def display_ip_address():
    """Show the device's IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        lcd_display(f"IP: {ip}")
        s.close()
    except Exception:
        lcd_display("No Network")
  - Purpose: Shows the device's current IP address
  - Example: Displays local network IP address
  - Useful for: Network configuration, troubleshooting
7. Progress Bar Simulation
def display_progress(percentage):
    """Display a simple progress bar"""
    bar = "#" * int(percentage / 10)
    lcd_display(f"Progress:{bar}")
  - Purpose: Creates a simple visual progress indicator
  - Example: Shows progress as a series of '#' characters
  - Useful for: Displaying task completion or loading status

---
📝 Exercises: LCD Display with Raspberry Pi

🔹 Exercise 1: Date and Time Display with Blinking Effect
Objective:
- Learn how to display real-time date and time on an LCD screen.
- Implement a blinking effect for enhanced visibility.
Instructions:
1. Display the current date and time on the LCD.
2. Implement a blinking effect where the display turns on and off at 1-second intervals.
3. Continuously update the time every second.
Complete below code:
import time
import smbus2
import signal
from datetime import datetime

# I2C address of LCD (Check your LCD module: usually 0x27 or 0x3F)
LCD_ADDR = 0x27  
bus = smbus2.SMBus(1)

# LCD commands
LCD_CHR = 1  # Data mode
LCD_CMD = 0  # Command mode
LCD_BACKLIGHT = 0x08  # Backlight ON
ENABLE = 0b00000100  # Enable bit

# Function to send command to LCD
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

# Function to initialize LCD
def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Turn on display, no cursor
    lcd_byte(0x28, LCD_CMD)  # 2 lines, 5x8 font
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)

# Function to display text on LCD
def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)  # Move to first line
    for char in text:
        lcd_byte(ord(char), LCD_CHR)

# Function to clear LCD
def lcd_clear():
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)

# Signal handler to clear LCD on Ctrl+C
def signal_handler(sig, frame):
    print("\nClearing LCD and exiting...")
    lcd_clear()
    exit(0)

# Attach signal handler
signal.signal(signal.SIGINT, signal_handler)

# Initialize LCD
lcd_init()

try:
    while True:
        # Get current date and time
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
        time_str = now.strftime("%H:%M:%S")  # Format: HH:MM:SS

        # Display Date
        lcd_display(date_str)
        time.sleep(1)
        
        # Clear display for blinking effect
        lcd_clear()
        time.sleep(0.5)
        
        # Display Time
        lcd_display(time_str)
        time.sleep(1)

        # Clear display again for blinking effect
        lcd_clear()
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

- 

---
🔹 Exercise 2: Display Messages Using Buttons

Objective:
- Use physical buttons to change the displayed message on the LCD.
- Learn how to handle button inputs with GPIO.
Button Configuration:
Button
Row GPIO
Column GPIO
SW1
19
22
SW2
19
24
SW3
19
25
SW4
19
23
Instructions:
1. When SW1 is pressed, display "Message 1".
2. When SW2 is pressed, display "Message 2".
3. When SW3 is pressed, display "Message 3".
4. When SW4 is pressed, display "Message 4".

Complete below code:
import time
import smbus2
import signal
from gpiozero import Button, OutputDevice

# LCD setup
LCD_ADDR = 0x27  
bus = smbus2.SMBus(1)

LCD_CHR = 1  # Data mode
LCD_CMD = 0  # Command mode
LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100

# Button matrix: 1 row and 1 column
row = Button(19, pull_up=True)
col = OutputDevice(22, initial_value=True)

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

def lcd_init():
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.2)

def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)
    for char in text[:16]:
        lcd_byte(ord(char), LCD_CHR)

def lcd_clear():
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.2)

def signal_handler(sig, frame):
    print("\nClearing LCD and exiting...")
    lcd_clear()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run_lcd_with_button():
    """Run LCD display with one button using gpiozero"""
    lcd_init()
    lcd_clear()
    
    try:
        while True:
            col.off()  # Activate column
            lcd_clear()
            time.sleep(0.05)

            if row.is_pressed:
                lcd_clear()
                lcd_display("Button Pressed")
                time.sleep(0.5)  # Debounce delay

            col.on()  # Deactivate column
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
run_lcd_with_button()



---
🔹 Exercise 3: Sensor-Based Message Display

Objective:
- Use sensors (LDR, Motion, Sound) to trigger different messages on the LCD.
- Learn how to read sensor data using GPIO.
Sensor Assignments:
Sensor
GPIO Pin
Sound Sensor
26
Motion Sensor
27
LDR Sensor
4
Instructions:
1. If the sound sensor detects a noise, display "Sound Detected!".
2. If motion is detected, display "Motion Detected!".
3. If the LDR sensor detects darkness (low light), display "Low Light!".

Complete below code:
import time
import signal
import smbus2
from gpiozero import DigitalInputDevice

# LCD I2C settings
LCD_ADDR = 0x27
bus = smbus2.SMBus(1)

LCD_CHR = 1
LCD_CMD = 0
LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100

# LDR GPIO pin
LDR_GPIO = 4
ldr = DigitalInputDevice(LDR_GPIO)

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

def lcd_init():
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.2)

def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)
    for char in text[:16]:
        lcd_byte(ord(char), LCD_CHR)

def lcd_clear():
    lcd_byte(0x01, LCD_CMD)
    time.sleep(0.2)

def signal_handler(sig, frame):
    print("\nExiting...")
    lcd_clear()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run_ldr_lcd_monitor():
    """Continuously monitor LDR and display light state on LCD."""
    lcd_init()
    lcd_clear()

    last_state = ldr.value  # 1 = no light, 0 = light present

    try:
        while True:
            current_state = ldr.value
            if current_state != last_state:
                lcd_clear()
                if current_state:
                    lcd_display("It's Dark")
                    print("Dark")
                else:
                    lcd_display("It's Light")
                    print("Light")
                last_state = current_state
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        lcd_clear()
        print("LDR monitoring stopped.")


---
Quiz on LCD 1602 with Raspberry Pi

1. What is the default I2C address of the LCD 1602 module?
- A) 0x20  
- B) 0x27  
- C) 0x30  
- D) 0x50  


---
2. What is the primary advantage of using an I2C adapter with the LCD 1602?
- A) It increases the screen resolution  
- B) It reduces the number of GPIO pins required  
- C) It speeds up text rendering  
- D) It makes the LCD waterproof  


---
3. Which GPIO pins are used for I2C communication on the Raspberry Pi?
- A) GPIO 14 & GPIO 15  
- B) GPIO 2 & GPIO 3  
- C) GPIO 17 & GPIO 18  
- D) GPIO 4 & GPIO 5  


---
4. Which Python library is used to communicate with the LCD 1602 using I2C?
- A) RPi.GPIO  
- B) time  
- C) smbus2  
- D) serial  


---
5. What command is used to check the I2C address of the LCD?
- A) sudo i2cscan  
- B) sudo raspi-i2c  
- C) i2cdetect -y 1  
- D) i2c_address_check  
 

---
6. What does the function lcd_clear() do?
- A) Clears the LCD screen  
- B) Turns off the LCD backlight  
- C) Resets the Raspberry Pi  
- D) Displays a default message  


---
7. What does the lcd_byte() function primarily do?
- A) Sends data to the LCD screen  
- B) Converts text to numbers  
- C) Initializes the Raspberry Pi  
- D) Changes the screen brightness  


---
8. What is the purpose of the ENABLE bit (0b00000100) in LCD control?
- A) It powers on the LCD  
- B) It enables backlight brightness  
- C) It latches data onto the LCD  
- D) It changes font size  

---
9. How do you initialize the LCD for 4-bit mode in Python?
- A) lcd_byte(0x33, LCD_CMD) followed by lcd_byte(0x32, LCD_CMD)  
- B) lcd_init_4bit()  
- C) lcd_start_4bit_mode()  
- D) lcd_byte(0x04, LCD_CMD)  
  

---
10. What happens if you press Ctrl+C while the script is running?
- A) The Raspberry Pi restarts  
- B) The script exits and the LCD is cleared  
- C) The LCD freezes  
- D) The text starts blinking  


---
🤔 Activity Reflection & Questions
1️⃣ What happens if you change "Autobotic" to another text?  
2️⃣ How can you display text on the second row of the LCD?  
3️⃣ Can you modify the script to scroll text across the LCD?

---
📖 Additional Resources
1. Official Raspberry Pi Projects: https://projects.raspberrypi.org/en  
