import mysql.connector
import json

def charger_donnees():

  connection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="AmoulcodE1004",
  database="projetcovid19",
  port=3306
  )
  if connection.is_connected():
      print("connexion bien établie")

  cursor = connection.cursor()

  # loading json file as a dictionary
  f = open('./functions/2020_Janvier.json',)
  data = json.load(f)
  j=0
  liste = []
  # storing data in bdd
  while j< 405:
      for col, contenu in data.items():
          j = str(j)
          liste.append(data[col][j])

      liste = tuple(liste) # transform list to tuple for insert
      # ****************insert request*****************
      request = "insert into fichier(nbre_cas_contact, nbre_cas_communautaires, nbre_gueris, nbre_deces, nbre_test, nbre_cas_importes, nbre_cas_graves, date_communique, nbre_vaccines, nbre_positifs, num_communique) values(%s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
      cursor.execute(request, liste)
      connection.commit()
      print("insertion ",j, "reussie")
      liste = list(liste) # transform the tuple again to a list
      del liste[:] # delete all elements in the list
      j = int(j)
      j +=1
      if j==405:
        print("chargement terminé")
        break
  
  connection.close()
  cursor.close()											
