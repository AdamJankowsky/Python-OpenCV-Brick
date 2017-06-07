import cv2
import numpy as np
from brick import *

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)


for fram in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    frame = fram.array

    cv2.imwrite('photo.jpg', frame)

    rawCapture.truncate(0)
    key = cv2.waitKey(10)
    break