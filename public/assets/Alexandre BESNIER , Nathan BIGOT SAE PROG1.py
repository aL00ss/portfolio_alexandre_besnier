# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:26:49 2022

@author: abesni05
"""

import json,csv,sys
try:
    f = open('concentrations-polluants-dans-lair-ambiant.json','r')
    # ouvre le programme.
except FileNotFoundError:
    print('le fichier est introuvable.')
    sys.exit()
# test si le fichier est présent et le ferme si il n'est pas là.
db = json.load(f)
# lit le fichier json et l'attribue à la variable "db".
listefinale = {}
compteur = 1
# compte chaque ligne présent dans la liste finale (si il y a moins de ligne que dans le fichier json par exemple).
for key in db:
    try:
        ligne = key["fields"]
        # attribue les valeurs du dictionaire fields de rang "key" à une variable: "ligne".
        NomStation= ligne["nom_station"]
        lattitude= ligne["x_wgs84"]
        longitude= ligne["y_wgs84"]
        dateDebut= ligne["date_debut"]
        dateDebut= dateDebut[-2:]+"-"+dateDebut[6:8]+"-"+dateDebut[:4]
        valur = ligne["valeur"]
        polluant= ligne["nom_poll"]
        unite = ligne["unite"]
        # attribue à des variables les différentes valeures recherchées dans fields.
        listefinale[compteur]=[NomStation,lattitude,longitude,dateDebut,valur,polluant,unite]
        compteur += 1
    except KeyError:
        pass
#si une valeur est manquante, saute une ligne dans listefinale
entette= ["NomStation","lattitude","longitude","dateDebut","values","polluant","unites"]
fichier = open("transformerFichierJsonToCSV.csv","wt",encoding ="utf-8")
#crée le fichier csv dans lequel on pourra écrire.
csvWriter = csv.writer(fichier,delimiter=";")
#delimite le fichier csv avec ";"
csvWriter.writerow(entette)
#utilise la variable entette comme entête du fichier csv.
for ligne in (listefinale.values()):
    csvWriter.writerow(ligne)
    #écrit les valeurs correspondant à la variable listefinale dans le fichier csv.
fichier.close()
f.close()
#ferme les fichiers;