import cv2
import serial
# variables
# distance from camera to object(face) measured
Known_distance = 30 #centimeter
# width of face in the real world or Object Plane
Known_width =14.3
# Colors  >>> BGR Format(BLUE, GREEN, RED)
GREEN = (0,255,0) 
RED = (0,0,255)
BLACK = (0,0,0)
YELLOW =(0,255,255)
WHITE = (255,255,255)

fonts = cv2.FONT_HERSHEY_COMPLEX
fonts2 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
fonts3 =cv2.FONT_HERSHEY_COMPLEX_SMALL
fonts4 =cv2.FONT_HERSHEY_TRIPLEX
# Camera Object 
cap = cv2.VideoCapture(2) # Number According to your Camera
Distance_level =0
# face detector object
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# focal length finder function
def FocalLength(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image* measured_distance)/ real_width
    return focal_length
# distance estimation function
def Distance_finder (Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length)/face_width_in_frame
    return distance
#face detection Fauction 
def face_data(image, CallOut, Distance_level):
    face_width = 0
    face_x, face_y =0,0
    face_center_x =0
    face_center_y =0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        line_thickness =2
        print(len(faces))
        LLV = int(h*0.12) 
        # print(LLV)

        # cv2.rectangle(image, (x, y), (x+w, y+h), BLACK, 1)
        cv2.line(image, (x,y+LLV), (x+w, y+LLV), (GREEN),line_thickness)
        cv2.line(image, (x,y+h), (x+w, y+h), (GREEN),line_thickness)
        cv2.line(image, (x,y+LLV), (x, y+LLV+LLV), (GREEN),line_thickness)
        cv2.line(image, (x+w,y+LLV), (x+w, y+LLV+LLV), (GREEN),line_thickness)
        cv2.line(image, (x,y+h), (x, y+h-LLV), (GREEN),line_thickness)
        cv2.line(image, (x+w,y+h), (x+w, y+h-LLV), (GREEN),line_thickness)

        face_width = w
        face_center=[]
        # Drwaing circle at the center of the face 
        face_center_x =int(w/2)+x
        face_center_y =int(h/2)+y
        if Distance_level <10:
            Distance_level=10
        
        # cv2.circle(image, (face_center_x, face_center_y),5, (255,0,255), 3 )
        if CallOut==True:
            # cv2.line(image, (x,y), (face_center_x,face_center_y ), (155,155,155),1)
            cv2.line(image, (x,y-11), (x+210, y-11), (YELLOW), 25)
            cv2.line(image, (x,y-11), (x+Distance_level, y-11), (GREEN), 25)
            
            # cv2.circle(image, (face_center_x, face_center_y),2, (255,0,255), 1 )
            # cv2.circle(image, (x, y),2, (255,0,255), 1 )
           
        # face_x = x
        # face_y = y

    return face_width, faces, face_center_x, face_center_y

# reading reference image from directory
ref_image = cv2.imread("Ref_image.png")

ref_image_face_width,_, _,_= face_data(ref_image, False, Distance_level)
Focal_length_found = FocalLength(Known_distance, Known_width, ref_image_face_width)
print(Focal_length_found)

cv2.imshow("ref_image", ref_image)

while True:
    _, frame = cap.read()
    # calling face_data function
    # Distance_leve =0

    face_width_in_frame,Faces ,FC_X, FC_Y= face_data(frame, True, Distance_level)
    # finding the distance by calling function Distance finder
    for (face_x, face_y, face_w, face_h) in Faces:
        if face_width_in_frame !=0:

            Distance = Distance_finder(Focal_length_found, Known_width,face_width_in_frame)
            Distance = round(Distance,2)
            # Drwaing Text on the screen
            Distance_level= int(Distance)

            cv2.putText(frame, f"Distance {Distance} CM", (face_x-6,face_y-6), fonts,0.7, (BLACK),2)
    cv2.imshow("frame", frame )

    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
