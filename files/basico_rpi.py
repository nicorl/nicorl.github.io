# -*- coding: utf-8 -*-
import cv2
import numpy as np
import argparse
from datetime import datetime
from matplotlib import pyplot as plt
from conexbbdd import ConexBBDD

import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 20

conbd = ConexBBDD()

# Definición del color a captar #
red_inf_1 = (160, 50, 50)
red_sup_1 = (180, 255, 255)
range_red = "{}-{}".format(red_inf_1[0], red_sup_1[0])
blue_inf = (110,50,50)
blue_sup = (130,255,255)
range_blue = "{}-{}".format(blue_inf[0], blue_sup[0])
green_inf = (50, 50, 50)
green_sup = (70, 255, 255)
range_green = "{}-{}".format(green_inf[0], green_sup[0])
# Fin definición del color a captar #
# Pasar variable de sesión como argumento al arrancar #
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--frame", required=True,
    help="Intervalo de frames entre capturas (~30fps/s)")
args = vars(ap.parse_args())
# Pasar variable de sesión como argumento al arrancar #

cap = cv2.VideoCapture(0)
color = ('b','g','r')
contador = 0
z= 0
limite = int(args["frame"])

file_name = ""

while 1:
    # Abrimos cámara #
    ret, img = cap.read()
    # Aplicamos HSV #
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Aplicamos máscara de color rojo, azul y verde sobre HSV #
    mask_red = cv2.inRange(hsv, red_inf_1, red_sup_1)
    mask_blue = cv2.inRange(hsv, blue_inf, blue_sup)
    mask_green = cv2.inRange(hsv, green_inf, green_sup)
    mask_green = cv2.inRange(hsv, green_inf, green_sup)
    # Contador de frames # 
    contador += 1
    
    # Cada X frames # 
    if contador >= limite:
        contador = 0
        now = datetime.now()
        file_name = now.strftime("%d-%b-%Y-%H-%M-%S")
        #humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        # Guardamos la imagen #
        cv2.imwrite(r"{}.png".format(file_name), img)
        # Guardamos el histograma con los 3 canales #
        for i,col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
            #print("Color: {} - Valor Histr: {}".format(col, sum(histr)))
        plt.savefig("{}-hst.png".format(file_name))
        plt.clf()
        
        # Guardamos valor del histograma para el color rojo con máscara aplicada #
        histr = cv2.calcHist([mask_red],[0],None,[20],[236,256])
        #plt.plot(histr,color = 'k')
        #plt.xlim([0,20])
        levelredcolor = sum(histr)
        #print("[MASK] Color: k - Valor Histr: {}".format(levelredcolor))
        #plt.savefig("imgs\{}-hst-mask.png".format(file_name))
        #plt.clf()       
        
        # Guardamos valor del histograma para el color azul con máscara aplicada #
        histr = cv2.calcHist([mask_blue],[0],None,[20],[236,256])
        levelbluecolor = sum(histr)

        # Guardamos valor del histograma para el color verde con máscara aplicada #
        histr = cv2.calcHist([mask_green],[0],None,[20],[236,256])
        levelgreencolor = sum(histr)
                
        conbd.add_reg(file_name, levelbluecolor, levelgreencolor, levelredcolor)
        file_name = ""
        

        
    cv2.imshow('Camera video',img)
    #cv2.imshow('HSV',hsv)
    #cv2.imshow('Mascara de color',mask)
    #cv2.imshow('Camera video',np.vstack((img, mask)))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()