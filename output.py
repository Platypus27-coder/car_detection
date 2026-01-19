from ultralytics import YOLO

model = YOLO("runs/detect/train10/weights/best.pt")

model.predict(
    source="yolov10/yolo_data/val/images",
    save=True,
    conf=0.25
)
