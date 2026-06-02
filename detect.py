from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("detected.jpg", show=True)

print("Detection completed")
