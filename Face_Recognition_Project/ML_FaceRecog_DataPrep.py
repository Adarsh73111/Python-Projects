import cv2
import numpy as np
import os
offset = 20
dataset_path = "./data/"
faceData = []
labels = []
nameMap = {}
classId = 0
# Load face datasets 
for f in os.listdir(dataset_path):
    if f.endswith(".npy"):
        nameMap[classId] = f[:-4]  # Remove .npy extension
        dataItem = np.load(os.path.join(dataset_path, f))
        m = dataItem.shape[0]
        faceData.append(dataItem)
        target = classId * np.ones((m,))
        labels.append(target)
        classId += 1
# Combine all class data into training set
XT = np.concatenate(faceData, axis=0)
yT = np.concatenate(labels, axis=0).reshape((-1, 1))
print("Training Data Shape:", XT.shape)
print("Training Labels Shape:", yT.shape)
print("Class Map:", nameMap)
# Euclidean distance function
def dist(p, q):
    return np.sqrt(np.sum((p - q) ** 2))
# KNN classifier
def knn(X, y, xt, k=5):
    m = X.shape[0]
    dlist = []
    for i in range(m):
        d = dist(X[i], xt)
        dlist.append((d, y[i][0]))  # Ensure scalar label
    dlist = sorted(dlist, key=lambda x: x[0])  # Sort by distance
    top_k = dlist[:k]
    labels = [label for _, label in top_k]
    labels, counts = np.unique(labels, return_counts=True)
    idx = counts.argmax()
    pred = labels[idx]
    return int(pred)
# Initialize camera and Haar model
cam = cv2.VideoCapture(0)
model = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
while True:
    success, img = cam.read()
    if not success:
        print("Reading Camera Failed!")
        continue
    faces = model.detectMultiScale(img, 1.3, 5)
    for f in faces:
        x, y, w, h = f
        print(f)
        # Clamp the region inside image bounds
        x1 = max(x - offset, 0)
        y1 = max(y - offset, 0)
        x2 = min(x + w + offset, img.shape[1])
        y2 = min(y + h + offset, img.shape[0])
        cropped_face = img[y1:y2, x1:x2]
        if cropped_face.size == 0:
            continue
        cropped_face = cv2.resize(cropped_face, (100, 100))
        # Predict using KNN
        classPredicted = knn(XT, yT, cropped_face.flatten())
        namePredicted = nameMap[classPredicted]
        print(f"Predicted: {namePredicted}")
        # Draw prediction on frame
        cv2.putText(img, namePredicted, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Prediction Window", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
