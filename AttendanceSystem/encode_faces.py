import face_recognition
import os
import pickle

def encode_faces():
    face_encodings = {}
    for person in os.listdir("faces"):
        person_path = os.path.join("faces", person)
        encodings = []
        for img_file in os.listdir(person_path):
            img_path = os.path.join(person_path, img_file)
            image = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(image)
            if encoding:  # Ensure face was detected
                encodings.append(encoding[0])
        face_encodings[person] = encodings
    
    with open("encodings.pkl", "wb") as f:
        pickle.dump(face_encodings, f)
    print("Face encodings saved.")

# Usage
encode_faces()
