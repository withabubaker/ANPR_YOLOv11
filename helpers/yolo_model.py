from ultralytics import YOLO

def load_model():
    print(f"Loading model... ")
    model = YOLO("best.pt")   
    classes = model.names
    return model, classes

def detecting(frame, model):
    results = model(frame)[0] # get the first result
    labels = results.boxes.cls.cpu().numpy() # label
    coordinates = results.boxes.xyxy.cpu().numpy() # bouning box
    confidences = results.boxes.conf.cpu().numpy() # confidence score

    detections = []
    for label, coord, conf in zip(labels, coordinates, confidences):
        if conf > 0.55: # confidence threshold
            detections.append((label, coord))
    return detections