# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:54:17 2022

@author: Asus
"""

import cv2
import os
import shutil
import datetime
import time #to calculate frame per second 
import numpy as np

path = "F:/captures/4th year thesis/datasets/Sign language/point data"
out_path = "F:/captures/4th year thesis/datasets/Sign language/training"

dir_list = os.listdir(path)

# print(dir_list)

for fol in dir_list:
    # print(fol)
# fol = dir_list[0]
    child_folder = fol
    split = child_folder.split("_")
    sup_fol = split[0]
    # print(sup_fol)
    out_super = os.path.join(out_path,sup_fol)
    if os.path.exists(out_super):
        shutil.rmtree(out_super)
    os.mkdir(out_super)
    

for fol in dir_list:
    # print(fol)
# fol = dir_list[0]
    child_folder = fol
    split = child_folder.split("_")
    sup_fol = split[0]
    # print(sup_fol)
    out_super = os.path.join(out_path,sup_fol)

    out_folder = os.path.join(out_super,child_folder)
    cur_path = path+"/"+fol
    cur_dir = os.listdir(cur_path)
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    os.mkdir(out_folder)
    # print(cur_dir)
    # print(cur_path," ",len([entry for entry in os.listdir(cur_path) if os.path.isfile(os.path.join(cur_path, entry))]))
    # count = len([entry for entry in os.listdir(cur_path) if os.path.isfile(os.path.join(cur_path, entry))])
    
    count = 9
    for item in reversed(cur_dir):
        # print(item)
        original = os.path.join(cur_path,item)
        target = os.path.join(out_folder,item)
        # print(original,"  ",target)
        shutil.copyfile(original, target)
        if count==0:
            break
        count-=1