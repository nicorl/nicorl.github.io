---
title: "Gathering pic and histogram"
excerpt: "Computer vision with python code for take a photo and get its histogram"
collection: portfolio
---

The purpose of this report is to explain how to I track some colours from a fixed source.

I've divide code in some parts to make it easier for newbies, because of it's what I would like to receive.

### Set up a database

First, we are going to step up a mysql database. I hope you have installed WAMP/XAMP/LAMP or just MySQL server in your computer.

I've just installed WAMP and configure `phpmyadmin` in order to make it easy for me.

Before we started, I highlight that this are the connection information that we will need:
```mysql
host:localhost
user:root
password:(blank)
database:color_tracker
```

Once you have your MySQL server running, please type this on console, for adding a new database:

 <span style="color:orange">WARNING!: remove spaces, it's just 1 line</span>
```
> CREATE TABLE `color_tracker`.`trackingData` ( `Image` VARCHAR(200) NOT NULL ,
  `Histogram` VARCHAR(200) NOT NULL , `BlueChannel` INT(6) NOT NULL , `GreenChannel`
   INT(6) NOT NULL , `RedChannel` INT(6) NOT NULL ) ENGINE = MyISAM;
```

Now, we are able to add data records about info we want to gather.

### Create a library to connect with

Our second step is going to be a library creation. We will call this library from the main file (`tracker.py`). The idea is call a function to add info in our database.

I think the code below is not a big deal, just an constructor with a function to add data in a table called `trackingdata`.
```python
import mysql.connector
from mysql.connector import Error

class ConexBBDD():
    # This is the function. We will call as something.add_reg(arg1,arg2,arg3,...)
    def add_reg(self, file_name, niv_azul, niv_ver, niv_roj):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='color_tracker',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            # Be careful here with the names of columns in trackingdata table!
            mySql_insert_query = """INSERT INTO trackingdata (Image, Histogram, BlueChannel, GreenChannel, RedChannel)
                                    VALUES (%s, %s, %s, %s, %s) """
            nombre = "{}.png".format(file_name)
            histograma = "{}-hst.png".format(file_name)
            print("[BBDD] Table trackingdata. {}-{}-{}-{}-{}".format(nombre, histograma, int(niv_azul[0]), int(niv_ver[0]), int(niv_roj[0])))
            recordTuple = (nombre, histograma, int(niv_azul[0]), int(niv_ver[0]), int(niv_roj[0]))
            cursor.execute(mySql_insert_query, recordTuple)
            connection.commit()


        except mysql.connector.Error as error:
            print("Error adding data in trackingdata {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
```


### Main code!

Now we are in condition to add the main code for the app.

The point is that we are going to track colors, so we have to set boundaries about them.

 <span style="color:orange">Keypoint: HSV at OpenCV library. Could be difficult to use if you don't understand properly. </span>

 An insight:

![image](https://docs.opencv.org/3.4/Threshold_inRange_HSV_colorspace.jpg)

My code commented:

```python
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
```
