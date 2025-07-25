#!/usr/bin/env python3
import serial
import time
import sys

# Configure serial port
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

def send_servo_command(angle, duration):
    """Send servo command to Pico"""
    try:
        # Validate parameters
        if not (0 <= angle <= 180):
            print(f"Error: Angle must be between 0-180, got {angle}")
            return False
        
        if duration <= 0:
            print(f"Error: Duration must be positive, got {duration}")
            return False
        
        # Open serial connection
        print(f"Connecting to Pico on {SERIAL_PORT}...")
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=3)
        time.sleep(1)  # Wait for connection
        
        # Create command
        command = f"servo_send({angle},{duration})"
        print(f"Sending command: {command}")
        
        # Send command
        ser.write(f"{command}\n".encode('utf-8'))
        
        # Wait for acknowledgment
        print("Waiting for response...")
        response = ser.readline().decode('utf-8').strip()
        print(f"Pico responded: {response}")
        
        # Check response
        if "SERVO_ACK" in response:
            print(f"✓ Servo moved to {angle}° for {duration}s successfully!")
            success = True
        elif "SERVO_ERROR" in response:
            print(f"✗ Servo command failed - invalid parameters")
            success = False
        elif "SERVO_PARSE_ERROR" in response:
            print(f"✗ Command format error")
            success = False
        else:
            print(f"✗ Unexpected response: {response}")
            success = False
        
        ser.close()
        return success
        
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def interactive_mode():
    """Interactive servo control"""
    print("\n=== Interactive Servo Control ===")
    print("Commands:")
    print("- Enter: angle,duration (e.g., 90,2)")
    print("- 'q' to quit")
    print("- 'center' to move to 90°")
    print("- 'sweep' for demo sweep")
    
    while True:
        try:
            user_input = input("\nEnter command: ").strip().lower()
            
            if user_input == 'q':
                break
            elif user_input == 'center':
                send_servo_command(90, 1)
            elif user_input == 'sweep':
                demo_sweep()
            else:
                # Parse angle,duration
                parts = user_input.split(',')
                if len(parts) == 2:
                    angle = int(parts[0].strip())
                    duration = float(parts[1].strip())
                    send_servo_command(angle, duration)
                else:
                    print("Invalid format. Use: angle,duration (e.g., 90,2)")
        
        except ValueError:
            print("Invalid input. Use numbers only.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

def demo_sweep():
    """Demo servo sweep"""
    print("Running servo sweep demo...")
    positions = [0, 45, 90, 135, 180, 90]
    
    for pos in positions:
        print(f"Moving to {pos}°...")
        if not send_servo_command(pos, 1):
            print("Demo stopped due to error")
            break
        time.sleep(0.5)  # Small delay between moves

def quick_commands():
    """Quick preset commands"""
    commands = {
        '1': (0, 1),      # Left
        '2': (90, 1),     # Center  
        '3': (180, 1),    # Right
        '4': (45, 2),     # Left-center for 2s
        '5': (135, 2),    # Right-center for 2s
    }
    
    print("\n=== Quick Commands ===")
    print("1: Left (0°)")
    print("2: Center (90°)")
    print("3: Right (180°)")
    print("4: Left-center (45°) for 2s")
    print("5: Right-center (135°) for 2s")
    
    choice = input("Select (1-5): ").strip()
    
    if choice in commands:
        angle, duration = commands[choice]
        send_servo_command(angle, duration)
    else:
        print("Invalid choice")

def main():
    if len(sys.argv) == 3:
        # Command line usage: python3 servo_control.py 90 2
        try:
            angle = int(sys.argv[1])
            duration = float(sys.argv[2])
            send_servo_command(angle, duration)
        except ValueError:
            print("Usage: python3 servo_control.py <angle> <duration>")
            print("Example: python3 servo_control.py 90 2")
    
    elif len(sys.argv) == 1:
        # Interactive menu
        print("=== Pico Servo Control ===")
        print("1. Interactive mode")
        print("2. Quick commands")
        print("3. Demo sweep")
        print("4. Center servo")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == '1':
            interactive_mode()
        elif choice == '2':
            quick_commands()
        elif choice == '3':
            demo_sweep()
        elif choice == '4':
            send_servo_command(90, 1)
        else:
            print("Invalid choice")
    else:
        print("Usage:")
        print("  python3 servo_control.py                    # Interactive menu")
        print("  python3 servo_control.py <angle> <duration> # Direct command")
        print("Example:")
        print("  python3 servo_control.py 90 2              # 90° for 2 seconds")

if __name__ == "__main__":
    main()
