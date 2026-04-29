---
title: "TP : Gerer les sauvegardes — mise en place, test de backup/restauration et plan de sauvegarde"
publishDate: 2026-01-05
img: /assets/UrBackup-Logo.jpg
img_alt: Logo UrBackup
description: "J’ai mis en place une solution de sauvegarde, teste la sauvegarde/restauration et defini un plan de backup."

tags:
  - "Compétence - Gérer le patrimoine informatique"
---
TP : gestion des sauvegardes (backups)

1. **Objectif**

Mettre en place un dispositif de sauvegarde (serveur + client), tester la sauvegarde et la restauration, puis definir un plan de sauvegarde et des elements de supervision.

2. **Travail realise (demarche)**

- **Mise en place du serveur (UrBackup)**
  - Installation du serveur de sauvegarde (choix du dossier d’installation).
  - Parametrage des regles cote serveur (repertoire de sauvegarde, options generales).

- **Mise en place du client**
  - Ajout/enregistrement d’un poste client dans la console.

- **Tests de sauvegarde**
  - Creation d’un fichier de test sur le poste client.
  - Lancement et suivi de la sauvegarde jusqu’a completion.

- **Tests de restauration**
  - Acces aux sauvegardes du client depuis la console et verification de la presence des donnees.
  - Test de restauration (restaurer un dossier vers un client).

- **Planification et supervision**
  - Definition d’intervalles (incrementele et complet) pour la sauvegarde de fichiers.
  - Suivi des activites et controle de l’etat des sauvegardes.

3. **Ce que je retiens (apports)**

- Une sauvegarde n’a de valeur que si la restauration est testee.
- Le plan de sauvegarde doit definir quoi sauvegarder, quand, combien de temps conserver et comment verifier.

