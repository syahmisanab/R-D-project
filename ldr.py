#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

# Define the GPIO pin for the LDR
LDR_GPIO = 4

if __name__ == '__main__':
    # Set up GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    # Set up the LDR GPIO pin as input
    GPIO.setup(LDR_GPIO, GPIO.IN)

    pressed = False

    try:
        while True:
            # Check if the LDR is detecting light
            if not GPIO.input(LDR_GPIO):
                if not pressed:
                    print("Light Detected!")
                    pressed = True
            else:
                pressed = False

            # Sleep for a short period to debounce
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Clean up GPIO settings on program interruption
        print("\nProgram interrupted")

    finally:
        GPIO.cleanup()
        print("GPIO cleanup complete")
