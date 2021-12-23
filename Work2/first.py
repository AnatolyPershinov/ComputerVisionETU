import cv2
from ctypes import windll as win
import numpy

__IMAGE_PATH__ = "./images/2-1.jpg"
__RESOLUTION__ = (win.user32.GetSystemMetrics(0), win.user32.GetSystemMetrics(1))


def show(image, name, size=100, delay=0, closewindow=False):
    img_height, img_width = image.shape[:2]
    
    image = cv2.resize(
        src=image, 
        dsize= (img_width//__RESOLUTION__[0]*size, img_height//__RESOLUTION__[1]*size)
    )

    cv2.imshow(name, image)
    cv2.waitKey(delay)

    if closewindow:
        cv2.destroyAllWindows()


def main():
    image = cv2.imread(__IMAGE_PATH__)
    show(image, "original")

    blurimage = cv2.medianBlur(
        src=image,
        ksize=33
    )
    
    show(blurimage, "blured")

    buf = blurimage[:, :, 0].copy() 
    blurimage[:, :, 0] = blurimage[:, :, 2].copy()
    blurimage[:, :, 2] = buf

    show(blurimage, "replace chanels")


main()
    