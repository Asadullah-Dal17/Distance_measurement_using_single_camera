# Distance_measurement_using_single_camera


## Clone this Repo:
git clone https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera

## install Opencv-python on Windows 
pip install opencv-python

install Opencv-python on Linux or Mac
pip3 install opencv-python

# Run the code
## windows:
python distance.py

------ OR ---------

python Updated_distance.py

## linux or Mac: 
python3 distance.py

------ OR ---------

python3 Updated_distance.py



### *Focal Length Finder Function Description* 

```python
# focal length finder function
def FocalLength(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image* measured_distance)/ real_width
    return focal_length

```
The Focal Length finder Function Tacks Three Arguments:

```measured_distance``` It is distance which we have measured while capturing reference image. ***From object to Camera*** which is ```Known_distance = 72.2 #centimeter```  


```real_width``` Its measure with width of object in real world, here i measure the width of face in real world which was ```Known_width =14.3 #centimeter```  

```width_in_rf_image``` it width of object in the image/frame it will be in **pixels**


### *Distance Finder Function Description* 

```python
# distance estimation function
def Distance_finder (Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length)/face_width_in_frame
    return distance

```
This Funciton Taks Three Argument, 

``` Focal_Length``` it is focal length, out of **FocalLength** finder function.

```real_face_width``` Its measure with width of object in real world, here i measure the width of face in real world which was ```Known_width =14.3 #centimeter```  

```face_width_in_frame``` width of face in the frame, unit will pixels here.


You can Which my Video on the Youtube. As well
Youtube Video: https://youtu.be/zzJfAw3ASzY

if You found this Helpful, please star it.

if you have any Query feel free to ask me on my Social Media.

### Updated_Distance.py Looks something likes This.


<img alt="Gif Update Distnace code " src="Update-Distance-Output.gif">


I have also create  <a href ="https://github.com/Asadullah-Dal17/Face-Following-Robot-using-Distance-Estimation"> <strong>Face Following Robot </strong> </a> which use distance Estimation, if you are interested you can Watch my<a href ="https://youtu.be/5FSOZe96kNg"> <strong>Youtube Video</strong>  </a> 
## Join Me on Social Media

<a href="https://www.youtube.com/c/aiphile"> <img alt="AiPhile Youtube" src="icons/youtube.svg"  width="60" height="60">
</a>
<a href="https://www.facebook.com/AIPhile17">
<img alt="AiPhile Facebook" src="icons/facebook.svg"  width="60" height="60">
</a>
<a href="https://www.instagram.com/aiphile17/"> <img alt="AiPhile Insta" src="icons/insta.svg"  width="60" height="60">
</a>
<a href="https://github.com/Asadullah-Dal17"> <img alt="Github" src="icons/github.svg"  width="60" height="60">
</a>

