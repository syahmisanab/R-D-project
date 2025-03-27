# 📝 Exercises: Sound Detector with Raspberry Pi

## 🔹 Exercise 1: Sound Detection and LED Blink

### Objective:  
- Use a sound detector sensor (GPIO 26) to detect sound.  
- When sound is detected, make an LED (GPIO 18) blink.  

### Components & Pin Configuration:  
- **Sound Detector Sensor** → GPIO 26  
- **LED** → GPIO 18  

### Complete the below code:
```python
#!/usr/bin/python3
from gpiozero import Button, LED
import time

# Define components
sound_sensor = Button(26, pull_up=False)  # Sound sensor
led = LED(18)  # LED

# Main loop
while True:
    if sound_sensor.is_pressed:
        print("🔊 Sound Detected! Blinking LED...")
        for _ in range(3):  # Blink 3 times
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
    time.sleep(0.1)
```

---

## 🔹 Exercise 2: Sound Detection and LDR (Darkness) Activates a Buzzer

### Objective:  
- Use a sound detector sensor (GPIO 26) and an LDR (GPIO 4) to detect sound and darkness.  
- If sound is detected and it is dark, activate a buzzer (GPIO 17).  

### Components & Pin Configuration:  
- **Sound Detector Sensor** → GPIO 26  
- **LDR Light Sensor** → GPIO 4  
- **Buzzer** → GPIO 17  

### Complete the below code:
```python
#!/usr/bin/python3
from gpiozero import Button, LightSensor, Buzzer
import time

# Define components
sound_sensor = Button(26, pull_up=False)  # Sound sensor
ldr = LightSensor(4)  # Light sensor
buzzer = Buzzer(17)  # Buzzer

# Main loop
while True:
    if sound_sensor.is_pressed and ldr.value < 0.2:  # Low light (darkness)
        print("🔊 Sound Detected & Darkness! Activating Buzzer...")
        buzzer.on()
        time.sleep(1)
        buzzer.off()
    time.sleep(0.1)
```

---

## 🔹 Exercise 3: Sound and Motion Detection Activates a Vibration Motor

### Objective:  
- Use a sound detector sensor (GPIO 26) and a motion sensor (GPIO 27).  
- If both sound and motion are detected, activate a vibration motor (GPIO 15).  

### Components & Pin Configuration:  
- **Sound Detector Sensor** → GPIO 26  
- **PIR Motion Sensor** → GPIO 27  
- **Vibration Motor** → GPIO 15  

### Complete the below code:
```python
#!/usr/bin/python3
from gpiozero import Button, MotionSensor, OutputDevice
import time

# Define components
sound_sensor = Button(26, pull_up=False)  # Sound sensor
motion_sensor = MotionSensor(27)  # PIR motion sensor
vibration_motor = OutputDevice(15)  # Vibration motor

# Main loop
while True:
    if sound_sensor.is_pressed and motion_sensor.motion_detected:
        print("🔊 Sound & Motion Detected! Activating Vibration Motor...")
        vibration_motor.on()
        time.sleep(2)  # Keep motor on for 2 seconds
        vibration_motor.off()
    time.sleep(0.1)
```
