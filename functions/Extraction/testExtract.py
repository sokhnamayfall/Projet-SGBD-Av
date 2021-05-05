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
        print(f)
        if "jpg" in f.split("."):   
            img1=cv2.imread(nomRepertoire+f)
            text1=pytesseract.image_to_string(img1,lang="eng")
            #recuperation de la date dans le nom du ficher cela va nous permettre de savoir si ce fichier 
            # est un de debut de commmunique ou la suite 
            date=f.split(".")[0].split("_")[1]
            #print(text1)
            extraire.update(date,text1)
            #extraire.get_all_localites()
            i+=1
extraire.to_csv()
data=list(extraire.num_communique.values())
date=list(extraire.date_communique.values())
test=list(extraire.nombre_tests.values())
gueris=list(extraire.nombre_gueris.values())
deces=list(extraire.nombre_deces.values())
communautaire=list(extraire.nombre_cas_communautaire.values())

print("rapport num communique non recuperer sur nombre total = "+str(len([d for d in data if d==None ])/len(data)))
print("rapport date communique non recuperer sur nombre total = "+str(len([d for d in date if d==None ])/len(date)))
print("rapport test communique non recuperer sur nombre total = "+str(len([d for d in test if d==None ])/len(date)))
print("rapport gueris communique non recuperer sur nombre total = "+str(len([d for d in gueris if d==None ])/len(date)))
print("rapport deces communique non recuperer sur nombre total = "+str(len([d for d in deces if d==None ])/len(date)))
print("rapport communautaire communique non recuperer sur nombre total = "+str(len([d for d in communautaire if d==None ])/len(date)))
extraire.to_csv()

# print(extraire.num_communique)
# print(extraire.nombre_cas_communautaire)
# print(extraire.nombre_cas_contacts)

