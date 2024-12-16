import cv2
import os

def capture_images(name):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Images")
    count = 0
    path = f"faces/{name}"
    os.makedirs(path, exist_ok=True)
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.imshow("Capture Images", frame)
        
        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC key
            print("Closing capture.")
            break
        elif k % 256 == 32:  # SPACE key
            img_name = f"{path}/{name}_{count}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved!")
            count += 1
    
    cam.release()
    cv2.destroyAllWindows()

# Usage
capture_images("John_Doe")
