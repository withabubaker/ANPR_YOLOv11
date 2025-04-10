import easyocr
import numpy as np
import cv2
import re

def easyocr_load():
    return easyocr.Reader(['en'])

def easyocr_reading(img, coords, reader):
    xmin, ymin, xmax, ymax = coords
    nplate = img[int(ymin):int(ymax), int(xmin):int(xmax)]
    ocr_results = reader.readtext(nplate)

    #remove unwanted characters
    cleaned_results = []
    for bbox, text, conf in ocr_results:
        # Keep only letters and numbers and keep space between them
        cleaned_text = re.sub(r'[^A-Za-z0-9]', ' ', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        if cleaned_text:
            cleaned_results.append((bbox, cleaned_text, conf))
    return cleaned_results, nplate

def filtering(region, ocr, region_threshold):
    rectangle_size = region.shape[0] * region.shape[1]
    plate = []
    for result in ocr:
        length = np.sum(np.subtract(result[0][1], result[0][0]))
        height = np.sum(np.subtract(result[0][2], result[0][1]))
        if length * height / rectangle_size > region_threshold:
            plate.append(result[1])
    for ch in ['[', ']', '\'', '-', '#', '*']:
        plate = str(plate).replace(ch, '')
    return plate

def boxing(detections, frame, classes):
    reader = easyocr_load()
    for label, coords in detections:
        x1, y1, x2, y2 = map(int, coords)
        print(f"Extracting plate box...")
        ocr, nplate = easyocr_reading(img=frame, coords=[x1, y1, x2, y2], reader=reader)
        print("OCR results:", ocr)
        plate_num = filtering(nplate, ocr, region_threshold=0.40)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(frame, (x1, y1-100), (x2, y1), (0, 255, 0), -1)
        cv2.putText(frame, f"{plate_num}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 0, 0), 4)
    return frame