import cv2
from ultralytics import YOLO
import pygame
import time

# load YOLO model
model = YOLO("yolov8n.pt")

# alert sound
pygame.mixer.init()
alert = pygame.mixer.Sound("alert.wav")

# webcam
cap = cv2.VideoCapture(0)

# variables
prev_frame = None
fight_frames = 0
alert_cooldown = 0 

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # ---------------- MOTION DETECTION ----------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    motion_detected = False

    if prev_frame is not None:
        frame_diff = cv2.absdiff(prev_frame, gray)
        thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]

        motion_area = cv2.countNonZero(thresh)

        if motion_area > 12000:  # adjust based on camera
            motion_detected = True

    prev_frame = gray

    # ---------------- YOLO DETECTION ----------------
    results = model(frame)

    weapon_detected = False
    persons = []

    for r in results:
        boxes = r.boxes

        for box in boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # store persons
            if label == "person":
                persons.append((x1, y1, x2, y2))

            # weapon detection
            if label in ["knife", "gun"]:
                weapon_detected = True

            # draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # ---------------- WEAPON ALERT ----------------
    if weapon_detected:
        cv2.putText(frame, "WEAPON DETECTED", (40, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        if time.time() - alert_cooldown > 3:
            alert.play()
            alert_cooldown = time.time()

    # ---------------- FIGHT DETECTION ----------------
    fight_detected = False

    if len(persons) >= 2:
        for i in range(len(persons)):
            for j in range(i + 1, len(persons)):

                x1, y1, x2, y2 = persons[i]
                a1, b1, a2, b2 = persons[j]

                overlap_x = max(0, min(x2, a2) - max(x1, a1))
                overlap_y = max(0, min(y2, b2) - max(y1, b1))
                overlap_area = overlap_x * overlap_y

                if overlap_area > 5000 and motion_detected:
                    fight_detected = True

    # ---------------- SMART FILTER ----------------
    if fight_detected:
        fight_frames += 1
    else:
        fight_frames = 0

    if fight_frames > 5:
        cv2.putText(frame, "FIGHT DETECTED", (40, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        if time.time() - alert_cooldown > 3:
            alert.play()
            alert_cooldown = time.time()

    # ---------------- DISPLAY ----------------
    cv2.imshow("Campus Safety AI", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()