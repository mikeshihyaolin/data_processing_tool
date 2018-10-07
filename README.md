# Data Processing Tools

+ Convert images to video
+ Convert video to images

**Code Author: Shih-Yao (Mike) Lin**


## Platform
+ Ubuntu 

## Dependencies
+ OpenCV 

## Installation

* Clone this repo

```bash
git clone https://github.com/mikeshihyaolin/data_processing_tool.git
```

## Quick Start
+ Convert images to videos
```
python img2video.py --input_img_path [image_path] --output_video_path [video_path]
```
for example:
```
python img2video.py --input_img_path /example/images/ --output_video_path /example/output_video.mp4
```


+ Convert video to images
```
python video2img.py --input_video_path [video_path] --output_img_path [image_path]  
```
for example:
```
python video2img.py --input_video_path /example/input_video.mp4 --output_img_path /images/ 
```