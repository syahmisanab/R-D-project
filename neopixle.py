#use "sudo python3"

#!/usr/bin/env python3
import time
import board
import neopixel

# LED Strip Configuration
LED_PIN = board.D18  # GPIO 18
NUM_LEDS = 8         # Change this to the number of LEDs you have
BRIGHTNESS = 0.5     # Brightness (0.0 - 1.0)
ORDER = neopixel.GRB # Color order for WS2812B

# Initialize LED strip
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER)

# Function to cycle colors
def color_cycle(wait=0.5):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
    for color in colors:
        pixels.fill(color)
        pixels.show()
        time.sleep(wait)

# Main loop
try:
    while True:
        color_cycle()

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))  # Turn off LEDs on exit
    pixels.show()
    print("\nLEDs turned off. Exiting...")
