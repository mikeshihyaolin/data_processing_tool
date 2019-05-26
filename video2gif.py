# -*-coding:utf-8-*-
# @file   video2gif.py
# @author Shih-Yao (Mike) Lin
# @email  shihyaolin@tencent.com
# @date   2019-05-23
# @brief  convert a video to a gif file
# @usage  python video2gif.py --input_video_path [video_path] --output_gif_path [gif_path] --size [ratio]   

from moviepy.editor import *
import argparse
import time

def video2gif(input_video_path, output_gif_path, time_start = None, time_end = None, size = None):

	if time_start == None and time_end == None:
		clip = (VideoFileClip(input_video_path)
			.resize(float(size)))
	else:
		clip = (VideoFileClip(input_video_path)
			.subclip((0,time_start),(0,time_end))
			.resize(float(size)))
	clip.write_gif(output_gif_path)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_video_path","-i", type=str)
    parser.add_argument("--output_gif_path", "-o", type=str, default="./output.gif")
    parser.add_argument("--start_time", "-ts", type=str, default=None)
    parser.add_argument("--end_time", "-te", type=str, default=None)
    parser.add_argument("--size", "-s", type=str, default=0.5)
    args = parser.parse_args()

    start = time.time()

    print("input path: "+args.input_video_path)
    print("output path: "+args.output_gif_path)
    print("size ratio: "+args.size)

    video2gif(args.input_video_path, args.output_gif_path, args.start_time, args.end_time, args.size)

    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, "seconds.")