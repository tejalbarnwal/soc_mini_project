# Season of Code - MINI PROJECT
One of the interesting applications of CV is Emotion Detection through facial expressions. CV can recognize and tell you what your emotion is by just looking at your facial expressions. It can detect whether you are angry, happy, sad, etc.

## Summary
This consists of computer vision model that i build using Keras with a custom Convolutional Neural Network. We will use this model to check the emotions in real-time using OpenCV and webcam. The model was build and trained on google colab and used on PyCharm

The description consists of following -
  - [Dataset](https://github.com/tejalbarnwal/soc_mini_project/blob/main/README.md#dataset)
  - [Custom Model Architecture](https://github.com/tejalbarnwal/soc_mini_project/blob/main/README.md#custom-model-architecture)
  - [Testing and Results](https://github.com/tejalbarnwal/soc_mini_project/blob/main/README.md#testing-and-results)

## Dataset
The name of the data set is [FER-2013](https://www.kaggle.com/msambare/fer2013) which is an open-source data set that was made publicly available for a Kaggle competition. It contains 48 X 48-pixel colored images of the face. There are seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral) present in the data. 

## Custom Model Architecture
Consists of 5 stages of convolution max-pooling layers followed by 3 layers of fully connected layers and a softmax output layer. The convolution layers use 64,128,256,512 filters of size (3,3) respectively. The max-pooling layers use kernels of size (2,2) and stride 2. ReLU was utilized as the activation function. To improve the performance batchnorm at the end of every layer was added and dropouts of 0.3 and 0.5. The model was trained with 40 epochs with categorical crossentropy loss and Adam optimizer. Learning rate was fixed at its default value of 0.001


## Testing and Results
At the end of 40 epochs we have accuracy versus epochs graph as shown. So on test dataset we had a test accuracy of 65.3% and training accuracy of 74.7%  
![](https://github.com/tejalbarnwal/soc_mini_project/blob/main/acc.png) <br>

The FER2013[1], was a challenge proposed on Kaggle which was won by the team reaching the test accuracy of 75.2%.Human accuracy on the dataset is 65.5%.
So this proves that my model is decent enough!

[Link to video with live webcam feed](https://github.com/tejalbarnwal/soc_mini_project/blob/main/model1.webm)

There were some instances where the model didnt perform well
Examples of the those cases are:
- This is a case of fear but the model classified it as surprise
<img src="https://github.com/tejalbarnwal/soc_mini_project/blob/main/test3_result.png" width="300" height="300"/>
- This is a case of sad but the model classified it as surprised
![](https://github.com/tejalbarnwal/soc_mini_project/blob/main/test4_result.png)
