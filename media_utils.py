import os
import cv2
from ocr_utils import boxing
from yolo_model import detecting


def process_image(img_path, model, classes, output_dir):
    img_out_name = os.path.join(output_dir, f"result_{os.path.basename(img_path)}")
    frame = cv2.imread(img_path)

    if frame is None:
        print(f"Failed to read image: {img_path}")
        return

    print(f"Processing image: {img_path}")
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detecting(frame, model)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame = boxing(results, frame, classes)
    cv2.imwrite(img_out_name, frame)
    print(f"Image saved: {img_out_name}")



def process_video(video_path, model, classes, output_dir):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out_path = os.path.join(output_dir, f"result_{os.path.basename(video_path)}")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    print(f"Processing video: {video_path}")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detections = detecting(rgb_frame, model)
        boxed_frame = boxing(detections, frame, classes)
        out.write(boxed_frame)
        cv2.imshow("ANPR - Press Q to quit", boxed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved: {out_path}")