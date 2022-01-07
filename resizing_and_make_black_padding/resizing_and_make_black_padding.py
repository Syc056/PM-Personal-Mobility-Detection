import cv2 


for i in range (937) : # 937 is my dataset's amount
    try:
        count = int(i)
        print("\n\n\nImage" + str(count+1) + ".png\n\n\n")
        imageNDArray = cv2.imread("C:/Users/user/Desktop/Dataset/Dataset/e-scooter_convert_to_PNG/Image" + str(count+1) +".png") # path
        imageHeight, imageWidth = imageNDArray.shape[:2]
        if imageWidth > imageHeight :               
            if imageWidth <=512 :
                convert = 512/imageWidth
            else :
                convert = imageWidth/512
        elif imageWidth < imageHeight :
            if imageHeight <=512 :
                convert = 512/imageHeight
            else :
                convert = imageHeight/512
        elif imageWidth == imageHeight :
            if imageWidth <=512 :
                convert = 512/imageHeight    
            else :
                convert = imageHeight/512

        resizeWidth = int(convert * imageWidth)
        resizeHeight = int(convert * imageHeight)

        if imageWidth > imageHeight :
            resizeImageNDArray = cv2.resize(imageNDArray, (resizeWidth, resizeHeight), interpolation = cv2.INTER_CUBIC)
            resizeImageNDArray = cv2.copyMakeBorder(resizeImageNDArray,0,512-resizeHeight,0,0,cv2.BORDER_CONSTANT ,(0,0,0))
        
        elif imageWidth < imageHeight :
            resizeImageNDArray = cv2.resize(imageNDArray, (resizeWidth, resizeHeight), interpolation = cv2.INTER_CUBIC)
            resizeImageNDArray = cv2.copyMakeBorder(resizeImageNDArray,0,0,0,512-resizeWidth,cv2.BORDER_CONSTANT ,(0,0,0))

        elif imageWidth == imageHeight :
            resizeImageNDArray = cv2.resize(imageNDArray, (512, 512), interpolation = cv2.INTER_CUBIC)          
        
        cv2.imwrite("C:/Users/user/Desktop/Dataset/Dataset/e-scooter_convert_to_PNG/resize/resize_image"+ str(count+1) +".png", resizeImageNDArray)
    except :
        pass
        # print("error ocurred")

print("END")
