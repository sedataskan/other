import os
import sys
import cv2
from PIL import Image

chars = ["•", "@", "%", "+", ";", "☻", "♥", "*", "-", "~", "&"]


def resizeImage(image, newWidth=70):
    width, height = image.size
    aspectRatio = height / width
    newHeight = int(aspectRatio * newWidth)

    resizeimage = image.resize((newWidth, newHeight)).convert('L')

    return resizeimage


def pxToChars(image):
    pixel = image.getdata()
    character = "".join([chars[pix // 25] for pix in pixel])
    return character


def generateFrame(image, newWidth=70):
    newImageData = pxToChars(resizeImage(image))
    countPixels = len(newImageData)

    asciiImage = "\n".join([newImageData[index:(index + newWidth)] for index in range(0, countPixels, newWidth)])

    sys.stdout.write(asciiImage)
    os.system('cls' if os.name == 'nt' else 'clear')


cap = cv2.VideoCapture("resources/video.mp4")

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    generateFrame(Image.fromarray(frame))
    cv2.waitKey(2)
