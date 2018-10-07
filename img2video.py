#########################################################################################
# python img2video.py --input_img_path [image_path] --output_video_path [video_path]    #
#########################################################################################

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

def convert_img_to_video(input_path_, video_path ):

	jpg_list = sorted(glob.glob(input_path_+"/*"))

	if jpg_list == []:
		print("\n\n cannot find any imags in "+input_path_+"\n\n")
	else:

		img = []
		for i,fi in enumerate(jpg_list):
			print(fi)
			img.append(cv2.imread(fi))

		height,width,layers=img[1].shape
		name = video_path+".mp4"
		# name = name.replace(" ","")
		# print(name)
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		video = cv2.VideoWriter(name, fourcc, 20.0, (width,height))

		for i, fi in enumerate(img):
			video.write(fi)
		video.release()


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_img_path", type=str)
	parser.add_argument("--output_video_path", type=str)
	args = parser.parse_args()

	start = time.time()

	print("input path: "+args.input_img_path)
	print("output path: "+args.output_video_path)

	convert_img_to_video(args.input_img_path, args.output_video_path)

	end = time.time()
	elapsed = end - start
	print ("Time taken: ", elapsed, "seconds.")
