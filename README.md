# Distance measurement using single:one:camera :camera:

![GitHub Repo stars](https://img.shields.io/github/stars/Asadullah-Dal17/Distance_measurement_using_single_camera?style=social) ![GitHub forks](https://img.shields.io/github/forks/Asadullah-Dal17/Distance_measurement_using_single_camera?style=social) ![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCc8Lx22a5OX4XMxrCykzjbA?style=social)

You can use this code to measures the distance from object to camera using **_single camera_** :camera: .

I have detect a face in the frame and estimated a distance using the width of face.

## Distance & Speed Estimation Demo

https://user-images.githubusercontent.com/66181793/122644855-bb8ac000-d130-11eb-85c3-c7ff4bd6474c.mp4

### Video Tutorials
[**Distance Estimation Youtube Tutorail**](https://youtu.be/zzJfAw3ASzY) ![YouTube Video Views](https://img.shields.io/youtube/views/zzJfAw3ASzY?style=social)

[**Distance & Speed Estimation Youtube Tutorial**](https://youtu.be/DIxcLghsQ4Q) ![YouTube Video Views](https://img.shields.io/youtube/views/DIxcLghsQ4Q?style=social)

[**YoloV4 Object Detection & Distance Estimation**](https://youtu.be/FcRCwTgYXJw) ![YouTube Video Views](https://img.shields.io/youtube/views/FcRCwTgYXJw?style=social)

## YoloV4 Distance Estimation

https://user-images.githubusercontent.com/66181793/124917186-f5066b00-e00c-11eb-93cf-24d84e9c2e7a.mp4



:heavy_check_mark: I have included [**Speed Estimation**](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera/tree/main/Speed) code is well check that out.

:heavy_check_mark: I have include [**Distance estimation of multiple objects using Yolo V4**](https://github.com/Asadullah-Dal17/Yolov4-Detector-and-Distance-Estimator) Object Detector Opencv-python

## Clone this Repo:

git clone https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera

## install Opencv-python

- Windows

  pip install opencv-python

- _install Opencv-python on Linux or Mac_

  pip3 install opencv-python

## Run the code

- windows: :point_down:

  python distance.py

  ------ OR ---------

  python Updated_distance.py

- linux or Mac :point_down:

  python3 distance.py

  ------ OR ---------

  python3 Updated_distance.py

### :bulb:_Focal Length Finder Function Description_ :bulb:

```python
# focal length finder function
def focal_length(measured_distance, real_width, width_in_rf_image):

    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    #return focal length.
    return focal_length_value

```

The Focal Length finder Function Tacks Three Arguments:

`measured_distance` It is distance which we have measured while capturing reference image:straight*ruler:. \*\*\_From object to Camera*\*\* which is `Known_distance = 72.2 #centimeter`

`real_width` Its measure with width of object in real world, here i measure the width of face in real world which was `Known_width =14.3 #centimeter`

`width_in_rf_image` it width of object in the image/frame it will be in **pixels**

### :bulb:_Distance Finder Function Description_ :bulb:

```python
# distance estimation function

def distance_finder(focal_length, real_face_width, face_width_in_frame):

    distance = (real_face_width * focal_length)/face_width_in_frame
    return distance

```

This Funciton Taks Three Argument,

` Focal_Length` it is focal length, out of **FocalLength** finder function.

`real_face_width` Its measure width of object in real world, here i measure the width of face in real world which was `Known_width =14.3 #centimeter`

`face_width_in_frame` width of face in the frame, unit will pixels here.



I have also create <a href ="https://github.com/Asadullah-Dal17/Face-Following-Robot-using-Distance-Estimation"> <strong>Face Following Robot </strong> </a> which use distance Estimation, if you are interested you can Watch my<a href ="https://youtu.be/5FSOZe96kNg"> <strong>Youtube Video</strong> </a>

if You found this Helpful, please star :star: it.

if you have any Query feel free to ask me on my Social Media.

Keep me motivated to work on project like these, please subscribe to my Youtube Channel <img src ="/icons/youtub-icon.svg" width ="30">

## :green_heart: Join Me on Social Media :green_heart:

<a href="https://www.youtube.com/c/aiphile"> <img alt="AiPhile Youtube" src="icons/youtub-icon.svg"  width="60" height="60">
</a>
<a href="https://www.facebook.com/AIPhile17">
<img alt="AiPhile Facebook" src="icons/facebook-icon.svg"  width="60" height="60">
</a>
<a href="https://www.instagram.com/aiphile17/"> <img alt="AiPhile Insta" src="icons/instagram-icon.svg"  width="60" height="60">
</a>
<a href="https://github.com/Asadullah-Dal17"> <img alt="Github" src="icons/github-icon.svg"  width="60" height="60">
</a>
