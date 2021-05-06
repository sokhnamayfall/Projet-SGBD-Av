from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import sys
import mysql.connector
import os
import matplotlib.pyplot as plt
import json


connection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="AmoulcodE1004",
  database="projetcovid19",
  port=3306
)
if connection.is_connected():
  print("connexion bien établie")

curseur = connection.cursor()

f = open('functions/2020_Janvier.json',)
data = json.load(f)

request = "SELECT sum(NbrCas) from localite WHERE nom_region="+"'"+sys.argv[1]+"'"+""
curseur.execute(request)
Nbre_Cas=curseur.fetchone()
print(Nbre_Cas[0])

def details():
    x=[]
    y=[]
    N_total=0
    request = "SELECT date_communique from fichier "
    curseur.execute(request)
    Dates=curseur.fetchall()
    for i in range(len(Dates)):
        if(sys.argv[1]=="DAKAR"):
            request1 = "SELECT SUM(nbrCas) from localite where nom_region='Dakar'"
            curseur.execute(request1)
            Nbre_Cas=curseur.fetchone()
            #print(Nbre_Cas[0])
            y.append(Dates[i][0])
            x.append(Nbre_Cas)
        else:
            Loc=[]
            print(Dates[i][0])
            request0 = "SELECT nom_localite from region"
            curseur.execute(request0)
            Localites=curseur.fetchall()
            for p in enumerate(Localites):
                print(p[1][0])
                Loc.append(p[1][0])
            if (sys.argv[1] in Loc) :
                print("in")
                request1 = "SELECT nbrCas from localite where nom_region='"+""+sys.argv[1]+""+"'"
                curseur.execute(request1)
                Nbre_Cas=curseur.fetchone()
                y.append(Dates[i][0])
                x.append(Nbre_Cas)
            else: 
                print("not in")
        print(Liste_Dates)
    plt.title("Courbe temporelle d'évolution de: "+sys.argv[1])
    print(x)
    print(y)
    plt.plot(x,y,color='green',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
    plt.xlabel('Vitesse')
    plt.ylabel('Temps')
    plt.show()

fenetre1 = Tk()

fenetre1.title(sys.argv[1])
fenetre1.geometry("200x120")

N_total=0

var = StringVar()
lbl = Label(fenetre1, textvariable=var)
request = "SELECT date_communique from fichier"
curseur.execute(request)
Dates=curseur.fetchall()
for i in range(len(Dates)):
    if(sys.argv[1]=="DAKAR"):
        request1 = "SELECT SUM(Nbre_Cas) from "+"`"+Dates[i][0]+"`"+" where Localites LIKE 'DAKAR_%'"
        curseur.execute(request1)
        Nbre_Cas=curseur.fetchone()
        #print(Nbre_Cas[0])

var.set(""+ sys.argv[1]+"\n Nbre de cas: "+str(Nbre_Cas[0])+"")
lbl.grid(row=0, column=1)
Button(
      fenetre1,
      text="Quitter",
      command=fenetre1.destroy
  ).grid(row=1, column=1, sticky=E)
fenetre1.mainloop()
