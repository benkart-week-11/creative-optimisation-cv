import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class MatchingDetector:
    def __init__(self,mode) -> None:
        self.mode = mode
        
    def template_matching_image(self,template_path, image_path, method='cv.TM_CCOEFF'):
        img = cv.imread(image_path,0)
        img2 = img.copy()
        template = cv.imread(template_path,0)
        w, h = template.shape[::-1]
        # All the 6 methods for comparison in a list
       
        img = img2.copy()
        method = eval(method)
        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img,top_left, bottom_right, 255, 2)
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(method)
        plt.show()
        