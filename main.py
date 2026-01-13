import cv2
import time
from utils import get_center
from speed_calculation import calculate_speed
from config import MIN_WIDTH, MIN_HEIGHT

# ===============================
# CAMERA INITIALIZATION
# ===============================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Camera opened:", cap.isOpened())
if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

# Camera warm-up
time.sleep(2)

# ===============================
# VIDEO RECORDING SETUP
# ===============================
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0

video_filename = "recorded_output.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

if not out.isOpened():
    print("❌ VideoWriter not opened")
    cap.release()
    exit()

print("🎥 Video recording started...")

# ===============================
# WINDOW SETUP
# ===============================
WINDOW_NAME = "Vehicle Speed Detection"
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, 960, 540)

fullscreen = False  # fullscreen state

# ===============================
# BACKGROUND SUBTRACTOR
# ===============================
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

    # Save ORIGINAL frame to video
    out.write(frame)

    # Resize frame for display (window size aware)
    try:
        _, _, win_w, win_h = cv2.getWindowImageRect(WINDOW_NAME)
        if win_w > 0 and win_h > 0:
            display_frame = cv2.resize(frame, (win_w, win_h))
        else:
            display_frame = frame
    except:
        display_frame = frame

    # ===============================
    # ON-SCREEN INSTRUCTIONS
    # ===============================
    cv2.putText(
        display_frame,
        "ESC: Exit & Save Video | F: Toggle Fullscreen",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # ===============================
    # OBJECT DETECTION
    # ===============================
    fg_mask = bg_subtractor.apply(display_frame)
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
                display_frame,
                f"{speed} km/h",
                (x, max(60, y - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        previous_positions[obj_id] = center

        cv2.rectangle(
            display_frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow(WINDOW_NAME, display_frame)

    # ===============================
    # KEY HANDLING
    # ===============================
    key = cv2.waitKey(1) & 0xFF

    # ESC key → Exit
    if key == 27:
        print("ESC pressed – closing camera and saving video...")
        break

    # F key → Toggle Fullscreen
    elif key == ord('f') or key == ord('F'):
        fullscreen = not fullscreen
        if fullscreen:
            cv2.setWindowProperty(
                WINDOW_NAME,
                cv2.WND_PROP_FULLSCREEN,
                cv2.WINDOW_FULLSCREEN
            )
            print("Fullscreen enabled")
        else:
            cv2.setWindowProperty(
                WINDOW_NAME,
                cv2.WND_PROP_FULLSCREEN,
                cv2.WINDOW_NORMAL
            )
            cv2.resizeWindow(WINDOW_NAME, 960, 540)
            print("Fullscreen disabled")

# ===============================
# CLEAN EXIT
# ===============================
cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Camera closed successfully")
print(f"✅ Video saved successfully as '{video_filename}'")
