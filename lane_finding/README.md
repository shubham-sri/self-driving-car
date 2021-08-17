# **Finding Lane Lines on the Road** 

[//]: # (Image References)
[image1]: ./examples/masked.png "Color Masked"
[image2]: ./examples/blur.png "Blur"
[image3]: ./examples/smooth.png "Smooth"
[image4]: ./examples/result.ong "Result"

---

## Reflection

### Basic idea and thinking
I have a question before staring this project. **How human can recognize lane stips on the road?** 
So I proccessed data which is in my mind and come with few points
- Houman are good to recognize colors even very small change in color can be recognized by human and I used this thought as base to build this project
- I have to split intrest area into two part which contain one strip of lane, which help in left, right identification and disconnections.

### Pipeline desciption
My pipeline consisted of 7 steps. 
- **Apply Color Mask** - Applied color mask to remove unwanted color.
![Color Masked][image1]
- **Smoothing** - Applied smoothing to resconstruct distorted part on image.
![Smooth][image3]
- **Gaussian Blur** - Applied Gaussian Blur to remove some unwanted data and generalize the output.
![Blur][image2]
- **Canny Edge Detection** - Applied to dectect lane strip edges.
- **Region of Interest** - Applied this function to select regio which contain lane strip, to remove unwanted data. This function can devide area of interest into two part left and right.
- **Hough Lines** - This compute lines in edge image. This function consiste **draw line** and **compute connected line**
    - *Zero axis point* - This function compute line to complete last disconnected strip to end of image frame
    - *Draw Line* - Function can draw line for image as mask
- **Weighted Image** - This function add original image frame and line mask image.
![Result][image4]


**Note:** *Improvement in* **draw_line** *is to connect the diconnected line using* **add_zero_axis_point**. *Function* **add_zero_axis_point** *compute lowest line point and then find line with touches end of image frame*. **P.html** *is export of jupyter notebook*

## 2. Identify potential shortcomings with your current pipeline
- Lane at top of **Region of Interest** is little bit wrong positioned


## 3. Suggest possible improvements to your pipeline
- Enhace pixels for exmaple make yellow and white strip pixels more brighter and other color dull