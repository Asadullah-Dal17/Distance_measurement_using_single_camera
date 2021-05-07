# Distance measurement using single:one:camera :camera:

You can use this code to measuere the distance from object to camera using **_single camera_** :camera: .

I have detect a face in the frame and estimated a distance using the width of face.

I have included [**Speed Estimation**](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera/tree/main/Speed) code is well check that out.

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
def FocalLength(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image* measured_distance)/ real_width
    return focal_length

```

The Focal Length finder Function Tacks Three Arguments:

`measured_distance` It is distance which we have measured while capturing reference image:straight*ruler:. \*\*\_From object to Camera*\*\* which is `Known_distance = 72.2 #centimeter`

`real_width` Its measure with width of object in real world, here i measure the width of face in real world which was `Known_width =14.3 #centimeter`

`width_in_rf_image` it width of object in the image/frame it will be in **pixels**

### :bulb:_Distance Finder Function Description_ :bulb:

```python
# distance estimation function
def Distance_finder (Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length)/face_width_in_frame
    return distance

```

This Funciton Taks Three Argument,

` Focal_Length` it is focal length, out of **FocalLength** finder function.

`real_face_width` Its measure width of object in real world, here i measure the width of face in real world which was `Known_width =14.3 #centimeter`

`face_width_in_frame` width of face in the frame, unit will pixels here.

You can Watch my Video on the Youtube: https://youtu.be/zzJfAw3ASzY

### Updated_Distance.py Looks something likes This.

[Youtube Tutorial](https://youtu.be/zzJfAw3ASzY)

<img alt="Gif Update Distnace code " src="Ouput_Updated_distance.gif">

### Speed and Distance Estimation

[Youtube Tutorial](https://youtu.be/DIxcLghsQ4Q)
<img alt="speed and Distance Estimation" src="speed_distance_estiamtion.gif">

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
