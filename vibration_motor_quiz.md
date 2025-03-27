

# ❓ Quiz – Vibration Motor with Raspberry Pi  

1️⃣ **Which GPIO pin is used to control the vibration motor in our lesson?**  
   - A) 17  
   - B) 18  
   - C) 15  
   - D) 27  
   - ✅ **Answer:** C) 15  

2️⃣ **What function is used to turn ON the vibration motor?**  
   - A) motor.start()  
   - B) motor.activate()  
   - C) motor.on()  
   - D) motor.begin()  
   - ✅ **Answer:** C) motor.on()  

3️⃣ **What happens if we remove the sleep() function in the script?**  
   - A) The motor will never turn off  
   - B) The motor will turn off immediately  
   - C) The Raspberry Pi will restart  
   - D) The motor will run for 5 seconds  
   - ✅ **Answer:** A) The motor will never turn off  

4️⃣ **What will the following Python code do?**  
   ```python
   from gpiozero import OutputDevice  
   import time  
   
   vibration_motor = OutputDevice(15)  
   vibration_motor.on()  
   time.sleep(2)  
   vibration_motor.off()
   ```
   - A) The motor will vibrate for 2 seconds, then stop  
   - B) The motor will keep vibrating indefinitely  
   - C) The script will throw an error  
   - D) The motor will not turn on  
   - ✅ **Answer:** A) The motor will vibrate for 2 seconds, then stop  

5️⃣ **What is the output of this script?**  
   ```python
   from gpiozero import OutputDevice  
   import time  
   
   vibration_motor = OutputDevice(15)  
   
   for i in range(3):  
       vibration_motor.on()  
       time.sleep(1)  
       vibration_motor.off()  
       time.sleep(1)
   ```
   - A) The motor will vibrate continuously for 3 seconds  
   - B) The motor will vibrate in 1-second pulses, repeating 3 times  
   - C) The motor will vibrate once and stop  
   - D) The motor will not turn on  
   - ✅ **Answer:** B) The motor will vibrate in 1-second pulses, repeating 3 times  

6️⃣ **What is missing in the following Python script?**  
   ```python
   import time  
   
   vibration_motor = OutputDevice(15)  
   
   vibration_motor.on()  
   time.sleep(3)  
   vibration_motor.off()
   ```
   - A) The `OutputDevice` import is missing  
   - B) The GPIO pin is incorrect  
   - C) The `time.sleep()` function should be removed  
   - D) The script is correct as it is  
   - ✅ **Answer:** A) The `OutputDevice` import is missing  

7️⃣ **What does `vibration_motor.off()` do in the script?**  
   - A) Turns the vibration motor on  
   - B) Stops the script execution  
   - C) Turns the vibration motor off  
   - D) None of the above  
   - ✅ **Answer:** C) Turns the vibration motor off  

8️⃣ **Which sensor can be used to trigger the vibration motor based on ambient light levels?**  
   - A) PIR motion sensor  
   - B) Sound sensor  
   - C) LDR (Light Dependent Resistor)  
   - D) Ultrasonic sensor  
   - ✅ **Answer:** C) LDR (Light Dependent Resistor)  

9️⃣ **How can we modify the script to make the motor vibrate in pulses?**  
   - A) Use multiple `vibration_motor.on()` and `vibration_motor.off()` calls with `sleep()` in between  
   - B) Remove the `time.sleep()` function  
   - C) Use a loop with `vibration_motor.on()` only  
   - D) Set a higher delay in `time.sleep()`  
   - ✅ **Answer:** A) Use multiple `vibration_motor.on()` and `vibration_motor.off()` calls with `sleep()` in between  

🔟 **Which component is used to manually activate the vibration motor?**  
   - A) Buzzer  
   - B) Button (GPIO 19 & 22)  
   - C) LED  
   - D) LCD Display  
   - ✅ **Answer:** B) Button (GPIO 19 & 22)  

