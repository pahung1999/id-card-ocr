import cv2
import numpy as np
import sys
from pyzbar.pyzbar import decode

def crop_qr(image):
    h ,w,c= image.shape
    x_topleft= w*8//10
    y_topleft=0
    qr_size= h*3//10
    image=image[y_topleft:y_topleft+qr_size,x_topleft:x_topleft+qr_size]
    return image
def sharpen_img(image):
    image=cv2.resize(image,(700,700))
    # kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    # image=cv2.filter2D(image, -1, kernel)
    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # image=cv2.filter2D(image, -1, kernel)
    kernel = np.array([[-1,-1,-1,-1,-1],
                               [-1,2,2,2,-1],
                               [-1,2,8,2,-1],
                               [-2,2,2,2,-1],
                               [-1,-1,-1,-1,-1]])/8.0
    image=cv2.filter2D(image, -1, kernel)
    return image

def decode_qr(img):
    img=sharpen_img(img)
    img=cv2.resize(img,(200,200))

    cv2.imshow('', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Decode QR
    texts = decode(img)
    for text in texts:
        tt = text.data.decode("utf-8")
        return tt