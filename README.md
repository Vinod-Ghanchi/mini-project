# mini-project

Problem Definition: To make a virtual application menu that opens different apps based on the location and configuration of our fingers. The menu must open different apps when we point at different places in the webcam with our index finger and middle finger raised. 

On running the code, the webcam output will be shown through a new window.

On detection of hands, the hand landmarks are continuously highlighted on the window

On raising of the middle and index fingers, boxes are made on the tip of the fingers to indicate Selection mode

When user guides hands to different parts of the window, different apps are opened

Made on Pycharm, using external modules such as OpenCV, keras, numpy, and mediapipe. Run with the help of a webcam

The final result is a window that gets opened after running the code. The window shows a continuous output of the webcam. In the window itself there are indicators to show the places where the hands need to be pointed to open a specific app. This is the virtual menu. When the required two hands are raised. A box is made on the fingertips to show that the program is now in ‘Selection Mode’. This is to avoid accidental opening of apps.
