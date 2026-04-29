---
title: "TP : GLPI + LDAP/AD — integration a Active Directory et import utilisateurs/groupes"
publishDate: 2025-11-22
img: /assets/templateur.jpg
img_alt: Image de couverture par defaut
description: "J’ai configure GLPI pour se connecter a Active Directory via LDAP afin d’importer utilisateurs et groupes."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
  - "Compétence - Répondre aux incidents et aux demandes d’assistance et d’évolution"
---
GLPI : integration LDAP / Active Directory

1. **Objectif**

Integrer GLPI avec Active Directory afin de centraliser la gestion des comptes (annuaire), faciliter l’administration et fiabiliser l’authentification/import des utilisateurs et des groupes.

2. **Travail realise (demarche)**

- Preparation cote Active Directory (pre-requis annuaire).
- Configuration LDAP dans GLPI.
- Connexion GLPI <-> AD (parametrage de la liaison).
- Importation des groupes et des utilisateurs depuis AD.
- Verifications et tests de connexion.

3. **Ce que je retiens (apports)**

- L’integration LDAP permet d’aligner GLPI sur le referentiel d’identites (AD) : moins de doubles saisies et des droits plus coherents.
- Les tests/validations (connexion, import, affectation) sont indispensables avant mise en production.

