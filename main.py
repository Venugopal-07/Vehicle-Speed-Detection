import cv2
import time
from utils import get_center
from speed_calculation import calculate_speed
from config import MIN_WIDTH, MIN_HEIGHT

# ===============================
# CAMERA SETUP
# ===============================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Camera opened:", cap.isOpened())
if not cap.isOpened():
    exit()

# Camera warm-up
time.sleep(2)

# ===============================
# VIDEO RECORDING SETUP
# ===============================
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(
    "recorded_output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    20,
    (frame_width, frame_height)
)

print("🎥 Recording started... Press ESC to stop")

# Background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500, varThreshold=50, detectShadows=True
)

previous_positions = {}

# ===============================
# MAIN LOOP
# ===============================
while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Save frame to video file
    out.write(frame)

    fg_mask = bg_subtractor.apply(frame)
    _, fg_mask = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if w < MIN_WIDTH or h < MIN_HEIGHT:
            continue

        center = get_center(x, y, w, h)
        obj_id = id(cnt)

        if obj_id in previous_positions:
            speed = calculate_speed(previous_positions[obj_id], center)
            cv2.putText(
                frame,
                f"{speed} km/h",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        previous_positions[obj_id] = center

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Vehicle Speed Detection (Recording)", frame)

    # Press ESC to stop
    if cv2.waitKey(1) & 0xFF == 27:
        print("ESC pressed – stopping recording")
        break

# ===============================
# CLEAN EXIT
# ===============================
cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Camera closed")
print("✅ Video saved as recorded_output.mp4")
