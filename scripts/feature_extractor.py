import cv2
import numpy as np

import os
import pickle as pkl


class LogoDetector:

import matplotlib.pyplot as plt

class FeatureDetector:

    def __init__(self) -> None:
        pass

    def createDetector(self):
        detector = cv2.ORB_create(nfeatures=2000)
        return detector

    def getFeatures(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detector = self.createDetector()
        kps, descs = detector.detectAndCompute(gray, None)
        return kps, descs
    
    def detectFeatures(self, query_img, train_img,threshold=0.8):
        
        # Convert it to grayscale
        # Convert it to grayscale
        query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
        train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)
            
       # Initialize the ORB detector algorithm
        orb = self.createDetector()

        # Now detect the keypoints and compute
        # the descriptors for the query image
        # and train image
        queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
        trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)
        
        # Initialize the Matcher for matching
        # the keypoints and then match the
        # keypoints
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(queryDescriptors,trainDescriptors,k=2)
        
        good = []
        for m,n in matches:
            if m.distance < threshold*n.distance:
                
                good.append(m)
        
        return queryKeypoints, trainKeypoints, good
        
    def plot_matching(self,matches,query_img,train_img,queryKeypoints,trainKeypoints):
        # draw the matches to the final image
        # containing both the images the drawMatches()
        # function takes both images and keypoints
        # and outputs the matched query image with
        # its train image
        final_img = cv2.drawMatches(query_img, queryKeypoints,
        train_img, trainKeypoints, matches,None)

        final_img = cv2.resize(final_img, (1000,650))

        # Show the final image
        plt.imshow(final_img)

        return kps, descs, img.shape[:2][::-1]

    def detectFeatures(self, imagePath, train_features):
        img = cv2.imread(imagePath)
        train_kps, train_descs, shape = train_features
        # get features from input image
        kps, descs, _ = self.getFeatures(img)
        # check if keypoints are extracted
        if not kps:
            return None
        # now we need to find matching keypoints in two sets of descriptors (from sample image, and from current image)
        # knnMatch uses k-nearest neighbors algorithm for that
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches = bf.knnMatch(train_descs, descs, k=2)
        good = []
        # apply ratio test to matches of each keypoint
        # idea is if train KP have a matching KP on image, it will be much closer than next closest non-matching KP,
        # otherwise, all KPs will be almost equally far
        for m, n in matches:
            if m.distance < 0.8 * n.distance:
                good.append([m])
        # stop if we didn't find enough matching keypoints
        if len(good) < 0.1 * len(train_kps):
            return None
        # estimate a transformation matrix which maps keypoints from train image coordinates to sample image
        src_pts = np.float32([train_kps[m[0].queryIdx].pt for m in good
                              ]).reshape(-1, 1, 2)
        dst_pts = np.float32([kps[m[0].trainIdx].pt for m in good
                              ]).reshape(-1, 1, 2)

        m, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        return m, mask
"""
if m is not None:
# apply perspective transform to train image corners to get a bounding box coordinates on a sample image
scene_points = cv2.perspectiveTransform(np.float32(
[(0, 0), (0, shape[0] - 1), (shape[1] - 1, shape[0] - 1), (shape[1] - 1, 0)]).reshape(-1, 1, 2), m)
rect = cv2.minAreaRect(scene_points)
# check resulting rect ratio knowing we have almost square train image
if rect[1][1] > 0 and 0.4 < (rect[1][0] / rect[1][1]) < 1.2:
# return bounding box
return rect
return None
"""


if __name__ == "__main__":
    dir_path = os.getcwd()

    assets_path = dir_path + "/Assets"

    # Change Asset folder name
    fol_name = '/2b7e702f208b7fd60d15d0bdadd269f4'

    # Change File name
    file_name = '/_preview.png'

    image_path = assets_path + fol_name + file_name

    features = LogoDetector()
    # get train features
    img = cv2.imread(image_path)
    train_features = features.getFeatures(img)
    # detect features on test image
    retval, mask = features.detectFeatures(image_path, train_features)
    
"""
if region is not None:
Saving the bounding box coordinates in a pickle file
with open('_preview.pkl', 'wb') as f:
pkl.dump(region, f)
draw rotated bounding box
box = cv2.boxPoints(region)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    
display the image
cv2.imshow("Preview", img)
"""
        if m is not None:
            # apply perspective transform to train image corners to get a bounding box coordinates on a sample image
            scene_points = cv2.perspectiveTransform(np.float32([(0, 0), (0, shape[0] - 1), (shape[1] - 1, shape[0] - 1), (shape[1] - 1, 0)]).reshape(-1, 1, 2), m)
            rect = cv2.minAreaRect(scene_points)
            # check resulting rect ratio knowing we have almost square train image
            if rect[1][1] > 0 and 0.8 < (rect[1][0] / rect[1][1]) < 1.2:
                return rect
        return None