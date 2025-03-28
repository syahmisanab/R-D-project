## 📝 Exercises: Controlling WS2812B (NeoPixel) LED Strip with Raspberry Pi  

---  

### 🔹 Exercise 1: Implement a Lighting Effect  

**Objective:**  
- Learn to control WS2812B (NeoPixel) LED strips using Python.  
- Implement a lighting effect on the LED strip.  

**Instructions:**  
1. Write a Python script to control the WS2812B LED strip.  
2. Implement one of the following effects:  
   - **Color Cycling** – LEDs change colors in a loop (Red → Green → Blue).  
   - **Rainbow Effect** – Smooth transition through a rainbow color spectrum.  
   - **Chasing Effect** – A moving light effect where LEDs turn on sequentially.  
   - **Breathing Effect** – LEDs smoothly fade in and out.  
3. Run the script and observe the effect.  

✅ **Expected Outcome:** The LED strip continuously displays the chosen effect.  

---  

### 🔹 Exercise 2: Change Effects Using a Matrix Button  

**Objective:**  
- Learn how to use a matrix button to change LED effects.  
- Implement user interaction for selecting different lighting modes.  

**Button Configuration:**  

| Button | Row GPIO | Column GPIO |
|--------|----------|-------------|
| SW1    | 19       | 22          |
| SW2    | 19       | 24          |
| SW3    | 19       | 25          |
| SW4    | 19       | 23          |

**Instructions:**  
1. Modify the previous script to allow switching between effects using a **matrix button**.  
2. Pressing the button should cycle through the following effects:  
   - **First press** → Color Cycling  
   - **Second press** → Rainbow Effect  
   - **Third press** → Chasing Effect  
   - **Fourth press** → Breathing Effect  
3. Ensure that each button press changes the effect sequentially.  

✅ **Expected Outcome:** Pressing the matrix button changes the lighting effect on the LED strip.  

---  

### 🔹 Exercise 3: Display the Current Effect on an LCD Screen  

**Objective:**  
- Learn how to display text on an **LCD 1602** screen using I2C.  
- Display the name of the currently active lighting effect.  

**Pin Configuration (I2C Bus):**  

| Component      | Raspberry Pi GPIO |
|---------------|------------------|
| SDA (Data)    | GPIO 2 (SDA)      |
| SCL (Clock)   | GPIO 3 (SCL)      |

**Instructions:**  
1. Extend your previous code by integrating an **LCD 1602 screen**.  
2. Whenever the lighting effect changes, update the LCD screen with the effect’s name.  
3. Example: If the **Chasing Effect** is running, the LCD should display:  
   ```
   Effect: Chasing
   ```  
4. Ensure that the LCD screen updates in real-time as the effect changes.  

✅ **Expected Outcome:** The LCD screen always displays the name of the active effect.  

---  

🚀 **Test your code, experiment with different effects, and have fun!**  
