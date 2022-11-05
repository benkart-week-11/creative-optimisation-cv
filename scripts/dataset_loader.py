import os, glob
import numpy as np
import cv2
import pandas as pd
from sklearn.model_selection import train_test_split

class DatasetLoader:
    def __init__(self,image_folder='../data/Challenge_Data/Assets/*',
                 numeric_path='../data/selected_numeric_feature.csv', 
                 IMG_WIDTH=256,
                 IMG_HEIGHT=256):
        self.image_folder = image_folder
        self.numeric_path = numeric_path
        self.IMG_WIDTH=IMG_WIDTH
        self.IMG_HEIGHT=IMG_HEIGHT
        
    def read_numerical_data(self):
        return pd.read_csv(self.numeric_path) 
   
    def read_image_data(self):
        folder_list = glob.glob(self.image_folder)
        img_data_array=[]
        img_id=[]
        for folder in folder_list:
            image_path = os.path.join(folder,'_preview.png')
            if os.path.exists(image_path):
                image= cv2.imread( image_path, cv2.COLOR_BGR2RGB)
                image=cv2.resize(image, (self.IMG_HEIGHT, self.IMG_WIDTH),interpolation = cv2.INTER_AREA)
                image=np.array(image)
                image = image.astype('float32')
                image /= 255 
                img_data_array.append(image)
                img_id.append(folder.split('/')[-1])
                # extract the image array and class name

        img_df = pd.DataFrame({'img':img_data_array,'id':img_id})
   
        return img_df
    
    def merge_data_from_multiple_source(self):
        # extract the image array and class name
        
        img_df = self.read_image_data()
        numeric_df = self.read_numerical_data()
        dataset = img_df.merge(numeric_df,on='id')
        
        return dataset.drop(['id'],axis=1)
    def dataset_preprocess(self,x,y):
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
        
        img_train = X_train['img']
        
        numeric_train = X_train[[str(x) for x in range(256)]]

        img_test = X_test['img']
        numeric_test = X_test[[str(x) for x in range(256)]]


        imgtr=[]
        for im in img_train:
            imgtr.append(im)
            
        imgtt=[]
        for im in img_test:
            imgtt.append(im)

        img_train_data =  np.array(imgtr)
        img_test_data =  np.array(imgtt)
        
        return img_train_data,img_test_data,numeric_train,numeric_test, y_train, y_test            
