---
title: "Gestion de droits Windows "
description: "Article court: définition d’Active Directory et résumé de l’activité de gestion des droits (groupes, partages, vérifications)."
publishDate: 2025-10-06
tags:
  - Compétence 1
img: "/assets/Tpad.png"

---
## Active Directory (définition rapide)

Active Directory (AD) est le service d’annuaire de Microsoft. Il centralise l’authentification et l’autorisation des utilisateurs et des ordinateurs, organise les objets (unités d’organisation, groupes) et permet d’appliquer des règles de sécurité via les GPO. AD s’appuie notamment sur LDAP, Kerberos et DNS pour gérer l’identité et l’accès aux ressources du domaine.

## Ce que j'ai fait 

- Créér des utilisateurs et des groupes du domaine, puis attribuer les droits via les groupes (pas de droits directs sur les comptes).
- Créér des dossiers partagés sur le serveur et appliquer des permissions NTFS minimales (lecture/modification) par groupe.
- Vérifier côté client que les droits effectifs correspondent aux attentes.

Validation (extrait):
- `prof1` peut écrire dans « seconde1 » et « commun ».
- `eleve211` lit « seconde1 » sans pouvoir écrire et n’a pas d’accès à « commun ».

---
