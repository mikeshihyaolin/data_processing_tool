# Basic data processing scripts

+ Convert images to video
+ Convert video to images

**Code Author: Shih-Yao (Mike) Lin**


## Platform
+ Ubuntu 

## Dependencies
+ OpenCV
+ ffmpeg

## Installation

* Clone this repo

```bash
git clone https://github.com/mikeshihyaolin/data_processing_tool.git
```

## Quick Start
+ Convert images to videos
```
python img2video.py -i [image_path] -o [video_path]
```
for example:
```
python img2video.py -i /example/images/ -o /example/output_video.mp4
```
<br/><br/>

+ Convert video to images
```
python video2img.py -i [video_path] -o [image_path]  
```
for example:
```
python video2img.py -i /example/input_video.mp4 -o /images/ 
```
