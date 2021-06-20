
import cv2 
import time
import os
# chose your camera number:
cam_number =2
camera = cv2.VideoCapture(cam_number)
starting_time =time.time()
Frame_Counter= 0
Cap_frame =0 
Dir_name = "capture_images"
number_image_captured =20
capture_image=False
while True:
    # checking the Directory Exist or not .
    IsDirExist = os.path.exists(Dir_name)
    print(IsDirExist)
    # if there is no Directory named "capture_image", simply create it. using os 
    if not IsDirExist:
        os.mkdir(Dir_name)

    Frame_Counter+=1
    # reading the frames from camera 
    ret, frame = camera.read()
    # reading saving frame seperatly
    ret, saving_frame = camera.read()
    # finding with and height of image 
    height, width, dim = saving_frame.shape
    # print(width, height, dim)

    # writing the width and height of on the image saving image 
    cv2.putText(saving_frame, f"Height: {height}", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,255,0),1)
    cv2.putText(saving_frame, f"Width:  {width}", (30, 70), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,255,0),1)
    # capture frame if capture_image is ture and number_image_captured are less then 10
    # if we press 'c' on keyboard then capture_image become 'True'
    if capture_image==True and Cap_frame <= number_image_captured:
        Cap_frame+=1
        cv2.putText(frame, 'Capturing', (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0,244, 255),1)
        cv2.imwrite(f"{Dir_name}/frame-{Cap_frame}.png", saving_frame)
    else:
        cv2.putText(frame, 'Not Capturing', (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0, 255),1)
        Cap_frame =0
        capture_image =False
    cv2.imshow("frame", frame)
    cv2.imshow("saving Image", saving_frame)
    total_time = time.time()
    frame_time=total_time -starting_time
    # calculating how much frame pass in each second

    fps = Frame_Counter/frame_time
    # print(fps)
    # print(capture_image)
     # when we press 'q' it quites the program
    if cv2.waitKey(1) == ord('q'):
        break
    # if we press 'c' on the keyboard then it starts capturing the images. 
    if cv2.waitKey(1)==ord('c'):
        capture_image= True
   
# finally closing the camera 
camera.release()
# closing all opend windows
cv2.destroyAllWindows()