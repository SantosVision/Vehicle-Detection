import cv2
import numpy as np
'''
Vehicle VehicleDetection

By Anell Santos
'''

cars_cascade = cv2.CascadeClassifier('C:FILE PATH HERE/car.xml')


def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
        if np.array(frame.all()) == frame.all():
            print('Vehicle')

        font = cv2.FONT_HERSHEY_SIMPLEX
        name = 'Vehicle'
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
    return frame


def Simulator():
    CarVideo = cv2.VideoCapture('Your vehicle mp4 video file path HERE')
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        controlkey = cv2.waitKey(1)
        if ret:
            cars_frame = detect_cars(frame)
            cv2.imshow('frame', cars_frame)
        else:
            break
        if controlkey == ord('q'):
            break

    CarVideo.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Simulator()
