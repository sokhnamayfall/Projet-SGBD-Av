# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import twint
import pandas as pd
import os
import urllib.request
import nest_asyncio
from os import path

# import filedialog module
from tkinter import filedialog


def tweets_download():
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

    # telechargement des images
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
        urllib.request.urlretrieve(
            data['thumbnail'][i], str(max)+"."+data['date'][i]+".jpg")
        max -= 1
        if i == 0:
            print("Téléchargement terminé!")

# Function for opening the
# file explorer window


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/Users/Christian/Python/Projet-SGBD-Av/downloads",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


def show_data_loader():
    main_frame.grid_forget()
    second_frame.grid(column=1, row=1)


def go_back():
    main_frame.grid(column=1, row=1)
    second_frame.grid_forget()


# Create the root window
window = Tk()
window.title('File Explorer')
window.geometry("500x500")
main_frame = Frame(window)
main_frame.configure(background="white")
label_file_explorer = Label(main_frame,
                            text="Covid-19 Progression Modeler",
                            width=100, height=4,
                            fg="blue")
button_explore = Button(main_frame,
                        text="Browse Files",
                        command=browseFiles)
button_download = Button(main_frame,
                         text="Download from Twitter",
                         command=tweets_download)
button_data_loader = Button(
    main_frame, text="data loader", command=show_data_loader)
button_exit = Button(main_frame,
                     text="Exit",
                     command=exit)

label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_download.grid(column=1, row=3)
button_data_loader.grid(column=1, row=4)
button_exit.grid(column=1, row=5)


second_frame = Frame(window)

button = Button(second_frame, text="click me")
button.grid(column=1, row=1)
main_frame.grid(column=1, row=1)
window.mainloop()
