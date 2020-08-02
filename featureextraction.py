import cv2
import numpy as np
import numpy
from PIL import Image
import sys
#Input Image
ipfile='c:/xampp/htdocs/'+str(sys.argv[1])
input_img= cv2.imread(ipfile)
image = cv2.imread(ipfile)
try:
    gray_img =  cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray_img, 5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


    #Circle detection using HoughCircle
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))

    #To get the pixel values of image
    def get_image(image_path):
        """Get a numpy array of an image so that one can access values[x][y]."""
        image = Image.open(image_path, "r")
        width, height = image.size
        pixel_values = list(image.getdata())
        return pixel_values
        """if image.mode == "RGB":
            channels = 3
        elif image.mode == "L":
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None
        pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
        return pixel_values
        """
    #Storing green ration of each circle
    Green_Ratio = []
    count=1

    #calculating RGB ratio
    for i in circles[0,:]:
        cv2.circle(input_img,(i[0],i[1]),i[2],(0,255,0),6)
        cv2.circle(input_img,(i[0],i[1]),2,(0,0,255),3)

        #Crop the circle from image
        crop = input_img[i[1]-i[2]:i[1]+i[2],i[0]-i[2]:i[0]+i[2]]

        #Store the cropped image
        cv2.imwrite('Circle'+str(count)+'.jpg',crop)

        #Find the pixel values of image
        pixel = get_image('./Circle'+str(count)+'.jpg')

        red   = []
        green = []
        blue  = []

        for pix in pixel:
            if(pix!=(255,255,255) and pix!=(0,0,0)):
                red.append(pix[0])
                green.append(pix[1])
                blue.append(pix[2])

        #Append Green Ratio of Each Circle
        Green_Ratio.append(round(sum(green)/len(green),2))

        #RGB values of Each Circle
        #print("Circle "+str(count))
        #print()
        #print("({:.2f},{:.2f},{:.2f})".format(sum(red)/len(red),sum(green)/len(green),sum(blue)/len(blue)))
        #print()
        count+=1
