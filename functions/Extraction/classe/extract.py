from collections import OrderedDict
import pandas as pd
month={"JANVIER":"1","FÉVRIER":"2","MARS":"3","AVRIL":"4","MAI":"5","JUIN":"6","JUILLET":"7","AOUT":"8","SEPTEMBRE":"9","OCTOBRE":"10","NOVEMBRE":"11","DÉCEMBRE":"12"}
class DataAcquisition():
    def __init__(self):
        self.nextID=0;
        self.textePivot="";
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
        self.localites=OrderedDict();
        
    def get_num_communique(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="COMMUNIQUE":
                self.texte=" ".join(tab_texte[i+1:])
                if (tab_texte[i+1].isdigit()):
                    return int(tab_texte[i+1])
                else :
                    return None
    def get_date_communique(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            mois=str(None)
            #Chech the month dans la partie en haut : Dakar, le 23/12/6288 
            # if tab_texte[i]=="Dakar,":
            #     if len(tab_texte[i+2].split("/"))>=2:
            #         mois=tab_texte[i+2].split("/")[1]
                
            if tab_texte[i]=="Ce":
                #self.texte=" ".join(tab_texte[i+3:])
                
                #La date vient apres le "le" car le format est Dakar, le ... 
                #[:4] pour enlever la virgule apres l'annee
                print("OK")
                keys=month.keys()
                if not mois.isdigit():
                    mois=str(None)
                print(tab_texte[i+3])
                if tab_texte[i+3].upper() in keys:
                    mois=month[tab_texte[i+3].upper()]
                return "-".join([tab_texte[i+2],mois,tab_texte[i+4][:4]])
    def get_nombre_tests(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="tests" or tab_texte[i]=="test":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="réalisés," or tab_texte[i+1]=="réalisé,":
                      
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1])
                    return None
                   
    def get_nombre_positifs(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="sont" or tab_texte[i]=="est":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="revenus" or tab_texte[i+1]=="revenu":    
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1]) 
                    return None
    def get_nombre_cas_contacts(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas" :
                if tab_texte[i+1]=="contact" or tab_texte[i+1]=="contacts":  
                #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1]) 
                    return None
    def get_nombre_cas_communautaire(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas":
                 if tab_texte[i+1]=="issus" or tab_texte[i+1]=="issu":
                #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    print(self.texte)
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1])
                    return None
    def get_nombre_cas_importes(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="importé" or tab_texte[i+1]=="importés":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1]) 
                    return None
    def get_nombre_gueris(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="patients" or tab_texte[i].lower()=="patient":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="suivis" or tab_texte[i+1]=="suivi" or tab_texte[i+1]=="hospitalisés" or tab_texte[i+1]=="hospitalisé":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1]) 
                    return None
    def get_nombre_deces(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="nouveaux":
                if tab_texte[i+1].lower()=="décés":
                #La nombre vient apre le premier mot "Sur"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1]) 
                    return 0
            if tab_texte[i].lower()=="décés":
                #La nombre vient apre le premier mot "Sur"
                if (tab_texte[i-1].lower()=="aucun"):
                    tab_texte[i-1]="0"
                self.texte=" ".join(tab_texte[i+1:])
                if (tab_texte[i-1].isdigit()):
                    return int(tab_texte[i-1]) 
                return 0

    def get_nombre_cas_graves(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nombre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="graves" or tab_texte[i+1]=="grave":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1])
                    return None 
    def get_nombre_vaccines(self):
        tab_texte=self.texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="personnes" or tab_texte[i].lower()=="personne":
                if "vaccinées" or "vaccinée" in tab_texte[i:i+6]:
                    #La nombre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    self.texte=" ".join(tab_texte[i+1:])
                    if (tab_texte[i-1].isdigit()):
                        return int(tab_texte[i-1]) 
                    return None
    
    def is_format_with_parenthesis(self):
        print(self.texte)
        tab_texte=self.texte.split()
        for chaine in tab_texte:
            if "(" in chaine:
                if ")" in chaine:
                    return True
        return False
    def is_format_dakar_autres_regions(self):
        if not self.is_format_with_parenthesis():
            tab=self.texte.split()
            for i in range(len(tab)):
                if tab[i]=="comme":
                    if tab[i+1]=="suit" or tab[i+1]=="suit:":
                        return True
            return False
    def get_digits(self,chaine):
        res = [i for i in chaine if i.isdigit()]
        print(res)
        if len(res)!=0:
            return int("".join(res))
        return -1
    def get_communautaire_paragraphe(self):
        fin=len(self.textePivot)
        deb=0
        tab=self.textePivot.split()
        for i in range(len(tab)):
            if tab[i]=="suit" or tab[i]=="suit:":
                deb=i+1
            if tab[i]=="patients" or tab[i]=="patient":
                fin=i-1
        self.textePivot=self.textePivot[deb:fin] 
        return self.textePivot   
    def get_localites(self):
        print(self.textePivot.split())
        self.get_communautaire_paragraphe()
        if ";" in self.textePivot.split():
            print("Vraaaaaaaaaaaaaaaaaaaaaaaa")  
            tab_texte=self.textePivot.split()
            for i in range(len(tab_texte)) :
                if tab_texte[i]=="dont" or tab_texte[i]=="dont:":
                    self.textePivot=" ".join(tab_texte[i+2:])
                    debut=i+2
                    break
            dakar=self.textePivot
            #fin
            #partie recup autre regions
            j=0
            for i in range(len(self.textePivot)):
                if self.textePivot[i]==".":
                    dakar=self.textePivot[:i]
                    break
                j=j+1
            tab_texte_dakar=dakar.split(";")
            self.textePivot=self.textePivot[j:]
            print(dakar)
            
            data={}
            for chaine in tab_texte_dakar:
                if len(chaine)>0:
                    chaine=chaine.split()
                    
                    if len(chaine)>0 and ( chaine[0]=='-' or chaine[0]=='>'):
                        nbre_cas=chaine[1]
                        k=2
                    else: 
                        k=1
                        nbre_cas=chaine[0]   
                    print(nbre_cas)
                    nbre_cas=self.get_digits(nbre_cas)
                    # if nbre_cas[0]=="O":
                    #     nbre_cas=nbre_cas[1:]
                    # nbre_cas=int(nbre_cas)

                    chaine=" ".join(chaine[k:])
                    #effacer les articles qui commencent la liste des localite ex: aux a etc
                    chaine=" ".join(chaine.split()[1:])
                    # split les localites
                    chaine=chaine.split(",")
                    localitesBis=chaine[-1].split("et")
                    
                    chaine=chaine[:-1]
                    if (len(localitesBis)==2):   
                        chaine.append(localitesBis[0])
                        chaine.append(localitesBis[1])
                    else:
                        chaine.append(localitesBis[0])
                    #place a la sauvegarde
                    print(self.num_communique[self.nextID])
                    if nbre_cas in self.localites[self.num_communique[self.nextID]].keys():
                        for local in chaine:
                            self.localites[self.num_communique[self.nextID]][nbre_cas].append(local)
                    else:
                        self.localites[self.num_communique[self.nextID]][nbre_cas]=chaine
                    i=i+1
                return self.localites
    def get_all_localites(self):
        if self.is_format_with_parenthesis():
            print("ok")
        if self.is_format_dakar_autres_regions():
            #partie de la recuperation des localite de dakar
            #debut
            self.localites[self.num_communique[self.nextID]]={}
            self.get_localites()
            self.get_localites()
            #print(self.get_localites())
        self.nextID=self.nextID+1
            #for i in range(len())
            
                
    def get_nombre_cas_communautaire_par_localite(self):
        #first check the format of the text .On a decele deux types de formats 
        tab_texte=self.texte.split()
        if self.is_format_with_parenthesis():
            print("ok")
        else:
            print("ok")

            
    def register(self):
        #l'ordre de l appel des getter est important car on pour optimiser les calculs on supprimes les chaines inutiles
        self.date_communique[self.nextID]=self.get_date_communique()        
        self.num_communique[self.nextID]=self.get_num_communique()
        self.nombre_tests[self.nextID]=self.get_nombre_tests()
        self.nombre_positifs[self.nextID]=self.get_nombre_positifs()
        self.nombre_cas_contacts[self.nextID]=self.get_nombre_cas_contacts()
        self.nombre_cas_importes[self.nextID]=self.get_nombre_cas_importes()
        self.nombre_cas_communautaire[self.nextID]=self.get_nombre_cas_communautaire()
        self.get_all_localites()
        self.nombre_gueris[self.nextID]=self.get_nombre_gueris()
        self.nombre_deces[self.nextID]=self.get_nombre_deces()
        self.nombre_cas_graves[self.nextID]=self.get_nombre_cas_graves()
        self.nombre_vaccines[self.nextID]=self.get_nombre_vaccines()   
        self.nextID=self.nextID+1
    def update(self,dateFile,texte):
        self.texte=texte
        self.textePivot=self.texte
        dates=self.date_communique.values()
        keys=self.date_communique.keys()
        if dateFile not in dates:
            self.register()
            print("ok")
    def to_csv(self):
        dictio={"num_communique":list(self.num_communique.values()),"date_communique":list(self.date_communique.values()),"nbre_test":list(self.nombre_tests.values()),
                "nbre_gueris":list(self.nombre_gueris.values()),"nbre_positifs":list(self.nombre_positifs.values()),
                "nbre_cas_contact":list(self.nombre_cas_contacts.values()),"nbre_cas_communautaire":list(self.nombre_cas_communautaire.values()),
                "nbre_cas_importes":list(self.nombre_cas_importes.values()),
                "nbre_deces":list(self.nombre_deces.values()),"nbre_cas_graves":list(self.nombre_cas_graves.values()),
                "nbre_vaccines":list(self.nombre_vaccines.values())
                }
        data=pd.DataFrame(dictio)
        localite=pd.DataFrame(self.localites)
        data.to_json("covid.json")
        localite.to_json("localite.json")
        data.to_csv("covid2.csv")
        return True
# import cv2 
# import pytesseract
# from collections import OrderedDict
# img1=cv2.imread("/Users/macbook/Desktop/projetMbacke/Projet-SGBD-Av/functions/Extraction/communiques/119_2020-12-31.jpg")
# text1=pytesseract.image_to_string(img1,lang="eng")
# dA=DataAcquisition() 

        
         


# dA.update("dsjqsd.jpeg",text1)

# dA.get_all_localites()
# print(dA.localites)
# print(dA.date_communique)
# # print(dA.texte)
# print(dA.get_nombre_tests())
# print(dA.get_nombre_positifs())
# #print(dA.get_nombre_vaccines(text1))
# print(dA.get_nombre_gueris(  ))
# print(dA.get_nombre_cas_contacts())
# print(dA.get_nombre_cas_importes())
#print(dA.date_communique)
