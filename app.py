from ultralytics import YOLO
import cv2

# 1. Medium Model load karo (Accuracy ma nano model karta ghano saras chhe)
model = YOLO('yolov8m.pt')

# 2. WebCam input
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Camera open nathi thai shakyo.")
    exit()

print("✅ Accurate Multi-Object Detection chalu thai gayo chhe. Close karva mate 'q' dabo.")

while True:
    success, frame = cap.read()
    if not success or frame is None:
        print("❌ Frame load nathi thai rahyu.")
        break

    # -------------------------------------------------------------
    # conf=0.55 -> 55% thi vadhare confidence hoy tyare j detect karse (False objects nai ave)
    # iou=0.45  -> Duplicate/overlapping boxes ne remove karse
    # -------------------------------------------------------------
    results = model(frame, conf=0.55, iou=0.45)

    # Frame ma jetla accurate objects male ena boxes
    boxes = results[0].boxes
    total_objects = len(boxes)

    # Annotated Frame with bounding boxes
    annotated_frame = results[0].plot()

    # Total Count Banner (Top-Left)
    cv2.rectangle(annotated_frame, (20, 20), (380, 70), (0, 0, 0), -1)
    cv2.putText(annotated_frame, f'Total Count: {total_objects}', (30, 55), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Output Window Show Karo
    cv2.imshow("Accurate Real-Time Object Counter", annotated_frame)

    # Press 'q' to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Program stopped.")
        break

# Safely close camera & windows
cap.release()
cv2.destroyAllWindows()