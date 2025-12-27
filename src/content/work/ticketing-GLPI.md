---
title: "GLPI : Optimisation de la Gestion des Tickets — mise en place d’un support structuré"
publishDate: 2025-12-27
img: /assets/glpi_ticketing.png
img_alt: Interface GLPI montrant la création, l’affectation et le suivi d’un ticket
description: "J’ai organisé une gestion de tickets dans GLPI"

tags:
- GLPI
- Ticketing
- ITSM
- ITIL
- CMDB

---

GLPI : Optimisation de la Gestion des Tickets


1. **Configuration des Profils Utilisateurs**

J’ai défini des profils distincts afin que chacun intervienne au bon niveau, sans mélange de responsabilités.

Self-Service (demandeurs) : accès limité à la création de tickets.

Technicien : droits étendus pour la gestion des tickets.

Superviseur : vue globale pour superviser et réassigner les tickets.

Paul Hochon (Self-Service) 
Guy Mauve (Technicien)
Marie Tim (Technicien) 
Sandy Kilot (Superviseur)

2. Affectation des Équipements et des Profils : Organisation des Responsabilités

Par la suite, j’ai attribué des profils utilisateurs ainsi que du matériel adapté à chaque personne :

Paul Hochon : Profil Self-Service associé à un poste client.

Guy Mauve et Marie Tim : Profils Technicien.

Sandy Kilot : Profil Superviseur.

Enjeu principal :

L’attribution précise des rôles et des équipements permet à chaque utilisateur d’intervenir uniquement dans son périmètre, ce qui limite les erreurs, améliore l’efficacité et évite les surcharges de travail.

3. Mise en Place et Suivi des Tickets : Une Démarche Indispensable
Contenu d’un ticket

Dans GLPI, un ticket doit comporter des informations structurées et détaillées afin d’assurer un traitement efficace :

Titre : résumé clair du problème (ex. : « L’imprimante ne fonctionne plus »).

Description : explication détaillée de l’incident (ex. : « L’imprimante HP123 ne répond plus depuis hier matin »).

Impact et urgence : éléments permettant d’évaluer la priorité.

Assignation : technicien en charge du ticket.

Pièces jointes : captures d’écran, fichiers journaux, ou autres preuves.

Statut : ouvert, en cours de traitement, résolu, etc.

Exemple concret

Paul Hochon (Self-Service) a ouvert un ticket afin de signaler un dysfonctionnement.

Guy Mauve (Technicien) a pris en charge le ticket, ajusté les niveaux d’impact et d’urgence, puis utilisé la matrice de priorité pour le classer comme « Important ».

Pourquoi cette organisation est essentielle ?

Répartition des responsabilités : les incidents urgents et les problèmes nécessitant une analyse approfondie sont traités à des niveaux distincts.

Gestion optimale des priorités : l’évaluation de l’impact et de l’urgence permet une meilleure allocation des ressources et une résolution plus rapide.


3. **Gestion des Problèmes**

Quand plusieurs incidents se ressemblent je crée un Problème.

Exemple :

Plusieurs tickets “panne disque” sur des serveurs DELL récents.

Sandy Kilot ouvre un Problème : “Pannes récurrentes de disques sur serveurs DELL”.

Il lie les incidents (celui de Paul, et d’autres) au Problème.

L’objectif devient alors : identifier la cause racine (lot matériel, firmware, conditions, configuration) et définir une action durable (mise à jour, remplacement préventif, standard).

4. **Rapport avec ITIL**

J’ai aligné l’organisation sur une logique ITIL simple et compréhensible :

Incident : restaurer vite le service.

Problème  : réduire la récurrence et traiter la cause racine.

Priorisation : impact + urgence → priorité.

Traçabilité : historique des actions.

GLPI fournit l’outil et le workflow ; ITIL fournit la méthode de classement et d’amélioration continue.

5. **Feedback Utilisateur**

Un élément central du processus de ticketing concerne le retour des utilisateurs :

GLPI offre la possibilité de demander au demandeur de valider la résolution, afin de s’assurer que la solution apportée répond réellement à son besoin.

6. **Différence entre un incident et un problème**

Incident : événement qui dégrade ou interrompt un service (objectif : remise en service rapide).
Ex : Paul n’a plus un service fiable à cause du RAID en défaut.

Problème : cause (ou cause potentielle) d’un ou plusieurs incidents (objectif : éviter la répétition).
Ex : Sandy identifie une série de pannes disque récurrentes et lance une action durable.

---