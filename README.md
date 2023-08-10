
# Face Detection in Python

This is a simple guide on how to use the `face_detection` library in Python to perform face detection in images. The `face_detection` library provides an easy way to detect faces in images using pre-trained models. You can install the library using pip and then use it in your Python code.

## Installation

To install the `face_detection` library, you can use the following pip command:

```bash
pip install face-detection
```

## Usage

Follow these steps to perform face detection using the `face_detection` library:

1. **Import the necessary modules:**

   In your Python script (e.g., `main.py`), start by importing the required modules:

   ```python
   import face_detection
   import cv2
   ```

2. **Load an image:**

   Load the image on which you want to perform face detection using OpenCV:

   ```python
   image_path = "path/to/your/image.jpg"
   image = cv2.imread(image_path)
   ```

3. **Load the face detection model:**

   Load the pre-trained face detection model using the `face_detection` library:

   ```python
   face_detection_model = face_detection.build_model("DSFDDetector")
   ```

   You can also choose different face detection models provided by the library.

4. **Perform face detection:**

   Use the loaded model to detect faces in the image:

   ```python
   detections = face_detection_model.detect(image)
   ```

5. **Draw bounding boxes around detected faces:**

   Iterate through the detected faces and draw bounding boxes around them:

   ```python
   for detection in detections:
       x, y, w, h = detection["box"]
       cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
   ```

6. **Display or save the result:**

   You can choose to either display the image with bounding boxes using OpenCV's `imshow` function or save the result to a new image file:

   ```python
   cv2.imshow("Face Detection Result", image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

   # Or save the result
   output_path = "path/to/output/result.jpg"
   cv2.imwrite(output_path, image)
   ```

## Running the Code

After you've created your Python script (e.g., `main.py`) with the above code, you can run it using the following command:

```bash
python main.py
```

This will execute the face detection code on the specified image and display the result with bounding boxes around detected faces.

Please make sure to replace `"path/to/your/image.jpg"` with the actual path to the image you want to perform face detection on.

Remember that the accuracy of face detection may vary depending on the image quality, lighting conditions.
