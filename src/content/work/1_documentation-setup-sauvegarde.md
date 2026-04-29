---
title: "Mise à disposition : Documentation, scripts de setup et sauvegarde — faciliter le déploiement chez le client"
publishDate: 2026-02-05
img: /assets/templateur.jpg
img_alt: Image de couverture par defaut
description: "J’ai produit la documentation et des scripts de setup/sauvegarde pour faciliter le déploiement et l’exploitation."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Travailler en mode projet"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
---
Documentation + scripts de setup et sauvegarde

1. **Objectif**

Lors de mon stage de 2e année, j’ai réalisé une documentation de référence pour la passation du projet et j’ai développé des scripts de setup et de sauvegarde. L’objectif était qu’un repreneur (technique ou non) puisse comprendre rapidement l’application, la maintenir, la déployer et l’exploiter, en sécurisant particulièrement les zones sensibles (authentification, rôles/RBAC, RGPD, migrations, modules critiques).

2. **Travail réalisé**

- **Documentation de passation (Semaine 5)**
  - Mise en place d’un point d’entrée unique `doc/README.md` orientant vers 3 parcours :
    - Produit (utilisateurs)
    - Engineering (développeurs)
    - Exploitation (ops)
  - Structuration de la documentation en dossiers :
    - `doc/user/` : guide utilisateur, FAQ, glossaire, documentation par module avec un format homogène (objectif, accès/roles, actions, règles/erreurs).
    - `doc/dev/` : architecture (Streamlit Cloud <-> Supabase), onboarding, lancement local, migrations Alembic, configuration/secrets, modèle de données, checklist de tests.
    - `doc/ops/` : déploiement, runbook (sauvegarde/restauration, vérifs post-déploiement, gestion incident), sécurité.
  - Rédaction d’un document `HANDOVER.md` pour expliquer la méthode de lecture/modification et les points de vigilance.

- **Scripts de setup / premier lancement (Semaine 5)**
  - Développement de scripts (Bash) pour faciliter le premier lancement : initialisation, création des tables et remplissage avec des données par défaut (seed), avec un compte configuré.

- **Sauvegarde périodique et exploitation (Semaine 6)**
  - Mise en place de scripts Bash / PowerShell pour effectuer des sauvegardes périodiques de la base PostgreSQL (Supabase) dans une version locale.
  - Fréquence de sauvegarde ajustable selon le besoin du client.

3. **Productions / preuves**

- <a href="/assets/BESNIER%20Alexandre%20CR%20S5.pdf" download>Télécharger le compte-rendu (PDF) - Semaine 5</a>

---
