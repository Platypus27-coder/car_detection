from ultralytics import YOLO

model = YOLO("yolov10n.pt")

model.train(
    data="yolov10/yolo_data/data.yml",
    epochs=20,
    batch=4,
    device="cpu"
)
