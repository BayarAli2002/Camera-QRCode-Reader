import cv2
from pyzbar.pyzbar import decode
import time

# Open the camera
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: Failed to open camera.")
    exit()

# Set camera resolution
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Main loop
start_time = time.time()
run_duration = 60  # Run for 60 seconds
while time.time() - start_time < run_duration:
    success, frame = cam.read()
    if not success:
        print("Error: Failed to capture frame.")
        continue

    try:
        for barcode in decode(frame):
            barcode_data = barcode.data.decode('utf-8')
            print("Type:", barcode.type)
            print("Data:", barcode_data)
    except Exception as e:
        print("Error:", e)

    cv2.imshow("QR Code Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
