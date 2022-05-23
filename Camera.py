# program to capture single image from webcam in python

# importing OpenCV library
import time

import cv2
import os
# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
def CameraInput(date,room,number):
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    # Directory
    directory = str(date)
    urls_path = []
    # Parent Directory path
    parent_dir = os.getcwd();
    sub_dir = parent_dir+"\\"+directory
    # Path
    try:
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
    except:
        print("Okey")
    try:
        path = os.path.join(sub_dir, str(room))
        os.mkdir(path)
    except:
        print("Okey")
    # reading the input using the camera
    i=0
    while i<number:
        result, image = cam.read()
        i=i+1
    # If image will detected without any error,
    # show result
        if result:
            url_path = str(parent_dir)+"\\"+str(date)+"\\"+str(room)+"\\"+str(i)+".png";
            print(url_path)
            cv2.imwrite(url_path, image)
            urls_path.append(str(url_path));
        else:
            print("No image detected at index "+str(i)+". Please! try again")

        time.sleep(0.5)
    return urls_path;