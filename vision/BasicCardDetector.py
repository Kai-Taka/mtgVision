import cv2

import numpy as np

import pytesseract as pt

# imageO = cv2.imread("C:\\Users\\imper\\OneDrive\\Documentos\\tpr-4-armor-sliver.jpg", 1)

# image = cv2.cvtColor(imageO, cv2.COLOR_BGR2GRAY)

# ret, thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
# thresh = cv2.dilate(thresh, kernel, iterations = 1)
# thresh = cv2.erode(thresh, kernel, iterations = 1)
# cv2.imshow("test", thresh)
# cv2.waitKey(0)

# cont, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for i in range(len(cont)):
# 	img = np.copy(imageO)
# 	c= cont[i]
# 	h = hierarchy[0][i]
# 	if h[2] == -1:
# 		continue
# 	if cv2.contourArea(c)/(image.shape[0]*image.shape[1]) < 0.04:
# 		continue

# 	x,y,w,h = cv2.boundingRect(c)

# 	img = img[y:y+h, x:x+w]

# 	print(i)
# 	print(pt.image_to_string(img, config = r"--oem 3 --psm 6"))
# 	cv2.imshow("test", img)
# 	cv2.waitKey(0)


class BasicCardDetector:
    def __init__(self):
        self.kenel = np.ones((2,2), np.uint8)
        
    def preProcess(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img,150, 255, cv2.THRESH_BINARY_INV)
        thresh = cv2.dilate(thresh, self.kernel, iterations = 1)
        thresh = cv2.erode(thresh, self.kenel, iterations = 1)
        return thresh
    
    def getCardName(self, img):
        cont, hierarchy = cv2.findContours(preProcess(np.copy(img)), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for i in range(len(cont)):
            c = cont[i]
            h = hierarchy[0][i]
            #No children (open shape)
            if h[2] == -1:
                continue
            
            
        