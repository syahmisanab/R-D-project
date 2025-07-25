# main.py - IP receiver with OLED display and Servo control
import sys
import time
from machine import Pin, SoftI2C, PWM
import ssd1306

# Initialize I2C and OLED
i2c = SoftI2C(sda=Pin(4), scl=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize Servo on GP15
class Servo:
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(50)  # 50Hz for servo control
        self.current_angle = 90  # Track current position
    
    def write_angle(self, angle):
        """Move servo to specific angle (0-180 degrees)"""
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180
        
        # Convert angle to duty cycle
        pulse_width = 1 + (angle / 180)  # 1ms to 2ms
        duty = int((pulse_width / 20) * 65535)
        self.pwm.duty_u16(duty)
        self.current_angle = angle
    
    def get_angle(self):
        return self.current_angle

# Initialize servo
servo = Servo(15)
servo.write_angle(90)  # Start at center position

def display_message(title, message, line2="", line3=""):
    """Display formatted message on OLED"""
    oled.fill(0)
    oled.text(title, 0, 0)
    oled.text(message, 0, 10)
    if line2:
        oled.text(line2, 0, 20)
    if line3:
        oled.text(line3, 0, 30)
    oled.show()

def validate_ip(ip_str):
    """Simple IP validation"""
    try:
        parts = ip_str.split('.')
        if len(parts) == 4:
            for part in parts:
                num = int(part)
                if not (0 <= num <= 255):
                    return False
            return True
    except:
        pass
    return False

def parse_servo_command(command):
    """Parse servo command: servo_send(90,2)"""
    try:
        # Remove 'servo_send(' and ')'
        if command.startswith('servo_send(') and command.endswith(')'):
            params = command[11:-1]  # Remove 'servo_send(' and ')'
            parts = params.split(',')
            if len(parts) == 2:
                angle = int(parts[0].strip())
                duration = float(parts[1].strip())
                return angle, duration
    except:
        pass
    return None, None

def format_ip_for_display(ip):
    """Format IP for better OLED display"""
    if len(ip) > 12:  # If IP is long, split it
        parts = ip.split('.')
        line1 = f"{parts[0]}.{parts[1]}"
        line2 = f"{parts[2]}.{parts[3]}"
        return line1, line2
    return ip, ""

def handle_servo_command(angle, duration):
    """Handle servo movement command"""
    if 0 <= angle <= 180 and duration > 0:
        # Display servo action on OLED
        display_message("Servo Command:", f"Angle: {angle}", f"Duration: {duration}s", "Moving...")
        
        # Move servo
        servo.write_angle(angle)
        
        # Wait for specified duration
        start_time = time.time()
        while time.time() - start_time < duration:
            time.sleep(0.1)
        
        # Show completion
        display_message("Servo Done:", f"Held {angle} deg", f"for {duration}s", "Ready...")
        
        return True
    return False

# Initial display
display_message("Pico Ready", "IP & Servo", "Control", "Waiting...")
sys.stdout.write("PICO READY\n")

received_ip = None

while True:
    line = sys.stdin.readline()
    if not line:
        time.sleep(0.1)
        continue
    
    line = line.strip()
    
    if line:
        # Echo back for debugging
        sys.stdout.write("GOT:" + line + "\n")
        
        # Check if it's a servo command
        if line.startswith('servo_send('):
            angle, duration = parse_servo_command(line)
            if angle is not None and duration is not None:
                if handle_servo_command(angle, duration):
                    sys.stdout.write("SERVO_ACK\n")
                else:
                    display_message("Servo Error:", "Invalid params", f"A:{angle} D:{duration}", "Try again...")
                    sys.stdout.write("SERVO_ERROR\n")
            else:
                display_message("Servo Error:", "Parse failed", line[:12], "Check format")
                sys.stdout.write("SERVO_PARSE_ERROR\n")
        
        # Check if it's an IP address
        elif validate_ip(line):
            received_ip = line
            line1, line2 = format_ip_for_display(line)
            
            # Display IP on OLED
            display_message("IP Received:", line1, line2, "Status: OK")
            
            # Send acknowledgment
            sys.stdout.write("IP_ACK\n")
        
        # Unknown command
        else:
            display_message("Unknown Cmd:", line[:12], "Supported:", "IP or servo_send")
            sys.stdout.write("UNKNOWN_CMD\n")
    
    time.sleep(0.1)
