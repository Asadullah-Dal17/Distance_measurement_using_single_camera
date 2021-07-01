import cv2 as cv


# data
Know_distance =30 # in centimeters
#mine is 14.3 something, measure your face width, are google it 
Know_width_face =14.3 #centimeters
# chose your camera
cam_number =1
face_detector = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
camera = cv.VideoCapture(cam_number)
def FocalLengthFinder(Measured_distance, real_width_of_face, width_of_face_in_image):
    # finding focal length
    focal_length = (width_of_face_in_image* Measured_distance)/real_width_of_face
    return focal_length

def Distance_Measurement(face_real_width, Focal_Length, face_with_in_image):
   distance= (face_real_width * Focal_Length)/face_with_in_image 
   return distance 
def Face_Detection(image):
    f_width =0
    Gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(Gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv.rectangle(image, (x,y), (x+w, y+h), (255,255,255), 1)
        f_width =w
    print(f_width)
    return f_width, image
reference_image =cv.imread("rf.png")
face_w , image_read= Face_Detection(reference_image)
cv.imshow("ref", image_read)
calculate_focal_length =FocalLengthFinder(Know_distance, Know_width_face,face_w)
print(calculate_focal_length)
font = cv.FONT_HERSHEY_SIMPLEX 
while True:
    ret, frame = camera.read()
    height, width, dim = frame.shape
    # change the color of image
    # print(height, width)
    Gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(Gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 1)
        distance =Distance_Measurement(Know_width_face,calculate_focal_length, w)
        print(distance)

        cv.putText(frame, f" Distance = {distance}", (50,50),font, 0.7, (0,255,0), 3)

    cv.imshow('frame', frame)

    if cv.waitKey(1)==ord('q'):
        break
camera.release()
cv.destroyAllWindows()
