import cv2 as cv 
import numpy as np
# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (255,0,0)
RED = (0,0,255)
CYAN = (255,255,0)
YELLOW =(0,255,255)
MAGENTA = (255,0,255)
GREEN = (0,255,0)
PURPLE = (128,0,128)
ORANGE = (0,165,255)
PINK = [147,20,255]    
INDIGO=[75,0,130]   
VIOLET=[238,130,238]   
GRAY=[127,127,127]  

def textBG(img, text, position, fonts ,scaling=1, color=(0,255,0), thickness=1, padding=3):
    img_h, img_w = img.shape[:2]
    x, y = position
    (w, h ), p= cv.getTextSize(text, fonts, scaling, thickness)
    # print(w, h)
    cv.rectangle(img, (x-p, y+p), (x+w+p, y-h-p), (255, 0,234), -1)
    
    cv.putText(img, text, position,fonts, scaling,  color, thickness)

def textBGoutline(img, text, position, fonts=cv.FONT_HERSHEY_SIMPLEX ,scaling=1, text_color=(0,255,0), thickness=1, bg_color=(BLACK)):
    img_h, img_w = img.shape[:2]
    x, y = position
    (w, h ), p= cv.getTextSize(text, fonts, scaling, thickness)
    # print(w, h)
    cv.rectangle(img, (x-p, y+p), (x+w+p, y-h-p), bg_color, -1)
    cv.rectangle(img, (x-p, y+p), (x+w+p, y-h-p), text_color,thickness, cv.LINE_AA)
    
    cv.putText(img, text, position,fonts, scaling,  text_color, thickness, cv.LINE_AA    )
def fillPolyTrans(img, points, color, opacity, line_thickness=2):
    """
    @param img: (mat) input image, where shape is drawn.
    @param points: list [tuples(int, int) these are the points custom shape,FillPoly
    @param color: (tuples (int, int, int)
    @param opacity:  it is transparency of image.
    @return: img(mat) image with rectangle draw.

    """
    list_to_np_array = np.array(points, dtype=np.int32)
    overlay = img.copy()  # coping the image
    cv.fillPoly(overlay,[list_to_np_array], color )
    new_img = cv.addWeighted(overlay, opacity, img, 1 - opacity, 0)
    # print(points_list)
    img = new_img
    cv.polylines(img, [list_to_np_array], True, color,line_thickness, cv.LINE_AA)
    return img
