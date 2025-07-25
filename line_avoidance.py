# smart_line_follow_full.py

import cv2
import numpy as np
import time

from gpiozero import DistanceSensor
from motor_driver import MotorDriver
from robot_corner import run_corner_sequence  # your corner routine

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

# === Ultrasonic Setup ===
# TRIG → BCM 24, ECHO → BCM 23
ultra = DistanceSensor(trigger=24, echo=23, max_distance=2.0)
OBSTACLE_THRESHOLD_CM = 5.0

def main():
    cap = cv2.VideoCapture(0)
    time.sleep(2)

    U_TURN_DURATION_BOTH = 15.0
    U_TURN_SPEED = 900

    # Last‑seen logic for line loss
    last_seen_cx = None
    LOST_LINE_THRESHOLD_FRAMES = 10
    lost_line_counter = 0

    try:
        while True:
            # ——————————————————————————————
            # 1) Obstacle check (highest priority)
            dist_cm = ultra.distance * 100.0
            if dist_cm is not None and dist_cm < OBSTACLE_THRESHOLD_CM:
                print(f"[!] Obstacle at {dist_cm:.1f} cm — corner avoidance")
                brake()
                run_corner_sequence()
                print("[✓] Maneuver complete; resuming line follow")
                # give sensors/motors a moment to settle
                time.sleep(0.2)
                last_seen_cx = None
                lost_line_counter = 0
                continue
            # ——————————————————————————————

            # 2) Grab camera frame
            ret, frame = cap.read()
            if not ret:
                print("⚠️  Camera not detected")
                break

            frame = cv2.resize(frame, (320, 240))
            roi = frame[100:260, :]
            debug_roi = roi.copy()

            # ——————————————————————————————
            # 3) Line‑following logic
            hsv_line = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            lower_line = np.array([0, 0, 0])
            upper_line = np.array([179, 79, 73])
            thresh_line = cv2.inRange(hsv_line, lower_line, upper_line)

            M_line = cv2.moments(thresh_line)
            center_frame = frame.shape[1] // 2

            if M_line["m00"] > 0:
                cx_line = int(M_line["m10"] / M_line["m00"])
                last_seen_cx = cx_line
                lost_line_counter = 0

                # Steering based on line position
                if cx_line < center_frame - 30:
                    print("← Line left")
                    left(300)
                elif cx_line > center_frame + 30:
                    print("→ Line right")
                    right(300)
                else:
                    print("↓ Line center")
                    forward(200)

                # Sharper correction if very far off
                if cx_line < center_frame - 70:
                    print("↺ Spin left")
                    spin_left(900)
                elif cx_line > center_frame + 70:
                    print("↻ Spin right")
                    spin_right(900)

                # Debug drawing
                cv2.line(debug_roi,
                         (center_frame, 0),
                         (center_frame, debug_roi.shape[0]),
                         (0, 255, 255), 2)
                cv2.rectangle(debug_roi,
                              (cx_line - 5, 0),
                              (cx_line + 5, 10),
                              (0, 255, 0), 2)
                cv2.line(debug_roi,
                         (center_frame, debug_roi.shape[0] // 2),
                         (cx_line, 5),
                         (255, 255, 0), 1)

            else:
                # Line not detected this frame
                lost_line_counter += 1
                if last_seen_cx is not None and lost_line_counter < LOST_LINE_THRESHOLD_FRAMES:
                    print(f"– Line lost, using last_seen_cx={last_seen_cx}")
                    if last_seen_cx < center_frame:
                        left(200)
                    else:
                        right(200)
                else:
                    print("✖️ Line gone too long or never seen → back & brake")
                    backward(200)
                    time.sleep(0.7)
                    brake()
            # ——————————————————————————————

            # ——————————————————————————————
            # 4) Green‑marker logic (exactly your original code)
            hsv_green = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            lower_green = np.array([69, 71, 0])
            upper_green = np.array([98, 255, 255])
            mask_green = cv2.inRange(hsv_green, lower_green, upper_green)

            contours_green, _ = cv2.findContours(
                mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            green_marker_positions = []
            for cnt in contours_green:
                area = cv2.contourArea(cnt)
                if area > 300:
                    M_green = cv2.moments(cnt)
                    if M_green["m00"] > 0:
                        cx_green = int(M_green["m10"] / M_green["m00"])
                        green_marker_positions.append(cx_green)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(debug_roi, (x, y), (x + w, y + h),
                                      (0, 255, 0), 2)
                        cv2.putText(debug_roi, "Green", (x, y - 5),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 1)

            if len(green_marker_positions) >= 2:
                left_found = any(p < center_frame - 40 for p in green_marker_positions)
                right_found = any(p > center_frame + 40 for p in green_marker_positions)
                if left_found and right_found:
                    print("⟲ Both green → U-turn")
                    brake()
                    spin_right(U_TURN_SPEED)
                    time.sleep(U_TURN_DURATION_BOTH)
                    brake()
                elif left_found:
                    print("↺ Green left only → adjust left")
                    spin_left(U_TURN_SPEED)
                    time.sleep(0.4)
                    brake()
                elif right_found:
                    print("↻ Green right only → adjust right")
                    spin_right(U_TURN_SPEED)
                    time.sleep(0.4)
                    brake()

            elif len(green_marker_positions) == 1:
                cxg = green_marker_positions[0]
                if cxg < center_frame - 40:
                    print("↺ Single green left → carve left")
                    forward(300)
                    time.sleep(0.4)
                    brake()
                    spin_left(900)
                    time.sleep(0.3)
                    brake()
                elif cxg > center_frame + 40:
                    print("↻ Single green right → carve right")
                    forward(300)
                    time.sleep(0.4)
                    brake()
                    spin_right(900)
                    time.sleep(0.3)
                    brake()
            # ——————————————————————————————

            # 5) Display debug
            combined_debug = np.hstack((
                cv2.cvtColor(thresh_line, cv2.COLOR_GRAY2BGR),
                roi,
                cv2.cvtColor(mask_green, cv2.COLOR_GRAY2BGR)
            ))
            cv2.imshow("Debug View [Thresh|ROI|Green]", combined_debug)
            cv2.imshow("Overlay Debug", debug_roi)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Program stopped by user")

    finally:
        brake()
        cap.release()
        cv2.destroyAllWindows()
        ultra.close()

if __name__ == "__main__":
    main()
