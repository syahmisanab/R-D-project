import RPi.GPIO as GPIO
import time

# Define GPIO pins based on your custom board
IN1 = 7   # Motor A
IN2 = 6
IN3 = 5   # Motor B
IN4 = 9

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([IN1, IN2, IN3, IN4], GPIO.OUT)

# PWM Setup
pwm_freq = 1000  # Frequency in Hz
pwm1 = GPIO.PWM(IN1, pwm_freq)
pwm2 = GPIO.PWM(IN2, pwm_freq)
pwm3 = GPIO.PWM(IN3, pwm_freq)
pwm4 = GPIO.PWM(IN4, pwm_freq)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

def motorA_forward(speed=50):
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(0)

def motorA_backward(speed=50):
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(speed)

def motorB_forward(speed=50):
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(0)

def motorB_backward(speed=50):
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(speed)

def stop_motors():
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(0)

try:
    print("Motors running...")

    # Move both motors forward at 70% speed
    motorA_forward(70)
    motorB_forward(70)
    time.sleep(2)

    # Move both motors backward at 70% speed
    motorA_backward(70)
    motorB_backward(70)
    time.sleep(2)

    # Stop motors
    stop_motors()

except KeyboardInterrupt:
    print("Stopping motors...")
    stop_motors()
    GPIO.cleanup()
