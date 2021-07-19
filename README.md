# Season of Code - MINI PROJECT
One of the interesting applications of CV is Emotion Detection through facial expressions. CV can recognize and tell you what your emotion is by just looking at your facial expressions. It can detect whether you are angry, happy, sad, etc.

## Summary
This consists of computer vision model that we will build using Keras and Resnet50 – a variant of Convolutional Neural Network. We will use this model to check the emotions in real-time using OpenCV and webcam. The model was build and trained on google colab and used on PyCharm

The description consists of following -
  - Dataset
  - Custom Model Architecture
  - Testing and Results

## Dataset
The name of the data set is FER-2013 which is an open-source data set that was made publicly available for a Kaggle competition. It contains 48 X 48-pixel colored images of the face. There are seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral) present in the data. 

## Custom Model Architecture
Consists of 5 stages of convolution max-pooling layers followed by 3 layers of fully connected layers and a softmax output layer. The convolution layers use itna filters of size itna respectively. The max-pooling layers use kernels of size itna and stride itna. ReLU was utilized as the activation function. To improve the performance batchnorm at the end of every layer was added and dropouts of itnas after yeye layer respectively. The model was trained with itna epochs with ye loss and ye optimizer. Learning rate was fixed at 


## Testing and Results
Custom Mode Results 
Learning Results
