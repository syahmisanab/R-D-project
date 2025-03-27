# 📝 Exercises: Vibration Motor Control

## Exercise 1: Vibration Motor with Light Sensor (LDR)  

**Objective:**  
- Use an **LDR (Light Sensor - GPIO 4)** to detect light levels.  
- Activate a **vibration motor (GPIO 15)** when it gets dark.  

**Components & Pin Configuration:**  
- **LDR Light Sensor** → GPIO 4  
- **Vibration Motor** → GPIO 15  

### Complete the below code:  

```python
#!/usr/bin/python3
from gpiozero import OutputDevice, DigitalInputDevice
import time

# Define components
ldr = DigitalInputDevice(4)  # LDR sensor
vibration_motor = OutputDevice(15)  # Vibration motor

# Main loop
while True:
    if not ldr.is_active:  # Darkness detected
        print("Darkness detected! Vibrating...")
        vibration_motor.on()
    else:
        vibration_motor.off()
    time.sleep(0.1)
```

---

## Exercise 2: Control Vibration Motor Using a Button  

**Objective:**  
- Learn how to turn a **vibration motor (GPIO 15)** on and off using a **matrix button (GPIO 19 & GPIO 22)**.  
- Understand how to use a button as an input with Raspberry Pi.  

**Components & Pin Configuration:**  
- **Vibration Motor** → GPIO 15  
- **Matrix Button** → GPIO 19 (Row), GPIO 22 (Column)  

### Complete the below code:  

```python
#!/usr/bin/python3
from gpiozero import OutputDevice, Button
import time

# Define components
vibration_motor = OutputDevice(15)
button = Button((19, 22))  # Matrix button (row, column)

# Main loop
while True:
    if button.is_pressed:
        print("Button Pressed! Vibrating...")
        vibration_motor.on()
    else:
        vibration_motor.off()
    time.sleep(0.1)  # Small delay for responsiveness
```

---

## Exercise 3: Vibration Alarm System (Motion Sensor, LED, Buzzer & Vibration Motor)  

**Objective:**  
- Create a simple alarm system that **activates a vibration motor (GPIO 15), buzzer (GPIO 17), and red LED (GPIO 21)** when motion is detected.  

**Components & Pin Configuration:**  
- **PIR Motion Sensor** → GPIO 27  
- **Vibration Motor** → GPIO 15  
- **Passive Buzzer** → GPIO 17  
- **Red LED** → GPIO 21  

### Complete the below code:  

```python
#!/usr/bin/python3
from gpiozero import MotionSensor, OutputDevice, LED, Buzzer
import time

# Define components
pir = MotionSensor(27)  # PIR motion sensor
vibration_motor = OutputDevice(15)  # Vibration motor
buzzer = Buzzer(17)  # Buzzer
red_led = LED(21)  # Red LED

# Main loop
while True:
    if pir.motion_detected:
        print("⚠️ Motion Detected! Activating Alarm...")
        vibration_motor.on()
        buzzer.on()
        red_led.on()
        time.sleep(3)  # Keep alarm active for 3 seconds
    else:
        vibration_motor.off()
        buzzer.off()
        red_led.off()
    time.sleep(0.1)
```

---

## ✅ Summary  
- **Exercise 1:** Use an **LDR sensor** to detect darkness and activate the **vibration motor**.  
- **Exercise 2:** Press a **matrix button** (GPIO 19 & GPIO 22) to activate the **vibration motor**.  
- **Exercise 3:** Create an **alarm system** with a **motion sensor, buzzer, LED, and vibration motor**.  
