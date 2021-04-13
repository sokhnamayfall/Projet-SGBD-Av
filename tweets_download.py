import twint
import pandas as pd
import os
import urllib.request
import nest_asyncio
from os import path

nest_asyncio.apply()

t = twint.Config()
t.Username = "MinisteredelaS1"
t.Search = "Communiqué #Cov19sn"
t.Output = "ImagesCommunique.csv"
t.Store_csv = True
t.Images = True

# Récupération des tweets
if not path.exists("communiqués-covid19SN"):
  os.mkdir("communiqués-covid19SN")
  os.chdir("communiqués-covid19SN")
  
twint.run.Search(t)

#telechargement des images
data_OG = pd.read_csv('ImagesCommunique.csv')
data = data_OG.copy()

data = data[['date', 'thumbnail']]

# telechargement des communiqués
if not path.exists("communiqués-covid19SN"):
  os.mkdir("communiqués")
  os.chdir("communiqués")
else:
  os.chdir("communiqués-covid19SN")

max = len(data)-1

for i in range(0, max+1):
  urllib.request.urlretrieve(data['thumbnail'][i], str(max)+"."+data['date'][i]+".jpg")
  max-=1
  if i==0:
    print("Téléchargement terminé!")