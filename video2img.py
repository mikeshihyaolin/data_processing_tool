# -*-coding:utf-8-*-
# @file   video2img.py
# @author Shih-Yao (Mike) Lin
# @email  shihyaolin@tencent.com
# @date   2019-03-20
# @brief  generate video from multi-inputs images
# @usage  python video2img.py --input_video_path [video_path] --output_img_path [image_path]    

import subprocess
import os
import sys
from os import listdir, makedirs
import shutil
from os.path import isfile, isdir, join
import time
path_ffmpeg='ffmpeg' # for server used
import argparse

def reset(reset_path):
    path = reset_path
    if os.path.isdir(path):
        shutil.rmtree(path)
        makedirs(path)
    else:
        makedirs(path)

def convert_video_to_imgs(video_path, img_path):
    args = [path_ffmpeg, \
    '-i',video_path,'-qscale:v', '2',img_path+"/%05d.jpg" ]
    proc = subprocess.Popen(args)
    stdout, stderr = proc.communicate()
    print(img_path)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_video_path","-i", type=str)
    parser.add_argument("--output_img_path", "-o", type=str)
    args = parser.parse_args()

    start = time.time()

    print("input path: "+args.input_video_path)
    print("output path: "+args.output_img_path)
    reset(args.output_img_path)

    convert_video_to_imgs(args.input_video_path, args.output_img_path)

    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, "seconds.")
