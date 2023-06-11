---
title: Régression sur données réelles
publishDate: 2023-12-14
img: /assets/sae_Régression linéare.png
img_alt: Courbes de régression
description: |
  Voici un des graphiques produit avec R Studio :
tags:
  - R Studio
---

## Résumé du projet

 Pour ce projet en binôme de régression sur des données réelles visant à prédire le prix de vente des logements en 2021 dans les Deux-Sèvres et la Charente-Maritime, nous avons utilisé un jeu de données d'entraînement contenant des informations sur les logements, y compris le prix de vente. Nous avons également utilisé un jeu de données de test avec les mêmes variables, mais sans le prix de vente. Notre objectif était de développer un modèle de prédiction fiable en utilisant R Studio.

Dans un premier temps, nous avons exploré les données pour détecter d'éventuelles valeurs manquantes ou aberrantes.Nous avons ainsi fait un nettoyage des données en supprimant les observations extrêmes afin de garantir la qualité de nos analyses.

Ensuite, nous avons construit plusieurs modèles de régression, tels que linéaire, logarithmique, puissance et exponentielle. Après avoir analysé les SCR (Sommes des Carrés des Résidus) entre les varriables et la valeur foncière, nous avons choisi le modèle le plus performant, avec une somme des carrés des résidus minimale.

Pour mieux comprendre les données, nous avons utilisé des graphiques pour visualiser les distributions et les corrélations entre différentes variables.

Enfin, nous avons utilisé le modèle sélectionné pour prédire le prix de vente des logements dans le jeu de données de test. Les prédictions ont été enregistrées dans un fichier CSV nommé "prediction.csv", contenant les identifiants des logements du jeu de test et les valeurs prédites pour le prix de vente.

Ce projet m'a a permis de développer mes compétences en régression sur R Studio, en utilisant des graphiques pour l'analyse exploratoire des données et en interprétant les résultats des modèles de régression.

les documents principaux du projet: <a href="/assets/Fichiers (1).zip" download>télécharger</a>