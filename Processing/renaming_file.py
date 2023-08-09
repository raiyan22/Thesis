# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:32:00 2022

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
            dst = f"{str(count)}.npy"
            src =f"{file_path}/{file}"  # foldername/filename, if .py file is outside folder
            dst =f"{file_path}/{dst}"
            
            # print(dst)
            # print(src)
             
            # rename() function will
            # rename all the files
            os.rename(src, dst)
            count = count+1