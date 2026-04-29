---
title: "Évolutions : Intégration des retours client — améliorations, tests fonctionnels et correctifs applicatifs"
publishDate: 2026-02-05
img: /assets/templateur.jpg
img_alt: Image de couverture par defaut
description: "J’ai intégré des retours client, réalisé des tests fonctionnels et apporté des correctifs sur l’application."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Répondre aux incidents et aux demandes d’assistance et d’évolution"
  - "Compétence - Travailler en mode projet"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
---
Intégration retours client + tests + correctifs

1. **Contexte**

Lors de mon stage de 2e année, j’ai présenté l’état de l’application au client A. Suite à cette présentation, nous avons organisé une réunion de cadrage afin de recueillir des retours métier (notamment sur la finance et le suivi du temps). L’objectif de cette phase était d’intégrer rapidement les demandes, de sécuriser les modules existants et de livrer une version plus cohérente et exploitable.

2. **Travail réalisé**

- **Réunion de cadrage (Semaine 6)**
  - Présentation de l’état d’avancement au client et recueil des retours.
  - Identification des points à retoucher sur les modules Finance et Calendrier / suivi du temps.

- **Retouches du module de gestion financière**
  - Amélioration de l’ergonomie et des parcours de gestion (création rapide, listes filtrables, fiches détaillées par catégorie).
  - Mise à jour de la base de données via des migrations Alembic afin d’aligner le schéma et l’interface (UI).

- **Évolution du module Calendrier en “Feuille d’heures”**
  - Ajout d’une nouvelle page dédiée à la saisie mensuelle des heures (statuts, horaires, pause, soirées, week-ends, calculs automatiques).
  - Ajustement du calendrier pour afficher les statuts issus de la feuille d’heures, avec un rendu dépendant du rôle (RBAC).

- **Tests et correctifs sur les modules existants**
  - Module “Personnes” : vérifications et corrections liées à la création de comptes et à la bonne prise en compte des informations.
  - Corrections ponctuelles sur plusieurs pages : navigation, libellés, cohérence RBAC, et retouches diverses (dont RGPD).
  - Évolutions techniques associées : nouvelles migrations de base de données et ajout/ajustement de models et repositories.

3. **Productions / preuves**

- <a href="/assets/CR_Semaine_6_BESNIER_Alexandre.pdf" download>Télécharger le compte-rendu (PDF) - Semaine 6</a>

---
