# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:14:25 2022

@author: Asus
"""

import cv2
import os
import shutil
import datetime
import time #to calculate frame per second 
import numpy as np

path = "F:/captures/4th year thesis/datasets/Sign language/Videos"

dir_list = os.listdir(path)

for sup in dir_list:
    # print(sup)
    sup_path = os.path.join(path, sup)
    sup_dir = os.listdir(sup_path)
    count = 0
    for sub in sup_dir:
        dst = f"{sup}_{str(count)}.mp4"
        src =f"{sup_path}/{sub}"  # foldername/filename, if .py file is outside folder
        dst =f"{sup_path}/{dst}"
        
        # print(dst)
        # print(src)
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        count = count+1