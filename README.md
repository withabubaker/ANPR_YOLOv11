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

Install the libraries and dependencies in requirements.txt

```python
pip3 install -r requirements.txt

```

Run the model

```python
python deploy.py <folder_path | image_path | video_path>
```
Example: 
if you want to run the model against all the images in the images folder
python deploy.py D:/ANPR/images
