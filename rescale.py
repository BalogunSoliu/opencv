from turtle import width
import cv2 as cv
from cv2 import resize
#resizing video or px frames
img = cv.imread('pictures/face1.jpg')
dimensions = img.shape
 
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

class sizing:
    def __init__(self,frame,scale):
        self.frame = frame
        self.scale = scale
    
    def resizing(self):
        width = int(self.frame.shape[1] * self.scale)
        height = int(self.frame.shape[0] * self.scale)
        dimensions = (width,height)
        return cv.resize(self.frame, dimensions, interpolation=cv.INTER_AREA)
