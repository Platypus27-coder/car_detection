from ultralytics import YOLO
model = YOLO("runs/detect/train10/weights/best.pt")
# Nếu test cả một thư mục ảnh test_images
# model.predict(
#     source="test_images",
#     save=True,
#     conf=0.25
# )
## Nếu test một ảnh
model.predict(
    source="yolov10/test_imgaes/854745-hd_1280_720_50fps.mp4",
    save=True,
    conf=0.25
)

