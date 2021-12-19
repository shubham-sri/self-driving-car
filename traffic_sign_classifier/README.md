# **Traffic Sign Recognition** 

## Writeup

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./outputs/plot.dataset.png "Visualization"
[image2]: ./new_data/11.jpg "Traffic Sign 1"
[image3]: ./new_data/17.jpeg "Traffic Sign 2"
[image4]: ./new_data/22.jpg "Traffic Sign 3"
[image5]: ./new_data/35.jpeg "Traffic Sign 4"
[image6]: ./new_data/4.jpg "Traffic Sign 5"
[image7]: ./outputs/cnn.png "Traffic Sign 5"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

You're reading it! and here is a link to my [project code](https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.ipynb)

### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the numpy library to calculate summary of the traffic signs data set:

* The size of training set is 34799
* The size of the validation set is 4410
* The size of test set is 12630
* The shape of a traffic sign image is 32, 32, 3
* The number of unique classes/labels in the data set is 43

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a bar chart showing how the data ...

![alt text][image1]

### Design and Test a Model Architecture

#### 1. Preprocessed the image data

I converted sign images to gray scale because, sign is not dependent on color.

I normalize images between range on -1 to 1, to prevent neural net from vanishing gradient problem 

#### 2. Model architecture 

My final model consisted of the following layers:

| Layer         |     Description        |
|:-------------:|:----------------------:|
| Conv2D (L1) | filters = 6, stride = 1x1, k_size=5x5, output = [28, 28, 6]|
| Conv2D (L2) | filters = 16, stride = 1x1, k_size=5x5, output = [24, 24, 16]|
| MaxPool (L3) | stride = 2x2, k_size=2x2, output = [12, 12, 16]|
| Conv2D (L4) | filters = 32, stride = 1x1, k_size=3x3, output = [10, 10, 32]|
| MaxPool (L5) | stride = 2x2, k_size=2x2, output = [5, 5, 32]|
| Conv2D (L6) | filters = 32, stride = 2x2, k_size=3x3, output = [5, 5, 32]|
| Conv2D (L7) | filters = 128, stride = 1x1, k_size=1x1, output = [5, 5, 128]|
| Flatten (L8) | output = [800]|
| Flatten (L9) | output = [800]|
| Concat (L10) | output = [1600]|
| Dense (L11) | output = [1024]|
| Dense (L12) | output = [400]|
| Dense (L13) | output = [43]|



#### 3. Model training

To train the model, I used batch size 128 and number of epochs 80 with learning rate 0.0001.
In each epoch I trained model using training data and after batch training completed I validate model
using validation data.


#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* training set accuracy of 0.999
* validation set accuracy of 0.954
* test set accuracy of 0.941

As all we know deep learning is all about how we well tune our hyper params, so used iterative approach:
* I just chosen sequential model in which I just stacked each layer over each other
* With that model I'm unable to achieve desired accuracy and model get over fitted
* For achieve better accuracy over validation data firstly I tried to make network deeper, but still facing some problem over validation data to fix those issues I created branches model and concat which help me get better model 
* I tried to tune `keep_prob` for a dropout and keep lower `learning_rate` and high `epochs`
* I have decreased the `kernel_size` as goes deeper to network
* First I tried with `Gradient Descent` but facing issue that after few epoch improvement get stopped, but after that I used `Adam Optimizer` which gives better result 

Final model arch. is here...
![alt text][image7]

 

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

![alt text][image2] ![alt text][image3] ![alt text][image4] 
![alt text][image5] ![alt text][image6]

The first I read the image then resize it to 32x32 using OpenCv, then apply the processing to image.

Image quality selected
* I have chosen different size image then resized to 32x32
* Chosen different angle image to get better performance check
* Few are taken under sunlight also which mimic real world image

#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image.                             |     Prediction                    |
|:----------------------------------:|:---------------------------------:|
| Right-of-way at the next intersection	 | Right-of-way at the next intersection 	|
| No entry	 | No entry 	|
| Speed limit (50km/h)	 | Speed limit (50km/h) 	|
| Ahead only	 | Ahead only 	|
| Bumpy road	 | Road work 	|


The model was able to correctly guess 4 of the 5 traffic signs, which gives an accuracy of 80%.
The test accuracy is 94%, but when I'm testing over real data of five image I'm getting 80%.

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The code for making predictions on my final model is located in the 16th cell of the Ipython notebook.

For the first image, the model is relatively sure that this is a `Right-of-way at the next intersection` sign (probability of 0.67), and the image does contain a `Right-of-way at the next intersection` sign. The top five soft max probabilities were

| Probability            |     Prediction                                |
|:----------------------:|:---------------------------------------------:|
| 0.673			 | Right-of-way at the next intersection 	|
| 0.327			 | Speed limit (50km/h) 	|
| 0.000			 | Roundabout mandatory 	|
| 0.000			 | Yield 	|
| 0.000			 | Turn right ahead 	|

For second image, the model predict `No entry` (probability 1.0) sign, and the sign is `No entry` sign.

| Probability            |     Prediction                                |
|:----------------------:|:---------------------------------------------:|
| 1.000			 | No entry 	|
| 0.000			 | Yield 	|
| 0.000			 | Speed limit (20km/h) 	|
| 0.000			 | Speed limit (30km/h) 	|
| 0.000			 | Speed limit (50km/h) 	|

For the third image, the model predict `Speed limit (50km/h) ` (probability 1.0) sign, and the sign is `Speed limit (50km/h) ` sign.

| Probability            |     Prediction                                |
|:----------------------:|:---------------------------------------------:|
| 1.000			 | Speed limit (50km/h) 	|
| 0.000			 | Speed limit (60km/h) 	|
| 0.000			 | Speed limit (80km/h) 	|
| 0.000			 | Speed limit (30km/h) 	|
| 0.000			 | No passing for vehicles over 3.5 metric tons 	|

For the forth image, the model predict `Ahead only` (probability 1.0) sign, and the sign is `Ahead only` sign.

| Probability            |     Prediction                                |
|:----------------------:|:---------------------------------------------:|
| 1.000			 | Ahead only 	|
| 0.000			 | Road work 	|
| 0.000			 | Dangerous curve to the left 	|
| 0.000			 | Road narrows on the right 	|
| 0.000			 | Double curve 	|

For the forth image, the model predict `Road work` (probability 0.840) sign, but the sign is `Bumpy road` sign.

| Probability            |     Prediction                                |
|:----------------------:|:---------------------------------------------:|
| 0.840			 | Road work 	|
| 0.160			 | Pedestrians 	|
| 0.000			 | Dangerous curve to the left 	|
| 0.000			 | Road narrows on the right 	|
| 0.000			 | Traffic signals 	|