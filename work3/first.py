import cv2
import numpy
from ctypes import windll as win
import math

__IMAGE_PATH__ = "./images/3-1.jpg"
__RESOLUTION__ = (win.user32.GetSystemMetrics(0), win.user32.GetSystemMetrics(1))

def show(image, name, size=100, delay=0, closewindow=False):
    img_height, img_width = image.shape[:2]
    
    # image = cv2.resize(
    #     src = image, 
    #     dsize = (img_width//__RESOLUTION__[0]*size, img_height//__RESOLUTION__[1]*size)
    # )

    cv2.imshow(name, image)
    cv2.waitKey(delay)

    if closewindow:
        cv2.destroyAllWindows()


def main():
    image = cv2.imread(__IMAGE_PATH__, cv2.COLOR_RGB2GRAY)
    show(image, "image")
    lines = cv2.HoughLinesP(
        image = image,
        rho=1,
        theta=math.pi/180,
        threshold=1
    )

    for line in lines:
        line = line[0]
        print(line)
        image = cv2.line(image, line[0], line[1], (0,0,255))

    show(image, "lines")
    
main()