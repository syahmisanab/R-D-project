## 📝 LDR Sensor Quiz

### 1️⃣ What happens to the resistance of an LDR when light intensity increases?
A) It increases  
B) It decreases  
C) It stays the same  
D) It fluctuates randomly  

### 2️⃣ Which GPIO pin is used for the LDR sensor in our exercises?
A) 17  
B) 18  
C) 4  
D) 27  

### 3️⃣ Why do we use a digital input method instead of an analog input for the LDR?
A) The Raspberry Pi does not have analog input  
B) Digital input is more accurate  
C) Analog input is not supported by Python  
D) LDR sensors only work in digital mode  

### 4️⃣ How can we measure precise light intensity values with the Raspberry Pi?
A) Use a DigitalInputDevice  
B) Use an Analog-to-Digital Converter (ADC) like MCP3008  
C) Use a higher voltage power supply  
D) Use a resistor with a lower value  

### 5️⃣ What is the output state of the LDR sensor when the light level is low?
A) HIGH (1)  
B) LOW (0)  
C) It fluctuates randomly  
D) It depends on the resistor value  

### 6️⃣ What will this code output when the LDR detects darkness?

```python
if not ldr.is_active:
    print("Darkness Detected!")
```

A) "Light Detected!"  
B) "Darkness Detected!"  
C) No output  
D) The program will crash  

### 7️⃣ What component is needed if we want to measure gradual changes in light intensity?
A) A relay  
B) An LED  
C) An Analog-to-Digital Converter (ADC)  
D) A transistor  

### 8️⃣ Which of the following correctly turns on an LED when the LDR detects darkness?
```python
if not ldr.is_active:
    led.on()
```
A) Correct  
B) Incorrect  

### 9️⃣ How can we modify the code to turn on an LED when light is detected?
A) Use `if ldr.is_active: led.on()`  
B) Use `if not ldr.is_active: led.on()`  
C) Use `led.on()` without conditions  
D) Change GPIO pins  

### 🔟 What is the main purpose of an LDR sensor?
A) Detect sound  
B) Measure humidity  
C) Detect light intensity  
D) Control a motor  

---

## ✅ Answers:
1️⃣ B) It decreases  
2️⃣ C) 4  
3️⃣ A) The Raspberry Pi does not have analog input  
4️⃣ B) Use an Analog-to-Digital Converter (ADC) like MCP3008  
5️⃣ B) LOW (0)  
6️⃣ B) "Darkness Detected!"  
7️⃣ C) An Analog-to-Digital Converter (ADC)  
8️⃣ A) Correct  
9️⃣ A) Use `if ldr.is_active: led.on()`  
🔟 C) Detect light intensity  
