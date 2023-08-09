# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:24:52 2022

@author: Asus
"""

import os

no_of_videos_counter = 1
no_of_videos = 29

folder = "C:/Zephyrrus/zDesktop/thesis/dataset/valo-F30-L10/"
file_counter = 0
folder_counter = 0

action_folder = os.listdir(folder)

for each_video_folder in action_folder :
    file_counter = 0
    for filename in os.listdir( f'{folder}{each_video_folder}' ):
        # print(count)
        # print(filename)

        dst = f"{str(file_counter)}.npy"
        src =f"{folder}{each_video_folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}{each_video_folder}/{dst}"

        # print(src)
        # print(dst)
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        file_counter = file_counter + 1 


    print(f'folder {each_video_folder} done')
    
    folder_counter = folder_counter + 1 

print('all done')