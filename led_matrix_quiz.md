## 📝 LED Matrix (MAX7219) Quiz  

**1. What communication protocol does the MAX7219 use to interface with a microcontroller?**  
- A) I2C  
- B) SPI  
- C) UART  
- D) PWM  
✅**Answer: B) SPI**  

**2. How many 8x8 LED matrices can a single MAX7219 control?**  
- A) 1  
- B) 4  
- C) 8  
- D) 64  
✅**Answer: A) 1**  

**3. What function is used to draw individual pixels on an LED matrix using the Luma library?**  
- A) draw.line()  
- B) draw.circle()  
- C) draw.point()  
- D) draw.pixel()  
✅**Answer: C) draw.point()**  

**4. Which of the following is NOT an advantage of using the MAX7219 driver?**  
- A) Simplifies LED matrix control  
- B) Requires fewer GPIO pins  
- C) Uses complex wiring with resistors  
- D) Supports daisy-chaining multiple matrices  
✅**Answer: C) Uses complex wiring with resistors**  

**5. What will the following Python code do when executed?**  
```python
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, rotate=0)

with canvas(device) as draw:
    draw.rectangle((0, 0, 7, 7), outline="white")
```  
- A) Display a filled square  
- B) Display an empty square (border only)  
- C) Display a cross  
- D) Display nothing  
✅**Answer: B) Display an empty square (border only)**  

**6. What function can be used to display scrolling text using the Luma library?**  
- A) display_scroll()  
- B) show_message()  
- C) text_scroll()  
- D) draw.text()  
✅**Answer: B) show_message()**  

**7. What does the `contrast()` function in the Luma library control?**  
- A) Scrolling speed  
- B) Display brightness  
- C) Refresh rate  
- D) Number of matrices in a chain  
✅**Answer: B) Display brightness**  

**8. If an LED matrix display shows distorted or missing patterns, what could be the cause?**  
- A) Incorrect SPI connections  
- B) Low power supply voltage  
- C) A faulty MAX7219 chip  
- D) All of the above  
✅**Answer: D) All of the above**  

**9. What will be displayed when running the following code?**  
```python
with canvas(device) as draw:
    for x in range(8):
        draw.point((x, x), fill="white")
```  
- A) A horizontal line  
- B) A vertical line  
- C) A diagonal line from top-left to bottom-right  
- D) A random pattern of dots  
✅**Answer: C) A diagonal line from top-left to bottom-right**  

**10. What is missing from this code that prevents it from displaying text on the LED matrix?**  
```python
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, rotate=0)

show_message(device, "HELLO", fill="white")
```  
- A) The `font` parameter is missing  
- B) The `scroll_delay` parameter is missing  
- C) The `canvas` function is missing  
- D) The `fill` parameter should be "black" instead of "white"  
✅**Answer: A) The `font` parameter is missing**  
