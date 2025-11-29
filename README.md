# Distance measurement using single:one:camera :camera:

![GitHub Repo stars](https://img.shields.io/github/stars/Asadullah-Dal17/Distance_measurement_using_single_camera?style=social) ![GitHub forks](https://img.shields.io/github/forks/Asadullah-Dal17/Distance_measurement_using_single_camera?style=social) ![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCc8Lx22a5OX4XMxrCykzjbA?style=social)

If you want to estimate distance of objects with your simple webcam, then this algorithm(*Triangle similarity*) would be helpful for you to find Distance *from object to camera*, I have provide to two examples, one is simple **face detection and distance Estimation**, other is **Yolo4 object detection and distance Estimation**

Here in this readme file you will get short description, if need more details, then you can watch video tutorial on YouTube as well.

## Distance & Speed Estimation Demo

https://user-images.githubusercontent.com/66181793/122644855-bb8ac000-d130-11eb-85c3-c7ff4bd6474c.mp4

### Video Tutorials

[**Distance Estimation Youtube Tutorail**](https://youtu.be/zzJfAw3ASzY) ![YouTube Video Views](https://img.shields.io/youtube/views/zzJfAw3ASzY?style=social)

[**Distance & Speed Estimation Youtube Tutorial**](https://youtu.be/DIxcLghsQ4Q) ![YouTube Video Views](https://img.shields.io/youtube/views/DIxcLghsQ4Q?style=social)

[**YoloV4 Object Detection & Distance Estimation**](https://youtu.be/FcRCwTgYXJw) ![YouTube Video Views](https://img.shields.io/youtube/views/FcRCwTgYXJw?style=social)
[*Project GitHub Repository*](https://github.com/Asadullah-Dal17/Yolov4-Detector-and-Distance-Estimator)

## YoloV4 Distance Estimation

https://user-images.githubusercontent.com/66181793/124917186-f5066b00-e00c-11eb-93cf-24d84e9c2e7a.mp4

## Distance Estimation on Raspberry Pi 🍓 

https://user-images.githubusercontent.com/66181793/138200943-74d28b4d-bd0e-49fd-8836-4a01b35118eb.mp4

✔️ here is source code and details for Instllation of Opencv-python on 🍓 Pi 😃 [Distance Estimation on Raspberry pi 🍓](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera/tree/main/Raspberry_pi) 


:heavy_check_mark: I have included [**Speed Estimation**](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera/tree/main/Speed) code is well check that out.

:heavy_check_mark: You can find the implementation of  [**Distance estimation of multiple objects using Yolo V4**](https://github.com/Asadullah-Dal17/Yolov4-Detector-and-Distance-Estimator) Object Detector Opencv-python

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

The Focal Length finder Function has three Arguments:

`measured_distance` is the distance which we have measured while capturing the reference image:straight*ruler:. \*\*\_From object to Camera*\*\* which is `Known_distance = 72.2 #centimeter`

`real_width` It's measured as the width of the object in the real world, here I measured the width of the face in real-world which was `Known_width =14.3 # centimetre`

`width_in_rf_image` is the width of the object in the image/frame it will be in **pixels**

### :bulb:_Distance Finder Function Description_ :bulb:

```python
# Distance estimation function

def distance_finder(focal_length, real_face_width, face_width_in_frame):

    distance = (real_face_width * focal_length)/face_width_in_frame
    return distance

```

This Function takes three Arguments,

` Focal_Length` is the focal length, out of the **FocalLength** finder function.

`real_face_width` measures the width of an object in the real world, here I measured the width of a face in real-world which was `Known_width =14.3 #centimeter`

`face_width_in_frame` is the width of the face in the frame, the unit will be pixels here.



I have also created <a href ="https://github.com/Asadullah-Dal17/Face-Following-Robot-using-Distance-Estimation"> <strong>Face Following Robot </strong> </a> which uses distance Estimation If you are interested you can Watch my<a href ="https://youtu.be/5FSOZe96kNg"> <strong>Youtube Video</strong> </a> 
You can create the following Robot with Raspberry That would be easy then, using Arduino Stuff, Raspberry 🍓 Pi will make it a system on Robot 🤖

If you found this helpful, please star :star: it.

You can Watch my Video Tutorial on Computer Vision Topics, just check out my YouTube Channel <a href="https://www.youtube.com/c/aiphile">  <img alt="AiPhile Youtube" src="https://user-images.githubusercontent.com/66181793/131223988-882d53a0-4882-468f-9bd7-46b46466baae.png"  width="20"> </a>


## 📫 Let's Connect

<div align=\"center\">

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@asadullah-dal)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/aiphile17)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/aiphile)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ai_phile)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@aiphile)
[![Portfolio](https://img.shields.io/badge/Portfolio-00C7B7?style=for-the-badge&logo=About.me&logoColor=white)](https://asadullah-dal17.github.io/asadullahdal.github.io)

### 💼 Freelance Platforms

[![Fiverr](https://img.shields.io/badge/Fiverr-1DBF73?style=for-the-badge&logo=fiverr&logoColor=white)](https://www.fiverr.com/asadullahdal482)
[![Kwork](https://img.shields.io/badge/Kwork-Freelance-black?style=for-the-badge&logo=kwork&logoColor=white)](https://kwork.com/user/asadullah92)

</div>

## 💬 Questions or Need Help?

If you have any questions or need help with the project, feel free to DM me on [Instagram](https://www.instagram.com/aiphile17)!

<a href="https://www.instagram.com/aiphile17">
    <img src="https://img.shields.io/badge/Instagram-purple?style=for-the-badge&logo=Instagram&logoColor=white" height=20  alt="Insta Badge"/>
  </a>

