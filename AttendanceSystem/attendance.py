import cv2
import face_recognition
import csv
from datetime import datetime

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load known face encodings and names
known_face_encodings = []  # List to store encodings of known faces
known_face_names = []      # List to store names corresponding to known faces

# Add your known faces' encodings and names (Example)
# known_face_encodings.append(face_recognition.face_encodings(face_image)[0])
# known_face_names.append("Name")

# Function to mark attendance in CSV
def mark_attendance(name):
    filename = 'attendance.csv'
    # Open the file in append mode or create it if it doesn't exist
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([name, dt_string])
    print(f"Attendance marked for {name}.")

# Main face recognition and attendance marking function
def recognize_and_mark_attendance():
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Convert the image from BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all face locations in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            # Get the face encodings for the faces in the current frame
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                # Check if the face matches any known face
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "John_Doe"  # Default name if no match is found

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                # Draw a rectangle around the face
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                # Draw the name label
                cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                # Mark attendance if a face is recognized
                mark_attendance(name)

        # Display the resulting frame
        cv2.imshow('Attendance System', frame)

        # Press 'q' to quit the webcam capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    recognize_and_mark_attendance()
