# robotics_lab_mini_project
KMITL Robotics Laboratory 3 Mini Project - Face Mask Detection

Note:
The images folder is the dataset that's been selected from this original dataset https://www.kaggle.com/datasets/andrewmvd/face-mask-detection

Steps Taken For This Project:
1. Upload all images in dataset to Roboflow
2. Annotate imaage by drawing bounding boxes around people wearing face masks for the all dataset
3. Split data to 80% train, 20% valid, and 0% test which equates to 45 images in the training set, 11 images in the validation set, and 1 image for the testing set
4. Preprocessing set to Auto-Orient and Resize by stretching to 640 pixels by 640 pixels
5. Augmentation set to flip horizontally
6. Generate augmentation 2 times
7. Export dataset to YOLOv8 format by exporting as import link and copy that text to paste in code
8. Run Robotics_Lab_Mini_Project.ipynb where the copied dataset should be paste in there
9. Run and train model till the model is accurate
10. Download best.pt file that is the best model trained
11. Download Raspberry Pi image file and flash it to SD Card
12. Setup Raspberry Pi to boot and pip install ultralytics and pip install opencv-python
13. Download Raspberry_Pi_YOLOv8_Model_Camera_Implemenation.py and best.pt and store them in the same folder
14. Launch Raspberry_Pi_YOLOv8_Model_Camera_Implementation.py and detect whether people are wearing face masks or not

Enjoy
Let me knoww if there are any issues
