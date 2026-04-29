---
title: "TP : Gerer les sauvegardes — mise en place, test de backup/restauration et plan de sauvegarde"
publishDate: 2026-01-05
img: /assets/templateur.jpg
img_alt: Image de couverture par defaut
description: "J’ai mis en place une solution de sauvegarde, teste la sauvegarde/restauration et defini un plan de backup."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
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

4. **Captures (extraits du TP)**

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20130202.jpg" alt="Installation du serveur UrBackup." loading="lazy" decoding="async" />
  <figcaption>Installation du serveur UrBackup.</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20130245.jpg" alt="Parametres serveur UrBackup (repertoire de sauvegarde, options generales)." loading="lazy" decoding="async" />
  <figcaption>Parametres serveur (repertoire de sauvegarde et options).</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20130316.jpg" alt="Liste des clients et etat des sauvegardes." loading="lazy" decoding="async" />
  <figcaption>Vue des clients et etat des sauvegardes.</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20130930.jpg" alt="Fichier de test cree sur le poste client (testBackup.txt)." loading="lazy" decoding="async" />
  <figcaption>Fichier de test cote client pour valider la sauvegarde.</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20131042.jpg" alt="Acces aux sauvegardes du client et possibilites de restauration." loading="lazy" decoding="async" />
  <figcaption>Acces aux sauvegardes et options de restauration.</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20131115.jpg" alt="Activite de sauvegarde terminee (100%)." loading="lazy" decoding="async" />
  <figcaption>Suivi d’activite : sauvegarde complete.</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20backup/Capture%20d'%C3%A9cran%202024-12-08%20131312.jpg" alt="Planification : intervalle sauvegarde incrementele et complete." loading="lazy" decoding="async" />
  <figcaption>Exemple de planification (incrementele / complete).</figcaption>
</figure>
