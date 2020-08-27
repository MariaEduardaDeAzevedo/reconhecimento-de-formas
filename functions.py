import cv2 as cv
import json

def import_json(path):
    file = open(path, 'r')
    data = json.load(file)

    return data

def to_grayscale(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    return gray_image 

def to_blur(image):
    blur_image = cv.GaussianBlur(image, (5,5), 1)

    return blur_image

def to_canny(image):
    canny_image = cv.Canny(image, 50, 50)

    return canny_image

def get_contours(image):
    contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    return contours

def draw_contour(image, contours):
    data = import_json('files/forms.json')
    for contour in contours:
        cv.drawContours(image, contour, -1, (255,0,0), 1)
        perimeter = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.02*perimeter, True)
        connors = len(approx)
        area = cv.contourArea(contour)
        x1, y1, x2, y2 = cv.boundingRect(approx)
        if connors > 2 and area > 500:
            cv.rectangle(image, (x1, y1), (x1+x2, y1+y2), (0,255,0), thickness=2)
            form = "Forma identificada"

            if str(connors) in data.keys():
                form = data.get(str(connors))

            cv.putText(image, form, (x1+20, y1+10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
