"""
Часть 1
С помощью средств библиотек OpenCV и NumPy создайте изображение шахматной доски шириной в 4 клетки и длиной в 6 клеток. 
Пусть верхний левый квадрат будет синим, а его сосед справа - белым. Сохраните его на компьютере, а затем выводите  
изображение на экран следующим образом:

в цвете в полном размере на 5 секунд, затем закрыть;
в оттенках серого в полном размере на 7 секунд, затем закрыть;
в цвете в 2 раза меньше, чем исходный размер, на 9 секунд, затем закрыть;
в оттенках серого в 4 раза меньше, чем исходный размер, на 11 секунд, затем закрыть.
"""

import cv2
import numpy
__WIDTH__ = 480
__HEIGHT__ = 720
color_types = {
    "RGB"         : 0,
    "GrayScale"   : cv2.COLOR_BGR2GRAY
}


def showimage(image, name, code, scale=1, delay=0): # обработка и вывод изображения
    new_size = (int(__WIDTH__ * scale),int(__HEIGHT__ * scale))
    image = cv2.resize(image, new_size)
    if code != 0:
        image = cv2.cvtColor(image, code=code)
    cv2.imshow(name, image)
    cv2.waitKey(delay*1000)
    cv2.destroyAllWindows()


def draw(width, height): # создание изображения
    colors = [(255, 0, 0), (255, 255, 255)]
    blank = numpy.zeros((width, height, 3), numpy.uint8)
    counter = 0
    for py in range(0, height, height//4):
        for px in range(0, width, width//6):
                
            blank = cv2.rectangle(
                img = blank,
                pt1 = (py, px), 
                pt2 = (py+height//4, px+width//6),
                thickness = -1,
                color = colors[counter%2],                    
            )
            counter += 1
        counter += 1
    return blank

def main():
    img = draw(__WIDTH__, __HEIGHT__)
    showimage(img, "Option1", code=color_types["RGB"], delay=5)
    showimage(img, "Option2", code=color_types["GrayScale"], delay=7)
    showimage(img, "Option3", scale=0.5, code=color_types["RGB"], delay=9)
    showimage(img, "Option4", scale=0.25, code=color_types["GrayScale"], delay=11)

main()
