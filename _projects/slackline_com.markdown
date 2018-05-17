---
layout: page
date: 2018-03-05
title: Centre of MAss Tracking
description: slacklining!
brief: A small computer vision project to show that the centre of mass of someone walking on a slackline stays fixed vertically on top of the line (unless you fall!). By employing Python and OpenCV we are able to track an approximation of the centre of mass of a person slacklining in a video.
img: https://user-images.githubusercontent.com/4785303/37111220-106c5d7e-2237-11e8-8ba0-3f2fb095fd88.jpeg
skills: Python, OpenCV, Jupyter notebooks, physics
how-to: example videos and code below
no_img: yes
---

[OpenCV](https://opencv.org/) is an open source computer vision library which can be interfaced from Python. It provides lots of functionalities and is very powerful.

In this project we are interested in studying the center of mass of a person standing on a slackline. The key point is that the center of mass anybody on a slackline stays vertically on top of the contact point of the foot with the line itself, even when limbs are waving around. This can be tested empirically by recording someone walking on the line and employing OpenCV to detect body contours and find the geometric centroid of the person's body.

As a rough example, I recorded myself walking on the line:


```python
YouTubeVideo('fL3lAojlZY8', width=700, height=400)
```

{% include video.html id="fL3lAojlZY8" %}

Ideally, you want to wear clothes with different colours from the background, as it makes contour detection much easier. In the example video above, I achieved this partially. The blue coat is generally easy to detect, however, some shadows make it black in some areas and some detail is lost. Similarly with the jeans, they look quite black and white, hence their detection needs more care. Until I get the chance to record a better video, we will focus on detecting the upper body only, which usually provides a decent approximation.

### Import necessary libraries

```python
%matplotlib inline
import cv2
import imutils
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['figure.figsize'] = [15, 10]
from IPython.lib.display import YouTubeVideo
```

### Test contour selection

First, we will try the contour detection on a still frame from the example video. Many sophisticated contour detection techniques exist, which are outside of the scope of this short example. We will focus on colour detection, where we specify a range of RGB colours to look for, and an area of the image to do so (computationally cheaper and quicker).

In our case, we want the colour range to contain most blues, and little else. For the image area, we will broadly select the range of pixels that contain the body.

```python
testFile = './pick_colours/test1.png'
boundaries = [([75, 0, 0], [255, 255, 70])] # OpenCV uses BGR, not RGB!
sizes = [80, 400, 400, 800]                 # In pixels

scale = 1
image = cv2.imread(testFile)
image = cv2.resize(image, (0, 0), fx=1./scale, fy=1./scale)
height, width, channels = image.shape
imageCropped = image[int(sizes[0]/scale):int(sizes[1]/scale),
                     int(sizes[2]/scale):int(sizes[3]/scale)]

plt.figure(figsize=(10,5))
plt.imshow(cv2.cvtColor(imageCropped, cv2.COLOR_BGR2RGB))
plt.title("Image cropped to show only the body")
plt.show()
```

<div class="img_single">
    <img class="col two" src="https://user-images.githubusercontent.com/4785303/36992242-3d722e66-20a2-11e8-84b5-aba6109cc123.png"/>
</div>


```python
lower = np.array(boundaries[0][0], dtype = "uint8")
upper = np.array(boundaries[0][1], dtype = "uint8")

# Crop the image, process only the cropped bit
mask = cv2.inRange(imageCropped, lower, upper)
mask[mask != 0] = 1
imageCropped[mask==1, 0] = 0
imageCropped[mask==1, 1] = 255
imageCropped[mask==1, 2] = 0
image[int(sizes[0]/scale):int(sizes[1]/scale),
      int(sizes[2]/scale):int(sizes[3]/scale)] = imageCropped

# Find blue contours (coat)
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
for c in cnts:
    # Retain only large enough contours, this deletes outliers
    if cv2.contourArea(c) > 3000:
        c[:,0,0] += int(sizes[2]/scale)
        c[:,0,1] += int(sizes[0]/scale)
        # Compute the center of the contour
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # Draw the contour and center of the shape on the image
        cv2.drawContours(image, [c], -1, (0, 69, 255), 2)
        cv2.line(image, (cX-15, cY), (cX+15, cY), (0, 0, 255), 2)
        cv2.line(image, (cX, cY-15), (cX, height), (0, 0, 255), 2)

imageCropped = image[int(sizes[0]/scale):int(sizes[1]/scale),
                     int(sizes[2]/scale):int(sizes[3]/scale)]

plt.figure(figsize=(10,5))
plt.imshow(cv2.cvtColor(imageCropped, cv2.COLOR_BGR2RGB))
plt.title("Upper body contour detection")
plt.show()
```

<div class="img_single">
    <img class="col two" src="https://user-images.githubusercontent.com/4785303/36992243-3dab4138-20a2-11e8-920d-99f0cf4716ce.png"/>
</div>

As we can see in the previous image, we can easily obtain a rough upper body contour.  With a better choice of contour detection algorithm (maybe motion detection) and/or brigther clothes (red or orange would be ideal in this example video), a more accurate contour of the body could be obtained.

We can also find the geometric centroid of the contour, which roughly corresponds to its centre of mass (assuming uniform body density, which seems to be a good approximation). We are now ready to embed the cropped image in the full image.


```python
# Frame the cropped image with a white rectangle
cv2.rectangle(image, (int(sizes[2]/scale), int(sizes[0]/scale)),
                     (int(sizes[3]/scale), int(sizes[1]/scale)),
              (255, 255, 255), 3)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Full image with upper body contour detection")
plt.show()
```

<div class="img_single">
    <img class="col three" src="https://user-images.githubusercontent.com/4785303/36992276-54eda93a-20a2-11e8-84ae-9a1b47e5af97.jpg"/>
</div>

### Video analysis

So far, we are able to approximately find the centre of gravity in a picture of someone standing on a slackline. This can be easily extended to deal with a video instead.

The key point is that a video is just a sequence of stills (frames), so we can grab each frame of the video, apply the processing described above, and put the resulting image as a frame in an output video.


```python
# Open video
videoInFile = './video_tests/clip1.mp4'
videoIn = cv2.VideoCapture(videoInFile)

# Find width and height
w = videoIn.get(cv2.CAP_PROP_FRAME_WIDTH);
h = videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT);

# The video can be scaled down to reduce computing time
scale = 1
fps = 30
minContourSize = 3000
capSize = (int(w/scale), int(int(h/scale)/2))

# Output video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
videoOut = cv2.VideoWriter('output.mp4', fourcc, fps, (int(w),int(h)))

# Define the list of boundaries: blue (coat)
boundaries = [([75, 0, 0], [255, 255, 70])]
# Window frames for each colour
sizes = [[80, 400, 400, 800]]
# Centroid coordinates and masses
centroids = np.zeros([len(boundaries), 2], dtype=int)
masses = np.zeros(len(boundaries))

# Iterate over the frames of the video, one by one
while videoIn.isOpened():
    # Read frame
    ret, image = videoIn.read()
    image = cv2.resize(image, (0, 0), fx=1./scale, fy=1./scale)
    imageTemp = image.copy()
    height, width, channels = image.shape

    # Loop over different colours (in our case just one, the blue coat)
    for j in range(len(boundaries)):
        imagePart = image[int(sizes[j][0]/scale):int(sizes[j][1]/scale),
                         int(sizes[j][2]/scale):int(sizes[j][3]/scale)]
        lower = np.array(boundaries[j][0], dtype = "uint8")
        upper = np.array(boundaries[j][1], dtype = "uint8")
        mask = cv2.inRange(imagePart, lower, upper)
        imageTemp[int(sizes[j][0]/scale):int(sizes[j][1]/scale),
               int(sizes[j][2]/scale):int(sizes[j][3]/scale)] = imagePart
        # Find contours
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # _NONE
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        for c in cnts:
            if cv2.contourArea(c) > minContourSize/scale:
                c[:,0,0] += int(sizes[j][2]/scale)
                c[:,0,1] += int(sizes[j][0]/scale)
                # Compute the center of the contour
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                centroids[j] = np.array([cX, cY])
                masses[j] = cv2.contourArea(c)
                # Draw the contour and center of the shape on the image
                cv2.drawContours(imageTemp, [c], -1, (0, 69, 255), 2)

    for j in range(len(boundaries)):
        # Add window frames to the image to check
        cv2.rectangle(imageTemp, (int(sizes[j][2]/scale), int(sizes[j][0]/scale)),
                      (int(sizes[j][3]/scale), int(sizes[j][1]/scale)),
                      (255, 255, 255), 1)
        # Draw centroid lines
        cv2.line(imageTemp, (centroids[j][0]-15, centroids[j][1]), (centroids[j][0]+15, centroids[j][1]), (255, 255, 255), 1)
        cv2.line(imageTemp, (centroids[j][0], centroids[j][1]-15), (centroids[j][0], height), (255, 255, 255), 1)

    # Compute mean centroid using contour centroids and their respective masses
    mult = masses/sum(masses)
    centroidTotal = sum((centroids.T * mult).T, 0)

    try:
        cv2.line(imageTemp, (int(centroidTotal[0])-15, int(centroidTotal[1])), (int(centroidTotal[0])+15, int(centroidTotal[1])), (0, 0, 255), 2)
        cv2.line(imageTemp, (int(centroidTotal[0]), int(centroidTotal[1])-15), (int(centroidTotal[0]), height), (0, 0, 255), 2)
    except:
        pass
    # Write frame to videoOut
    videoOut.write(imageTemp)

# Clean up
cv2.destroyAllWindows()
videoIn.release()
videoOut.release()
```

Depending on the length and resolution of the video, this analysis can take a while. When the code finishes, we should have our output video file ready. Mine looks like this:


```python
YouTubeVideo('2epc_1mojQs', width=700, height=400)
```

{% include video.html id="2epc_1mojQs" %}

<br>

We can see that our approximated centre of mass roughly stays centered on top of the line. Of course, contour detection is not great in this example, as shadows are not captured in the coat. Also, the legs play a significant role in balance, and were not captured in our example. As mentioned earlier, with a bit of care, one could use motion detection, or combine black and white contours to pick up the legs and include them in the analysis. Orange leggings would also do the trick!

<hr>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT){:target="_ blank"}
The code snippets accompanying this project are available under an MIT license.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_ blank"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">The two example videos shown above, hosted in YouTube</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Alvaro Perez-Diaz</span> are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_ blank">Creative Commons Attribution 4.0 International License</a>.
