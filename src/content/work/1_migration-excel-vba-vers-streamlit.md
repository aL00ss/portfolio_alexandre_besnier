---
title: "Migration : Excel/VBA vers une application web Python/Streamlit (ERP) — travail en équipe avec Git"
publishDate: 2026-02-05
img: /assets/templateur.jpg
img_alt: Image de couverture par defaut
description: "En équipe, j’ai participé à la migration d’un outil Excel/VBA vers une application web Python/Streamlit de type ERP."

tags:
  - "Compétence - Répondre aux incidents et aux demandes d’assistance et d’évolution"
  - "Compétence - Travailler en mode projet"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
---
Migration : Excel/VBA -> Python/Streamlit (ERP)

1. **Contexte**

Lors de mon stage de 2e année, j’ai travaillé en équipe (2 personnes) sur la migration d’un outil de gestion associatif initialement développé sous Excel/VBA vers une application web Python avec Streamlit. L’objectif était de répondre aux besoins du client identifiés lors d’une réunion de cadrage (semaine 1), tout en rendant l’outil plus moderne et plus simple à faire évoluer.

2. **Objectifs**

- Comprendre le fonctionnement de l’existant Excel/VBA et reprendre les traitements métiers.
- Transposer les formulaires Excel en interface web (formulaires, tableaux, tableaux de bord).
- Mettre en place une architecture plus modulaire et maintenable.

3. **Travail réalisé**

- **Mise en place du projet Streamlit**
  - Création du projet et structuration du code pour séparer l’accès aux données, la logique métier et l’interface.

- **Analyse et redéfinition de la structure de la base de données**
  - Reprise du modèle de données et préparation de la couche d’accès aux données via l’ORM (SQLAlchemy).

- **Architecture en couches (mise en place dès le début de la migration)**
  - `codes/models/` : modèles de données (tables) via SQLAlchemy.
  - `codes/repositories/` : fonctions d’accès à la base (CRUD) avec des requêtes construites via l’API SQLAlchemy (select, where, etc.).
  - `codes/services/` : couche intermédiaire pour des fonctions d’analyse (notamment pour les dashboards).
  - `pages/` : pages Streamlit (interface) appelant les repositories pour afficher et modifier les données.
  - `db.py` : création/connexion à la base au lancement de l’application.
  - `.streamlit/` : configuration de l’application (mise en page, paramètres).

- **Portage des fonctionnalités VBA vers Streamlit**
  - Développement de formulaires CRUD pour les tables de la base de données, avec contrôles de saisie et validations.
  - Exemple: page “Contributions” avec une liste déroulante (selectbox) permettant de sélectionner une contribution et d’afficher l’ensemble des informations liées (date, bénévole, activité, code analytique, etc.).

- **Fonctionnalités supplémentaires demandées**
  - Mise en place de dashboards dynamiques répondant aux attentes du client.
  - Améliorations sur la gestion des contributions des bénévoles.

- **Ergonomie / navigation**
  - Développement d’une barre de navigation appelée sur chaque page afin d’améliorer le parcours utilisateur.
  - Mise en place d’une vue “gestion base de données” de type phpMyAdmin (sélection de table, filtres, édition/ajout) et ajout d’une fonction d’export des données en Excel.

- **Travail en équipe et suivi**
  - Gestion du projet avec Git (travail en branches) et GitHub (kanban et user stories).

4. **Productions / preuves**

- <a href="/assets/BESNIER%20Alexandre%20CR%20S2.pdf" download>Télécharger le compte-rendu (PDF) - Semaine 2</a>

---
