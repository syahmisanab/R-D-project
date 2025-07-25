#!/usr/bin/env python3
import serial
import time
import socket
import subprocess

# Configure serial port
SERIAL_PORT = '/dev/ttyACM0'  # Updated to ACM0
BAUD_RATE = 115200

def get_ip_address():
    """Get the actual IP address of the Raspberry Pi"""
    try:
        # Connect to external server to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "No IP"

def get_wifi_ssid():
    """Get current WiFi SSID"""
    try:
        result = subprocess.check_output(
            ["iwconfig", "wlan0"],
            stderr=subprocess.DEVNULL
        ).decode()
        for line in result.splitlines():
            if "ESSID" in line:
                ssid = line.split("ESSID:")[1].strip().strip('"')
                return ssid if ssid else "No SSID"
        return "No SSID"
    except Exception:
        return "No SSID"

def wait_for_network(timeout=30):
    """Wait until the Pi has a network connection or timeout"""
    print("Waiting for network connection...")
    for i in range(timeout):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            s.close()
            print(f"Network connected after {i+1} seconds")
            return True
        except:
            time.sleep(1)
            if i % 5 == 0:  # Print status every 5 seconds
                print(f"Still waiting... ({i}/{timeout})")
    return False

def send_ip_address():
    try:
        # Wait for network first
        if not wait_for_network(timeout=30):
            print("No network connection found!")
            return
        
        # Get actual IP address
        ip_address = get_ip_address()
        ssid = get_wifi_ssid()
        
        print(f"Network: {ssid}")
        print(f"IP Address: {ip_address}")
        
        if ip_address == "No IP":
            print("Could not get IP address!")
            return
        
        # Open serial connection
        print(f"Connecting to Pico on {SERIAL_PORT}...")
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        time.sleep(2)  # Wait for connection to stabilize
        
        # Wait for Pico ready signal
        print("Waiting for Pico ready signal...")
        ready_received = False
        for _ in range(10):  # Wait up to 10 seconds
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                print(f"Pico says: {response}")
                if "PICO READY" in response:
                    ready_received = True
                    break
            time.sleep(1)
        
        if not ready_received:
            print("Warning: Didn't receive Pico ready signal, sending anyway...")
        
        print(f"Sending IP address: {ip_address}")
        
        # Send IP address with newline terminator
        message = f"{ip_address}\n"
        ser.write(message.encode('utf-8'))
        
        # Wait for acknowledgment
        print("Waiting for acknowledgment...")
        for _ in range(5):  # Wait up to 5 seconds for ACK
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                print(f"Pico responded: {response}")
                if "IP_ACK" in response:
                    print("✓ IP address received successfully by Pico!")
                    break
                elif "IP_ERROR" in response:
                    print("✗ Pico reported IP format error!")
                    break
            time.sleep(1)
        
        ser.close()
        print("Serial communication completed!")
        
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        print("Make sure:")
        print("1. Pico is connected via USB")
        print("2. No other program is using the serial port")
        print("3. You have permission to access the serial port")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_ip_address()
