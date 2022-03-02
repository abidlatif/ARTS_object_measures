def getContours(The_Image,The_Image_Contours):
    The_Contours, The_Hierarchy = cv2.findContours(The_Image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in The_Contours:
        Contour_Area = cv2.contourArea(cont)     # to get the Contour_Area passing contour Contour_Area
        Minimum Area = cv2.getTrackbarPos("The_Area", "Arguments")  # Setting the Contour_Area according to the trackbbar
        if Contour_Area > Minimum Area:                 #getting and printing text Contour_Area values according to the trackbar values 
            cv2.drawContours(The_Image_Contours, cont, -1, (255, 0, 255), 7)
            perimeter = cv2.arcLength(cont, True)
            Approximately = cv2.approxPolyDP(cont, 0.02 * perimeter, True)
            print(len(Approximately))
            i , j , k, l = cv2.boundingRect(Approximately) # passing the boundry values to the variables
            cv2.rectangle(The_Image_Contours, (i , j ), (i + k , j + l ), (0, 255, 0), 5) # colored rectangle 
                # writting text on the boundry lines of the images and cornor points on console
            cv2.putText(The_Image_Contours, "Points: " + str(len(Approximately)), (i + k + 20, j + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(The_Image_Contours, "The_Area: " + str(int(Contour_Area)), (i + k + 20, j + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0 , 255), 2)
