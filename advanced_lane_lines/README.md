## Advance Lane Detection

[//]: # (Image References)

[image1]: ./output_images/calibrated_test2.jpg "Undistorted"
[image2]: ./output_images/threshold_calibrated_test6.jpg "Binary Example"
[image3]: ./output_images/bird_eye_calibrated_test2.jpg "Warp Example"
[image4]: ./output_images/sliding_window_calibrated_test2.jpg "Sliding Example"
[image5]: ./output_images/final_calibrated_test2.jpg "Output"

---
## Steps for image and video pipeline

**Notes:** All computation code is in ***src*** folder

`src` folder consist files `distortion.py`, `line.py`, `prespective.py`, `thresholding.py` and `utils.py`. 
To run project run `P2.ipynb` jupyter notebook

### Camera Calibration

#### 1. Class Distortion is used for camera calibration.

`class Distortion` defined in `src/distortion.py`. `Distortion` consist two methods `calculate` and `fix`. 
The `calculate` method compute the `objpoints` and `imgpoints` using chess board image from `camera_cal` folder and `fix`
method compute calibrated image using `objpoints` and `imgpoints` computed by `calculate` method.

I stored `objpoints` and `imgpoints` in `Distortion` class as attributes and used it for future computation. 

Following is the output image of one of the test image
![alt text][image1]

#### 2. Class Thresholding is used for threshold image generation

I computed `gradient` and `color` thresholding and combine it for computed threshold image  

Following is the output image of one of the test image
![alt text][image2]

#### 3. Class Perspective is used for bird eye view

`Class Prespective` uses default config for `src` and `dst`
```python
src = np.float32([[200, 720], [1100, 720], [595, 450], [685, 450]])
dst = np.float32([[300, 720], [980, 720], [300, 0], [980, 0]])
```
This class consist two `transform` and `inverse_transform`, `transform` to convert image to bird eye view and `inverse_transform` to reverse the transform

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image3]

#### 4. Poly fit (this step consist two sub steps)

All poly fit computation function defined in `Class Line`. Line class defined to Handle video and image both.

#### 4.1 Only for image

I used the `poly_sliding_window` method to fit poly line in image using sliding window algo.

Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:
![alt text][image4]

#### 4.2 Only for video

I used the `result` method with uses `poly_sliding_window` and `poly_search_around`. 
On very 100 frames 10 frames are processed by sliding window and remaining are with search around also

#### 5. For lane curvature and position of the vehicle used line class

I used `class Line` which compute lane curvature using `calculate_curve`, `calculate_curve` uses `leftx`, `lefty`, `rightx`, `righty`.
For vehicle position I used `calc_vehicle_offset` using `image_shape`, `left_fit`, `right_fit`.

#### 6. For final result

I implemented `plot_lines` in `utils.py` which draw lane overlay and inverse transform it and add it to undistorted image

![alt text][image5]

Here's a [link to my video result](./output_videos/project_video.mp4)
