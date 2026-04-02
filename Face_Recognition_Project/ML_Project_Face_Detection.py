import cv2
import numpy as np
import os
fileName = input("Enter the name of the person: ").strip()
dataset_path = "./data/"
offset = 20
os.makedirs(dataset_path, exist_ok=True)
cam = cv2.VideoCapture(0)
model = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faceData = []
skip = 0
while True:
    success, img = cam.read()
    if not success:
        print("Reading Camera Failed!")
        continue
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = model.detectMultiScale(grayImg, 1.3, 5)
    faces = sorted(faces, key=lambda f: f[2] * f[3])  # Sort by area
    if len(faces) > 0:
        x, y, w, h = faces[-1]  # Largest face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        x1 = max(x - offset, 0)
        y1 = max(y - offset, 0)
        x2 = min(x + w + offset, img.shape[1])
        y2 = min(y + h + offset, img.shape[0])
        cropped_face = img[y1:y2, x1:x2]
        if cropped_face.size > 0:
            cropped_face = cv2.resize(cropped_face, (100, 100))
            skip += 1
            if skip % 10 == 0:
                faceData.append(cropped_face)
                print(f"Saved so far: {len(faceData)}")
            cv2.imshow("Cropped Face", cropped_face)
    cv2.imshow("Image Window", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# Prepare and save dataset
faceData = np.asarray(faceData)
print("Final face dataset shape:", faceData.shape)
m = faceData.shape[0]
faceData = faceData.reshape((m, -1))
filepath = os.path.join(dataset_path, fileName + ".npy")
np.save(filepath, faceData)
print("Data Saved Successfully to:", filepath)
# Release resources
cam.release()
cv2.destroyAllWindows()
