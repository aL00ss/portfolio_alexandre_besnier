---
title: "Traitement d’un ticket et évolution du module de Planning Poker"
publishDate: 2025-06-30
img: /assets/session_vote.jpg
img_alt: formulaire de création d'une session de poker planning dans Odoo
description: "J'ai créé un module odoo répondnat aux besoins d'Innlog."

tags:
  - Stage
  - Réponse aux incidents et aux demandes d'assistance et d'évolution
---
## Résumé de la mission

Au cours de mon stage chez **Innlog**, j’ai pris en charge une demande d’évolution sur le module de **Planning Poker**, qui étend le module **Projet** d’Odoo pour organiser des sessions de vote d’estimation de la charge de travail d’une tâche.

il fallait notifier **en temps réel** chaque participant lorsqu’une nouvelle session de vote démarrait, puis l’emmener automatiquement sur sa propre interface de vote. J’ai donc :

1. **Analyser le ticket** pour comprendre le besoin.
2. **Conçevoir une solution technique** exploitant le **bus** d’Odoo (un canal de diffusion de messages instantanés entre le serveur et les interfaces).
3. **Développer** un composant JavaScript avec **OWL** (Odoo Web Library) :  
   - À la réception du message “session lancée” sur le bus, j’affiche une **popup** avec un bouton **« Voter »**.  
   - En cliquant, l’utilisateur est redirigé vers sa vue de vote individuelle.
4. **Patcher** le client web d’Odoo pour écouter l’événement et envoyer la notification sur le canal personnel de chaque participant.
5. **Tester** en conditions réelles (plusieurs comptes simultanés) pour m’assurer que tous recevaient bien l’alerte et pouvaient voter sans incident.
6. **Présenter** la fonctionnalité lors d’une réunion d’équipe, avec un tutoriel visuel pour mes collègues non-développeurs.

Cette mission m’a permis de renforcer ma réactivité face aux demandes internes.

---
