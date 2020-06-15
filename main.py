from os import listdir
from os.path import isfile, join
# Imports PIL module
from PIL import Image
import cv2
from matplotlib import pyplot as plt
from sklearn import svm
import numpy as np

def retrieve_files():
    trainingPathLabel0 = "./Dataset/Training Set/label0/"
    trainingPathLabel1 = "./Dataset/Training Set/label1/"
    trainingPathLabel2 = "./Dataset/Training Set/label2/"

    entries = listdir(trainingPathLabel0)
    print(entries)

    #for file in entries:
        # open method used to open different extension image file 
        #img = cv2.imread(trainingPathLabel0 + file, 0)
    img = cv2.imread(trainingPathLabel2 + "lx11-n.jpg", 0)
    img = cv2.medianBlur(img, 5)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    y = np.zeros((len(th3), 1), dtype=int)
    # classifier = svm.SVC()
    # classifier.fit(th3, y)
    # print(th3)
    
    # plt.imshow(th3, 'gray')
    # plt.show()

# This method will show image in any image viewer  

if __name__ == "__main__":
    retrieve_files()
    pass