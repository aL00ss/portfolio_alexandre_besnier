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

2. **Création et Gestion des Tickets**
Exemple de ticket (avec Paul)

Titre : “Dégradation RAID 5 sur serveur DELL — alerte disque”
Demandeur : Paul Hochon
Type : Incident
Actif lié : Serveur DELL (production)
Description :

Symptôme : alerte RAID / disque en défaut

Depuis : 09:10

Périmètre : service impacté (ex : fichiers partagés / applicatif)

Preuves : capture, log, référence d’alerte

Paul décrit le symptôme et joint une capture. Le support complète ensuite le reste (impact, priorité, tâches).

Quelles infos doivent être dans un ticket

Pour éviter les allers-retours inutiles, j’ai standardisé une checklist :

Titre clair (symptôme + système concerné)

Description (contexte, depuis quand, fréquence)

Catégorie (matériel / réseau / applicatif…)

Actif / CI (serveur, poste, imprimante)

Impact (combien de personnes / quel service)

Urgence (délai acceptable avant blocage)

Pièces jointes (captures, logs, messages d’erreur)

Contact (si besoin d’un échange rapide)

Impact / urgence → priorité (rôle de Guy)

Quand Guy Mauve prend le ticket, il qualifie :

Impact : ex. “élevé” si le serveur supporte plusieurs utilisateurs

Urgence : ex. “haute” si le service est en risque d’arrêt

GLPI calcule ensuite la priorité via la matrice. Ça rend le tri cohérent et défendable.


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