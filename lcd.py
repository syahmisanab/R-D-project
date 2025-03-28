import time
import smbus2
import signal

# I2C address of LCD (default is 0x27 or 0x3F, check your LCD module)
LCD_ADDR = 0x27  
bus = smbus2.SMBus(1)

# LCD commands
LCD_CHR = 1  # Data mode
LCD_CMD = 0  # Command mode
LCD_BACKLIGHT = 0x08  # Backlight ON
ENABLE = 0b00000100  # Enable bit

# Function to send command to LCD
def lcd_byte(bits, mode):
    high_bits = mode | (bits & 0xF0) | LCD_BACKLIGHT
    low_bits = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT
    bus.write_byte(LCD_ADDR, high_bits)
    bus.write_byte(LCD_ADDR, high_bits | ENABLE)
    time.sleep(0.0005)
    bus.write_byte(LCD_ADDR, high_bits & ~ENABLE)
    bus.write_byte(LCD_ADDR, low_bits)
    bus.write_byte(LCD_ADDR, low_bits | ENABLE)
    time.sleep(0.0005)
    bus.write_byte(LCD_ADDR, low_bits & ~ENABLE)

# Function to initialize LCD
def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Turn on display, no cursor
    lcd_byte(0x28, LCD_CMD)  # 2 lines, 5x8 font
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)

# Function to display text on LCD
def lcd_display(text):
    lcd_byte(0x80, LCD_CMD)  # Move to first line
    for char in text:
        lcd_byte(ord(char), LCD_CHR)

# Function to clear LCD
def lcd_clear():
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.2)

# Signal handler to clear LCD on Ctrl+C
def signal_handler(sig, frame):
    print("\nClearing LCD and exiting...")
    lcd_clear()
    exit(0)

# Attach signal handler
signal.signal(signal.SIGINT, signal_handler)

# Main function
if __name__ == "__main__":
    lcd_init()
    lcd_display("autobotic")
    
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        pass
