# -*-coding:utf-8-*-
# @file   img_flip.py
# @author Shih-Yao (Mike) Lin
# @email  shihyaolin@tencent.com
# @date   2019-05-30
# @brief  flip all the images in a folder
# @usage  python3 flip_imgs.py --input_img_path [image_path] \
# 						--horizontal [1/0] --vertical [0/1] \
#						--output_flipped_img_folder [output_image_folder] 

import cv2
import pickle
import glob
import argparse
import numpy as np
import os, sys
from os import listdir, makedirs
import subprocess
import shutil
from os.path import isfile, isdir, join
import shutil
import time

def reset(reset_path):
    path = reset_path
    if os.path.isdir(path):
        shutil.rmtree(path)
        makedirs(path)
    else:
        makedirs(path)

def flip_imgs(input_img_path, output_folder, h_flip, v_flip):

	reset(output_folder)

	img_list = sorted(glob.glob(input_img_path+"/*"))

	if img_list == []:
		print("\n\n cannot find any imags in "+input_img_path+"\n\n")
	else:

		img = []
		for i,fi in enumerate(img_list):
			print(fi)
			img.append(cv2.imread(fi))

		for i, fi in enumerate(img):
			new_img = fi.copy()
			if h_flip == 1 and v_flip == 0:
				new_img = cv2.flip( fi, 1 )
			elif h_flip == 0  and v_flip == 1:
				new_img = cv2.flip( fi, 0 )
			elif h_flip == 1  and v_flip == 1:
				new_img = cv2.flip( fi,-1 )
			else:
				new_img = img
			
			cv2.imwrite(output_folder+"/flip_%05d.jpg"%i, new_img)

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_img_path", "-i", type=str)
	parser.add_argument("--output_flipped_img_folder", "-o", type=str)
	parser.add_argument("--horizontal", "-hf", type=str, default="1")
	parser.add_argument("--vertical", "-vf", type=str, default="0")

	args = parser.parse_args()

	print("args.horizontal_flip: "+str(args.horizontal))
	print("args.vertical_flip: "+str(args.vertical))

	start = time.time()

	flip_imgs(args.input_img_path, args.output_flipped_img_folder, int(args.horizontal), int(args.vertical))

	end = time.time()
	elapsed = end - start
	print ("Time taken: ", elapsed, "seconds.")
