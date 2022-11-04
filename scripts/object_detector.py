from pathlib import Path
import cv2
import os
   
from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt

class ObjectDetector:
    def __init__(self,mode,net=None) -> None:
        self.mode = mode
        self.net = net
    def load_yolo(self):
        self.net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)
        return self.net
     
    def detect_from_image(self,image_path,net):
        x, img = data.transforms.presets.yolo.load_test(image_path, short=512)
        # print('Shape of pre-processed image:', x.shape)
        class_IDs, scores, bounding_boxs = net(x)
        return class_IDs, scores, bounding_boxs,img
    
    def detect_from_video(self,video_path,net):
        result = {'class_IDs':[],
                  'scores':[],
                  'bounding_boxs':[],
                  'img':[]}
        # Opens the Video file
        cap= cv2.VideoCapture(video_path)
        i=0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            ps = (frame>0).sum()
            tp = frame.shape[0]*frame.shape[1]
            cv2.imwrite('kang'+str(i)+'.jpg',frame)
            x, img = data.transforms.presets.yolo.load_test('kang'+str(i)+'.jpg', short=512)
            # print('Shape of pre-processed image:', x.shape)
            class_IDs, scores, scores = net(x)
            
            result['class_IDs'].append(class_IDs)
            result['scores'].append(scores)
            result['bounding_boxs'].append(scores) 
            result['img'].append(img)
            if os.path.isfile('kang'+str(i)+'.jpg'):
                os.remove('kang'+str(i)+'.jpg')
            i+=1
        cap.release()
        cv2.destroyAllWindows()
            
        return result
        
    def plot_detection(self,img,class_IDs, scores, bounding_boxs):
       ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
                                class_IDs[0], class_names=self.net.classes)
       plt.show() 