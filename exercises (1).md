## 📝 Exercises: LCD Display with Raspberry Pi

### 🔹 Exercise 1: Date and Time Display with Blinking Effect

#### Objective:
- Learn how to display real-time date and time on an LCD screen.
- Implement a blinking effect for enhanced visibility.

#### Instructions:
1. Display the current date and time on the LCD.
2. Implement a blinking effect where the display turns on and off at 1-second intervals.
3. Continuously update the time every second.


### 🔹 Exercise 2: Display Messages Using Buttons

#### Objective:
- Use physical buttons to change the displayed message on the LCD.
- Learn how to handle button inputs with GPIO.

#### Button Configuration:

| Button | Row GPIO | Column GPIO |
|--------|---------|-------------|
| SW1    | 19      | 22          |
| SW2    | 19      | 24          |
| SW3    | 19      | 25          |
| SW4    | 19      | 23          |

#### Instructions:
1. When SW1 is pressed, display "Message 1".
2. When SW2 is pressed, display "Message 2".
3. When SW3 is pressed, display "Message 3".
4. When SW4 is pressed, display "Message 4".


### 🔹 Exercise 3: Sensor-Based Message Display

#### Objective:
- Use sensors (LDR, Motion, Sound) to trigger different messages on the LCD.
- Learn how to read sensor data using GPIO.

#### Sensor Assignments:

| Sensor         | GPIO Pin |
|---------------|---------|
| Sound Sensor  | 26      |
| Motion Sensor | 27      |
| LDR Sensor    | 4       |

#### Instructions:
1. If the sound sensor detects a noise, display "Sound Detected!".
2. If motion is detected, display "Motion Detected!".
3. If the LDR sensor detects darkness (low light), display "Low Light!".

---

Enjoy experimenting with these exercises! 🚀
