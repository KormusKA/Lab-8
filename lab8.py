import numpy as np
import cv2
import time

def task1():
    path = "images/variant-8.jpg"
    img = cv2.imread(path)

    width, height = img.shape[:2]
    (cX, cY) = (width // 2, height // 2)    #нашли центр изображения
    (x_start, x_end) = cX-200, cX+200
    (y_start, y_end) = cY-200, cY+200

    img_cropped = img[x_start:x_end, y_start:y_end]
    cv2.selectROI(img_cropped)

    new_path = "variant-8-cropped.jpg"
    cv2.imwrite(new_path, img_cropped)

    print(f"Обрезанное изображение сохранено как {new_path}")

def task2():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    i = 0

    if not cap.isOpened():
        print("Не удалось открыть камеру")
        return

    print("Для выхода нажмите клавишу 'q'")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Не удается получить кадр")
            break
        

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(c)
            cX = x + (w // 2)
            cY = y + (h // 2)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (cX, cY), 3, (255, 0, 0), -1)
            
            if i % 5 == 0:
                print(f'Центр: {cX}, {cY}')

        cv2.imshow('task2', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()
    cv2.destroyAllWindows()

def task3():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    i = 0

    if not cap.isOpened():
        print("Не удалось открыть камеру")
        return

    print("Для выхода нажмите клавишу 'q'")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Не удается получить кадр")
            break
        

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(c)
            cX = x + (w // 2)
            cY = y + (h // 2)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            height, width = frame.shape[:2]

            cv2.line(frame, (0, cY), (width, cY), (0, 0, 255), 1)
            cv2.line(frame, (cX, 0), (cX, height), (0, 0, 255), 1)
            
            if i % 5 == 0:
                print(f'Центр: {cX}, {cY}')

        cv2.imshow('task2', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #task1()
    #task2()
    task3()