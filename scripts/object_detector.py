from pathlib import Path
import cv2
   
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
        print('Shape of pre-processed image:', x.shape)
        class_IDs, scores, bounding_boxs = net(x)
        
        return class_IDs, scores, bounding_boxs,img
    
    def detect_from_video(self,video_path,net):
        # Opens the Video file
        cap= cv2.VideoCapture('football1.mp4')
        i=0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            cv2.imwrite('kang'+str(i)+'.jpg',frame)
            i+=1
            x, img = data.transforms.presets.yolo.load_test('kang'+str(i)+'.jpg', short=512)
            print('Shape of pre-processed image:', x.shape)
            class_IDs, scores, bounding_boxs = net(x)
            
            cap.release()
            cv2.destroyAllWindows()
            
        return class_IDs, scores, bounding_boxs,img
        
    def plot_detection(self,img,class_IDs, scores, bounding_boxs):
       ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
                                class_IDs[0], class_names=self.net.classes)
       plt.show() 