# -*-coding:utf-8-*-
# @file   img2video_concat.py
# @author Shih-Yao (Mike) Lin
# @email  shihyaolin@tencent.com
# @date   2019-05-29
# @brief  generate a video by concatenating multi videos
# @usage  python3 videos2concated_video.py --input_video_path "[video_path 1] [video_path 2] ... [video_path N]" --output_video_path [concated_video_path]

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

def convert_multivideo_to_video(input_path, video_path, fps, start, end):

	path_list = []
	img_list = []
	video_path = video_path.replace(" ","")
	str_list = input_path.split(" ")

	new_h_list = []
	new_w_list = []

	nb_inputs = 0
	# # load images
	# # note: img_list[input_image_index][frame_index]
	for i, f in enumerate(str_list):	
		# load video
		vidcap = cv2.VideoCapture(f)
		success,image = vidcap.read()
		count = 0
		tmp_list = []
		while success and count >= start and count <= end:  
		  success,image = vidcap.read()
		  tmp_list.append(image)
		  count += 1
		nb_inputs = nb_inputs + 1
		img_list.append(tmp_list)
	# print("img_list: "+str(img_list))
	print("nb_inputs: "+str(nb_inputs))

	nb_frames = len(img_list[0])
	print("nb_frames: "+str(nb_frames))

	w_, h_, _ = img_list[0][0].shape

	# estimate the updated width and height of the the rest of input images
	w_tmp = 0
	for i in range(nb_inputs):
		w, h, _ = img_list[0][i].shape
		imgScale = h_ / h
		print(imgScale)
		new_h_list.append(h*imgScale)
		new_w_list.append(w*imgScale)
		w_tmp = w_tmp + int(w*imgScale)

	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	video = cv2.VideoWriter(video_path, fourcc, float(fps), (w_tmp,h_))

	# image resizing and video producing
	for j in range(nb_frames):
		print(j)
		img = []
		for i in range(nb_inputs):

			# print(int(new_w_list[i]))
			# print(int(new_h_list[i]))

			rows = int(new_w_list[i])
			cols = int(new_h_list[i])

			M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
			img_list[i][j] = cv2.warpAffine(img_list[i][j],M,(cols,rows))

			img_list[i][j]= cv2.resize(img_list[i][j],(int(new_w_list[i]),int(new_h_list[i])))

			# print(img_list[i][j].shape)
			# font = cv2.FONT_HERSHEY_SIMPLEX
			# if i == 0:
			# 	cv2.putText(img_list[i][j],'BD',(200, 600), font, 4,(255,0,0),10,cv2.LINE_AA)
			# else:
			# 	cv2.putText(img_list[i][j],'AD',(200, 600), font, 4,(255,0,0),10, cv2.LINE_AA)

			if i ==0:
				img = img_list[i][j]
			else:
				img = np.hstack((img, img_list[i][j]))
		video.write(img)
	video.release()


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_videos_path", "-i", type=str)
	parser.add_argument("--output_video_path", "-o", type=str)
	parser.add_argument("--start", "-s", type=str, default="0")
	parser.add_argument("--end", "-e", type=str, default="300")

	parser.add_argument("--frame_rate", "-fps", type=str, default="20.0")
	args = parser.parse_args()

	start = time.time()

	str_list = args.input_videos_path.split(" ")
	for i, f in enumerate(str_list):
		print("input path: "+f)
	print("output path: "+args.output_video_path)
	print("start: "+str(args.start)+" frame")
	print("end: "+str(args.end)+" frame")
	print("fps: "+args.frame_rate)

	convert_multivideo_to_video(args.input_videos_path, args.output_video_path, args.frame_rate, int(args.start), int(args.end))

	end = time.time()
	elapsed = end - start
	print ("Time taken: ", elapsed, "seconds.")
