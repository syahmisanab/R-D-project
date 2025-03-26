#!/usr/bin/env python3

import time
from gpiozero import LightSensor

# Define LDR sensor on GPIO 4
ldr = LightSensor(4)

def main():
    """Continuously monitor light levels."""
    try:
        while True:
            if ldr.light_detected:
                print("💡 Light Detected!")
            else:
                print("🌑 No Light Detected!")

            time.sleep(0.1)  # Small delay to prevent spam

    except KeyboardInterrupt:
        print("\n[INFO] Program interrupted by user.")

if __name__ == '__main__':
    main()
