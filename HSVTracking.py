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


yellow = Brick('yellow')
red = Brick('red')
blue = Brick('blue')

yellowtab = []
redtab = []
bluetab = []

for fram in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    frame = fram.array

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    FilterFromImage(hsvFrame,yellow,yellowtab)
    FilterFromImage(hsvFrame,red,redtab)
    FilterFromImage(hsvFrame,blue,bluetab)

    RemoveOldFromLists(yellowtab,bluetab,redtab)

    rawCapture.truncate(0)
    key = cv2.waitKey(1)