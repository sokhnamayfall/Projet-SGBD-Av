# Python program to create
# a file explorer in Tkinter

# import all components
import twint
import pandas as pd
import os
import urllib.request
import nest_asyncio
from os import path
# from the tkinter library
from tkinter import *


# import filedialog module
from tkinter import filedialog


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

  for i in range(0, max+1):
    urllib.request.urlretrieve(data['thumbnail'][i], data['date'][i]+".jpg")
    max-=1
    print("Téléchargement en cours...")
    if i==max:
          print("Téléchargement terminé!")

# Function for opening the
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "./communiqués-covid19SN",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	
	
																								
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							text = "Covid-19 Progression Modeler",
							width = 100, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_download = Button(window,
						text = "Download from Twitter", 
						command = tweets_download)

button_exit = Button(window,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_download.grid(column = 1, row = 3)

button_exit.grid(column = 1,row = 4)

# Let the window wait for any events
window.mainloop()
