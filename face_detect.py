import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('pictures/face1.jpg')
template = cv.imread('pictures/face2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray1 = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Format', togray)
#cv.imshow('',img)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rectangle = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
faces1_rectangle = haar_cascade.detectMultiScale(gray1,scaleFactor=1.1,minNeighbors=3)

print(f"Image:No of faces found: {len(faces_rectangle)}")
print(f"Template:No of faces found: {len(faces1_rectangle)}")

for (x,y,w,h) in faces_rectangle:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.rectangle(template, (x,y), (x+w,y+h), (0,255,0), thickness=2)



result = (img == template)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title(result), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title(result), plt.xticks([]), plt.yticks([])
#plt.suptitle(meth)
plt.show()

cv.waitKey(0)