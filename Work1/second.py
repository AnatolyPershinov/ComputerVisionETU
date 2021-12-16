"""Для выполнения этой части задания используйте камеру. Выведите на экран видео с камеры в оттенках серого. 
В правом нижнем углу кадра напишите дату выполнения задания. 
Программа должна завершаться по нажатию на клавишу q (на нажатия на другие клавиши программа реагировать не должна)."""
import cv2
import numpy 

def main():
    key = 0
    
    while True: 
        cap = cv2.VideoCapture("videoplayback.mp4") # чтобы захватить видео с камеры этой функции следует передать 0
        cap.set(3,720)
        cap.set(4,460)

        while True:
            ret, frame = cap.read()
            try:
                frame = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
                frame = cv2.putText(frame, "16.12.2021", (300,270), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            except Exception:
                cap.release()
                break
                
            cv2.imshow("Window", frame)
            key = cv2.waitKey(50)

            if key == 113 or key == 233: # 133 - q 233 - й 
                break

        if key == 113 or key == 233:
            break
    

main()
