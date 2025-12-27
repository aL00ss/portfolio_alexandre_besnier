---
title: "Sauvegarde : 3-2-1-1-0, rétention et tests de restauration (définitions courtes)"
publishDate: 2025-12-27
img: "/assets/backup_basics.png"
img_alt: "Illustration de stratégie de sauvegarde et restauration"
description: |
  Définitions courtes des concepts essentiels : stratégie 3-2-1-1-0, politique de rétention et tests de restauration, avec une image par point (liens en fin d’article).
tags:
  - Backup
  - Continuité d’activité
  - Sécurité
---

Stratégie 3-2-1-1-0

La règle 3-2-1-1-0 décrit une stratégie de sauvegarde où l’on conserve 3 copies des données, sur 2 supports différents, avec 1 copie hors site, 1 copie immuable, et 0 erreur grâce à la vérification/tests réguliers des backups.


La rétention définit combien de points de restauration (quotidiens/hebdomadaires/mensuels) sont conservés et pendant combien de temps, afin d’équilibrer historique disponible et consommation de stockage (souvent via un modèle type GFS/promotion des points).


Les tests de restauration consistent à restaurer périodiquement des fichiers/dossiers (et parfois des machines) pour confirmer que les sauvegardes sont réellement récupérables et que la procédure est maîtrisée.
