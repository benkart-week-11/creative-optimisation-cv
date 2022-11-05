# import the necessary packages
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.layers import Concatenate, concatenate
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
import tensorflow as tf

import pandas as pd


class BuildModel:
    def __init__(self):
        pass
    
    def create_mlp(self,x):
    x = Dense(256, activation="relu")(x)
    x = Dense(256, activation="relu")(x)
    x = Dense(128, activation="relu")(x) 
    return x

  
    def mode4text_feature(self,x):
        x = Dense(256, activation="relu")(x)
        x = Dense(256, activation="relu")(x)
        x = Dense(128, activation="relu")(x) 
        return x

    def pretrained_cnn_model(self,x_inputs):
        mobilenetv2 = tf.keras.applications.MobileNetV2(
            input_tensor = x_inputs, 
            weights="imagenet", include_top=False, alpha=0.35) 
        x = mobilenetv2.get_layer('out_relu').output
        x = GlobalAveragePooling2D(name='gap')(x)
        x = Dense(128,activation='relu')(x)
        return x
    def build_model(self,input1_shape, input2_shape,input3_shape):
        input1 = Input(shape=input1_shape, name="input_image")
        input2 = Input(shape=input2_shape, name="input_numerical") 
        # input3 = Input(shape=input3_shape, name="input_text")  
        
        x_image = self.pretrained_cnn_model(input1)
        x_numerical = self.create_mlp(input2)
        # x_text = self.mode4text_feature(input3)
        
        x = Concatenate(axis=1)([x_image,x_numerical])
        x = Dense(20, activation='relu')(x)
        x = Dense(1, activation="linear")(x)

        return tf.keras.Model(inputs=[input1,input2],outputs=x)
    
    def train_model(self,train_x,train_y):
        model = build_model(input1_shape=(256,256,3), input2_shape=(256),input3_shape=(256))
        opt =  tf.keras.optimizers.Adam(learning_rate=1e-3, decay=1e-3 / 200)
        model.compile(loss="mean_absolute_percentage_error", optimizer=opt)
        
        history = model.fit( x=[tf.cast(img_train_data,tf.float64), tf.cast(numeric_train,tf.float64)],
                  y = tf.cast(y_train, tf.float64),
                  epochs=15,batch_size=8)
        