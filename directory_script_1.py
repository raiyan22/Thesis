# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:10:04 2022

@author: Asus
"""

import os

folder = "F:/captures/4th year thesis/datasets/Sign language/training/valo/0"

for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(count)}"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
        
        # print(dst)
        # print(src)
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)