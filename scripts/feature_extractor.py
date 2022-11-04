import cv2
import numpy as np
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
    

            