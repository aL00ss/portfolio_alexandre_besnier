---
title: "TP : Active Directory — domaine, utilisateurs, groupes, habilitations et partage"
publishDate: 2025-12-22
img: /assets/Active-Directory-Logo.png
img_alt: Image de couverture par defaut
description: "J’ai mis en place un domaine Active Directory et verifie les niveaux d’habilitation associes a un service (groupes, droits, partage)."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
---
TPAD : mise en place d’un domaine AD et des habilitations

1. **Objectif**

Mettre en place un domaine Active Directory et verifier les niveaux d’habilitation associes a un service : organisation de l’annuaire, creation de comptes/groupes, permissions et integration de postes clients.

2. **Contexte**

La gestion des habilitations dans Active Directory (AD) permet de controler qui accede a quelles ressources (dossiers partages, services, applications) et avec quels droits. L’objectif est d’appliquer le principe du moindre privilege et de rendre l’administration plus simple (droits par groupes plutot que par utilisateurs).

3. **Travail realise (principales etapes)**

- Creation du domaine AD (preparation VM Windows, installation/parametrage).
- Gestion des utilisateurs du domaine :
  - creation des unites d’organisation (UO),
  - creation de groupes,
  - creation d’utilisateurs,
  - gestion des permissions.
- Mise en place d’un partage (dossier partage + droits) et exercice de groupes locaux.
- Integration d’un PC au domaine et validations de configuration.

4. **Points importants (habilitations)**

- **Groupes de securite** : attribuer des droits a des groupes plutot qu’a des utilisateurs individuellement.
- **UO (Organizational Units)** : organiser les comptes pour faciliter la gestion (par classe, service, departement, etc.).
- **Verification / audit** : verifier regulierement les acces et tracer les changements de droits.
- **Mises a jour** : tenir compte des changements de roles (arrivee, depart, changement de poste) dans les habilitations.

5. **Illustrations (extraits du TP)**

<figure>
  <img src="/assets/tp%20ad/Capture%20d_%C3%A9cran%202024-10-02%20095428.png" alt="Exemple de structure dans Utilisateurs et ordinateurs Active Directory (UO, groupes, dossiers partages)." loading="lazy" decoding="async" />
  <figcaption>Exemple de structure dans l'annuaire (UO, groupes et partage).</figcaption>
</figure>

<figure>
  <img src="/assets/tp%20ad/imageTP46.png" alt="Schema de principe : groupes globaux, groupes locaux de domaine et permissions sur une ressource partagee." loading="lazy" decoding="async" />
  <figcaption>Principe de gestion des droits : groupes + permissions sur la ressource.</figcaption>
</figure>

6. **Ce que je retiens (apports)**

- La structuration (UO/groupes) simplifie l’administration et la mise en conformite des droits.
- Les tests de droits sont essentiels pour verifier que l’habilitation correspond au besoin (et au principe du moindre privilege).

