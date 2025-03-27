## 🚀 Exercise: 4-Digit 7-Segment Display  

### **Exercise 1: Countdown from 9999 to 0000**
🔧 Modify the script to display a countdown starting from 9999 down to 0000, updating every second.  

#### **🛠️ What You’ll Learn**
- How to loop through a number sequence and update the display.
- How to ensure numbers are displayed in a 4-digit format.
- How to clear the display when the countdown is complete.

#### **💡 Steps**
1️⃣ Initialize the 7-segment display using the **HT16K33 driver**.  
2️⃣ Start from **9999** and count down to **0000**.  
3️⃣ Ensure the number is always **4 digits** (e.g., 42 → 0042).  
4️⃣ Wait **1 second** before updating the display.  
5️⃣ Clear the display after reaching **0000**.  

#### **📝 Python Code**
```python
import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4

# Initialize I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the 4-digit 7-segment display
display = Seg7x4(i2c)

try:
    print("Starting countdown from 9999 to 0000...")
    
    for num in range(9999, -1, -1):  # Countdown from 9999 to 0000
        formatted_number = str(num).zfill(4)  # Ensure 4-digit format
        display.print(formatted_number)
        print(f"Displaying: {formatted_number}")  # Debugging output
        time.sleep(1)  # Wait for 1 second

    print("Countdown complete!")

except KeyboardInterrupt:
    print("\nCountdown stopped by user.")

finally:
    display.fill(0)  # Clear the display on exit
    print("Display cleared.")
```

---

### **Exercise 2: Display Current Time**
🔧 Modify the script to display the current time (HH:MM) format. Ensure that the colon blinks every second.

#### **🛠️ What You’ll Learn**
- How to get the current time using `datetime.now()`.
- How to format time into HHMM format for the display.
- How to create a blinking effect on the colon (`:`) every second.
- How to handle user interruptions (CTRL + C) safely.

#### **💡 Steps**
1️⃣ Initialize the 7-segment display.  
2️⃣ Retrieve the current time using `datetime.now()`.  
3️⃣ Format the time to **HHMM** (24-hour format).  
4️⃣ Enable the colon (`:`) to blink every second.  
5️⃣ Repeat the process every second to keep the time updated.  

#### **📝 Python Code**
```python
import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4
from datetime import datetime

# Initialize I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the 4-digit 7-segment display
display = Seg7x4(i2c)

try:
    print("Displaying real-time clock (HH:MM)... Press CTRL+C to stop.")

    while True:
        now = datetime.now()
        time_str = now.strftime("%H%M")  # Get time in HHMM format

        display.print(time_str)  # Display the time
        display.colon = True  # Turn ON colon
        print(f"Time: {time_str} :")  # Debugging output
        time.sleep(1)

        display.colon = False  # Turn OFF colon (Blink effect)
        print(f"Time: {time_str}  ")  # Debugging output
        time.sleep(1)

except KeyboardInterrupt:
    print("\nClock display stopped by user.")

finally:
    display.fill(0)  # Clear display on exit
    print("Display cleared.")
```

---

### **Exercise 3: Motion-Based Alert**
🔧 Connect a motion sensor (PIR) to the Raspberry Pi. When motion is detected:

✅ Display **"ON"** on the 7-segment display.  
✅ Turn on the **buzzer** for 1 second.  
✅ Turn on an **LED** as a visual alert.  

When no motion is detected, display **"OFF"** and turn off the **buzzer** and **LED**.  

#### **🛠️ What You’ll Learn**
- How to detect motion using a **PIR sensor**.  
- How to trigger the **7-segment display** and output devices (**LED & buzzer**).  
- How to continuously monitor the environment for motion changes.  

#### **💡 Steps**
1️⃣ Connect the **PIR motion sensor** to a GPIO pin (e.g., GPIO **17**).  
2️⃣ Connect an **LED** and a **buzzer** to separate GPIO pins.  
3️⃣ When motion is detected:  
   - Display **"ON"** on the 7-segment display.  
   - Activate the **buzzer** for 1 second.  
   - Turn on the **LED**.  
4️⃣ When no motion is detected:  
   - Display **"OFF"**.  
   - Turn off both the **buzzer** and **LED**.  

#### **📝 Python Code**
```python
import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4
from gpiozero import MotionSensor, LED, Buzzer

# Initialize I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the 7-segment display
display = Seg7x4(i2c)

# Initialize PIR sensor, LED, and Buzzer
pir = MotionSensor(17)  # GPIO 17 for motion sensor
led = LED(27)  # GPIO 27 for LED
buzzer = Buzzer(22)  # GPIO 22 for Buzzer

try:
    print("Monitoring motion... Press CTRL+C to stop.")

    while True:
        if pir.motion_detected:
            display.print("ON")  # Show "ON" when motion detected
            buzzer.on()  # Turn on buzzer
            led.on()  # Turn on LED
            print("Motion detected! Alert activated.")
            time.sleep(1)
            buzzer.off()  # Turn off buzzer after 1 sec
        else:
            display.print("OFF")  # Show "OFF" when no motion
            led.off()  # Turn off LED
            print("No motion detected.")

        time.sleep(0.5)  # Check motion every 0.5 seconds

except KeyboardInterrupt:
    print("\nMotion monitoring stopped by user.")

finally:
    display.fill(0)  # Clear display on exit
    led.off()  # Turn off LED
    buzzer.off()  # Turn off buzzer
    print("All outputs cleared.")
```
