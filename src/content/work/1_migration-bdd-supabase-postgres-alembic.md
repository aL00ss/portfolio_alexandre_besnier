---
title: "Migration : Base de données locale vers PostgreSQL (Supabase) — SQLAlchemy et migrations Alembic"
publishDate: 2026-02-05
img: /assets/streamlit-logo.png
img_alt: Image de couverture par defaut
description: "J’ai migré la base de données vers PostgreSQL via Supabase avec SQLAlchemy et Alembic."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Répondre aux incidents et aux demandes d’assistance et d’évolution"
  - "Compétence - Travailler en mode projet"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
---
Migration BDD : local -> PostgreSQL/Supabase (SQLAlchemy/Alembic)

1. **Objectif**

Lors de mon stage de 2e année, l’application Streamlit a évolué vers un usage multi-utilisateurs. Pour répondre à cette contrainte (partage des données, comptes utilisateurs, sessions persistantes), j’ai migré la base de données initialement stockée en local vers une base PostgreSQL hébergée sur Supabase. En parallèle, j’ai mis en place un versioning du schéma avec Alembic afin de fiabiliser l’évolution de la base sans perte de données.

2. **Travail réalisé**

- **Migration vers PostgreSQL (Supabase)**
  - Passage d’une base locale à une base distante PostgreSQL, accessible à distance et adaptée au multi-utilisateur.
  - Centralisation des données applicatives (comptes, données métiers) et préparation à un déploiement plus “production”.

- **Connexion sécurisée**
  - Mise en place d’une connexion via les secrets Streamlit (`st.secrets`) afin d’éviter d’exposer les identifiants dans le code.

- **ORM + structure de code**
  - Utilisation de SQLAlchemy pour relier le code Python aux tables et relations.
  - Maintien d’une architecture modulaire (models / repositories / services / pages) afin d’isoler la logique d’accès aux données.

- **Migrations Alembic**
  - Mise en place d’Alembic pour versionner le schéma (dossier `alembic/`) et appliquer les évolutions nécessaires au fur et à mesure.
  - Ajout de nouvelles migrations lors des évolutions (ex: alignement schéma/UI suite à des retours client).

- **Validation**
  - Vérification de la cohérence des données et du bon fonctionnement de l’application après migration (accès, CRUD, parcours utilisateurs).

3. **Productions / preuves**

- <a href="/assets/BESNIER%20Alexandre%20CR%20S3.pdf" download>Télécharger le compte-rendu (PDF) - Semaine 3</a>

---
