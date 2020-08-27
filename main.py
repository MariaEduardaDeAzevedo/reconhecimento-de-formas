import cv2 as cv
import functions

video1 = cv.VideoCapture('assets/video_1.mp4')
video2 = cv.VideoCapture('assets/video_2.mp4')
video3 = cv.VideoCapture('assets/video_3.mp4')
video4 = cv.VideoCapture('assets/video_4.mp4')

while True:
    success1, frame1 = video1.read()
    success2, frame2 = video2.read()
    success3, frame3 = video3.read()
    success4, frame4 = video4.read()

    if success1 and success2 and success3 and success4:
        height1, width1 = frame1.shape[:2]
        height2, width2 = frame2.shape[:2]
        height3, width3 = frame3.shape[:2]
        height4, width4 = frame4.shape[:2]

        frame1 = cv.resize(frame1, (width1 - (width1*85//100), height1 - (height1*85//100)))
        frame_copy1 = frame1.copy()
        frame2 = cv.resize(frame2, (width2 - (width2*85//100), height2 - (height2*85//100)))
        frame_copy2 = frame2.copy()
        frame3 = cv.resize(frame3, (width3 - (width3*85//100), height3 - (height3*85//100)))
        frame_copy3 = frame3.copy()
        frame4 = cv.resize(frame4, (width4 - (width4*85//100), height4 - (height4*85//100)))
        frame_copy4 = frame4.copy()

        #Pré-processamento com gradientes
        gray_image1 = functions.to_grayscale(frame1)
        blur_image1 = functions.to_blur(gray_image1)
        canny_image1 = functions.to_canny(blur_image1)
        
        gray_image2 = functions.to_grayscale(frame2)
        blur_image2 = functions.to_blur(gray_image2)
        canny_image2 = functions.to_canny(blur_image2)

        gray_image3 = functions.to_grayscale(frame3)
        blur_image3 = functions.to_blur(gray_image3)
        canny_image3 = functions.to_canny(blur_image3)

        gray_image4 = functions.to_grayscale(frame4)
        blur_image4 = functions.to_blur(gray_image4)
        canny_image4 = functions.to_canny(blur_image4)

        contour1 = functions.get_contours(canny_image1)
        functions.draw_contour(frame_copy1, contour1)
        cv.imshow('Video 1', frame_copy1)

        contour2 = functions.get_contours(canny_image2)
        functions.draw_contour(frame_copy2, contour2)
        cv.imshow('Video 2', frame_copy2)

        contour3 = functions.get_contours(canny_image3)
        functions.draw_contour(frame_copy3, contour3)
        cv.imshow('Video 3', frame_copy3)

        contour4 = functions.get_contours(canny_image4)
        functions.draw_contour(frame_copy4, contour4)
        cv.imshow('Video 4', frame_copy4)
    else:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
