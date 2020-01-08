# -*- coding: utf-8 -*-
import cv2                              # computer vision library
import argparse                         # to add arguments when calling the file (p.e.: python maincode.py -f 30)
from datetime import datetime           # to get time and date
from matplotlib import pyplot as plt    # to plot histograms
from conexbbdd import ConexBBDD         # our database library!

conbd = ConexBBDD()                     # assign our constructor

# Color boundaries #
red_inf_1 = (160, 50, 50)
red_sup_1 = (180, 255, 255)

blue_inf = (110,50,50)
blue_sup = (130,255,255)

green_inf = (50, 50, 50)
green_sup = (70, 255, 255)

# End color boundaries #

# Argument for take an photo even f frames #
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--frame", required=True,
    help="Frame interval between captures (~30fps/s)")
args = vars(ap.parse_args())
# End Argument for take an photo even f frames #

cap = cv2.VideoCapture(0)   # Define de source
color = ('b','g','r')       # Define de histogram colours
contador = 0                # Frame counter
limite = int(args["frame"]) # Frame limit, assigned by argument

file_name = ""              # Necessary to work

while 1:
    # Open the camera #
    ret, img = cap.read()
    # HSV Transform #
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Masks red, blue, green, over HSV <- (three times the same with different colours) #
    mask_red = cv2.inRange(hsv, red_inf_1, red_sup_1)
    mask_blue = cv2.inRange(hsv, blue_inf, blue_sup)
    mask_green = cv2.inRange(hsv, green_inf, green_sup)
    # Increase frame number #
    contador += 1

    # When condition #
    if contador >= limite:
        contador = 0
        # We define the filename through date.
        now = datetime.now()
        file_name = now.strftime("%d-%b-%Y-%H-%M-%S")
        # We save the image #
        cv2.imwrite(r"{}.png".format(file_name), img)
        # We save the histogram with the 3 channels #
        for i,col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
        plt.savefig("{}-hst.png".format(file_name))
        plt.clf()

        # We save the red, blue and green level captured by the camera #
        histr = cv2.calcHist([mask_red],[0],None,[20],[236,256])
        levelredcolor = sum(histr)

        histr = cv2.calcHist([mask_blue],[0],None,[20],[236,256])
        levelbluecolor = sum(histr)

        histr = cv2.calcHist([mask_green],[0],None,[20],[236,256])
        levelgreencolor = sum(histr)

        # We send the data to the database!
        conbd.add_reg(file_name, levelbluecolor, levelgreencolor, levelredcolor)
        # We drop the name of filename for next loop
        file_name = ""


    # Open the camera in a window
    cv2.imshow('Camera video',img)
    # When ESC pressed, stop running
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()