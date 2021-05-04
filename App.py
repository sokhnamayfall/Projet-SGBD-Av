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
import os
import glob
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

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

def tweets_download() : 

    print("Téléchargement terminé!")

def Browser():
  # zone de définition de fonctions
  
  def showSelected():
    countries = []
    cname = liste_fichiers.curselection()
    for i in cname:
        op = liste_fichiers.get(i)
        countries.append(op)
    for val in countries:
        print(val)

  def choisir_dossier ():
      "ouvre un dialogue de sélection de répertoire"
      # voir http://tkinter.unpythonic.net/wiki/tkFileDialog
      dossier = filedialog.askdirectory(
          initialdir = "./functions",
          title="Sélectionnez un dossier",
          mustexist=True,
          parent=fenetre,
      )
      # un dossier a vraiment été sélectionné ?
      if dossier:
          # on remplit la liste de fichiers
          remplir_liste(dossier)
      # end if
  # end def
  
  def remplir_liste (dossier):
      """
          remplit la liste de fichiers à partir de l'emplacement
          @dossier fourni en paramètre de fonction;
      """
      # init globales
      global dossier_actuel
      # on conserve le dossier en cours de traitement
      dossier_actuel = dossier
      # on récupère la liste des fichiers
      _liste_fichiers = glob.glob(normaliser(dossier, motif_fichiers))
      # on met à jour la listbox à travers la variable de contrôle
      cvar_fichiers.set(" ".join(map(os.path.basename, _liste_fichiers)))
  # end def
  
  def normaliser (chemin, *args):
      "met un chemin de fichier en conformité avec l'OS utilisé"
      return os.path.normpath(os.path.join(chemin, *args))
  # end def
  
  def afficher_fichier (event):
      "affiche le contenu du fichier sélectionné"
      # on récupère le nom du fichier
      fichier = normaliser(
          dossier_actuel,
          liste_fichiers.get(liste_fichiers.curselection() or 0)
      )
      # est-ce réellement un fichier ?
      if os.path.isfile(fichier):
          # oui, on peut l'ouvrir
          with open(fichier) as file_in:
              # on efface d'abord la zone de texte
              affichage_texte.delete("1.0", END)
              # on insère le nouveau contenu texte du fichier
              affichage_texte.insert("1.0", file_in.read())
          # end with
      # end if
  # end def

# début du programme
  
  # init variables globales
  dossier_actuel = "./functions"
  motif_fichiers = "*.json"
  
  # on commence par établir l'interface graphique (GUI)
  # on crée la fenêtre principale
  fenetre = Tk()
  fenetre.geometry("600x600")
  fenetre.config(background = "grey")
  fenetre.title("Liste des téléchargements")
  Button(
      fenetre,
      text="Télécharger les communiqués",
      command=tweets_download,
  ).grid(row=1, column=0)
  Button(
      fenetre,
      text="Extraire les données",
      command=tweets_download,
  ).grid(row=1, column=1)
  Button(
      fenetre,
      text="Charger les données",
      command=showSelected,
  ).grid(row=2, column=0)
  # on ajoute un bouton 'quitter'
  Button(
      fenetre,
      text="Quitter",
      command=fenetre.destroy
  ).grid(row=1, column=1, sticky=E)
  conteneur_fichiers = Frame(fenetre)
  # on rend le conteneur redimensionnable
  conteneur_fichiers.columnconfigure(0, weight=1)
  conteneur_fichiers.rowconfigure(1, weight=1)
  # on crée une étiquette texte dans ce conteneur
  Label(
      conteneur_fichiers,
      text="Veuillez sélectionner un fichier :"
  ).grid(row=0, column=0, sticky=EW)
  # on crée la liste des fichiers
  cvar_fichiers = StringVar()
  liste_fichiers = Listbox(conteneur_fichiers,selectmode = "multiple", listvariable=cvar_fichiers)
  liste_fichiers.grid(row=1, column=0, sticky=NS+EW)
  # avec sa scrollbar
  vbar_fichiers = Scrollbar(conteneur_fichiers, orient=VERTICAL)
  vbar_fichiers.grid(row=1, column=1, sticky=NS+W)
  # on connecte la scrollbar à la liste des fichiers
  liste_fichiers.configure(yscrollcommand=vbar_fichiers.set)
  vbar_fichiers.configure(command=liste_fichiers.yview)
  # on va gérer l'affichage des recettes sur simple clic
  # sur un fichier de la liste
  liste_fichiers.bind("<ButtonRelease-1>", afficher_fichier)
  # on crée un bouton de type 'Parcourir'
  Button(
      conteneur_fichiers,
      text="Sélectionner un dossier",
      command=choisir_dossier,
  ).grid(row=2, column=0)
  # on place le conteneur dans la fenêtre principale
  # avec des marges padx et pady
  conteneur_fichiers.grid(row=0, column=0, sticky=NS+EW, padx=5, pady=5)
  # on crée un conteneur pour l'affichage
  conteneur_affichage = Frame(fenetre)
  # on rend le conteneur redimensionnable
  conteneur_affichage.columnconfigure(0, weight=1)
  conteneur_affichage.rowconfigure(1, weight=1)
  # on crée une étiquette texte dans ce conteneur
  Label(
      conteneur_affichage,
      text="Prévisualisation :"
  ).grid(row=0, column=0, sticky=EW)
  # on crée la zone d'affichage de texte
  affichage_texte = ScrolledText(
      conteneur_affichage,
      bg="white",
      fg="blue",
      font="sans 12 bold",
      height=10,
      width=20,
  )
  affichage_texte.grid(row=1, column=0, sticky=NS+EW)
  
  # on place le conteneur dans la fenêtre principale
  # avec des marges padx et pady
  conteneur_affichage.grid(row=0, column=1, sticky=NS+EW, padx=5, pady=5)
  # on rend la fenêtre redimensionnable
  fenetre.rowconfigure(0, weight=1)
  fenetre.columnconfigure(1, weight=1)
  # pour finir
  # on lance la boucle événementielle principale
  fenetre.mainloop()	
  

Browser()
