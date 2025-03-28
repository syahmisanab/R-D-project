# I2C LCD Display: Advanced Functionality Guide

## Overview
This guide provides various Python functions to expand the capabilities of an I2C LCD display beyond simple text display.

## Prerequisites
- Raspberry Pi
- I2C LCD Module
- `smbus2` library
- `time` library
- Basic LCD initialization code

## Function Examples

### 1. Multiple Line Display
```python
def lcd_display_lines(line1, line2=""):
    """Display text on two LCD lines"""
    lcd_byte(0x80, LCD_CMD)  # First line
    for char in line1:
        lcd_byte(ord(char), LCD_CHR)
    
    lcd_byte(0xC0, LCD_CMD)  # Second line
    for char in line2:
        lcd_byte(ord(char), LCD_CHR)
```

### 2. Text Scrolling
```python
def lcd_scroll_text(text, delay=0.3):
    """Scroll text across the LCD screen"""
    text = text + " " * 16  # Add padding
    for i in range(len(text) - 15):
        lcd_clear()
        lcd_byte(0x80, LCD_CMD)
        for char in text[i:i+16]:
            lcd_byte(ord(char), LCD_CHR)
        time.sleep(delay)
```

### 3. Sensor Data Display
```python
def display_temperature():
    """Display temperature from a sensor"""
    temp = round(random.uniform(20.0, 35.0), 1)
    lcd_display(f"Temp: {temp}°C")
```

### 4. Date and Time Display
```python
def display_datetime():
    """Show current date and time"""
    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")
    
    lcd_display_lines(date_str, time_str)
```

### 5. Blinking Text
```python
def lcd_blink_text(text, blinks=3):
    """Create a blinking text effect"""
    for _ in range(blinks):
        lcd_display(text)
        time.sleep(0.5)
        lcd_clear()
        time.sleep(0.5)
```

### 6. IP Address Display
```python
def display_ip_address():
    """Show the device's IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        lcd_display(f"IP: {ip}")
        s.close()
    except Exception:
        lcd_display("No Network")
```

### 7. Progress Bar Simulation
```python
def display_progress(percentage):
    """Display a simple progress bar"""
    bar = "#" * int(percentage / 10)
    lcd_display(f"Progress:{bar}")
```

## Practical Considerations
- Implement robust error handling
- Adapt functions to your specific hardware
- Consider adding logging for debugging
- Ensure proper I2C communication

## Recommended Libraries
- `smbus2` for I2C communication
- `datetime` for time-related functions
- `socket` for network information
- `random` for simulation (replace with actual sensor libraries)

## Potential Expansions
- Integrate with GPIO for button interactions
- Add custom character creation
- Implement menu systems
- Connect with various sensors

## Safety and Best Practices
- Always include proper initialization
- Handle keyboard interrupts
- Close resources when not in use
- Use try-except blocks for error management

## Troubleshooting
- Verify I2C address
- Check wire connections
- Ensure proper power supply
- Update Raspberry Pi and libraries regularly

## Example Usage
```python
lcd_init()
display_datetime()
time.sleep(2)
display_ip_address()
```

## Conclusion
These functions demonstrate the versatility of I2C LCD displays. Experiment, adapt, and create unique display interactions for your projects!
