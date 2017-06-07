import numpy as np
import cv2
import copy
import urllib.request
import servo



def UpdateOrAddToList(x, y, shape, list):
    for l in list:
        l.x = x
        l.y = y
        return

    if (y > 300):
        return
    if (y < 100):
        return
    list.append(shape)
    NewShapeAddedEvent(shape)


def FilterFromImage(hsvFrame, brick, tab):
    mask = cv2.inRange(hsvFrame, brick.hsvl, brick.hsvu)
    mask = cv2.blur(mask, (40, 40))

    ret, thresholdImage = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)

    im, contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        del tab[:]

    for c in contours:
        m = cv2.moments(c)
        if cv2.contourArea(c) < 4000:
            continue
        if m[ 'm00' ] == 0:
            continue

        x = m[ 'm10' ] / m[ 'm00' ]
        y = m[ 'm01' ] / m[ 'm00' ]

        temp = Brick(brick.type)
        temp.x = x
        temp.y = y
        print("x: " +str(x) + " y: " +str(y))
        UpdateOrAddToList(x, y, temp, tab)


def NewShapeAddedEvent(shape):
    print(shape.type)
    urllib.request.urlopen("http://10.42.0.1:3000/bricks/new/" + shape.type).read()


def RemoveOldFromLists(l1, l2, l3):
    for l in l1:
        if l.y > 350:
            l1.remove(l)
            print(l.type + ' removed')
            deleted(l.type)

    for l in l2:
        if l.y > 350:
            l2.remove(l)
            print(l.type + ' removed')
            deleted(l.type)



    for l in l3:
        if l.y > 350:
            l3.remove(l)
            print(l.type + ' removed')
            deleted(l.type)

def deleted(type):
    if (type == 'yellow'):
        servo.update(80)
    else:
        servo.update(10)



class Brick:
    def __init__(self, type):
        self.type = type
        if type == 'yellow':
            self.hsvl = np.array([ 3, 213, 107 ])
            self.hsvu = np.array([ 23, 255, 226 ])
        elif type == 'red':
            self.hsvl = np.array([ 116, 180, 55 ])
            self.hsvu = np.array([ 180, 240, 145 ])
        else:
            self.hsvl = np.array([ 50, 222, 24 ])
            self.hsvu = np.array([ 128, 255, 130 ])

    def copy(self):
        return copy.copy(self)
