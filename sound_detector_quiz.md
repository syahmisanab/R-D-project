

# ❓ Quiz – Sound Detector Sensor with Raspberry Pi

## 1️⃣ Which GPIO pin is used to connect the sound detector sensor in this lesson?  
- A) GPIO 17  
- B) GPIO 22  
- C) GPIO 26  
- D) GPIO 5  
✅ **Answer: C) GPIO 26**  

---  

## 2️⃣ What happens when the sound level exceeds the threshold?  
- A) The sensor sends a LOW signal to the Raspberry Pi  
- B) The sensor sends a HIGH signal to the Raspberry Pi  
- C) The sensor starts vibrating  
- D) The Raspberry Pi reboots  
✅ **Answer: B) The sensor sends a HIGH signal to the Raspberry Pi**  

---  

## 3️⃣ Which Python library is used in this lesson to control the GPIO pins?  
- A) RPi.GPIO  
- B) gpiozero  
- C) wiringPi  
- D) pySerial  
✅ **Answer: B) gpiozero**  

---  

## 4️⃣ How does the Raspberry Pi detect sound using the sensor?  
- A) It measures the analog sound level directly  
- B) The sensor sends a digital HIGH signal when sound is detected  
- C) The Raspberry Pi reads a frequency value from the sensor  
- D) It converts sound waves into an electrical signal for processing  
✅ **Answer: B) The sensor sends a digital HIGH signal when sound is detected**  

---  

## 5️⃣ What will happen if we remove the `time.sleep(0.1)` function in the script?  
- A) The sensor will stop working  
- B) The script will constantly check for sound without delay  
- C) The Raspberry Pi will shut down  
- D) The sensor will only work for 10 seconds  
✅ **Answer: B) The script will constantly check for sound without delay**  

---  

## 6️⃣ What will the following Python code do?  

```python
from gpiozero import Button
import time

sound_sensor = Button(26, pull_up=False)

while True:
    if sound_sensor.is_pressed:
        print("🔊 Sound Detected!")
    time.sleep(0.5)
```

- A) The script will not run due to an error  
- B) "🔊 Sound Detected!" will print continuously when sound is detected  
- C) The Raspberry Pi will shut down  
- D) The sensor will work for 5 seconds only  
✅ **Answer: B) "🔊 Sound Detected!" will print continuously when sound is detected**  

---  

## 7️⃣ How can we safely stop the sound detection script?  
- A) Pressing CTRL + C  
- B) Disconnecting the sensor  
- C) Removing the Raspberry Pi power supply  
- D) Pressing the keyboard spacebar  
✅ **Answer: A) Pressing CTRL + C**  

---  

## 8️⃣ How can we modify the script to detect sound more frequently?  
- A) Increase `time.sleep(0.1)` to `time.sleep(1)`  
- B) Reduce `time.sleep(0.1)` to `time.sleep(0.05)`  
- C) Change `pull_up=False` to `pull_up=True`  
- D) Remove the `while True` loop  
✅ **Answer: B) Reduce `time.sleep(0.1)` to `time.sleep(0.05)`**  

---  

## 9️⃣ What will happen if we use `pull_up=True` instead of `pull_up=False`?  
- A) The sensor will stop working  
- B) The GPIO pin will default to HIGH instead of LOW  
- C) The sound detection will become more sensitive  
- D) The Raspberry Pi will freeze  
✅ **Answer: B) The GPIO pin will default to HIGH instead of LOW**  

---  

## 🔟 How can we modify the script to turn on an LED when sound is detected?  

```python
from gpiozero import Button, LED
import time

SOUND_PIN = 26
LED_PIN = 18

sound_sensor = Button(SOUND_PIN, pull_up=False)
led = LED(LED_PIN)

while True:
    if sound_sensor.is_pressed:
        led.on()
        print("🔊 Sound Detected! LED ON")
    else:
        led.off()
    time.sleep(0.1)
```

- A) The LED will turn on when sound is detected  
- B) The LED will always be on  
- C) The LED will turn off when sound is detected  
- D) The script will not work  
✅ **Answer: A) The LED will turn on when sound is detected**  

---  

