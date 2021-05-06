import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Button, Tk


def visual():
  pageV = Tk()
  pageV.geometry("510x150")
  pageV.config(background = "grey")
  pageV.title("Courbes d'évolution")

  Button(
      pageV,
      text="Quitter",
      command=pageV.destroy
  ).grid(row=4, column=1)

  covid=pd.read_csv("functions/covid2.csv")

  import math
  def have_not_digit(string):
    for i in string:
      if not i.isdigit():
        return False
    return True
  def clean_date(date):
    if date=="nan":
        return math.nan
    tab=list(str(date).split("-"))
    for i in range(len(tab)):
        if have_not_digit(tab[i])==False:
            return math.nan
        tab[i]=tab[i].strip()
        if len(tab[i])==1:
            tab[i]="0"+tab[i]
        if tab[i]=="None":
            return math.nan
    tab.reverse()
    return "-".join(tab)

  covid["date_communique"]=covid["date_communique"].apply(clean_date)
  covid.dropna(subset = ["date_communique"], inplace=True)
  covid.to_csv("covid_cleaned.csv")

  # chargement
  covid_series=pd.read_csv("covid_cleaned.csv",index_col='date_communique',parse_dates=True)
  covid_series.drop(['Unnamed: 0',"Unnamed: 0.1"],
    axis='columns', inplace=True)

  covid_series=covid_series.sort_index()

  #Evolution des nombre de cas positif
  def visualPositifs():
    covid_series["nbre_positifs"].plot(figsize=(9,6))
    plt.show()
  Button(
      pageV,
      text="Nbre Cas Positifs",
      command=visualPositifs
  ).grid(row=0, column=0)
  # evolution nombre de deces 
  def visualDeces():
    covid_series["nbre_deces"].plot(figsize=(9,6))
    plt.show()
  Button(
      pageV,
      text="Nbre Décès",
      command=visualDeces
  ).grid(row=0, column=1)
  # evolution nombre de cas communautaire 
  def visualCommunautaires():
    covid_series["nbre_cas_communautaire"].plot(figsize=(9,6))
    plt.show()
  Button(
      pageV,
      text="Nbre Cas Communautaires",
      command=visualCommunautaires
  ).grid(row=0, column=2) 
  # regrouper les donnees par frequence des mois dans l annee 2020
  def visualPositifsFrequence():
    covid_series.loc["2020","nbre_positifs"].resample('M').plot(figsize=(10,10))
    plt.show()
  Button(
      pageV,
      text="Fréquence Cas Positifs",
      command=visualPositifsFrequence
  ).grid(row=1, column=0)
  # regrouper les donnees par frequence des mois dans l annee 2020
  def visualCommunautairesFrequence():
    covid_series.loc["2020","nbre_cas_communautaire"].resample('M').plot(figsize=(10,10))
    plt.show()
  Button(
      pageV,
      text="Fréquence Cas Communautaires",
      command=visualCommunautairesFrequence
  ).grid(row=1, column=2)
  def visualPositifsMoisSemaines():
    plt.figure(figsize=(12,8))
    covid_series.loc["2020","nbre_positifs"].plot()
    covid_series.loc["2020","nbre_positifs"].resample('M').mean().plot(label='moyenne par mois',lw=3,ls=':',alpha=0.8)
    covid_series.loc["2020","nbre_positifs"].resample('W').mean().plot(label='moyenne par semaine',lw=2,ls='--',alpha=0.8)
    plt.legend()
    plt.show()
  Button(
      pageV,
      text="Vue Cas Positifs",
      command=visualPositifsMoisSemaines
  ).grid(row=2, column=0)
  def visualDecesMoisSemaines():
    plt.figure(figsize=(12,8))
    covid_series.loc["2020","nbre_deces"].plot()
    covid_series.loc["2020","nbre_deces"].resample('M').mean().plot(label='moyenne par mois', lw=3,ls=':',alpha=0.8)
    covid_series.loc["2020","nbre_deces"].resample('W').mean().plot(label='moyenne par semaine', lw=2,ls='--',alpha=0.8)
    plt.legend()
    plt.show()
  Button(
      pageV,
      text="Vue Nbre Décès",
      command=visualDecesMoisSemaines
  ).grid(row=2, column=1)
  def visualCommunautairesMoisSemaines():
    plt.figure(figsize=(12,8))
    covid_series.loc["2020","nbre_cas_communautaire"].plot()
    covid_series.loc["2020","nbre_cas_communautaire"].resample('M').mean().plot(label='moyenne par mois', lw=3,ls=':',alpha=0.8)
    covid_series.loc["2020","nbre_cas_communautaire"].resample('W').mean().plot(label='moyenne par semaine', lw=2,ls='--',alpha=0.8)
    plt.legend()
    plt.show()
  Button(
      pageV,
      text="Vue Cas Communautaires",
      command=visualCommunautairesMoisSemaines
  ).grid(row=2, column=2)
  # on rend la fenêtre redimensionnable
  pageV.rowconfigure(0, weight=1)
  pageV.columnconfigure(1, weight=1)
  # pour finir
  # on lance la boucle événementielle principale
  pageV.mainloop()	