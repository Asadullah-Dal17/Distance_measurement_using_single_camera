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
## linux or Mac: 
python3 distance.py


### *Focal Length Finder Function Description* 

```python
# focal length finder function
def FocalLength(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image* measured_distance)/ real_width
    return focal_length

```
The Focal Length finder Function Tacks Three Arguments:

```measured_distance``` It is distance which we have measured while capturing reference image. ***From object to Camera*** which is ```Known_distance = 30 #centimeter```  


```real_width``` Its measure with width of object in real world, here i measure the width of face in real world which was ```Known_width =14.3 #centimeter```  

```width_in_rf_image``` it width of object in the image/frame it will be in **pixels**









Youtube Video: https://youtu.be/zzJfAw3ASzY

