# Servo control on GP15
import machine
import time

class Servo:
    def __init__(self, pin):
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(50)  # 50Hz for servo control
    
    def write_angle(self, angle):
        """Move servo to specific angle (0-180 degrees)"""
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180
        
        # Convert angle to duty cycle
        # Standard servo: 1ms = 0°, 1.5ms = 90°, 2ms = 180°
        # Duty cycle = (pulse_width_ms / 20ms) * 65535
        pulse_width = 1 + (angle / 180)  # 1ms to 2ms
        duty = int((pulse_width / 20) * 65535)
        self.pwm.duty_u16(duty)
    
    def write_microseconds(self, microseconds):
        """Move servo using microsecond pulse width (500-2500μs)"""
        if microseconds < 500:
            microseconds = 500
        elif microseconds > 2500:
            microseconds = 2500
        
        duty = int((microseconds / 20000) * 65535)
        self.pwm.duty_u16(duty)
    
    def deinit(self):
        """Stop PWM"""
        self.pwm.deinit()

# Initialize servo on GP15
servo = Servo(15)

# Example usage functions
def servo_sweep():
    """Sweep servo from 0 to 180 degrees and back"""
    print("Sweeping servo...")
    
    # Sweep forward
    for angle in range(0, 181, 5):
        servo.write_angle(angle)
        time.sleep(0.05)
    
    time.sleep(0.5)
    
    # Sweep backward
    for angle in range(180, -1, -5):
        servo.write_angle(angle)
        time.sleep(0.05)

def servo_positions():
    """Move servo to specific positions"""
    positions = [0, 45, 90, 135, 180, 90]
    
    print("Moving to specific positions...")
    for pos in positions:
        print(f"Moving to {pos}°")
        servo.write_angle(pos)
        time.sleep(1)

def servo_center():
    """Center the servo at 90 degrees"""
    print("Centering servo...")
    servo.write_angle(90)

# Main program
if __name__ == "__main__":
    try:
        print("Servo control on GP15")
        print("Centering servo...")
        servo_center()
        time.sleep(2)
        
        # Uncomment the function you want to test:
        
        # Test 1: Sweep servo
        servo_sweep()
        
        # Test 2: Specific positions
        # servo_positions()
        
        # Test 3: Manual control
        # servo.write_angle(45)   # Move to 45 degrees
        # time.sleep(2)
        # servo.write_angle(135)  # Move to 135 degrees
        
        print("Done!")
        
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        servo.deinit()  # Clean up PWM
