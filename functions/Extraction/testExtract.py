from classe.extract import DataAcquisition
import cv2 
import pytesseract
from collections import OrderedDict
import pandas as pd
from os import listdir
nomRepertoire="communiques/"
from os.path import isfile, join
i=0
extraire=DataAcquisition()
for f in listdir(nomRepertoire):
    if isfile(join(nomRepertoire, f)):
        img1=cv2.imread(nomRepertoire+f)
        text1=pytesseract.image_to_string(img1,lang="eng")
        #recuperation de la date dans le nom du ficher cela va nous permettre de savoir si ce fichier 
        # est un de debut de commmunique ou la suite 
        date=f.split(".")[0].split("_")[1]
        extraire.update(date,text1)
        i+=1
        if (i==20):
            break
extraire.to_csv()
# print(extraire.num_communique)
# print(extraire.nombre_cas_communautaire)
# print(extraire.nombre_cas_contacts)

