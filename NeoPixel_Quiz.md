## 🎯 Quiz: NeoPixel & Raspberry Pi Basics

Test your understanding with this **10-question multiple-choice quiz**!  

---

### 📌 Quiz Questions

#### 1. What type of LED strip is used in this project?
- A) WS2811  
- B) WS2812B (NeoPixel) ✅  
- C) APA102  
- D) RGB5050  

---

#### 2. What is the main advantage of WS2812B LEDs?
- A) Each LED can be controlled individually ✅  
- B) They require multiple GPIO pins  
- C) They only support a single color  
- D) They do not need a power supply  

---

#### 3. Which GPIO pin is used to control the WS2812B data line?
- A) GPIO 17  
- B) GPIO 18 ✅  
- C) GPIO 22  
- D) GPIO 10  

---

#### 4. What library is used to control NeoPixels in Python?
- A) `RPi.GPIO`  
- B) `busio`  
- C) `neopixel` ✅  
- D) `pwm`  

---

#### 5. What does `auto_write=False` do when initializing the NeoPixel strip?
- A) It prevents automatic updates, requiring `pixels.show()` to refresh the LEDs ✅  
- B) It automatically updates the LEDs without needing `pixels.show()`  
- C) It turns off the LEDs when the script starts  
- D) It reduces power consumption  

---

#### 6. Which of the following effects cycles through red, green, and blue?
- A) Chasing Effect  
- B) Breathing Effect  
- C) Color Cycle ✅  
- D) Twinkle Effect  

---

#### 7. What function is responsible for generating colors in the Rainbow Effect?
- A) `color_cycle()`  
- B) `rainbow_cycle()`  
- C) `wheel()` ✅  
- D) `segment_colors()`  

---

#### 8. What happens when you press Ctrl+C while the script is running?
- A) The LEDs stay on indefinitely  
- B) The script ignores the command  
- C) The script gracefully exits and turns off the LEDs ✅  
- D) The script crashes  

---

#### 9. How is brightness controlled in the NeoPixel library?
- A) By changing the voltage of the Raspberry Pi  
- B) Using `pixels.brightness` ✅  
- C) By increasing the delay between color changes  
- D) By using multiple GPIO pins  

---

#### 10. What command is used to install the required NeoPixel library?
- A) `pip install rpi-gpio`  
- B) `pip install ws2812`  
- C) `pip install adafruit-circuitpython-neopixel` ✅  
- D) `pip install neopixel-led`  

---

### 📝 Activity Reflection & Questions

1. Why do WS2812B LEDs only need one GPIO pin for multiple LEDs?  
2. Which lighting effect do you think is the most visually impressive? Why?  
3. What are some real-world applications of NeoPixel-controlled lighting?  
4. If you were to create a new lighting effect, how would it work?  
5. What challenges might arise when using NeoPixels in large installations?  

---

### 📚 Additional Resources

- 🔗 **NeoPixel Guide:** [Adafruit NeoPixel Uber Guide](https://learn.adafruit.com/adafruit-neopixel-uberguide)  
- 🔗 **Raspberry Pi GPIO Documentation:** [RPi.GPIO Library](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)  
- 🔗 **NeoPixel Effects Examples:** [WS2812B Effects](https://www.tweaking4all.com/hardware/arduino/adruino-ws2812-led/)  

---

💡 **Awesome job completing this quiz!** 🚀 Ready to experiment with more LED effects? 😃  
