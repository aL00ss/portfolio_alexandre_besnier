---
title: Gestion de fichiers Python
publishDate: 2023-12-14
img: /assets/Python.PNG
img_alt: données sous Python
description: |
  Nous avons transformé des données sous Python:
tags:
  - Python
---

## Résumé du projet

Dans le cadre de ce projet, j'ai utilisé mes compétences informatiques pour traiter des données à des fins décisionnelles. La tâche consistait à gérer un fichier de données au format JSON et à le transformer en un fichier CSV répondant à des critères spécifiques.

Le jeu de données fournissait des informations sur les concentrations moyennes horaires de différents polluants dans l'air de la région de Poitiers. Mon objectif était de convertir ce fichier JSON en un fichier CSV avec des colonnes précises, telles que le nom de la station, la latitude, la longitude, la date de prélèvement, le nom du polluant, la valeur, et l'unité de mesure.

Pour réaliser cette transformation, j'ai développé un script Python appelé "transformerJsonToCsv.py". Ce script a été conçu pour extraire les données pertinentes du fichier JSON, les formater correctement et les exporter dans un fichier CSV. J'ai veillé à ce que le fichier CSV soit lisible dans Excel en utilisant le point-virgule comme séparateur et en prenant en compte les caractères spéciaux, tels que les accents.

En réalisant ce projet, j'ai acquis des compétences dans la maîtriser la syntaxe du langage Python et à utiliser efficacement les structures de données. J'ai également développé une compréhension approfondie des structures algorithmiques de base et de leur contexte d'utilisation. 

le code du projet:
```Python

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
