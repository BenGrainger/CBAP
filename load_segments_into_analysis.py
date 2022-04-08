import numpy as np
import subprocess
import os
import time
import math
import cv2

animal_clip_file = '#####'
folder = r'C:\Users\BMLab21\Documents\CrabStreams'
animal_clips_folder = os.path.join(folder, animal_clip_file)
contents = os.listdir(animal_clips_folder)
for file_name in contents:
    video = os.path.join(file_name, animal_clips_folder)
    cap = cv2.VideoCapture(video)
    arena_shape_path = '#####'
    arena_mask = np.dstack([arena_shape,arena_shape,arena_shape])
    while(True):
        ret, frame = cap.read()
        if ret == True:
            img = np.asarray(frame) * arena_mask
            analyzed = model.analyze(img) ##eventually this will feed the frame into my mask R CNN model like inception or YOLO
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
