import cv2
import numpy as np
import time
from motor_driver import MotorDriver

# === Initialize Motor Driver ===
md = MotorDriver(port="/dev/ttyUSB0", motor_type=2, upload_data=1)

# === Motor Control Functions ===
def forward(speed=400):
    md.control_speed(speed, speed, speed, speed)

def backward(speed=400):
    md.control_speed(-speed, -speed, -speed, -speed)

def left(speed=200):
    md.control_speed(0, 0, speed, speed)

def right(speed=200):
    md.control_speed(speed, speed, 0, 0)

def spin_left(speed=700):
    md.control_speed(-speed, -speed, speed, speed)

def spin_right(speed=700):
    md.control_speed(speed, speed, -speed, -speed)

def brake():
    print("Brake activated")
    md.send_data("$upload:0,0,0#")
    md.control_pwm(0, 0, 0, 0)
    time.sleep(0.05)
    md.control_speed(0, 0, 0, 0)

# === Kamera Setup ===
def main():
    cap = cv2.VideoCapture(0)
    time.sleep(2)

    U_TURN_DURATION_BOTH = 15.0
    U_TURN_SPEED = 900

    # --- Tambah Pembolehubah Last Seen ---
    last_seen_cx = None  # Akan menyimpan kedudukan X pusat garisan terakhir
    # Threshold untuk menentukan berapa lama robot akan teruskan dengan "last seen"
    # Atau berapa banyak frame ia akan tunggu sebelum declare hilang
    LOST_LINE_THRESHOLD_FRAMES = 10 # Contoh: berapa banyak frame garisan boleh hilang sebelum robot panik
    lost_line_counter = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("? Kamera tidak dikesan")
                break

            frame = cv2.resize(frame, (320, 240))
            roi = frame[100:260, :]
            debug_roi = roi.copy()
            
            # --- Line Following Logic ---
            hsv_line = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            lower_line = np.array([0, 0, 0])
            upper_line = np.array([179, 79, 73])
            thresh_line = cv2.inRange(hsv_line, lower_line, upper_line)

            M_line = cv2.moments(thresh_line)
            center_frame = frame.shape[1] // 2

            line_detected_current_frame = False
            if M_line["m00"] > 0:
                cx_line = int(M_line["m10"] / M_line["m00"])
                line_detected_current_frame = True
                last_seen_cx = cx_line  # Update last seen position
                lost_line_counter = 0 # Reset counter if line is seen

                # Pergerakan jika garisan dikesan
                if cx_line < center_frame - 30:
                    print("? Kiri (line)")
                    left(300)
                elif cx_line > center_frame + 30:
                    print("? Kanan (line)")
                    right(300)
                else:
                    print("? Tengah (line)")
                    forward(200)

                if cx_line < center_frame - 70:
                    print("?? Line too far left")
                    spin_left(900)
                elif cx_line > center_frame + 70:
                    print("?? Line too far right")
                    spin_right(900)

                cv2.line(debug_roi, (center_frame, 0), (center_frame, debug_roi.shape[0]), (0, 255, 255), 2)
                cv2.rectangle(debug_roi, (cx_line - 5, 0), (cx_line + 5, 10), (0, 255, 0), 2)
                cv2.line(debug_roi, (center_frame, debug_roi.shape[0] // 2), (cx_line, 5), (255, 255, 0), 1)
            else:
                # --- Logik "Last Seen" jika garisan tidak dikesan pada frame semasa ---
                lost_line_counter += 1
                if last_seen_cx is not None and lost_line_counter < LOST_LINE_THRESHOLD_FRAMES:
                    print(f"? Garisan hilang, menggunakan last_seen_cx: {last_seen_cx}")
                    # Teruskan bergerak mengikut arah last_seen_cx
                    if last_seen_cx < center_frame: # Jika garisan terakhir di kiri, teruskan pusing kiri
                        left(200)
                    else: # Jika garisan terakhir di kanan, teruskan pusing kanan
                        right(200)
                else:
                    # Jika garisan hilang terlalu lama atau tidak pernah dikesan
                    print("? Tiada garis dikesan (lama) atau tidak pernah dikesan")  
                    backward(200)
                    time.sleep(0.7)
                    brake()

            # --- Detect Green Marker(s) (Logik ini kekal sama) ---
            hsv_green = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            lower_green = np.array([69, 71, 0])
            upper_green = np.array([98, 255, 255])
            mask_green = cv2.inRange(hsv_green, lower_green, upper_green)

            contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            green_marker_positions = []
            for cnt in contours_green:
                area = cv2.contourArea(cnt)
                if area > 300:
                    M_green = cv2.moments(cnt)
                    if M_green["m00"] > 0:
                        cx_green = int(M_green["m10"] / M_green["m00"])
                        green_marker_positions.append(cx_green)

                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(debug_roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(debug_roi, "Green", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            # --- Green Marker Decision Logic (Kekal sama) ---
            if len(green_marker_positions) >= 2:
                left_marker_found = False
                right_marker_found = False
                
                for pos in green_marker_positions:
                    if pos < center_frame - 40:
                        left_marker_found = True
                    elif pos > center_frame + 40:
                        right_marker_found = True
                
                if left_marker_found and right_marker_found:
                    print("?? Both Green markers detected - Performing 180-degree U-turn!")
                    brake()
                    spin_right(U_TURN_SPEED)
                    time.sleep(U_TURN_DURATION_BOTH)
                    brake()
                elif left_marker_found:
                    print("?? Green detected on left (single) - adjusting")
                    spin_left(U_TURN_SPEED)
                    time.sleep(0.4)
                    brake()
                    # forward(300)
                    # time.sleep(0.4)
                    # brake()
                elif right_marker_found:
                    print("?? Green detected on right (single) - adjusting")
                    spin_right(U_TURN_SPEED)
                    time.sleep(0.4)
                    brake()
                    # forward(300)
                    # time.sleep(0.4)
                    # brake()

            elif len(green_marker_positions) == 1:
                cx_green_single = green_marker_positions[0]
                if cx_green_single < center_frame - 40:
                    print("?? Green on left - Spin left")
                    #spin_left(400)
                    #time.sleep(0.4)
                    #brake()
                    forward(300)
                    time.sleep(0.4)
                    brake()
                    spin_left(900)
                    time.sleep(0.3)
                    brake()
                elif cx_green_single > center_frame + 40:
                    print("?? Green on right - Spin right")
                    #spin_right(400)
                    #time.sleep(0.4)
                    #brake()
                    forward(300)
                    time.sleep(0.4)
                    brake()
                    spin_right(900)
                    time.sleep(0.3)
                    brake()
            combined_debug = np.hstack((cv2.cvtColor(thresh_line, cv2.COLOR_GRAY2BGR), roi, cv2.cvtColor(mask_green, cv2.COLOR_GRAY2BGR)))
            cv2.imshow("Debug View [Thresh | ROI | Green Mask]", combined_debug)
            cv2.imshow("Overlay Debug View", debug_roi)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")

    finally:
        brake()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
