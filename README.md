# Automatic Number Plate Recognition (ANPR) using EasyOCR, OpenCV, and YOLOv11
This project presents a license plate detection and recognition pipeline, leveraging YOLOv11 for object detection, OpenCV for image processing, and optical character recognition (OCR) for text extraction.

## Table of Contents
- Project Goals
- Process
- Dataset
- Setup and Installation
- Results
- Challenges
- Future Goals

## Project Goals

Build a model to detect and recognize vehicle number plates, enabling seamless parking entrance and exit as an alternative to using an access card. Utilize YOLOv11 for object detection, OpenCV for image processing, and EasyOCR for text recognition.



![alt text](https://github.com/withabubaker/ANPR_Yolov11/blob/main/img/headimg.jpg)


## Process

1. Insert the image or video into YOLOv11 model for object detection to extract the number plate region.
2. Use EasyOCR to read the text, ignoring all non-alphanumeric characters.
3. Apply a filtering function to select text that covers at least 55% of the detected region, ignore anything else.
4. Save the result in the output folder.


## Dataset

I collected 70 number plate images from various vehicles (SUVs, Trucks, Sedans, etc.) on the street using a phone camera.
Out of these, 50 images were used for training and 20 for testing.


## Setup and Installation

Python environment => 3.12.1

1. Clone the repo:

```bash
git clone https://github.com/withabubaker/ANPR_Yolov11.git
```

2. Install the required libraries and dependencies:

```bash
pip install -r requirements.txt
```

3. Run the model:

```bash
python deploy.py <folder_path | image_path | video_path>
```
Example: 
To run the model on all images inside a folder

```bash
python deploy.py D:/ANPR/images
```


## Results

the model's mPA scores are as follows: 
. mAP50-95(B): 0.807
. mAP50(B): 0.995

Sample results

<a href="https://www.youtube.com/watch?v=10Vzn9jfCFE">
  <img src="https://img.youtube.com/vi/10Vzn9jfCFE/maxresdefault.jpg" alt="Watch the video" width="500"/>
</a>
<br>
<br>
Sometimes,  the model confuses the "W" with the "H", as shown in the image below:
<br>
<br>
<img src="https://github.com/withabubaker/ANPR_Yolov11/blob/main/img/falseResult.jpg" alt="False result" width="400"/>

