# -*-coding:utf-8-*-
# @file   img2video_concat.py
# @author Shih-Yao (Mike) Lin
# @email  mike.lin@ieee.org
# @date   2019-03-20
# @brief  generate a video from multi-inputs images
# @usage  python3 img2video_concat.py --input_img_path "[image_path 1] [image_path 2] ... [image_path N]" --output_video_path [video_path]

import cv2
import pickle
import glob
import argparse
import numpy as np
import os, sys
from os import listdir, makedirs
import shutil
import time
import matplotlib.pyplot as plt
# matplotlib.use("gtk")

def convert_img_to_video(input_path, video_path, fps):

	path_list = []
	img_list = []
	video_path = video_path.replace(" ","")
	str_list = input_path.split(" ")

	new_h_list = []
	new_w_list = []

	# load image path
	# note: path_list[frame_index][input_image_index_path]
	nb_inputs = 0
	for i, f in enumerate(str_list):
		path_list.append(sorted(glob.glob(f+"/*")))
		nb_inputs = nb_inputs + 1
	nb_frames = len(path_list[0])
	print(len(path_list[0]))
	print(len(path_list[1]))

	# load images
	# note: img_list[frame_index][input_image_index]
	for i in range(nb_frames):
		tmp_list = []
		for j in range(nb_inputs):
			print(path_list[j][i])
			tmp_list.append(cv2.imread(path_list[j][i]))
		img_list.append(tmp_list)

	# find the width and height of the first input image
	h_, w_, _ = img_list[0][0].shape

	# estimate the updated width and height of the the rest of input images
	w_tmp = 0
	for i in range(nb_inputs):
		h, w, _ = img_list[0][i].shape
		imgScale = h_ / h
		new_h_list.append(h*imgScale)
		new_w_list.append(w*imgScale)
		w_tmp = w_tmp + int(w*imgScale)


	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	video = cv2.VideoWriter(video_path, fourcc, float(fps), (w_tmp,h_))

	# image resizing and video producing
	for i in range(nb_frames):
		img = []
		for j in range(nb_inputs):
			img_list[i][j]= cv2.resize(img_list[i][j],(int(new_w_list[j]),int(h_)))
			if j ==0:
				img = img_list[i][j]
			else:
				img = np.hstack((img, img_list[i][j]))
		video.write(img)
	video.release()


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_img_path", "-i", type=str)
	parser.add_argument("--output_video_path", "-o", type=str)
	parser.add_argument("--frame_rate", "-fps", type=str, default="20.0")
	args = parser.parse_args()

	start = time.time()

	str_list = args.input_img_path.split(" ")
	for i, f in enumerate(str_list):
		print("input path: "+f)
	print("output path: "+args.output_video_path)
	print("fps: "+args.frame_rate)

	convert_img_to_video(args.input_img_path, args.output_video_path, args.frame_rate)

	end = time.time()
	elapsed = end - start
	print ("Time taken: ", elapsed, "seconds.")
