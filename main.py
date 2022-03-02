# Real Time Object Measuremetn system 
# Class project for Real Time Systems Course supervised by Prof Ing Methias Deegneer
# Structure of teh program will be as under
    # Importing required Libraries 
    # define the screen settings for output 
    # Getting the live feed using secondary camera as laptop primary camera will not be good to show objects in surface
    # Setting the trackbar to enter precise object threshold because its important to get clean images 
    # to get the contours we have to Gussianblur then Grayscale image, 
    # then this grayscaled Video is cannied to achieve cornors and then dilatedd  video and gets required results
    # Function to display the Live feed with results of teh objects as real time written with required calculation of measure 
# Hardcoded screen settings are being used to counter the challenge of different screen resolutions. 
# Results of the system are being presented in pixels like area size so to show precise area calcuations, further can be converted. 
# Single Camera is being used with predefined settings of still video feed by camera

#Importing libraries for live video graphcics and array
import cv2  
import numpy as TheNumpy  
import getContours  # User defined function imported to get the contours of the objects coming infront of the camera
import getStack
#Defined the Screen size to be used as canves 
TotalFrameWidth = 850    #screen dimension of with 800
TotalFrameHeight = 650   #screen dimension of The_Height 800

TheUrlOfDroidApp = 'http://10.135.248.27:4747' #IP: Address: URL for secondary camera

LiveCameraFeed = cv2.VideoCapture(TheUrlOfDroidApp)  #  cv2 parameters to get the live feed of camera

LiveCameraFeed.set(3, TotalFrameWidth)       # setting the frame The_Width parameters  
LiveCameraFeed.set(4, TotalFrameHeight)     # setting the The_Height parameters
#function to run until getting feed
def empty(a):
    pass
cv2.namedWindow("Arguments")       # Trackbar parameters to set the name of the window
cv2.resizeWindow("Arguments",640,240)  # Trackbar parameters to set the size of the trackbar window
cv2.createTrackbar("The_Threshold_1","Arguments",23,255,empty) # Trackbar parameters range
cv2.createTrackbar("The_Threshold_2","Arguments",20,255,empty)
cv2.createTrackbar("The_Area","Arguments",5000,30000,empty)
# Function to output Screen with required parameters 
stackImages(scale,The_Array_Image)
getContours(The_Image,The_Image_Contours)
# Function to get the The_Contours of the images getting using the live feed and then printing to teh user
while True: # this function is going to check if the screen is working and getting live feed
    The_Success, The_Image = LiveCameraFeed.read()
    The_Image_Contours = The_Image 
    Blurr_Image = cv2.GaussianBlur(The_Image, (8, 8), 1) # first we do the live feed blur
    Gray_Image = cv2.cvtColor(Blurr_Image, cv2.COLOR_BGR2GRAY) # then we convert it into RGB color
    Threshold_Num_1 = cv2.getTrackbarPos("The_Threshold_1", "Arguments")  # track bar options on the screen
    Threshold_Num_2 = cv2.getTrackbarPos("The_Threshold_2", "Arguments")
    Canny_image = cv2.Canny(Gray_Image,Threshold_Num_1,Threshold_Num_2) # in order to draw the corner points
    The_Kernel = TheNumpy.ones((5, 5))  
    Dilating_Image = cv2.dilate(Canny_image, The_Kernel, iterations=1) # dilating the canny image
    getContours(Dilating_Image,The_Image_Contours) # calling the function written above to get the contors
    The_Stack_Image = stackImages(0.8,([The_Image_Contours]))
    cv2.imshow("Result", The_Stack_Image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
