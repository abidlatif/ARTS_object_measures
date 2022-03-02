def stackImages(scale,The_Array_Image):
    The_Rows = len(The_Array_Image)
    The_Coloumn = len(The_Array_Image[0])
    Avaliable_Rows = isinstance(The_Array_Image[0], list)
    The_Width = The_Array_Image[0][0].shape[1]
    The_Height = The_Array_Image[0][0].shape[0]
    if Avaliable_Rows:
        for i in range ( 0, The_Rows):
            for j in range(0, The_Coloumn):
                if The_Array_Image[i][j].shape[:2] == The_Array_Image[0][0].shape [:2]:
                    The_Array_Image[i][j] = cv2.resize(The_Array_Image[i][j], (0, 0), None, scale, scale)
                else:
                    The_Array_Image[i][j] = cv2.resize(The_Array_Image[i][j], (The_Array_Image[0][0].shape[1], The_Array_Image[0][0].shape[0]), None, scale, scale)
                if len(The_Array_Image[i][j].shape) == 2: The_Array_Image[i][j]= cv2.cvtColor( The_Array_Image[i][j], cv2.COLOR_GRAY2BGR)
        The_Blank_Image = TheNumpy.zeros((The_Height, The_Width, 3), TheNumpy.uint8)
        Horizantal = [The_Blank_Image]*The_Rows
        Horizantal_Contor = [The_Blank_Image]*The_Rows
        for x in range(0, The_Rows):
            Horizantal[i] = TheNumpy.hstack(The_Array_Image[i])
        Vertical = TheNumpy.vstack(Horizantal)
    else:
        for i in range(0, The_Rows):
            if The_Array_Image[i].shape[:2] == The_Array_Image[0].shape[:2]:
                The_Array_Image[i] = cv2.resize(The_Array_Image[i], (0, 0), None, scale, scale)
            else:
                The_Array_Image[i] = cv2.resize(The_Array_Image[i], (The_Array_Image[0].shape[1], The_Array_Image[0].shape[0]), None,scale, scale)
            if len(The_Array_Image[i].shape) == 2: The_Array_Image[i] = cv2.cvtColor(The_Array_Image[i], cv2.COLOR_GRAY2BGR)
        Horizantal= TheNumpy.hstack(The_Array_Image)
        Vertical = Horizantal
    return Vertical