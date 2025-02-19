import RPi.GPIO as GPIO
import time
from huskylib import HuskyLensLibrary

# Initialize HuskyLens
hl = HuskyLensLibrary("I2C", address=0x32)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Disable GPIO warnings
LEFT_FWD = 9  
LEFT_BWD = 20   
RIGHT_FWD = 6  
RIGHT_BWD = 5  

GPIO.setup([LEFT_FWD, LEFT_BWD, RIGHT_FWD, RIGHT_BWD], GPIO.OUT)

# PWM Setup
pwm_freq = 1000
pwm_LF = GPIO.PWM(LEFT_FWD, pwm_freq)
pwm_LB = GPIO.PWM(LEFT_BWD, pwm_freq)
pwm_RF = GPIO.PWM(RIGHT_FWD, pwm_freq)
pwm_RB = GPIO.PWM(RIGHT_BWD, pwm_freq)

pwm_LF.start(0)
pwm_LB.start(0)
pwm_RF.start(0)
pwm_RB.start(0)

# Motor Control Functions
def move_forward(speed=10):
    pwm_LF.ChangeDutyCycle(speed)
    pwm_LB.ChangeDutyCycle(0)
    pwm_RF.ChangeDutyCycle(speed)
    pwm_RB.ChangeDutyCycle(0)

def move_left(speed=10):
    pwm_LF.ChangeDutyCycle(0)
    pwm_LB.ChangeDutyCycle(0)
    pwm_RF.ChangeDutyCycle(speed)
    pwm_RB.ChangeDutyCycle(0)

def move_right(speed=10):
    pwm_LF.ChangeDutyCycle(speed)
    pwm_LB.ChangeDutyCycle(0)
    pwm_RF.ChangeDutyCycle(0)
    pwm_RB.ChangeDutyCycle(0)

def move_backwards(speed=10):
    pwm_LF.ChangeDutyCycle(0)
    pwm_LB.ChangeDutyCycle(speed)
    pwm_RF.ChangeDutyCycle(0)
    pwm_RB.ChangeDutyCycle(speed)

def stop_motors():
    pwm_LF.ChangeDutyCycle(0)
    pwm_LB.ChangeDutyCycle(0)
    pwm_RF.ChangeDutyCycle(0)
    pwm_RB.ChangeDutyCycle(0)

def detect_obstacle():
    blocks = hl.blocks()
    if blocks:
        return True
    return False

def avoid_obstacle():
    print("Obstacle detected. Avoiding...")
    move_backwards(50)
    time.sleep(1)  # Move backward for a short time
    move_right(60)   # Turn right (or left) to avoid the obstacle
    time.sleep(1)  # Adjust turn time based on your setup
    move_forward(70) # Continue moving forward after avoiding

try:
    while True:
        if detect_obstacle():
            avoid_obstacle()
        else:
            arrow = hl.arrows()  # Get detected arrow
            
            if arrow is None:
                print("No arrow detected")
                stop_motors()
            else:
                print(f"Arrow detected: {arrow}")
                if arrow.xTail > arrow.xHead:  # Turning left
                    move_left(60)
                elif arrow.xTail < arrow.xHead:  # Turning right
                    move_right(60)
                else:  # Move forward
                    move_forward(70)
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping motors...")
    stop_motors()
    GPIO.cleanup()
