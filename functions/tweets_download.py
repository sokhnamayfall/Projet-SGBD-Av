import twint
import pandas as pd
import os
import urllib.request
import nest_asyncio
from os import path

def tweets_download() : 
    
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
    else:
        os.chdir("communiqués-covid19SN")
        
    twint.run.Search(t)

    #telechargement des images
    data_OG = pd.read_csv('ImagesCommunique.csv')
    data = data_OG.copy()

    data = data[['date', 'thumbnail']]

    # telechargement des communiqués
    if not path.exists("communiqués"):
        os.mkdir("communiqués")
        os.chdir("communiqués")
    else:
        os.chdir("communiqués")

    max = len(data)-1

    print("Téléchargement : ")
    for i in range(0, max+1):
        urllib.request.urlretrieve(data['thumbnail'][i], str(i)+'_'+data['date'][i]+".jpg")
        print(".", end=" ")
        if i==max:
            print("Téléchargement terminé!")
    
