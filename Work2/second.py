import cv2
import numpy
from ctypes import windll as win

__IMAGE_PATH__ = "./images/2-2.jpg"
__RESOLUTION__ = (win.user32.GetSystemMetrics(0), win.user32.GetSystemMetrics(1))

def show(image, name, size=300, delay=0, closewindow=False):
    img_height, img_width = image.shape[:2]
    
    image = cv2.resize(
        src = image, 
        dsize = (img_width//__RESOLUTION__[0]*size, img_height//__RESOLUTION__[1]*size)
    )

    cv2.imshow(name, image)
    cv2.waitKey(delay)

    if closewindow:
        cv2.destroyAllWindows()

def main():
    image = cv2.imread(__IMAGE_PATH__)
    blurimage = cv2.medianBlur(
        src=image,
        ksize=33
    )
    
    show(blurimage, "blured")

    # edges = cv2.Canny(
    #     image=blurimage, 
    #     threshold1=50,
    #     threshold2=90,
    #     L2gradient=False
    # )

    edges = cv2.Laplacian(
        src=blurimage,
        ddepth=1,
        ksize=5
    )

    show(edges, "edges")

main() 
