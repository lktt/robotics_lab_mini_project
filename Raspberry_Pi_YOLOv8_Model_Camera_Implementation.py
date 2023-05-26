# Import Libraries
import cv2
from datetime import datetime
from ultralytics.yolo.engine.model import YOLO

# Import Our Model
model = YOLO('best.pt')

# Run Model While Activating Camera
results = model.predict(source = '0', show = True, conf = 0.5, save_conf = True, stream = True)

# Number Of Objects Detected
for r in results:
    print("Number of Detected Objects: ", len(r))