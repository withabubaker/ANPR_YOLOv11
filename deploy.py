import sys
import os
from helpers.yolo_model import load_model
from helpers.media_utils import process_image, process_video

def anpr(path):
    model, classes = load_model()
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)

    if os.path.isdir(path):
        image_files = [f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if not image_files:
            print("No images found in folder.")
            return
        
        for img_file in image_files:
            img_path = os.path.join(path, img_file)
            process_image(img_path, model, classes, output_dir)

    elif os.path.isfile(path):
        ext = os.path.splitext(path)[1].lower()

        if ext in ['.jpg', '.jpeg', '.png']:
            process_image(path, model, classes, output_dir)

        elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
            process_video(path, model, classes, output_dir)
        else:
            print(f"Unsupported file type: {ext}")
    else:
        print(f"Invalid path. Please provide a valid folder, image, or video file.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        anpr(path)
    else:
        print("Usage: python deploy.py <folder_path | image_path | video_path>")