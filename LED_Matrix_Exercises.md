## 📝 Exercises: LED Matrix (MAX7219) with Raspberry Pi

## 🔹 Exercise 1: Draw Custom Shapes on the Matrix

### Objective:  
- Learn how to design basic **shapes (diamond, square, circle, etc.)** using individual LED points.  
- Understand how **draw.point()** works to control each LED pixel.  

### Instructions:  
1. Modify the provided code to create different shapes.  
2. Use `draw.point((x, y), fill="white")` to light up specific LEDs.  
3. Try drawing:  
   - **Diamond (X shape)**  
   - **Square Frame**  
   - **Circle Approximation**  
   - **Your Own Design!**  

```python
#!/usr/bin/env python3
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time

# Initialize SPI communication
serial = spi(port=0, device=0, gpio=noop())

# Initialize the MAX7219 device
device = max7219(serial, cascaded=1, rotate=2)

def draw_shape():
    with canvas(device) as draw:
        draw.point((3, 3), fill="white")  # Center point (example)
        # Add your shape points here!

while True:
    draw_shape()
    time.sleep(2)
```

---

## 🔹 Exercise 2: Change Patterns Using Button Matrix

### Objective:  
- Use **button presses** to display **different patterns** on the LED matrix.  
- Learn how to handle **button matrix inputs** with GPIO.  

### Button Configuration:
| Button | Row GPIO | Column GPIO |  
|--------|---------|------------|  
| SW1    | GPIO 19 | GPIO 22    |  
| SW2    | GPIO 19 | GPIO 24    |  
| SW3    | GPIO 19 | GPIO 25    |  
| SW4    | GPIO 19 | GPIO 23    |  

### Instructions:  
1. When **SW1 is pressed**, show a **square pattern**.  
2. When **SW2 is pressed**, show a **cross pattern**.  
3. When **SW3 is pressed**, show a **circle approximation**.  
4. When **SW4 is pressed**, show a **diagonal wave animation**.  

```python
#!/usr/bin/python3
from gpiozero import Button
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

# Initialize devices
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, rotate=2)

# Define buttons
btn1 = Button(22)
btn2 = Button(24)
btn3 = Button(25)
btn4 = Button(23)

def draw_square():
    with canvas(device) as draw:
        draw.rectangle((1, 1, 6, 6), fill="white")

def draw_cross():
    with canvas(device) as draw:
        for x in range(8):
            draw.point((x, 3), fill="white")
        for y in range(8):
            draw.point((3, y), fill="white")

while True:
    if btn1.is_pressed:
        draw_square()
    elif btn2.is_pressed:
        draw_cross()
```

---

## 🔹 Exercise 3: Sensor-Based Animation Reactions

### Objective:  
- Make the LED matrix react to **real-world inputs** like **sound, motion, or light changes**.  
- Display different animations based on sensor data.  

### Sensor Assignments:
| Sensor  | GPIO Pin | Effect |
|---------|---------|--------|
| **Sound Sensor** | GPIO 26 | Pulsating Dot |
| **Motion Sensor** | GPIO 27 | Running Dots |
| **LDR Sensor** | GPIO 4  | Twinkling Stars |

```python
#!/usr/bin/python3
from gpiozero import Button, MotionSensor, LightSensor
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time

# Initialize devices
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, rotate=2)

# Define sensors
sound_sensor = Button(26, pull_up=False)
motion_sensor = MotionSensor(27)
ldr = LightSensor(4)

def pulsating_dot():
    for i in range(3):
        with canvas(device) as draw:
            draw.point((3, 3), fill="white")
        time.sleep(0.2)
        with canvas(device) as draw:
            pass  # Clear display
        time.sleep(0.2)

def running_dots():
    for x in range(8):
        with canvas(device) as draw:
            draw.point((x, 3), fill="white")
        time.sleep(0.1)

def twinkling_stars():
    with canvas(device) as draw:
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    draw.point((x, y), fill="white")
    time.sleep(2)

while True:
    if sound_sensor.is_pressed:
        pulsating_dot()
    if motion_sensor.motion_detected:
        running_dots()
    if ldr.value < 0.2:
        twinkling_stars()
```

---

## 💡 Optional Challenges  
✅ **Challenge 1:** **Scrolling Text Based on Sensor Input**  
- When the **sound sensor** detects noise, scroll a message **"Noise Detected!"** on the LED matrix.  

✅ **Challenge 2:** **Pattern Changer with Multiple Buttons**  
- Press **SW1 to cycle through patterns** instead of using separate buttons.  

✅ **Challenge 3:** **Create a Simple LED Game**  
- Example: **"Simon Says"** style game where the matrix displays a pattern, and the user must press the correct button.  
