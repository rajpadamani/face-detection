import cv2
import face_recognition
import os

# Load known faces and their names (you need to prepare these images in advance)
known_face_encodings = []
known_face_names = []

def get_image_paths_from_folder(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # Add more extensions if needed
    image_paths = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension.lower() in image_extensions:
                image_path = os.path.join(root, file)
                image_paths.append(image_path)

    return image_paths

def extract_filename_without_extension(file_path):
    file_name_with_extension = os.path.basename(file_path)
    file_name, _ = os.path.splitext(file_name_with_extension)
    return file_name

# Load and encode known faces
# image_paths = ['path_to_image_1.jpg', 'path_to_image_2.jpg']  # Add paths to your images
image_paths =  get_image_paths_from_folder('images')

for image_path in image_paths:
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    
    # Extract the name from the image path (assuming the filename is the name)
    known_face_names.append(extract_filename_without_extension(image_path))

# Load the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        break

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each detected face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"  # Default name if no match

        # If a match is found, use the name of the known face
        if True in matches:
            matched_index = matches.index(True)
            name = known_face_names[matched_index]

        # Draw a rectangle around the detected face and label it
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Face Recognition', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
