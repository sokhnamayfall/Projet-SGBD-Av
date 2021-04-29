import cv2 
import pytesseract
from collections import OrderedDict
img1=cv2.imread("/Users/macbook/Desktop/projetMbacke/photos/EyM9bC8XEAM_HeZ.jpeg")
text1=pytesseract.image_to_string(img1,lang="eng")
month={"JANVIER":1,"FEVRIER":2,"MARS":3,"AVRIL":4,"MAI":5,"JUIN":6,"JUILLET":7,"AOUT":8,"SEPTEMBRE":9,"OCTOBRE":10,"NOVEMBRE":11,"DECEMBRE":12}
class DataAcquisition():
    def __init__(self):
        self.nextID=0;
        self.num_communique=OrderedDict();
        self.texte="";
        self.date_communique=OrderedDict();
        self.date_extraction=OrderedDict();
        self.nombre_tests=OrderedDict();
        self.nombre_positifs=OrderedDict();
        self.nombre_cas_contacts=OrderedDict();
        self.nombre_cas_importes=OrderedDict();
        self.nombre_cas_communautaire=OrderedDict();
        self.nombre_deces=OrderedDict();
        self.nombre_gueris=OrderedDict();
        self.nombre_cas_graves=OrderedDict();
        self.nombre_vaccines=OrderedDict();
        self.nombre_cas_communautaire_par_region=OrderedDict();
        self.nombre_cas_communautaire_par_localite_Dakar=OrderedDict();
        
    def get_num_communique(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="COMMUNIQUE":
                self.num_communique=int(tab_texte[i+1])
                self.texte=" ".join(tab_texte[i+1:])
                return int(self.num_communique)
    def get_date_communique(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="Dakar,":
                self.texte=" ".join(tab_texte[i+3:])
                #La date vient apres le "le" car le format est Dakar, le ... 
                return tab_texte[i+2]
    def get_nombre_tests(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="tests" or tab_texte[i]=="test":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="réalisés," or tab_texte[i+1]=="réalisé,":
                      
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i:])
                    
                    return int(tab_texte[i-1])
                   
    def get_nombre_positifs(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="sont" or tab_texte[i]=="est":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="revenus" or tab_texte[i+1]=="revenu":    
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1]) 
    def get_nombre_cas_contacts(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas" :
                if tab_texte[i+1]=="contact" or tab_texte[i+1]=="contacts":  
                #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1]) 
    def get_nombre_cas_communautaire(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas":
                 if tab_texte[i+1]=="issus" or tab_texte[i+1]=="issu":  
                #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1])
    def get_nombre_cas_importes(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="importé" or tab_texte[i+1]=="importés":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1]) 
    def get_nombre_gueris(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="patients" or tab_texte[i].lower()=="patient":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="suivis" or tab_texte[i+1]=="suivi":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1]) 
    def get_nombre_deces(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="décés":
                #La nombre vient apre le premier mot "Sur"
                if (tab_texte[i-1].lower()=="aucun"):
                    tab_texte[i-1]="0"
                self.texte=" ".join(tab_texte[i+1:])
                return int(tab_texte[i-1]) 
    def get_nombre_cas_graves(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="graves" or tab_texte[i+1]=="grave":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1]) 
    def get_nombre_vaccines(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="personnes" or tab_texte[i].lower()=="personne":
                if "vaccinées" or "vaccinée" in tab_texte[i:i+6]:
                    #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    return int(tab_texte[i-1]) 
    def register(self):
        data=self.get_date_communique()
        self.date_communique[self.nextID]=3
        #self.num_communique[self.nextID]=self.get_num_communique()
        self.date_communique[self.nextID]=self.get_date_communique()
        self.nombre_tests[self.nextID]=self.get_nombre_tests()
        self.nombre_positifs[self.nextID]=self.get_nombre_positifs()
        self.nombre_cas_contacts[self.nextID]=self.get_nombre_cas_contacts()
        self.nombre_cas_communautaire[self.nextID]=self.get_nombre_cas_communautaire()
        self.nombre_cas_importes[self.nextID]=self.get_nombre_cas_importes()
        self.nombre_gueris[self.nextID]=self.get_nombre_gueris()
        self.nombre_deces[self.nextID]=self.get_nombre_deces()
        self.nombre_cas_graves[self.nextID]=self.get_nombre_cas_graves()
        self.nombre_vaccines[self.nextID]=self.get_nombre_vaccines()   
        self.nextID=self.nextID+1
    def update(self,texte):
        self.texte=texte
        self.register()
dA=DataAcquisition() 

dA.update(text1)
#print(dA.get_date_communique())
#print(dA.get_num_communique())
# print(dA.texte)
# print(dA.get_nombre_tests())
# print(dA.get_nombre_positifs())
# #print(dA.get_nombre_vaccines(text1))
# print(dA.get_nombre_gueris(  ))
# print(dA.get_nombre_cas_contacts())
# print(dA.get_nombre_cas_importes())
print(dA.date_communique)
            