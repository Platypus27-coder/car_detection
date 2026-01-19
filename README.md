## License

This project is based on the YOLOv10 repository by Ultralytics.

YOLOv10 is licensed under the **AGPL-3.0 License**.

All modifications and derived works in this repository therefore
also comply with the AGPL-3.0 license.

# Car Detection using YOLOv10

This project is a custom implementation based on the official YOLOv10 repository.
The goal is to train and evaluate a car detection model on a custom dataset.

Original YOLOv10 repository:
https://github.com/THU-MIG/yolov10

# 🚗 YOLOv10 Car Detection Project

Dự án này sử dụng **YOLOv10 (Ultralytics)** để huấn luyện và kiểm thử mô hình **phát hiện xe (car detection)** trên ảnh và video.

---

## 📌 1. Giới thiệu

* Framework: **Ultralytics YOLOv10**
* Ngôn ngữ: **Python**
* Môi trường: **Miniconda (conda env)**
* Bài toán: **Object Detection – 1 class (car)**

Dự án bao gồm:

* Train model với dataset tự chuẩn YOLO format
* Predict trên **ảnh / thư mục ảnh / video**
* Xuất kết quả bounding box

---

## 📂 2. Cấu trúc thư mục

```text
yolov10_test/
│
├── train.py                 # Script train model
├── output.py                # Script predict (ảnh / video)
│
├── yolov10/
│   └── yolo_data/
│       ├── train/
│       │   ├── images/
│       │   └── labels/
│       ├── val/
│       │   ├── images/
│       │   └── labels/
│       └── data.yml
│
├── runs/                     # YOLO tự sinh (weights, output)
├── datasets/                 # Ultralytics cache
└── README.md
```

---

## 🧱 3. Cài đặt Miniconda (BẮT BUỘC)

### 🔹 Bước 1: Tải Miniconda

* Truy cập: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
* Tải bản:

  * **Windows 64-bit**
  * Python **3.9 hoặc 3.10**

### 🔹 Bước 2: Cài đặt

* Double click file `.exe`
* Chọn:

  * ✔ Just Me
  * ✔ Add Miniconda to PATH (nếu có)
* Next → Install

### 🔹 Bước 3: Kiểm tra cài đặt

Mở **Anaconda Prompt** hoặc **PowerShell**:

```bash
conda --version
```

---

## 🧪 4. Tạo môi trường cho project

```bash
conda create -n object_detection python=3.10 -y
conda activate object_detection
```

---

## 📦 5. Cài đặt thư viện cần thiết

```bash
pip install --upgrade pip
pip install ultralytics opencv-python matplotlib
```

Kiểm tra:

```bash
yolo version
```

---

## 🗂 6. Chuẩn bị Dataset

### 🔹 Format YOLO

```
image.jpg
label.txt
```

`label.txt`:

```text
<class_id> <x_center> <y_center> <width> <height>
```

### 🔹 File `data.yml`

```yaml
path: yolov10/yolo_data
train: train/images
val: val/images

nc: 1
names:
  - car
```

⚠️ **Không dùng đường dẫn tuyệt đối**

---

## 🚀 7. Train model

Chạy trong thư mục gốc project:

```bash
python train.py
```

Ví dụ `train.py`:

```python
from ultralytics import YOLO

model = YOLO("yolov10n.pt")

model.train(
    data="yolov10/yolo_data/data.yml",
    epochs=50,
    imgsz=640,
    batch=8
)
```

📁 Model sau khi train nằm tại:

```
runs/detect/train*/weights/best.pt
```

---

## 🖼 8. Test trên ẢNH

```python
from ultralytics import YOLO

model = YOLO("runs/detect/train10/weights/best.pt")

model.predict(
    source="yolov10/yolo_data/val/images",
    save=True,
    conf=0.25
)
```

📁 Output:

```
runs/detect/predict/
```

---

## 🎥 9. Test trên VIDEO

```python
model.predict(
    source="test_videos/test.mp4",
    save=True,
    conf=0.25
)
```

### ❗ Video `.avi` không xem được?

👉 Dùng **VLC** hoặc convert:

```bash
ffmpeg -i output.avi output.mp4
```

---

## 🛠 10. Lỗi thường gặp

### ❌ `ModuleNotFoundError: ultralytics`

```bash
pip install ultralytics
```

### ❌ Dataset not found

* Kiểm tra `data.yml`
* Không dùng đường dẫn tuyệt đối

---

## 📌 11. Ghi chú

* Project được sử dụng dựa trên source của yolov10 !!!


---


