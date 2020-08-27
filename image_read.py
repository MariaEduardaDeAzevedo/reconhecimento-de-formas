import cv2 as cv

#Importação de imagem

image = cv.imread('assets/castle.jpg') #RGB
cv.imshow('Image', image)
cv.waitKey(0)


#Importação de vídeos

video = cv.VideoCapture('assets/video_1.mp4')

while True:
    success, frame = video.read()

    if success:
        height, width = frame.shape[:2]
        frame = cv.resize(frame, (width - (width*80//100), height - (height*80//100)))
        cv.imshow('Video', frame)
    else:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


#Capturando com a Web Cam

capture = cv.VideoCapture(0)

while True:
    success, frame = capture.read()

    if success:
        height, width = frame.shape[:2]
        cv.imshow('Cam', frame)
    else:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
