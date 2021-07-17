import cv2
from tensorflow import keras
import numpy as np
import h5py

model = keras.models.load_model('trial_model.h5')
print('\n\n')
print(model.summary())
########################################
face_cascade = cv2.CascadeClassifier("/home/tejal/Documents/soc_mini_project/haarcascade.xml")


outputToEmotionMap = {
    0: 'angry',
    1: 'disgusted',
    2: 'in fear',
    3: 'happy',
    4: 'neutral',
    5: 'sad',
    6: 'surprised'
}


img = cv2.imread("test3.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize=(100,100))
x1 = 0
y1 = 0
w1 = 0
h1 = 0

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)
    x1 = x
    y1 = y
    w1 = w
    h1 = h

cv2.imshow("img", img)
######################################
inputImage = np.reshape(cv2.resize(gray[y1:y1 + h1, x1:x1 + w1], (48,48)),(-1,48,48,1))
print("SHAPE IS", np.shape(inputImage))

# predicting with help of model - taking one with max probability
predictions = model.predict(inputImage)
maxProbabilityPredict = np.argmax(predictions)

# adjusting message
message = 'You are {}'.format(
    outputToEmotionMap[maxProbabilityPredict]
)
print("you are", message)

##################
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (x,y)

# fontScale
fontScale = 1

    # Blue color in BGR
color = (0, 255, 0)

    # Line thickness of 2 px
thickness = 2

    # Using cv2.putText() method
image = cv2.putText(img, message, org, font,
                    fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("emo_img", img)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
