import cv2 as cv
import time
# Required Distance data
MobileWith = 3.0  # inches
PersonWidth = 16  # Inches
KnownDistance = 45  # Inches

# setting parameters
CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.3
fonts1 = cv.FONT_HERSHEY_COMPLEX_SMALL
fonts2 = cv.FONT_HERSHEY_PLAIN
fonts3 = cv.FONT_HERSHEY_SIMPLEX

# colors for object detected
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 242)
GOLDEN = (32, 218, 165)
LIGHT_BLUE = (255, 9, 2)
PURPLE = (128, 0, 128)
CHOCOLATE = (30, 105, 210)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)
fonts = cv.FONT_HERSHEY_COMPLEX
# reading class name from text file
class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
#  setttng up opencv net
yoloNet = cv.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

model = cv.dnn_DetectionModel(yoloNet)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)


def FocalLength(measured_distance, real_width, width_in_rf_image):

    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length
# distance estimation function


def Distance_finder(Focal_Length, real_object_width, object_width_in_frame):

    distance = (real_object_width * Focal_Length)/object_width_in_frame
    return distance


def ObjectDetector(image):
    position = None
    objWidth = 2
    classes, scores, boxes = model.detect(
        image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    DataList = []
    box = None
    for (classid, score, box) in zip(classes, scores, boxes):

        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        # print(class_names[classid[0]])

        if classid == 0:
            objWidth = box[2]
            DataList.append(
                [class_names[classid[0]], box[2], (box[0], box[1]-14)])

            # print(label)
            # distance in centimeters
            # Distance = Distance_finder(FL[0], PersonWidth, box[2])
            # label = f'Distance = {round(Distance,2)} Inches'
        elif classid == 67:
            DataList.append(
                [class_names[classid[0]], box[2], (box[0], box[1] - 14)])
            objWidth = box[2]
        # adding more then two classes for distance estimation
            '''     
        elif classid == classId:
            DataList.append(
                [class_names[classid[0]], box[2], (box[0], box[1] - 14)])
            objWidth = box[2]
        
        '''

            # print(label)
            position = (box[0], box[1]-14)
        # print(DataDict)
        cv.rectangle(image, box, color, 2)
        cv.putText(image, label, (box[0], box[1]-10), fonts, 0.42, color, 1)
    return DataList, box


Ref_person = cv.imread("ReferenceImages/image14.png")
ref_Mobile = cv.imread('ReferenceImages/image4.png')
# print(f"mob {}")

mobilePxWidth, _ = ObjectDetector(ref_Mobile)
personPxWidth, _ = ObjectDetector(Ref_person)
print(mobilePxWidth[1][1].shape)
print(len(mobilePxWidth))

pFocalLength = FocalLength(KnownDistance, PersonWidth, personPxWidth[0][1])
mFocalLength = FocalLength(KnownDistance, MobileWith, mobilePxWidth[1][1])
# more classes
'''
mFocalLength = FocalLength(KnownDistance, MobileWith, mobilePxWidth[2][1])
'''




camera = cv.VideoCapture(1)
fourcc = cv.VideoWriter_fourcc(*'XVID')
camera.set(cv.CAP_PROP_FPS, 7)
# out = cv.VideoWriter('Output.mp4', fourcc, 7.0, (640, 480))
print(
    f'Mobile Focal Length : {mFocalLength} Person Focal Length:  {pFocalLength}')
frameCounter = 0
starting_time = time.time()
while True:
    # break
    frameCounter += 1

    ret, frame = camera.read()
    # orignal = frame.copy()
    objectData, position = ObjectDetector(
        frame)
    objRealWidth = None
    distance = None
    position = (0, 0)
    x, y = 0, 0
    for d in objectData:
        # print(d)
        if d[0] == 'person':
            x, y = d[2]
            distance = Distance_finder(pFocalLength, PersonWidth, d[1])
        elif d[0] == 'cell phone':
            distance = Distance_finder(mFocalLength, MobileWith, d[1])
            x, y = d[2]
        # print(position)
        cv.line(frame, (x, y-22+50), (x+130, y-22+50), (0, 0, 0), 24)
        cv.putText(frame, f'Distance: {round(distance,1)} In',
                   (x, y-20+50), fonts, 0.42, (0, 255, 0), 1)  # /39.3701

    end_time = time.time() - starting_time
    # print(end_time)
    fps = frameCounter/end_time
    # print(fps)
    cv.line(frame, (37, 34), (130, 34), (0, 0, 0), 26)
    cv.putText(frame, f'FPS: {round(fps,1)}',
               (40, 40), fonts, 0.7, (255, 0, 255), 1)
    # cv.imshow('oringal', orignal)



    # out.write(frame)

    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()

# out.release()
camera.release()
