## 📝 LDR Sensor Exercises

### Exercise 1: Light-Activated LED  
**Task:**  
Make an LED turn on when the LDR detects darkness.

**Instructions:**  
1. Connect an LED to GPIO 17.  
2. Modify the script so that when the LDR detects darkness, the LED turns on.  
3. If there is light, the LED should remain off.  

**Solution Code:**  
```python
from gpiozero import DigitalInputDevice, LED
import time

LDR_GPIO = 4
LED_GPIO = 17

ldr = DigitalInputDevice(LDR_GPIO)
led = LED(LED_GPIO)

try:
    while True:
        if not ldr.is_active:
            print("Darkness Detected! Turning on LED.")
            led.on()
        else:
            led.off()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram interrupted")
```

---

### Exercise 2: Light-Activated Buzzer  
**Task:**  
Make a buzzer sound when the LDR detects darkness.

**Instructions:**  
1. Connect a buzzer to GPIO 18.  
2. Modify the script so that when darkness is detected, the buzzer turns on.  
3. If there is light, the buzzer remains off.  

**Solution Code:**  
```python
from gpiozero import DigitalInputDevice, Buzzer
import time

LDR_GPIO = 4
BUZZER_GPIO = 18

ldr = DigitalInputDevice(LDR_GPIO)
buzzer = Buzzer(BUZZER_GPIO)

try:
    while True:
        if not ldr.is_active:
            print("Darkness Detected! Activating Buzzer.")
            buzzer.on()
        else:
            buzzer.off()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram interrupted")
```

---

### Exercise 3: Automatic Night Light System  
**Task:**  
Turn on an LED when darkness is detected and blink a buzzer twice.

**Instructions:**  
1. Connect an LED to GPIO 17 and a buzzer to GPIO 18.  
2. When darkness is detected, turn on the LED and make the buzzer beep twice.  
3. If there is light, turn off the LED and keep the buzzer silent.  

**Solution Code:**  
```python
from gpiozero import DigitalInputDevice, LED, Buzzer
import time

LDR_GPIO = 4
LED_GPIO = 17
BUZZER_GPIO = 18

ldr = DigitalInputDevice(LDR_GPIO)
led = LED(LED_GPIO)
buzzer = Buzzer(BUZZER_GPIO)

try:
    while True:
        if not ldr.is_active:
            print("Darkness Detected! Turning on LED and beeping buzzer.")
            led.on()
            for _ in range(2):
                buzzer.on()
                time.sleep(0.2)
                buzzer.off()
                time.sleep(0.2)
        else:
            led.off()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram interrupted")
```
