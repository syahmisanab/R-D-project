import RPi.GPIO as GPIO
import time

# GPIO Pin Definitions
IN1 = 17  # Motor A
IN2 = 18
IN3 = 22  # Motor B
IN4 = 23

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
    
    motorA_forward(70)
    motorB_forward(70)
    time.sleep(2)

    motorA_backward(70)
    motorB_backward(70)
    time.sleep(2)

    stop_motors()
    
except KeyboardInterrupt:
    print("Stopping motors...")
    stop_motors()
    GPIO.cleanup()
