import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

import webbrowser



brushThickness = 10
eraserThickness = 100

drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)


while True:
    success, img = cap.read()


    img = cv2.flip(img, 1)
    cv2.putText(img, 'Spotify', (800, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA, False)
    cv2.putText(img, 'Telegram', (550 ,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA, False)
    cv2.putText(img, 'Discord', (1050, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA, False)
    cv2.putText(img, 'Teams', (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA, False)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        print(len(lmList))

        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()
        # print(fingers)

        if fingers[1] and fingers[2]:
            print("Selection Mode")
            if y1 < 125:
                if 250 < x1 < 450:
                    os.startfile('"C:/Users/kushl/OneDrive/Desktop/Microsoft Teams (work or school).lnk"')
                    print("Opening Teams...")
                elif 550 < x1 < 750:
                    os.startfile('"C:/Users/kushl/OneDrive/Desktop/Telegram.lnk"')
                    print("Opening Telegram...")
                elif 800 < x1 < 950:
                     os.startfile('C:/Users/kushl/AppData/Roaming/Spotify/Spotify.exe')
                     print("Opening Spotify...")
                elif 1050 < x1 < 1200:
                    flag=0
                    if(flag==0):
                     os.startfile('"C:/Users/kushl/OneDrive/Desktop/Discord.lnk"')
                     print("Opening Discord...")
                     flag=1
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)






        # if fingers[1] and fingers[2] == False:
        #     cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
        #     print("Drawing Mode")
        #     if xp == 0 and yp == 0:
        #         xp, yp = x1, y1
        #
        #     cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
        #
        #     if drawColor == (0, 0, 0):
        #         cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
        #         cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
        #
        #     else:
        #         cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
        #         cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
        #
        #     xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    cv2.imshow("Image", img)
    if (cv2.waitKey(30) == ord('q')):
        file_name_path = 'C:/Users/kushl/PycharmProjects/MIniProject/' +  '.jpg'
        cv2.imwrite(file_name_path, imgInv)
        break
cap.release()

