# Basic data processing scripts 

+ Convert a video to images
+ Convert a video to a gif file
+ Convert images to a video
+ Convert and concatenate multimple input images to a video
+ Flip images

**Code Author: Shih-Yao (Mike) Lin**

## Dependencies
+ python3.6
+ glob2==0.6
+ moviepy==0.2.3.5
+ opencv-python==3.4.4.19

## Installation

* Clone this repo

```bash
git clone https://github.com/mikeshihyaolin/data_processing_tool.git
```
The directory tree should look like this:
```
${ROOT}
├── README.md
├── flip_imgs.py
├── img2video.py
├── img2video_concat.py
├── requirements.txt
├── video2gif.py
├── video2img.py
└── videos2concated_video.py
```

* Install dependencies
```
pip3 install -r ./requirements.txt
```

## Quick Start
+ Convert a video to images
```
python video2img.py -i [video_path] -o [image_path]  
```
+ Convert a video to a gif file
```
python video2gif.py -i [video_path] -o [gif_path] -s [ratio]   
```
+ Convert images to a video
```
python img2video.py -i [image_path] -o [video_path]
```
+ Convert and concatenate multimple input images to a video
```
python img2video_concat.py -i "[image_path1] [image_path 2] ... [image_path N]" -o [video_path]
```


