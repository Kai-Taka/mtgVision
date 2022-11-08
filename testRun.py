import cv2
import os
from vision.BasicCardDetector import BasicCardDetector

bcd = BasicCardDetector()

for card in os.listdir("test"):
    currentImg = cv2.imread(f"test/{card}")
    print(f"Checking card {card.split('.')[0]}")
    cv2.imshow(card, currentImg)
    cv2.waitKey(0)

#print(bcd.getCardName())