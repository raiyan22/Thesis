# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:54:39 2022

@author: Asus
"""

import cv2
import os
import shutil
import datetime
import time #to calculate frame per second 
import numpy as np

path = "F:/captures/4th year thesis/datasets/Sign language/training"

dir_list = os.listdir(path)

        
for sup in dir_list:
    # print(sup)
    sup_path = os.path.join(path, sup)
    sup_dir = os.listdir(sup_path)
    # count = 0
    for sub in sup_dir:
        file_path = os.path.join(sup_path, sub)
        file_dir = os.listdir(file_path)
        count = 0
        for file in file_dir:
            # print(file)
            dt = os.path.join(file_path,file)
            data = np.load(dt)
            if(len(data)!=126):
                print(len(data))