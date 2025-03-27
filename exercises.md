# 🚀 7-Segment Display Exercises

## Exercise 1: Countdown from 9999 to 0000  
🔧 Modify the script to display a countdown starting from **9999** down to **0000**, updating every second.

### Steps:
1. Create a loop that starts at **9999** and decreases down to **0000**.
2. Display the current number on the **7-segment display**.
3. Use `time.sleep(1)` to update the display every second.
4. Ensure the display **clears** when the countdown reaches **0000**.

---

## Exercise 2: Display Current Time  
🔧 Modify the script to display the **current time (HH:MM format)**. The **colon (:) should blink every second**.

### Steps:
1. Retrieve the **current time** using `datetime.now()`.
2. Format the time as `HHMM` (24-hour format).
3. Display the time on the **7-segment display**.
4. Make the **colon blink** by toggling `display.colon = True` and `False` every second.
5. Continuously update the display every **second**.

---

## Exercise 3: Motion-Based Alert  
🔧 Connect a **motion sensor (PIR)** to the Raspberry Pi. When motion is detected:
- Display `"ON"` on the **7-segment display**.
- Turn **ON** the **buzzer** for 1 second.
- Turn **ON** an **LED** as a visual alert.

### Steps:
1. Set up the **motion sensor (PIR)** on a GPIO pin.
2. Detect motion using `if pir.motion_detected:`.
3. When motion is detected:
   - Display `"ON"`.
   - Activate the **buzzer** and **LED**.
   - Keep them on for **1 second**, then turn them off.
4. When no motion is detected:
   - Display `"OFF"`.
   - Ensure the **buzzer** and **LED** remain off.

---

💡 **Bonus Challenge:**  
Try combining the **motion sensor** with the **countdown timer** to trigger a countdown when motion is detected! 🚀  
